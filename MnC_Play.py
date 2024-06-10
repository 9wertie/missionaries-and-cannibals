import pygame
import time
import random


w, h = 600, 400
win = pygame.display.set_mode((w, h))
pygame.font.init() 
my_font = pygame.font.SysFont('Comic Sans MS', 18)


def missionaries_left(count):
    for i in range(count):
        missionary = pygame.Rect(10,30*i+10,20,20)
        pygame.draw.rect(win , "green" , missionary)

def cannibals_left(count):
    for i in range(count):
        cannibal = pygame.Rect(40,30*i+10,20,20)
        pygame.draw.rect(win , "red" , cannibal)

def missionaries_right(count):
    for i in range(count):
        missionary = pygame.Rect(570,30*i+10,20,20)
        pygame.draw.rect(win , "green" , missionary)

def cannibals_right(count):
    for i in range(count):
        cannibal = pygame.Rect(540,30*i+10,20,20)
        pygame.draw.rect(win , "red" , cannibal)

def boat(side):
    if side == 0:
        boat = pygame.Rect(80,200,70,40)
        pygame.draw.rect(win , "white" , boat)
    elif side == 1:
        boat = pygame.Rect(460,200,70,40)
        pygame.draw.rect(win , "white" , boat)

def addToBoat(who):
    if(pos[6]==0):
        if who=="M" and (pos[4]+pos[5])<2 and pos[0]>0:
            pos[0]-=1
            pos[4]+=1
            boatQ.append("M")
        elif who=="C" and (pos[4]+pos[5])<2 and pos[1]>0:
            pos[1]-=1
            pos[5]+=1
            boatQ.append("C")
    elif(pos[6]==1):
        if who=="M" and (pos[4]+pos[5])<2 and pos[2]>0:
            pos[2]-=1
            pos[4]+=1
            boatQ.append("M")
        elif who=="C" and (pos[4]+pos[5])<2 and pos[3]>0:
            pos[3]-=1
            pos[5]+=1
            boatQ.append("C")

def setBoat():
    if(pos[6]==0):
        c=0
        for i in boatQ:
            if(i=="M"):
                missionary = pygame.Rect(boatloc[c][0],boatloc[c][1],20,20)
                pygame.draw.rect(win , "green" , missionary)
                c+=1
            elif(i=="C"):
                cannibal = pygame.Rect(boatloc[c][0],boatloc[c][1],20,20)
                pygame.draw.rect(win , "red" , cannibal)
                c+=1
    elif(pos[6]==1):
        c=2
        for i in boatQ:
            if(i=="M"):
                missionary = pygame.Rect(boatloc[c][0],boatloc[c][1],20,20)
                pygame.draw.rect(win , "green" , missionary)
                c+=1
            elif(i=="C"):
                cannibal = pygame.Rect(boatloc[c][0],boatloc[c][1],20,20)
                pygame.draw.rect(win , "red" , cannibal)
                c+=1

fail = [False]
won = [False]

def travel():
    if(pos[4]+pos[5]>=1):
        if(pos[6]==0):
            pos[2]+=pos[4]
            pos[3]+=pos[5]
            pos[4]=0
            pos[5]=0
            pos[6]=1
            boatQ.clear()
            if((pos[2]!=0 and pos[3]>pos[2]) or (pos[0]!=0 and pos[1]>pos[0])):
                fail[0] = True
            if (pos[0]==0 and pos[1]==0 and pos[2]==3 and pos[3]==3):
                won[0]=True

        elif(pos[6]==1):
            pos[0]+=pos[4]
            pos[1]+=pos[5]
            pos[4]=0
            pos[5]=0
            pos[6]=0
            boatQ.clear()
            if((pos[2]!=0 and pos[3]>pos[2]) or (pos[0]!=0 and pos[1]>pos[0])):
                fail[0] = True

def emptyBoat():
    if(pos[6]==0):
        pos[0]+=pos[4]
        pos[1]+=pos[5]
        pos[4]=0
        pos[5]=0
        boatQ.clear()
    elif(pos[6]==1):
        pos[2]+=pos[4]
        pos[3]+=pos[5]
        pos[4]=0
        pos[5]=0
        boatQ.clear()

boatloc = [[90,210],[120,210],[470,210],[500,210]]
boatQ = []


pos = [3,3,0,0,0,0,0]
def main():
    run = True
    busy_SPACE = False
    busy_DOWN = False
    busy_c = False
    busy_m = False 
    winner = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        reset = pygame.Rect(0,0,w,h)
        pygame.draw.rect(win , "black" , reset)
        

        if(not fail[0] and not won[0]):
            missionaries_left(pos[0])
            cannibals_left(pos[1])
            boat(pos[6])
            missionaries_right(pos[2])
            cannibals_right(pos[3])
            setBoat()

            pygame.display.update()


            keys = pygame.key.get_pressed()
            if keys[pygame.K_m] and busy_m == False:
                busy_m=True
                addToBoat("M")
            
            elif keys[pygame.K_c] and  busy_c == False:
                busy_c=True
                addToBoat("C")


            elif keys[pygame.K_SPACE] and  busy_SPACE == False:
                busy_SPACE=True
                travel()


            elif keys[pygame.K_DOWN] and  busy_DOWN == False:
                busy_DOWN=True
                emptyBoat()
            
            if not(keys[pygame.K_DOWN]):
                busy_DOWN=False
            if not(keys[pygame.K_SPACE]):
                busy_SPACE=False
            if not(keys[pygame.K_m]):
                busy_m=False
            if not(keys[pygame.K_c]):
                busy_c=False

        elif (fail[0] and not won[0]):
            reset = pygame.Rect(0,0,w,h)
            pygame.draw.rect(win , "black" , reset)
            pygame.font.init() 
            the_font = pygame.font.SysFont('Comic Sans MS', 72)
            text_surface = my_font.render("FAIL!", 1, (255, 0, 0))
            win.blit(text_surface, (250,150))
            pygame.display.update()
        
        elif (not fail[0] and won[0]):
            reset = pygame.Rect(0,0,w,h)
            pygame.draw.rect(win , "black" , reset)
            pygame.font.init() 
            the_font = pygame.font.SysFont('Comic Sans MS', 72)
            text_surface = my_font.render("WON!", 1, (0, 255, 0))
            win.blit(text_surface, (250,150))
            pygame.display.update()

    pygame.quit()



if __name__ == "__main__":
    main()