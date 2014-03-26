/*
    Scott Ruptash
    Mike Bujold
    Section A2
    Michael Bowling, Walter Bischof
*/
/*****************************************************
    GAMESTATS.CPP:
        Code in this file keeps track of score and
        lives, and drawing them to the screen.
        If an end-game state is reached, appropriate
        message is displayed at the end of game.
        Code here also draws pause message.
*****************************************************/

/* HEADER INCLUDES */
#include <Adafruit_ST7735.h>
#include <string.h>

#include "breakout.h"
#include "gameStats.h"


/* GLOBAL VARIABLES */
// keeps track of player score
int score;
// keeps track of lives player has left
int lives = STARTING_LIVES;
// penalty for losing a life. Varies depending on difficulty
int penalty;


/* FUNCTIONS */
// initialize score and penalty amount
void initializeScore(char difficulty)
{
    if(difficulty == 'e')
        penalty = 10;
        
    else if(difficulty == 'm')
        penalty = 50;
        
    else if(difficulty == 'h')
        penalty = 1000;
        
    score = 0;
}
        
// increase score by amount of points gathered
void increaseScore(int points)
{
    score += points;
    displayStats();
}

// lose a life, and get a score penalty
void decreaseLives()
{
    lives--;
    score -= penalty;
    
    if(score < 0)
        score = 0;
        
    displayStats();
    
    // check how many lives left. If zero, end the game.
    if(getLivesLeft() <= 0)
        endGame();
}

// returns score
int getScore()
{
    return score;
}

// returns lives left
int getLivesLeft()
{
    return lives;
}

// resets score to zero, lives to starting number of lives
void resetAll()
{
    score = 0;
    lives = STARTING_LIVES;
    displayStats();
}

// displays score and lives to bottom of screen
void displayStats()
{
    tft.setRotation(1);
    tft.setTextColor(ST7735_WHITE);
    tft.setTextSize(1);
    
    tft.fillRect(0, 120, SCREEN_HEIGHT, 8, ST7735_BLACK);
    
    tft.setCursor(5,120);
    
    tft.print("Score:");
    tft.print(score);
    
    tft.setCursor(100,120);
    
    tft.print("Lives:");
    if(lives == 3)
        tft.print("ooo");
    else if(lives == 2)
        tft.print("oo");
    else if(lives == 1)
        tft.print("o");

    tft.setRotation(0);
}

// ends game, prints message to screen then stays in loop
void endGame()
{
    // player loses, and doesn't get the glory of having a score.
    if(lives == 0)
    {
        tft.setRotation(1);
        tft.setTextColor(ST7735_WHITE);
        tft.setTextSize(2);
        
        tft.fillRect(0, 0, SCREEN_HEIGHT, SCREEN_WIDTH, ST7735_BLACK);
        tft.setCursor(24, 35);
        tft.print("GAME OVER!");
        
        tft.setTextSize(1);
        tft.setCursor(20, 90);
        tft.print("Rating: ");
        tft.setTextColor(ST7735_RED);
        
        while(true)
        {
            tft.setCursor(66, 90);
            tft.print("HUMAN GARBAGE");
            playTone(100, 50);
            delay(500);
            tft.fillRect(66, 90, SCREEN_WIDTH, 10, ST7735_BLACK);
            delay(500);
        }
    }
    // player takes out all blocks and wins. Score shown at the end.
    else
    {
        tft.setRotation(1);
        tft.setTextColor(ST7735_WHITE);
        tft.setTextSize(2);
        
        tft.fillRect(0, 0, SCREEN_HEIGHT, SCREEN_WIDTH, ST7735_BLACK);
        
        tft.setCursor(34, 35);
        
        tft.print("YOU WIN!");
        
        tft.setTextSize(1);
        tft.setCursor(34, 70);
        tft.print("Final Score: ");
        tft.print(score);
        
        tft.setCursor(24, 105);
        tft.print("Rating: ");
        
        
        String rating;
        char gameDiff = getDifficulty();
        
        if(score <= 15)
        {
            rating = "HUMAN GARBAGE";
            tft.setTextColor(ST7735_RED);
        }
        else if(score > 15 && score <= 40)
        {
            rating = "PATHETIC";
            tft.setTextColor(ST7735_RED);
        }  
        else if(score > 40 && score <= 65)
        {
            rating = "NOT TOO BAD";
            tft.setTextColor(ST7735_YELLOW);
        }    
        else if(score > 65 && score <= 90)
        {
            rating = "MEH";
            tft.setTextColor(ST7735_YELLOW);
        }   
        else if(score > 90 && score <= 115)
        {
            rating = "ALMOST WORTHY";
            tft.setTextColor(ST7735_YELLOW);
        }
        else if(score > 115 && score < 144)
        {
            rating = "GOOD";
            tft.setTextColor(ST7735_GREEN);
        }
        else if(score == 144 && gameDiff == 'e')
        {
            rating = "AMAZING";
            tft.setTextColor(ST7735_GREEN);
        }
        else if(score == 144 && gameDiff == 'm')
        {
            rating = "GODLIKE";
            tft.setTextColor(ST7735_GREEN);
        }
            
        else if(score == 144 && gameDiff == 'h')
        {
            rating = "GET A LIFE";
            tft.setTextColor(ST7735_RED);
        }
        
        while(true)
        {
            tft.setCursor(70, 105);
            tft.print(rating);
            playTone(50, 50);
            delay(500);
            tft.fillRect(70, 105, SCREEN_WIDTH, 10, ST7735_BLACK);
            delay(500);
        }
    }
}

// displays pause message to screen
void pauseGame(bool paused)
{
    tft.setRotation(1);
    tft.setTextColor(ST7735_WHITE);
    tft.setTextSize(2);
    
    if(paused)
    {
        tft.setCursor(45, 70);
        tft.print("PAUSED");
    }
    else
    {
        tft.fillRect(45, 70, SCREEN_WIDTH, 20, ST7735_BLACK);
    }
    
    tft.setRotation(0);
}

