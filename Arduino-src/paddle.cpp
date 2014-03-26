/*
    Scott Ruptash
    Mike Bujold
    Section A2
    Michael Bowling, Walter Bischof
*/
/*****************************************************
    PADDLE.CPP:
        Code in this file is responsible for
        everything related to the paddle. Changes
        the paddle position based on input
        from the joystick.
*****************************************************/

/* HEADER INCLUDES */
#include <Adafruit_ST7735.h>

#include "paddle.h"
#include "breakout.h"

/* GLOBAL VARIABLES */
// paddle position on-screen
int paddlePos;
int oldPaddlePos;
int PADDLE_WIDTH;
// determines if paddle moved
bool updateFlag = false;
// determines if paddle already shrunken
bool shrunken;


/* FUNCTIONS */
// Draws the paddle at the bottom of the screen
void drawPaddle()
{ 
  tft.fillRect(PADDLE_LEVEL, oldPaddlePos, PADDLE_HEIGHT, PADDLE_WIDTH, ST7735_BLACK);
  tft.fillRect(PADDLE_LEVEL, paddlePos, PADDLE_HEIGHT, PADDLE_WIDTH, ST7735_WHITE);
}

// initializes paddle on screen
void initializePaddle(char difficulty)
{
    // set paddle width based on difficulty
    if(difficulty == 'e')
        PADDLE_WIDTH = 35;
    
    else if(difficulty == 'm')
        PADDLE_WIDTH = 30;
        
    else if(difficulty == 'h')
        PADDLE_WIDTH = 25;
    
    paddlePos = (SCREEN_WIDTH/2) - (PADDLE_WIDTH/2);
    oldPaddlePos = 0;
    
    shrunken = false;
}

// gets paddle position
int getPaddlePosition()
{
    return paddlePos;
}

// moves paddle left or right by the increment
void adjustPaddle(char direction)
{
    // move right
    if(direction == 'r')
    {
        paddlePos += INCREMENT;
        
        if(paddlePos + PADDLE_WIDTH >= SCREEN_WIDTH)
            paddlePos = SCREEN_WIDTH - PADDLE_WIDTH;
    }
    // move left
    else if(direction == 'l')
    {
        paddlePos -= INCREMENT;
        
        if(paddlePos <= 0)
            paddlePos = 0;
    }
}

// updates and draws paddle on screen
void updatePaddlePos()
{
    oldPaddlePos = paddlePos;
    readJoystick('p');
    
    if(paddlePos != oldPaddlePos)
        updateFlag = !updateFlag;
      
    if(updateFlag)
    {
        drawPaddle();
        updateFlag = false;
    }
}

// shrink the paddle
void shrinkPaddle()
{
    if(!shrunken)
    {
        tft.fillRect(PADDLE_LEVEL, paddlePos, PADDLE_HEIGHT, PADDLE_WIDTH, ST7735_BLACK);
        PADDLE_WIDTH -= 10;
        tft.fillRect(PADDLE_LEVEL, paddlePos, PADDLE_HEIGHT, PADDLE_WIDTH, ST7735_WHITE);
        
        shrunken = true;
    }
}


