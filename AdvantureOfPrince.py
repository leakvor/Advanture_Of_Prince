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

 # ==================  PLAYER ===============
player_id=canvas.create_image(20,50, image = hero)

#=========================== ALL LEVELS =======================
def alllevels():
    canvas.delete("all")
    canvas.create_image(1,0, image = all_level_bg, anchor = "nw")
    # ______________________________LEVEL1_____________________________________
    canvas.create_image(200,250, image = level1_list, anchor = "nw", tags="level1-")
    # ______________________________LEVEL2_______________________________________
    canvas.create_image(565,250, image = level2_list, anchor = "nw", tags="level2-")
    # ______________________________LEVEL3_______________________________________
    canvas.create_image(950,250, image = level3_list, anchor = "nw", tags="level3-")
    canvas.create_image(20,20, image =button_exist, anchor = "nw",tags="backhome")

#===========================LEVEL1 =======================
def level01(event):
    canvas.delete("all")
    global player_id, score_id
    canvas.create_image(0,0,image=level1_bg, anchor='nw')
    canvas.create_image(20,20, image =button_exist, anchor = "nw",tags="backhome")
# ==================  DOOR  ===============
    canvas.create_image(1290,30, image=door , tags="DOOR", anchor=NW)
# ==================  LONG STONE IMAGE ===============
    canvas.create_image(500,500, image = long_wall , tags="PLATFORM", anchor=NW)
    canvas.create_image(10,530, image = long_wall , tags="PLATFORM", anchor=NW)
    canvas.create_image(750,600, image = long_wall , tags="PLATFORM", anchor=NW)
    canvas.create_image(250,400, image = long_wall ,tags="PLATFORM", anchor=NW)
    canvas.create_image(380,230, image = long_wall ,tags="PLATFORM", anchor=NW)
    canvas.create_image(650,180, image = long_wall ,tags="PLATFORM", anchor=NW)
    canvas.create_image(680,380, image = long_wall ,tags="PLATFORM", anchor=NW)
    canvas.create_image(1000,190, image = long_wall ,tags="PLATFORM", anchor=NW)
    canvas.create_image(1100,380, image = long_wall ,tags="PLATFORM", anchor=NW)
    canvas.create_image(920,490, image = long_wall ,tags="PLATFORM", anchor=NW)
    canvas.create_image(1225,100, image = long_wall ,tags="PLATFORM", anchor=NW)
    # ================== COIN IMAGE ======================
    canvas.create_image(150, 480, image = coin , tags = "COIN", anchor=NW)
    canvas.create_image(720, 330, image = coin , tags = "COIN", anchor=NW)
    canvas.create_image(720, 130, image = coin , tags = "COIN", anchor=NW)
    # ==================  WATER IMAGE ===============
    canvas.create_image(500,200, image=water, tags="WATER")
    canvas.create_image(550,470, image=water, tags="WATER")
    canvas.create_image(1000,460, image=water, tags="WATER")
    canvas.create_image(340,370, image=water, tags="WATER")
    canvas.create_image(1060,160, image=water, tags="WATER")
    # ================== BOOM IMAGE =================
    canvas.create_image(610,485, image=boom, tags="BOOM")
    # ================== FIRE IMAGE =================
    canvas.create_image(440,210, image=fire,tags="FIRE")
    canvas.create_image(800,360, image=fire,tags="FIRE")
    canvas.create_image(1120,170, image=fire,tags="FIRE")
    # ==================  PLAYER ===============
    player_id = canvas.create_image(30,50, image = hero, anchor=NW)
    # ==================  MONSTER IMAGE ===============
    canvas.create_image(820,560, image=monster, tags="MONSTER")
    canvas.create_image(1200,340, image=monster, tags="MONSTER")
    # ================== FLOWER IMAGE ==================
    canvas.create_image(900,580, image=flower)
    canvas.create_image(660,160, image=flower)
    canvas.create_image(1373,70, image=flower)
    canvas.create_image(1110,360, image=flower)
    gravity()

# =======================> LEVEL_2 <==========================

