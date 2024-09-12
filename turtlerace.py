from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=500,height=400)
colors=["red","blue","orange","pink","purple","black"]
your_bet=screen.textinput(title="user_bet",prompt="guess who is your bet,enter color")
y_distance=[-100,-60,-20,20,60,100]
all_turtle=[]
for index in range(0,6):
    tim=Turtle(shape="turtle")
    tim.color(colors[index])
    tim.pensize(15)
    tim.penup()
    tim.goto(x=-230,y=y_distance[index])
    all_turtle.append(tim)
is_on=False

if your_bet:
    is_on =True
    
while is_on:
    
    for tim in all_turtle:
        
        if tim.xcor()>230:
            is_on=False
            winning_color=tim.pencolor() 
            if winning_color==your_bet:
             print(f"your guess was right,your color{winning_color} won!!!")
            
            else:
             print("your guess was wrong,your color{winning_color} lost!!!")
        rand_distance=random.randint(0,10)
        tim.forward(rand_distance)
screen.exitonclick()