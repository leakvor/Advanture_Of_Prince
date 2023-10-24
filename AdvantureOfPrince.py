#============================ IMPORTS ============================
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
import time
# from random import randrange
import random
# ---------------------------------------------------------------------------
#=> CONSTANT
# ---------------------------------------------------------------------------

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 740
GRAVITY_FORCE = 9
JUMP_FORCE = 22
SPEED = 5
TIMED_LOOP = 10

#=> Global
# ---------------------------------------------------------------------------
score=0
notEvent=False
hight_score=0
keyPressed = []
coin_score=1
water_score=5
fire_score=10
isWin=False
isLose=False

# ---------------------------------------------------------------------------
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
root.title('Advanture OF Prince')
canvas = tk.Canvas(root)




# ---------------------------------------------------------------------------
#=> MAIN ROOT
# ---------------------------------------------------------------------------
canvas.pack(expand=True, fill='both')
root.mainloop()
