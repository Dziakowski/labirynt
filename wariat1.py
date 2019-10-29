import os
#import random
import platform

os.system('clear')

room = {    1:['▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒'],
        2:['▒',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▒'], # |
        3:['▒',' ',' ',' ',' ',' ',' ',' ',' ','▒','▒','▒','▒',' ',' ','▒'], # |
        4:['▒',' ',' ',' ',' ',' ',' ','▒',' ','▒',' ',' ',' ',' ',' ','▒'], # |
        5:['▒',' ',' ',' ',' ',' ','@','▒',' ','▒',' ',' ','▒',' ',' ','▒'], # |
        6:['▒',' ',' ',' ',' ',' ',' ','▒',' ',' ',' ',' ','▒',' ',' ','▒'], # x
        7:['▒',' ',' ',' ',' ','▒','▒','▒',' ','▒','▒',' ','▒',' ',' ','▒'], # |
        8:['▒',' ',' ',' ',' ',' ',' ',' ',' ',' ','▒','▒','▒',' ',' ','▒'], # |
        9:['▒',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','▒'], # |
       10:['▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒','▒']} # |
        # <------------------------------y--------------------------------->

stuff  = {'wall'  :  "▒",
          'player':  "@",
          'empty' :  " "}

def gamemap():
    for i in range(1,len(room)+1):
        print("".join(room[i]))

gamemap()

import keyboard #Using module keyboard
while True:  #making a loop
    try:  #used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('up'): #if key 'up' is pressed.You can use right,left,up,down and others
            print('You Pressed UP!')
            break #finishing the loop
        elif keyboard.is_pressed('down'):
            print('You Pressed DOWN!')
            break
        elif keyboard.is_pressed('left'):
            print('You Pressed LEFT!')
            break
        elif keyboard.is_pressed('right'):
            print('You Pressed RIGHT!')
            break
        else:
            pass
    except:
        break  #if user pressed other than the given key the loop will break