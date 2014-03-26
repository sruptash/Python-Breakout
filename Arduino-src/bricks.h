/*
    Scott Ruptash
    Mike Bujold
    Section A2
    Michael Bowling, Walter Bischof
*/
/**********************************
    HEADER FILE FOR BRICKS.CPP
***********************************/

#ifndef BRICKS_H
#define BRICKS_H

#include "breakout.h"

/* DEFINITIONS */
#define BRICK_WIDTH 19
#define BRICK_HEIGHT 9
#define BRICKS_PER_ROW 8
#define BRICK_ROWS 5
#define BRICK_TOTAL 40

/* SHARED FUNCTIONS */
char drawBricks(Point* p);

#endif
