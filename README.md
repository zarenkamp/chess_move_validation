This was the coding challenge for my current job.

## Chess Move Validation 
Write a command line program that checks whether a move on a chessboard
is valid or not.

## Input
The tool shall accept two chess board coordinates (e.g. A2 B2) as input parameters. 
The first coordinate specifies the piece to move. 
The second coordinate specifies the targeted position on the board 
the piece is to be moved to.

## Output
The tool shall output if the move is valid or not.
In the case that the move is invalid an additional reason 
(e.g. “Black rook at C5 is blocking the path.“)
shall be printed.

## Limited Set of Pieces
Not all chess pieces have to be supported by the tool. 
The only mandatory pieces which have to be supported are:
•	Pawn (ignoring initial 2 spaces move)
•	Rook (ignoring castling)
•	Bishop

## Board Initialization
The initial setup of the chess board can be hard coded into the tool 
and does not have to be the normal initial chess setup. 
The board can be initialized with any number and kind of pieces at any position.

## Info
Developed in Python 3.9

### Additional info
If you are running the game in a brighter colour scheme and you are not able
to see the pieces on the board properly, you can change the colours in draw_board.py
