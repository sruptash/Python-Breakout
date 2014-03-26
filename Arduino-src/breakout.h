/*
    Scott Ruptash
    Mike Bujold
    Section A2
    Michael Bowling, Walter Bischof
*/
/**********************************
    HEADER FILE FOR BREAKOUT.CPP
***********************************/

#ifndef BREAKOUT_H
#define BREAKOUT_H

#include <Adafruit_ST7735.h>

// global var needed for all source files drawing to display
extern Adafruit_ST7735 tft;

/* DEFINITIONS */
// display pins
#define TFT_CS 6  // CS line for TFT display
#define TFT_DC 7  // Data/command line for TFT
#define TFT_RST 8 // Reset line for TFT

// joystick pins and variables
#define VERT 1
#define HOR 0
#define SEL 9
#define OFFSET 60

// pause button pin
#define PAUSE 10

// speaker pin
#define SPEAKER 11

// height and width of screen
#define SCREEN_HEIGHT tft.width()
#define SCREEN_WIDTH tft.height()


/* POINT STRUCT */
typedef struct Point
{
    int x;
    int y;
} Point;


/* SHARED FUNCTIONS */
void playTone(int period, int duration);
void readJoystick(char purpose);
char getDifficulty();

#endif
