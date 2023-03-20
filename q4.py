
from turtle import *

def spiral(size, turns, angle):
    right(90)
    pen(speed=300)
    for i in range(turns):
        forward(size + 3*i)
        right(180-angle)
    
if __name__ == '__main__':
    input('Aperte Enter para desenhar a primeira espiral')
    spiral(10, 90, 90)
    input('Aperte Enter para desenhar a segunda espiral')
    reset()
    goto(0,0)
    spiral(10, 90, 89)
    
    done()