import turtle
import math

finestra = turtle.Screen() #creates an object from turtle.Screen 
finestra.bgcolor("orange") #sets some settings of the object



side =200

def square_diagonal(squareSide):
	diagonal= squareSide * (math.sqrt(2))
	return diagonal

def drawing_square():
	
	
	primaTartaruga = turtle.Turtle() #creates object from class
	primaTartaruga.shape("turtle") #sets some settings of the object
	primaTartaruga.color("black")
	primaTartaruga.speed(2)
	
	count = 0
	while (count < 4) :
		primaTartaruga.forward(side)
		primaTartaruga.right(90)
		count = count +1

def draw_circle():
	secondaTartaruga = turtle.Turtle()
	secondaTartaruga.color("blue")
	
	secondaTartaruga.circle(side)
	
def draw_triangle():
	terzaTartaruga = turtle.Turtle()
	terzaTartaruga.color("red")
	terzaTartaruga.right(45)
	count = 0
	while (count < 3) :
		terzaTartaruga.forward(square_diagonal(side))
		terzaTartaruga.right(120)
		count = count +1
	
	

drawing_square()
draw_circle()
draw_triangle()
finestra.exitonclick()





