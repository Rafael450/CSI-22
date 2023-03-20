from turtle import *

def draw_poly(t, n, sz):
    width(t)
    for i in range(n):
        forward(sz)
        left(360/n)
    done()