def level02(event):
    global player_id, score_id
    canvas.delete("all")
    canvas.create_image(0,0,image=level2,anchor='nw')
    canvas.create_image(20,20, image =button_exist, anchor = "nw",tags="backhome")

    # ============= long_wall =================

    canvas.create_image(0,650, image=long_wall, tags='PLATFORM', anchor=NW)
    canvas.create_image(150,250, image = long_wall , tags="PLATFORM", anchor=NW)
    canvas.create_image(200, 450, image= long_wall, tags='PLATFORM', anchor=NW)
    canvas.create_image(420, 550, image=long_wall, tags='PLATFORM', anchor=NW)
    canvas.create_image(400, 150, image=long_wall, tags='PLATFORM', anchor=NW)
    canvas.create_image(420, 350, image=long_wall, tags='PLATFORM', anchor=NW)

    canvas.create_image(650,450, image=long_wall, tags='PLATFORM', anchor=NW)
    canvas.create_image(650, 250, image=long_wall, tags='PLATFORM', anchor=NW)
    canvas.create_image(650, 650,image=long_wall, tags='PLATFORM', anchor=NW)
    canvas.create_image(850, 350, image=long_wall, tags='PLATFORM', anchor=NW)
    canvas.create_image(850, 150, image=long_wall, tags='PLATFORM', anchor=NW)
    canvas.create_image(1050, 250, image= long_wall, tags='PLATFORM', anchor=NW)
    canvas.create_image(1050, 450, image=long_wall,  tags='PLATFORM', anchor=NW)
    canvas.create_image(1200, 650, image=long_wall,  tags='PLATFORM', anchor=NW)
    canvas.create_image(1250, 400, image=long_wall, tags='PLATFORM', anchor=NW)
    canvas.create_image(950, 600, image=long_wall, tags='PLATFORM', anchor=NW)    

    # =============== DOOR ====================
    canvas.create_image(1335,330, image=door , tags="DOOR", anchor=NW)

    # =============== WATER ===================
    canvas.create_image(1150, 380, image= water, tags='WATER', anchor=NW)
    canvas.create_image(700, 180, image= water, tags='WATER', anchor=NW)
    canvas.create_image(240, 190, image= water, tags='WATER', anchor=NW)
    canvas.create_image(500, 480, image= water, tags='WATER', anchor=NW)

    # =============== FIRE ===================
    canvas.create_image(420, 300, image=fire, tags ='FIRE', anchor=NW)
    canvas.create_image(1300, 600, image=fire, tags ='FIRE', anchor=NW)
    canvas.create_image(750, 600, image=fire, tags ='FIRE', anchor=NW)

    # =============== BOOM ===================
    canvas.create_image(1080, 420, image=boom, tags='BOOM', anchor=NW)

    # =============== MONSTER ===================
    canvas.create_image(950, 260, image=monster, tags='MONSTER', anchor=NW)
    canvas.create_image(200, 360, image=monster, tags='MONSTER', anchor=NW)

    # =============== RANGER ===================
    canvas.create_image(150, 600, image=hero, anchor=NW)

    # =============== COIN ===================
    
    canvas.create_image(460, 100, image=coin, tags='COIN', anchor=NW)
    canvas.create_image(500, 300, image=coin, tags='COIN', anchor=NW)
    canvas.create_image(1100, 200, image=coin, tags='COIN', anchor=NW)
    canvas.create_image(1200, 600, image=coin, tags='COIN', anchor=NW)

    #   =============== PLAYER ===================
    
    player_id = canvas.create_image(30,50, image = hero, anchor=NW)
    canvas.create_rectangle(0,730,SCREEN_WIDTH,SCREEN_HEIGHT,fill="black",tags="PLATFORM")
    #   =============== PLAYER ===================
    score_id = canvas.create_text(1300, 15, text="Score:", font=("bold", 15), fill='white')
    gravity()

    #=========================== LEVEL3 =======================

def level03(event):
    global player_id
    canvas.delete("all")
    canvas.create_image(0,0,image=level3,anchor='nw')
    canvas.create_image(20,20, image =button_exist, anchor = "nw",tags="backhome")
