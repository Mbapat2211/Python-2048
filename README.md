# Python 2048

2048 is a single player sliding block game.

## Programming

The game is purely programmed using basic concepts of the python programming language.

## Objective

The objective of the game is to move the blocks around the grid such that adjacent blocks of identical value combine to double their value (starting value = 2) in order to reach a selected target score (default target = 2048) before the selected grid (default grid = 5*5) exhausts.

## Controls

The blocks can be moved along any of the 4 directions as long as the grid permits. This movement can be done using the ASWD keys. The direction choice is taken as an input from the user and accordingly all the blocks slide along the given direction.

## Logic

The program takes user input for the direction move sequence and moves the blocks through the empty grid slots (value = 0) along the given direction. The program also checks for adjacent blocks along the same given direction bearing equal values and combines these blocks and doubles their value. Finally, at the end of each move, the program checks whether the target score has been reached for any of the blocks or if the grid has exhausted or not.   