import tkinter as tk
from tkinter import *
from tkinter import ttk

class TrainControl( Frame ):

    #Define the structure of the GUI. Window & buttons, etc...
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Train Control")

        self.bellButton = Button( self, text = "Ring Bell", width = 25, command = self.ring_bell )
        self.bellButton.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )

        self.startButton = Button( self, text = "Start Train", width = 25, command = self.start_train )
        self.startButton.grid( row = 1, column = 1, columnspan = 2, sticky = W+E+N+S )

        self.accButton = Button( self, text = "Accelerate Train", width = 25, command = self.acc_train )
        self.accButton.grid( row = 2, column = 1, columnspan = 2, sticky = W+E+N+S )

        self.moveButton = Button( self, text = "Move Train", width = 25, command = self.move_train )
        self.moveButton.grid( row = 3, column = 1, columnspan = 2, sticky = W+E+N+S )

        self.decButton = Button( self, text = "Decelerate Train", width = 25, command = self.dec_train )
        self.decButton.grid( row = 4, column = 1, columnspan = 2, sticky = W+E+N+S )

        self.stopButton = Button( self, text = "Stop Train", width = 25, command = self.stop_train )
        self.stopButton.grid( row = 5, column = 1, columnspan = 2, sticky = W+E+N+S )

    #Listener functions for buttons
    def ring_bell(self):
        print("Ring the bell!")

    def start_train(self):
        print("Start the train!")

    def acc_train(self):
        print("Accelerate the train!")

    def move_train(self):
        print("Move the train!")

    def dec_train(self):
        print("Decelerate the train!")

    def stop_train(self):
        print("Stop the train!")

def main(): 
    TrainControl().mainloop()

if __name__ == '__main__':
    main()