# ========================== WHITE STONE IMAGE ================

    canvas.create_image(0, 650, image = long_wall, tags = "PLATFORM", anchor=NW)
    canvas.create_image(600, 330, image = long_wall, tags = "PLATFORM", anchor=NW)
    canvas.create_image(400, 430, image = long_wall,  tags = "PLATFORM", anchor=NW)
    canvas.create_image(200, 530, image = long_wall, tags = "PLATFORM", anchor=NW)
    canvas.create_image(800, 230, image = long_wall, tags = "PLATFORM", anchor=NW)
    canvas.create_image(1000, 130, image = long_wall, tags = "PLATFORM", anchor=NW)
    canvas.create_image(330, 230, image = long_wall, tags = "PLATFORM", anchor=NW)
    canvas.create_image(550, 130, image =long_wall, tags = "PLATFORM", anchor=NW)
    
    canvas.create_image(400, 650, image =long_wall, tags = "PLATFORM", anchor=NW)
    canvas.create_image(700, 580, image = long_wall, tags = "PLATFORM", anchor=NW)
    canvas.create_image(900, 450, image = long_wall, tags = "PLATFORM", anchor=NW)
    canvas.create_image(550, 650, image = long_wall, tags = "PLATFORM", anchor=NW)
    canvas.create_image(1110, 350, image = long_wall, tags = "PLATFORM", anchor=NW)
    canvas.create_image(1250, 530, image = long_wall, tags = "PLATFORM", anchor=NW)
    canvas.create_image(1250, 700, image = long_wall, tags = "PLATFORM", anchor=NW)
    canvas.create_image(950, 650, image = long_wall, tags = "PLATFORM", anchor=NW)
    canvas.create_image(1250, 230, image = long_wall, tags = "PLATFORM", anchor=NW)
    canvas.create_image(120, 130, image = long_wall, tags = "PLATFORM", anchor=NW)
# =========================== PLAYER =============================
    # canvas.create_image(100,550, image = hero, anchor=NW)
# =========================== PRINCESS ===========================
    canvas.create_image(1300,600, image = queen, tags = "QUEEN", anchor=NW)
# =========================== MONSTER ============================
    canvas.create_image(500, 350, image = monster, tags = "MONSTER", anchor=NW)
    canvas.create_image(90, 40, image = monster, tags = "MONSTER", anchor=NW)
    canvas.create_image(1050, 560, image = monster, tags = "MONSTER", anchor=NW)
# =========================== WATER IMAGE ========================
    canvas.create_image(250,460, image = water, tags = 'WATER', anchor=NW)
    canvas.create_image(700,265, image = water, tags = 'WATER', anchor=NW)
    canvas.create_image(350,170, image = water, tags = 'WATER', anchor=NW)
    canvas.create_image(1330,470, image = water, tags = 'WATER', anchor=NW)
# =========================== COIN IMAGE =========================
    canvas.create_image(300,480, image = coin, tags = "COIN", anchor=NW)
    canvas.create_image(1000,400, image = coin, tags = "COIN", anchor=NW)
    canvas.create_image(420,180, image = coin, tags = "COIN", anchor=NW)
    canvas.create_image(250,80, image = coin, tags = "COIN", anchor=NW)
    canvas.create_image(600,600, image = coin, tags = "COIN", anchor=NW)
    canvas.create_image(820,530, image = coin, tags = "COIN", anchor=NW)
    canvas.create_image(1000,80, image = coin, tags = "COIN", anchor=NW)
# =========================== FIRE IMAGE =========================
    canvas.create_image(500,600, image = fire, tags = "FIRE", anchor=NW)
    canvas.create_image(1250,480, image = fire, tags = "FIRE", anchor=NW)
    canvas.create_image(1110, 310, image = fire, tags = "FIRE", anchor=NW)
    # canvas.create_image(110, 600, image = fire, tags = "FIRE", anchor=NW)
# =========================== BOOM IMAGE =========================
    canvas.create_image(620,300, image = boom, tags = "BOOM", anchor=NW)
    canvas.create_image(750,550, image = boom, tags = "BOOM", anchor=NW)
    canvas.create_image(1350,200, image = boom, tags = "BOOM", anchor=NW)
