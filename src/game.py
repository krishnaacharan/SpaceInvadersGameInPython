import pygame
import random
import math
pygame.init()
screen=pygame.display.set_mode((800,600))
bg=pygame.image.load("space.jpg")
pygame.display.set_caption("SPACE INVADERS")
logo=pygame.image.load("rocket.png")
pygame.display.set_icon(logo)
player=pygame.image.load("rocket1.png")
bgs=pygame.image.load("bgs.jpg")
playerX=380
playerY=490
playerXChange=0
def Player(x,y):
    screen.blit(player,(x,y))
go=False
enemy=[]
enemyX=[]
enemyY=[]
enemyXChange=[]
enemyYChange=[]
numOfEnem=6
for i in range(numOfEnem):
    enemy.append(pygame.image.load("ufo.png"))
    enemyX.append(random.randint(0,746))
    enemyY.append(random.randint(10,70))
    enemyXChange.append(1)
    enemyYChange.append(40)

def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(bgs,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',60)
        L1 = largetext.render("SPACE", True, (000, 000, 000))
        screen.blit(L1, (130, 250))
        L = largetext.render("INVADERS", True, (255, 255, 255))
        screen.blit(L,(420,250))
        button("START",150,520,100,50,(255,255,255),(255,0,0),"play")
        button("QUIT", 550, 520, 100, 50, (255,255,255),(0,0,255), "quit")
        button("INSTRUCTION", 300, 520, 200, 50, (255,255,255),(0,255,0), "intro")
        pygame.display.update()

def button(msg,x,y,w,h,ic,ac,action=None):
    global score
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(screen,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                game()
            elif action=="quit":
                pygame.quit()
                quit()
            elif action=="intro":
                introduction()
            elif action=="menu" :
                intro_loop()

    else:
        pygame.draw.rect(screen ,ic,(x,y,w,h))
    smalltext=pygame.font.Font('freesansbold.ttf',25)
    s= smalltext.render(msg, True, (0, 0, 0))
    screen.blit(s,(x+15,y+15))

def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(bgs,(0,0))
        large=pygame.font.Font('freesansbold.ttf',80)
        small=pygame.font.Font('freesansbold.ttf',20)
        medium=pygame.font.Font('freesansbold.ttf',40)
        r=small.render("You are lost in space alone........",True,(0,0,0))
        screen.blit(r,(30,200))
        r = small.render("Aliens started attacking you.Save yourself", True,
                         (255, 255, 255))
        screen.blit(r, (360, 200))
        l=large.render('IN                   NS',True,(255,255,255))
        screen.blit(l,(100,100))
        q = large.render('STRUCTIO', True, (0, 0, 0))
        screen.blit(q, (170, 100))
        s1 = small.render('ARROW LEFT : Left turn', True, (0, 0, 0))
        screen.blit(s1, (150, 400))
        s2 = small.render('RIGHT LEFT : Right turn', True, (0, 0, 0))
        screen.blit(s2, (150, 450))
        s4 = small.render('SPACE : Shoot', True, (0, 0, 0))
        screen.blit(s4, (150, 500))
        m1 = medium.render('CONT ', True, (0,0,0))
        screen.blit(m1, (300, 300))
        mD = medium.render(' ROLS', True, (255, 255, 255))
        screen.blit(mD, (400, 300))
        s3 = small.render('P : Pause', True, (0, 0, 0))
        screen.blit(s3, (150, 550))
        s3 = small.render('R : Resume', True, (0, 0, 0))
        screen.blit(s3, (250, 550))
        button("BACK",600,450,100,50,(250,123,213),(241,231,123),"menu")
        pygame.display.update()

def Enemy(x,y):
    for i in range(numOfEnem):
        screen.blit(enemy[i],(x,y))

bullet=pygame.image.load("bullet.png")
bulletX=0
bulletY=500
bulletYChange=15
bulletState="ready"

score=0
font=pygame.font.Font('freesansbold.ttf',32)
Ofont=pygame.font.Font('freesansbold.ttf',64)
Wfont=          pygame.font.Font('freesansbold.ttf',64)
textX=10
textY=10
def pause():
    P = Wfont.render("| |", True, (255, 255, 255))
    screen.blit(P,(350,280))

def play():
    screen.blit(player, (350, 280))
def Iwin():
    w = Wfont.render("Hurray!! YOU WON", True, (255, 255, 255))
    screen.blit(w,(130,250))
    button("MENU", 250, 520, 100, 50, (255, 255, 255), (0, 0, 255), "menu")
    button("RESTART", 550, 520, 150, 50, (255, 255, 255), (0, 0, 255), "play")
def gameOver():
    G = Ofont.render("YOU LOST!!!!", True, (255, 255, 255))
    screen.blit(G,(200,250))
    button("MENU", 250, 520, 100, 50, (255, 255, 255), (0, 0, 255), "menu")
    button("RESTART", 550, 520, 150, 50, (255, 255, 255), (0, 0, 255), "play")
def Score(x,y):
    s=font.render("Score :"+str(score),True,(255,255,255))
    screen.blit(s,(x,y))
def Bullet(x,y):
    global bulletState
    bulletState = "fire"
    screen.blit(bullet,(x+16,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    D=math.sqrt(math.pow(enemyX-bulletX,2)+(math.pow(enemyY-bulletY,2)))
    if D<27:
        return True
    else:
        return False
def game():
    go=True
    textX = 10
    textY = 10
    playerX = 380
    global playerY
    playerXChange = 0
    bulletX = 0
    bulletY = 500
    bulletYChange = 15
    global bulletState
    global score
    score=0
    for j in range(numOfEnem):
        enemyY[j] = -60
    p=True
    q=True
    k=True
    while go:
        screen.fill((239, 245, 245))
        screen.blit(bg,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if p is True:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        playerXChange=-7
                    if event.key==pygame.K_RIGHT:
                        playerXChange=7
                    if event.key==pygame.K_SPACE:
                        if bulletState is "ready":
                            bulletX=playerX
                            Bullet(bulletX, bulletY)
                    if event.key == pygame.K_p:
                        playerXChange = 0
                        k=False
                        q=False
                        p = False
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_r:
                    play()
                    p=True
                    q=True
                    k=True
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    playerXChange=0;

        if playerX<=0:
            playerX=0
        if playerX>=746:
            playerX=746
        if bulletState is "fire":
            Bullet(bulletX,bulletY)
            bulletY-=bulletYChange
        if bulletY<=0:
            bulletY=490
            bulletState="ready"

        playerX+=playerXChange
        Player(playerX,playerY)
        if q is False:
            button("MENU", 250, 520, 100, 50, (255, 255, 255), (0, 0, 255), "menu")
        if k is False:
            pause()
            for i in range(numOfEnem):
                Enemy(enemyX[i], enemyY[i])
        if k is True:
            for i in range (numOfEnem):
                global l
                l=4
                if score>=15:
                    l=6
                if enemyY[i]>460:
                    for j in range(numOfEnem):
                        enemyY[j]=2000
                    gameOver()
                    break
                enemyX[i]+=enemyXChange[i]
                if enemyX[i] <= 0:
                    enemyX[i] = 0
                if enemyX[i] >= 746:
                    enemyX[i] = 746
                if enemyX[i]<=0:
                    enemyXChange[i]=l
                    enemyY[i] += enemyYChange[i]
                if enemyX[i]>=746:
                    enemyXChange[i]=-l
                    enemyY[i] += enemyYChange[i]
                Enemy(enemyX[i],enemyY[i])
                collision=isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
                if collision:
                    bulletY=490
                    bulletState="ready"
                    score+=1
                    enemyX[i] = random.randint(0, 746)
                    enemyY[i] = random.randint(10, 80)
                if score==30:
                    for j in range(numOfEnem):
                        enemyY[j]=-60
                    Iwin()
                    break

        Score(textX,textY)
        pygame.display.update()
intro_loop()
