from turtle import *

def draw_square(size):
    for _ in range(4):
        forward(size)
        left(90)
    
if __name__ == '__main__':
    speed(20)
    for i in range(5):
        pendown()
        draw_square(20 + 20*i)
        penup()
        right(90)
        forward(10)
        right(90)
        forward(10)
        right(180)
    done()