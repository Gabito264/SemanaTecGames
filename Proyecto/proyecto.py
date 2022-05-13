from turtle import *
from freegames import *

player = vector(0,0)
bullet = vector(player.x,player.y)
speed = vector(5,0)
count = 0
place = [vector(-210,50), vector(180,50), vector(0,180)]
score = 0
Kill = False
n = [100,200,300]
target = vector(-210,50)
#dibujar el jugador
def draw():
    global score
    global Kill
    square(player.x,player.y,15,'black')
    drawPlatform()
    if Kill==False:
        spawnTarget()
    if Kill== True:
        score+=1
        print(score)
        Kill = False
#mover el jugador hacia la derecha
def forward():
    clear()
    player.x+=75
    draw()
    
#mover el jugador hacia la izquierda
def back():
    clear()
    player.x-=75
    draw()
#Hacer el jugador que salte
def jump():
    if player.y < 200:
        player.y+=50
        clear()
        draw()
        
#Gravedad del sistema
def fall():
    if player.y >0:
        clear()
        player.y-=5
        draw()
    ontimer(fall, 50)
#Dibujar el límite del jugador
def drawPlatform():
    square(-250,-500,500,'grey')
#mostrar un disparo hacia la derecha
def shootRight():
    clear()
    draw()
    bullet.x=200
    goto(bullet.x,bullet.y)
    dot(20,'red')
    global count
    count+=1
    ontimer(bulletClear, 100)
#mostrar disparo hacia la izquierda
def shootLeft():
    clear()
    draw()
    bullet.x=-210
    goto(bullet.x,bullet.y)
    dot(20,'red')
    global count
    count+=1
    ontimer(bulletClear, 100)
#seleccionador de hacia dónde dispara el jugador
def getshot(n):
    bullet.x = player.x+7
    bullet.y = player.y+7
    if n == 1:
        shootRight()
    if n ==2:
        shootLeft()
#borrar disparo
def bulletClear():
    clear()
    draw()

#def checkKill():


def spawnTarget():
    global count
    global target
    if count < n[0]:
        target = place[0]
    if count > n[0] and count <n[1]:
        target = place[1]
    if count > n[1] and count <n[2]:
        target = place[2]
    count += 1
    if count == n[2]:
        count = 0
        n[0]-=10
        n[1]-=10
        n[2]-=10
    square(target.x,target.y,30,'green')
    #ontimer(spawnTarget,10)










setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
draw()
drawPlatform()
onkey(lambda: forward() , 'd')
onkey(lambda: back(), 'a')
onkey(lambda: jump(), 'w')
onkey(lambda: getshot(1), 'Right')
onkey(lambda: getshot(2), 'Left')
fall()
spawnTarget()
done()