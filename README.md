# Train Control Embedded System
### Assignment 2 - Group 7

The goal of this program is to control the train in Lab ECSS 3.217 at The University of Texas at Dallas. The program has a GUI with buttons on it. Each button is a function to control the train.

- Button (Ring the bell): a command is sent to the train to ring the bell
- Button (Start the train): a command is sent to the train to start the train
- Button (Accelerate the train): a command is sent to the train to accelerate
- Button (Move the train): a command is sent to the train to move the train
- Button (Decelerate the train): a command is sent to the train to decelerate the train
- Button (Stop the train): a command is sent to the train to stop the train

This was made for CS 4397 (Embedded Systems) at the University of Texas at Dallas, taught by Dr. Farokh Bastani.

## Setup

### Windows

1. Open Powershell
2. Change the current directory to be this folder.
3. Run python through the python provided with the script. The command will be:
```
./python/python.exe train.py
```

## How this procedure differs from the development of a general purpose application

The goal of this program is more specific than the general-purpose application. The program just focuses to control the train in Lab ECSS 3.217. It does not need to handle any other system. Therefore, the program does not have dynamic data structures or general functions.
