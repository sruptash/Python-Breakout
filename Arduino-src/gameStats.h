/*
    Scott Ruptash
    Mike Bujold
    Section A2
    Michael Bowling, Walter Bischof
*/
/**********************************
    HEADER FILE FOR GAMESTATS.CPP
***********************************/

#ifndef GAMESTATS_H
#define GAMESTATS_H

/* DEFINITIONS */
#define STARTING_LIVES 3

/* SHARED FUNCTIONS */
void initializeScore(char difficulty);
void increaseScore(int points);
void decreaseLives();
int getScore();
int getLivesLeft();
void resetAll();
void displayStats();
void endGame();
void pauseGame(bool paused);

#endif
