import turtle
import  time
import pygame
  
point = turtle.Turtle()
pygame.init()

def curve_of_heart():
    for i in range(200):
        point.right(1) # corner 
        point.forward(1) # space 

def draw_heart():
    
    point.fillcolor('RED')
    #begin
    point.begin_fill()
  
    # Draw the left line
    point.left(140)
    point.forward(112)
  
    # Draw the left curve
    curve_of_heart()
    point.left(120)
  
    # Draw the right curve
    curve_of_heart()
  
    # Draw the right line
    point.forward(112)
  
    # end
    point.end_fill()
    time.sleep(6)

def main():
    draw_heart()
    point.ht()
main()
