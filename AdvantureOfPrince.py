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
#=> Global
# player
# ---------------------------------------------------------------------------
#=> VARIABLES
# ---------------------------------------------------------------------------
game_start=tk.PhotoImage(file='image/bg.png')
game_over=tk.PhotoImage(file='image/Gameover.png')
game_win=tk.PhotoImage(file='image/Gamewin.png')
game_introduction=tk.PhotoImage(file='image/introduction-of-game.png')
game_story=tk.PhotoImage(file='image/story.png')

all_levels=tk.PhotoImage(file='image/all-level.png')
button_help=tk.PhotoImage(file='image/help.png')
button_play=tk.PhotoImage(file='image/start-play.png')
button_exist=tk.PhotoImage(file='image/exist.png')
level1_list=tk.PhotoImage(file='image/level1-list.png',)
level2_list=tk.PhotoImage(file='image/level2-list.png')
level3_list=tk.PhotoImage(file='image/level3-list.png')
level1_bg=tk.PhotoImage(file='image/level1.png')
level2=tk.PhotoImage(file='image/level2.png')
level3=tk.PhotoImage(file='image/level3.png')
story_list=tk.PhotoImage(file='image/story-list.png')
slide1=tk.PhotoImage(file='image/slide1.png')
slide2=tk.PhotoImage(file='image/slide2.png')
slide3=tk.PhotoImage(file='image/slide3.png')


hero=tk.PhotoImage(file='image/Ranger.png')
flower=tk.PhotoImage(file='image/flower.png')
queen=tk.PhotoImage(file='image/queen.png')
coin=tk.PhotoImage(file='image/coin.png')
water=tk.PhotoImage(file='image/water.png')
boom=tk.PhotoImage(file='image/boom.png')
door=tk.PhotoImage(file='image/door.png')
long_wall=tk.PhotoImage(file='image/long-wall.png')
monster=tk.PhotoImage(file='image/monster.png')
fire=tk.PhotoImage(file='image/fire.png')
all_level_bg= PhotoImage(file="image/all-levels.png")
score_id = canvas.create_text(600, 15, text="Score:", font=("bold", 15))
button_exists= PhotoImage(file="image/button_exist.png")
button_level=tk.PhotoImage(file='image/button_level.png')
play_again=tk.PhotoImage(file='image/playAgain.png')
retry=tk.PhotoImage(file='image/Retry.png')
back_to_game=tk.PhotoImage(file='image/back.png')


# ---------------------------------------------------------------------------
#=> MAIN ROOT
# ---------------------------------------------------------------------------
canvas.pack(expand=True, fill='both')
root.mainloop()
