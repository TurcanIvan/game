from os import system
from time import sleep
from keyboard import is_pressed
## INPUT DATA#####################################
frames     = 0

map_width  = 10
map_height = 10

invader_x  = 2
invader_y  = 1

invader_x1 = 4
invader_y1 = 1

player_x   = 10
player_y   = 10

bullet_x = 1
bullet_y = 10
bullet_shot = False

step_x   = 1

while True:
    frames += 1

    ## INVEDER MOVMENT #############################
    if invader_x != 1 and invader_x != map_width:
     invader_x += step_x
                    
    else:
        invader_y += 1
        step_x = step_x * -1
        invader_x += step_x 
        
        
    ## INVEDER MOVMENT #############################
    ## BULLET MOVMENT ##############################
    if bullet_shot and bullet_y !=1:
        bullet_y -= 1
    elif bullet_x  == invader_x and bullet_y== invader_y:
        print ("SHOT 1!!!")
    elif bullet_x  == invader_x1 and bullet_y == invader_y1:
        print("SHOT 2 !!!")
        print('YOU WIN !!!') 
        break  
    else:
        bullet_shot =False        
    ## BULLET MOVMENT ##############################
    system("cls")
     ## RENDER (SHOW) #############################
    print()
    for x in range(1,map_width+3):
        print("◻", end = " ")
    print() #"\n" - trecere din rind nou

    for y in range(1,map_height+1):
        print("◻", end = " ")
        for x in range(1,map_width+1):
            if x == invader_x and y == invader_y:
                print("🦂", end = "")
            elif x == invader_x1 and y == invader_y1:
                print("🦂", end = "")    
            elif x == player_x and y == player_y:
                print("🤖", end = "")
            elif x == bullet_x and y == bullet_y and bullet_shot:
                print("🙭", end = " ")
            else:
                print(".", end = " ")
        print("◻")


    for x in range(1,map_width+3):
        print("◻", end = " ")
    print()
    print("frames:",frames)
    print()
     ## RENDER (SHOW) #############################

     ## GAME OVER CONDITIONS ######################
    if  invader_y == map_height:
        print("GAME OVER!!!")
        break     
     ## GAME OVER CONDITIONS ######################
    sleep(0.1)
## DECISION MAKING ###########################
## INTERACT WITH PLAYER ######################
    if is_pressed("a"):
        player_x -= 1
    if is_pressed("d"):
        player_x += 1
    if is_pressed(" "):     
        bullet_shot = True
        bullet_y = map_height - 1
        bullet_x = player_x
        
## INTERACT WITH PLAYER ######################
## DECISION MAKING ###########################


##UPDATE DATA ################################
##UPDATE DATA ################################














# # # # # # # # # # # #
# . . . . . . . . . . #
# . . . . . . . . . . #
# . . . . . . . . . . #
# . . . . . . . . . . #
# . . . . . . . . . . #
# . . . . . . . . . . #
# . . . . . . . . . . #
# . . . . . . . . . . #
# . . . . . . . . . . #
# . . . . . . . . . . #
# # # # # # # # # # # #

## Special Characters 
# 🤖
# ◻
# 🙭
# ✧  
# 🦂
# 🦇

## Diagram / Lifecycle

# RENDER (SHOW)    <----    
#   |                  ^
#   |                  ^
#   |                  ^
#   v                  ^
# INTERACT WITH PLAYER ^
#   |                  ^ 
#   |                  ^
#   |                  ^
#   v                  ^
# DECISION MAKING      ^
#   |                  ^
#   |                  ^
#   |                  ^
#   v                  ^
# UPDATE DATA -------> ^