# =========================== PLAYER IMAGE =========================
    canvas.create_rectangle(0,730,SCREEN_WIDTH,SCREEN_HEIGHT,fill="black",tags="PLATFORM")
    player_id=canvas.create_image(100,200, image = hero, anchor=NW)
    score_id = canvas.create_text(1300, 15, text="Score:", font=("bold", 15), fill='white')
    gravity()
# ---------------------------------------------------------------------------

# ==============> Indroduction <==================
def introdution(event):
    canvas.delete("all")
    canvas.create_image(1, 0, image=game_introduction, anchor = 'nw')
    canvas.create_image(20,20, image =button_exist, anchor = "nw",tags="backhome")
# ==============> Story <==================
def story(event):
    canvas.delete("all")
    canvas.create_image(1, 0, image=game_story, anchor = 'nw')
    canvas.create_image(20,20, image =button_exist, anchor = "nw",tags="backhome")
# ---------------------------------------------------------------------------
def back(event):
    canvas.delete("all")
    home()
#=> CREATE GAME SHOW
# ---------------------------------------------------------------------------
def home():
    canvas.create_image(1, 0, image=game_start, anchor='nw')
    canvas.create_image(500,500,image=story_list, tags="story")
    canvas.create_image(700,500, image=button_play, tags="startgame")
    canvas.create_image(900,500,image=button_help, tags="help")
    # winsound.PlaySound("sound/open.mp3",winsound.SND_FILENAME | winsound.SND_ASYNC)

####### START GAME ######3
def startGame(event):
    canvas.delete('all')
    showSlid1()
    # winsound .PlaySound("Audioes\space-war.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
def showSlid1():
    canvas.create_image(1,0,image=slide1,anchor='nw')
    canvas.after(1000,showSlid2)
def showSlid2():
    canvas.create_image(1,0,image=slide2, anchor='nw')
    canvas.after(1000,showSlid3)
def showSlid3():
    canvas.create_image(1,0,image=slide3, anchor='nw')
    canvas.create_text(700,420,text="Loading...",font=('sansarif',28,'bold'),fill='white')
    canvas.after(2000,alllevels)

def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(player_id)
    platforms = canvas.find_withtag("PLATFORM")
    if coord[0] + dx < 0 or coord[0]+hero.width() + dx > SCREEN_WIDTH:
        return False
    if checkGround:
        overlap = canvas.find_overlapping(coord[0]+hero.width(), coord[1], coord[0]+ hero.width() , coord[1]+hero.height() + dy)
    else:
        overlap = canvas.find_overlapping(coord[0]+dx, coord[1]+dy, coord[0]+dx, coord[1]+ hero.width())
    for platform in platforms:
        if platform in overlap:
            return False
    return True
# ==============> WHEN JUMP <==================

def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player_id, 0, -force)
            root.after(TIMED_LOOP, jump, force-1)
def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()
def move():
    global score
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            x -= SPEED
        if "Right" in keyPressed:
            x += SPEED
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        if check_movement(x):
            canvas.move(player_id, x, 0)
        root.after(TIMED_LOOP, move)
# ==============>GRAVITY <==================        
def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player_id, 0, GRAVITY_FORCE)
    root.after(TIMED_LOOP, gravity)
def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)

#=> ALLOW WINDOWS KEYS AND TAGES BIND
# ---------------------------------------------------------------------------
# root.bind("<w>", movePlayerUp)
# root.bind("<s>", movePlayerDown)
# root.bind("<Button-3>", createBullet)
canvas.tag_bind("help","<Button-1>",introdution )
canvas.tag_bind("story","<Button-1>", level01)
canvas.tag_bind("backhome","<Button-1>", back)
canvas.tag_bind("button_level","<Button-1>", alllevels)
canvas.tag_bind("startgame","<Button-1>", startGame )
canvas.tag_bind("level1-","<Button-1>", level01 )
canvas.tag_bind("level2-","<Button-1>", level02 )
canvas.tag_bind("level3-","<Button-1>", level03 )
root.bind("<Key>", start_move)
root.bind("<KeyRelease>", stop_move)

#=> MAIN ROOT
# ---------------------------------------------------------------------------
canvas.pack(expand=True, fill='both')
home()
root.mainloop()
canvas.pack(expand=True, fill='both')
root.mainloop()
