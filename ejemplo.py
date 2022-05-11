from turtle import *
shape('turtle')
color('purple','cyan')
begin_fill() #dibujar forma que se rellene
while True:
    forward(200) #mueve la tortuga hacia adelante
    left(170) #Gira hacia la izquierda
    if abs(pos())<1:
        break
end_fill()
done()