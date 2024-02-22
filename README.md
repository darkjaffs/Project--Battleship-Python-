# Project--Battleship-Python-

(This game was made by me previously in C++ and then translated in python for CS50 Final Project. I decided to push it to github recently)

# DESCRIPTION:

In BATTLESHIP THE GAME, you are basically playing a guessing game with the computer, according to the size of the grid you select (between 6 and 9). The computer will randomly hide 4 ships in the grid. 1 carriership which occupies 5 spaces, 1 battleship which occupies 4 spaces and 2 frigates which occupies 2 spaces each. Our job is to guess where the ship are hidden before the ammunition runs out (amount of ammunition = gridsize * gridsize / 2). The player inputs the row and column of the place where they think the ship is hidden and depending on the fact, they missed or hit, the updated grid is shown on the screen. Once the user destroys atleast 70 % structure of each of the ships or he runs out of ammunition, the game ends. After the game ends, the user is shown the actual location of the ships and a prompt showing whether they won or lost.

The project only contains one file main.py which the python which includes all the code of the game. I have used multiple functions in the file and all the things that are happeing have been divided into multiple functions and called in main function instead of them being only in the main function. I have also made a function to clear screen instead of directly calling the command. In the program, I have used two global lists in which all the working is being performed. One list consists of only integers and the other consists of characters which are being displayed. Both lists are running simultaneously and changes are effecting each other at the same time as well. This enable us to perform the tasks we require in the background effectively without effecting much of the display. I have basically used functions to do everything so that it becomes easier to handle for errors and further new changes can be implemented easily. This makes our program more versatile and efficient since it is open to new changes and implementing them won’t effect the whole program or create errors elsewhere

I have a very important function which is called the game mechanics where all of the magic happens. Here all the background logic of the game does its work like keeping track of the hits and misses then ending incase we have won. Everything is done here.

I have also used a separate funtion to record user input and another important thing to note is I have used try and except in multiple places to tackle any errors that may occur throughout the program.

Separate functions have been used for assignment of spaces to each of the ships in the background list. So basically the background list consists of all zeros but where there are ships it consists of some numbers. We assigned 1 for frigate ship, 2 for carrier ship and 3 for battleship so we can differentiate between them by the numbers that have been assigned to the background grid. This helps assign the visible list and help to differentiate between them

Win check function is used which check whether we have destroyed enough ships or not by counting the number of shots on target.