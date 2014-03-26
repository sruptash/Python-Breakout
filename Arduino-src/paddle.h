/*
    Scott Ruptash
    Mike Bujold
    Section A2
    Michael Bowling, Walter Bischof
*/
/**********************************
    HEADER FILE FOR PADDLE.CPP
***********************************/

#ifndef PADDLE_H
#define PADDLE_H

/* DEFINITIONS */
#define PADDLE_HEIGHT 5
#define PADDLE_LEVEL 10
#define INCREMENT 3

/* EXTERN GLOBAL VARIABLES */
extern int PADDLE_WIDTH;

/* SHARED FUNCTIONS */
void drawPaddle();
void adjustPaddle(char direction);
void initializePaddle(char difficulty);
int getPaddlePosition();
void updatePaddlePos();
void shrinkPaddle();

#endif
