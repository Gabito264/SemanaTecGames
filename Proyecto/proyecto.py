from turtle import *
from freegames import *
from random import randrange
player = vector(0,0)
bullet = vector(player.x,player.y)
speed = vector(5,0)
count = 0
place = [vector(-210,50), vector(180,0), vector(0,180)]
score = 0
n = [100,200,300]
target = vector(-210,50)
#dibujar el escenario, jugador y target
def draw():
    square(player.x,player.y,15,'black')
    drawPlatform()
    spawnTarget()

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

#Dibujar la arena de combate
def drawPlatform():
    square(-250,-500,500,'grey')

#mostrar un disparo hacia la derecha
def shootRight():
    clear()
    draw()
    bullet.x=200
    goto(bullet.x,bullet.y)
    dot(20,'red')

    ontimer(bulletClear, 100)
    checkKill()

#mostrar disparo hacia la izquierda
def shootLeft():
    clear()
    draw()
    bullet.x=-210
    goto(bullet.x,bullet.y)
    dot(20,'red')

    ontimer(bulletClear, 100)
    checkKill()

#mostrar un disparo para arriba
def shootUp():
    clear()
    draw()
    bullet.y=180
    goto(bullet.x,bullet.y)
    dot(20,'red')

    ontimer(bulletClear, 100)
    checkKill()

#seleccionador hacia dónde dispara el jugador dependiendo de las arrowkeys
def getshot(n):
    bullet.x = player.x+7
    bullet.y = player.y+7
    if n == 1:
        shootRight()
    if n ==2:
        shootLeft()
    if n == 3:
        shootUp()

#borrar disparo
def bulletClear():
    clear()
    draw()
#checar si el jugador le dió al objetivo, para aumentar el score
def checkKill():
    global score
    if target == place[0] and bullet.x == -210 and bullet.y >target.y-15 and bullet.y <target.y+15:
        Kill = True
        score+=1
        print("score")
        print(score)
    if target == place[1] and bullet.x == 200 and bullet.y >target.y-15 and bullet.y <target.y+15:
        Kill = True
        score+=1
        print("score")
        print(score)
    if target == place[2] and bullet.y == 180 and bullet.x >-50 and bullet.x <50:
        Kill = True
        score+=1
        print("score")
        print(score)

#dibujar el target, que cambia de lugar cada cierto movimiento del jugador
def spawnTarget():
    global count
    global target
    if count < n[0]:
        target = place[0]
    if count >= n[0] and count <n[1]:
        target = place[1]
    if count >= n[1] and count <n[2]:
        target = place[2]
    count += 1
    if count == n[2]:
        count = 0
        n[0]-=10
        n[1]-=10
        n[2]-=10
    square(target.x,target.y,30,'green')


#Datos para iniciar turtle
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
onkey(lambda: getshot(3), 'Up')
fall()
spawnTarget()
done()