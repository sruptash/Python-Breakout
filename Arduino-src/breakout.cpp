/*
    Scott Ruptash
    Mike Bujold
    Section A2
    Michael Bowling, Walter Bischof
*/
/*****************************************************
    BREAKOUT.CPP:
        Code in this file is where the main loop
        resides. Includes functions for the hardware
        like joystick input, speaker output, and
        button output.
*****************************************************/

/* HEADER INCLUDES */
#include <Arduino.h>
#include <Adafruit_GFX.h>
#include <Adafruit_ST7735.h>
#include <SPI.h>

#include "breakout.h"
#include "gameStats.h"
#include "bricks.h"
#include "ball.h"
#include "paddle.h"


/* GLOBAL VARIABLES */
// tft display
Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);
// joystick centres
int X_CENTRE;
int Y_CENTRE;
// pause either on or off
bool paused;
// game in menu mode or game mode
bool menuMode;
// determines if menu selection was made recently. Also used for initial game draw
bool updateSel;
// determines game difficulty
char difficulty;


/* FUNCTIONS */
// used to play tones from the speaker
void playTone(int period, int duration)
{
    long elapsedTime = 0;
    int halfPeriod = period/2;

    while (elapsedTime < duration * 1000L)
    {
        digitalWrite(SPEAKER, HIGH);
        delayMicroseconds(halfPeriod);
        digitalWrite(SPEAKER, LOW);
        delayMicroseconds(halfPeriod);
        elapsedTime = elapsedTime + period;
    }
}

// reads in joystick movement, and adjusts paddle position
// alternatively, adjusts selected option in menu
// parameter used to differentiate the functions purpose
void readJoystick(char purpose)
{
    int joystick_x = analogRead(HOR);

    if(joystick_x > X_CENTRE + OFFSET)
    {
        // purpose is for moving paddle
        if(purpose == 'p')
            /* Move to the RIGHT */
            adjustPaddle('r');
        
        // purpose is for setting difficulty
        else if(purpose == 'm')
        {
            if(difficulty == 'e')
                difficulty = 'm';
                
            else if(difficulty == 'm')
                difficulty = 'h';
            
            else if(difficulty == 'h')
                difficulty = 'e';
            
            // wait till joystick back to center
            while(analogRead(HOR) != X_CENTRE) {}
            
            updateSel = true;
            playTone(100, 50);
        }
    }
    else if(joystick_x < X_CENTRE - OFFSET)
    {
        // purpose is for moving paddle
        if(purpose == 'p')
            /* Move to the LEFT */
            adjustPaddle('l');
        
        // purpose is for setting difficulty
        else if(purpose == 'm')
        {
            if(difficulty == 'e')
                difficulty = 'h';
                
            else if(difficulty == 'm')
                difficulty = 'e';
            
            else if(difficulty == 'h')
                difficulty = 'm';
                
            // wait till joystick back to center
            while(analogRead(HOR) != X_CENTRE) {}
            
            updateSel = true;
            playTone(100, 50);
        }
    }
}

// returns difficulty setting
char getDifficulty()
{
    return difficulty;
}

/* SETUP FUNCTION */
void setup()
{
    // Start serial communication for debugging
    Serial.begin(9600);

    // Calibrate 'centre' position of joystick, initialize joystick click
    X_CENTRE = analogRead(HOR);
    pinMode(SEL, INPUT);
    digitalWrite(SEL, HIGH);
    
    // initialize select/pause button
    pinMode(PAUSE, INPUT);
    digitalWrite(PAUSE, HIGH);

    // initialize speaker
    pinMode(SPEAKER, OUTPUT);

    // Initialize screen
    tft.initR(INITR_REDTAB);
    
    // initialize screen for menu mode.
    menuMode = true;
    updateSel = true;
    paused = false;
    difficulty = 'e';
}


/* LOOP FUNCTION */
void loop()
{
    // read pause pin, unpause game if button is clicked
    if(!menuMode)
    {
        if(digitalRead(PAUSE) == LOW && paused)
        {
            paused = false;
            while(digitalRead(PAUSE) == LOW) {}
            pauseGame(paused);
        }
    }
    // print menu instead
    else
    {
        tft.fillScreen(ST7735_BLACK);
        
        tft.setRotation(1);
        tft.setTextSize(2);
        
        tft.setCursor(29, 30);
        tft.setTextColor(ST7735_WHITE);
        tft.print("B");
        tft.setTextColor(ST7735_RED);
        tft.print("R");
        tft.setTextColor(ST7735_MAGENTA);
        tft.print("E");
        tft.setTextColor(ST7735_YELLOW);
        tft.print("A");
        tft.setTextColor(ST7735_GREEN);
        tft.print("K");
        tft.setTextColor(ST7735_BLUE);
        tft.print("O");
        tft.setTextColor(ST7735_WHITE);
        tft.print("U");
        tft.setTextColor(ST7735_RED);
        tft.print("T");
        tft.setTextColor(ST7735_MAGENTA);
        tft.print("!");
        
        tft.setTextColor(ST7735_WHITE);
        tft.setTextSize(1);
        tft.setCursor(28, 75);
        tft.print("Select Difficulty:");
    }
    
    /* MENU LOOP */
    while(menuMode)
    {
        // use pause button for selecting difficulty
        if(digitalRead(PAUSE) == LOW && menuMode)
        {
            menuMode = false;
            while(digitalRead(PAUSE) == LOW) {}
        }
        
        // print selection to screen
        if(updateSel)
        {
            tft.setTextSize(2);
            tft.fillRect(0, 90, SCREEN_HEIGHT, 20, ST7735_BLACK);
            
            if(difficulty == 'e')
            {
                tft.setTextColor(ST7735_GREEN);
                tft.setCursor(45, 90);
                tft.print("NORMAL");
            }
            else if(difficulty == 'm')
            {
                tft.setTextColor(ST7735_YELLOW);
                tft.setCursor(33, 90);
                tft.print("HARDCORE");
            }
            else if(difficulty == 'h')
            {
                tft.setTextColor(ST7735_RED);
                tft.setCursor(35, 90);
                tft.print("EXTREME!");
            }
            
            updateSel = false;
        }
        
        // read joystick, and print out selected option ('m' for menu)
        readJoystick('m');
    }
    
    /* GAME LOOP */
    while(!paused)
    {
        if(!updateSel)
        {
            // blacken screen and rotate back to normal
            tft.fillScreen(ST7735_BLACK);
            tft.setRotation(0);
            
            // initialize paddle position and difficulty
            initializePaddle(difficulty);
            // initial ball position and difficulty
            initializeBall(difficulty);
            // initialize score deduction from difficulty selection
            initializeScore(difficulty);
            
            // draw initial objects to screen
            drawPaddle();
            drawBricks(NULL);
            drawBall();
            displayStats();
            
            updateSel = true;
        }
        
        //Read select pin, to see if joystick has been clicked
        if(digitalRead(SEL) == LOW && ballOnPaddle())
        {
            launchBall();
            while(digitalRead(SEL) == LOW) {}
        }
        
        // read pause pin, pause game if button is clicked
        if(digitalRead(PAUSE) == LOW && !paused)
        {
            paused = true;
            pauseGame(paused);
            while(digitalRead(PAUSE) == LOW) {}
            break;
        }

        // update paddle position
        updatePaddlePos();

        // now update ball position
        updateBallPos();
        
        delay(15);
    }
}
