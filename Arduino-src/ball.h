/*
    Scott Ruptash
    Mike Bujold
    Section A2
    Michael Bowling, Walter Bischof
*/
/**********************************
    HEADER FILE FOR BALL.CPP
***********************************/

#ifndef BALL_H
#define BALL_H

/* DEFINITIONS */
#define BALL_RADIUS 2

/* SHARED FUNCTIONS */
void drawBall();
void initializeBall(char difficulty);
void updateBallPos();
bool ballOnPaddle();
void launchBall();

#endif

