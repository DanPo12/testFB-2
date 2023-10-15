# mon gros test
def main():
  import os
  from turtle import Turtle

  # Set the terminal window size (rows x columns)
  rows = 400  # Set the number of rows you want
  columns = 600  # Set the number of columns you want

  # Use ANSI escape codes to set the window size
  os.system(f"printf '\033[8;{rows};{columns}t'")

  # https://docs.python.org/3/library/turtle.html#turtle.Turtle
  # https://docs.python.org/3/library/turtle.html#turtle.Screen
    
  t = Turtle()
  t.width(3)          # set the width to something exemple 2 pixels 
  t.screen.bgcolor("white")
  drawAxes()
  drawCircles()
  # Your code to draw circles
  input("Press Enter to exit...")

def drawCircles():
  from turtle import Turtle

  t = Turtle()
  t.home()
  # print(t.pos())
  radius = 150
  numberOfCircles = 1
  for _i in range(numberOfCircles):  # draw circles
    t.penup()         # not to start drawing yet
    t.goto(0,-radius) # 
    t.pendown()       # now get ready to write so put the pen to paper
    t.circle(radius)  # this will draw the desired circle
    radius *= 2       # increase the radius of the next circle
    t.penup()         # not to start drawing yet

def drawAxes():
  from turtle import Turtle

  t = Turtle()
  t.width(3)          # set the width to something exemple 2 pixels 
  t.screen.bgcolor("white")
  t.penup()
  t.home()    
  t.width(1) 
  t.goto(-200, 0)  # Start drawing the x-axis from the left
  t.pendown()
  t.forward(400)  # Draw the x-axis to the right
  t.penup()
  t.goto(0, -200)  # Start drawing the y-axis from the bottom
  t.setheading(90)  # Turn to draw the y-axis upwards
  
  t.pendown()
  t.forward(400)  # Draw the y-axis upwards
  
  # Add unit marks on the x-axis
  for x in range(-180, 200, 20):  # Adjust the range and step size as needed
      t.penup()
      t.goto(x, -5)  # Position the mark below the x-axis
      t.pendown()
      t.goto(x, 5)  # Draw the mark above the x-axis
  
  # Add unit marks on the y-axis
  for y in range(-180, 200, 20):  # Adjust the range and step size as needed
      t.penup()
      t.goto(-5, y)  # Position the mark to the left of the y-axis
      t.pendown()
      t.goto(5, y)  # Draw the mark to the right of the y-axis
  
  t.penup()
  t.home() 
  t.goto(0,-7)
  t.write("X", True, align="center" )
  
  t.goto(-5,5)
  t.write((0,0), True, align="right" )
  
  t.goto(-2,200)
  t.write("+Y", True, align="right" )
  t.goto(-2,-200)
  t.write("-Y", True, align="right" )
  
  t.goto(-200,2)
  t.write("-X", True, align="right" )
  t.goto(200,2)
  t.write("+X", True, align="right" )
  # t.penup()
  t.goto(20,-20)
  t.write("20", True, align="center" )
  
main()
