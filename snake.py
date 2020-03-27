import pygame
import time
import random
class cube(object):
    def __init__(self,color,pos):
        self.color=color
        self.pos=pos
        self.dirnx=1
        self.dirny=0
        self.xs , self.ys = 10 , 10
        self.count = 0
        self.turnPos= []
        self.dirList = []

    def draw(self,surface):


        i = self.pos[0]
        j= self.pos[1]

        pygame.draw.rect(surface, (255,0,0), [i*20,j*20,20,20])






    def checkBoundary(self):
        if self.pos[0] > 25 and self.pos[1]<25:
            self.pos[0]=0
        elif self.pos[0]<25 and self.pos[1]>25:
            self.pos[1]=0
        elif self.pos[0]<25 and self.pos[1]<0:
            self.pos[1]=25
        elif self.pos[0]<0 and self.pos[1]<25:
            self.pos[0]=25


    def moveCube(self):
        self.pos[0]=self.pos[0]+self.dirnx
        self.pos[1]=self.pos[1]+self.dirny

    def snack(self,surface,i,j):
        pygame.draw.circle(surface, (255,0,0), [10+20*i,10+20*j], 5)




    def snakeMove(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            turnPos=[]
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirList.append([self.dirnx,self.dirny])
                    if self.dirnx == 1 and self.dirny==0:
                        self.dirnx=0
                        self.dirny=1
                    elif self.dirnx==-1 and self.dirny==0:
                        self.dirnx=0
                        self.dirny=-1
                    elif self.dirnx==0 and self.dirny==1:
                        self.dirnx=-1
                        self.dirny=0
                    elif self.dirnx==0 and self.dirny==-1:
                        self.dirnx=1
                        self.dirny=0
                    self.turnPos.append(self.pos)



                elif keys[pygame.K_RIGHT]:
                    self.dirList.append([self.dirnx,self.dirny])
                    if self.dirnx == 1 and self.dirny==0:
                        self.dirnx=0
                        self.dirny=-1
                    elif self.dirnx==-1 and self.dirny==0:
                        self.dirnx=0
                        self.dirny=1
                    elif self.dirnx==0 and self.dirny==1:
                        self.dirnx=1
                        self.dirny=0
                    elif self.dirnx==0 and self.dirny==-1:
                        self.dirnx=-1
                        self.dirny=0
                    self.turnPos.append(self.pos)
        self.moveCube()



class snake(object):
    def __init__(self,cubes):
        self.cubes=cubes

    def drawCubes(self,surface):
        drawGrid(20,25,surface)
        self.drawSnack(surface)
        for cub in self.cubes:
            if type(cub)==cube:
                cub.draw(surface)
        pygame.display.update()
    def drawSnack(self,surface):
        print(self.cubes[0].xs,self.cubes[0].ys)
        self.cubes[0].snack(surface,self.cubes[0].xs,self.cubes[0].ys)
        if (self.cubes[0].xs == self.cubes[0].pos[0] and self.cubes[0].ys == self.cubes[0].pos[1]):
            self.cubes[0].count+=1
            self.cubes[0].xs=random.randint(1,24)
            self.cubes[0].ys=random.randint(1,24)
            self.cubes[0].snack(surface,self.cubes[0].xs,self.cubes[0].ys)

    # def turn(self):
    #     for x in range(len(self.cubes)):
    #         if x>0 and len(self.cubes[0].turnPos)!=0:
    #             while self.cubes[x].pos != self.cubes[0].turnPos:
    #                 self.cubes[x].moveCube()




def drawGrid(w, rows, surface):
    surface.fill(BLAKC)
    sizeBtwn = w

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        pygame.draw.line(surface, WHITE, (x,0),(x,500))
        pygame.draw.line(surface, WHITE, (0,y),(500,y))

WHITE = (255, 255, 255)
BLAKC = (0,0,0)
RED=(0,255,0)

(width, height) = (500, 500)
screen = pygame.display.set_mode((width, height))
screen.fill(WHITE)
drawGrid(20,25,screen)
c=cube(RED ,[10,10])

running = True
snakeBody=[c]
s=snake(snakeBody)
clock=pygame.time.Clock()
while running:

    pygame.time.delay(50)
    if c.count>0:
        if len(snakeBody) != (c.count+1):
            snakeBody.append(0)
        for x in range(c.count):
            if c.dirnx == 1 and c.dirny==0:
                snakeBody[x+1]=cube(RED ,[c.pos[0]-(x+1),c.pos[1]])
            elif c.dirnx==-1 and c.dirny==0:
                snakeBody[x+1]=cube(RED, [c.pos[0]+(x-1),c.pos[1]])
            elif c.dirnx==0 and c.dirny==1:
                snakeBody[x+1]=cube(RED, [c.pos[0]-1,c.pos[1]-x])
            elif c.dirnx==0 and c.dirny==-1:
                snakeBody[x+1]=cube(RED, [c.pos[0]-1,c.pos[1]+x])


            # if snakeBody[x].pos != c.turnPos[-1]:
            #     snakeBody[x].dirnx=c.dirList[-1][0]
            #     snakeBody[x].dirny=c.dirList[-1][1]




    for a in snakeBody:
        if a!=0:
            a.snakeMove()
            a.checkBoundary()



    s.drawCubes(screen)
