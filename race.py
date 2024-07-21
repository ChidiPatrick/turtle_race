from turtle import Turtle, Screen
import random

colors = ["red","orange","yellow","blue","green","purple"]
all_turtle = []
y_pos = -110

race_is_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput("Place your bet!!!",prompt= "Which turtle will win the race? Enter a color:").lower()


for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230,y= y_pos)
    all_turtle.append(new_turtle)
    y_pos += 40

if user_bet:
    race_is_on = True

while race_is_on:
    
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner")
            else:
                print(f"You've lost! The {winning_color} is the winner")
        
        rand_distance = random.randint(0,6)
        turtle.forward(rand_distance)



screen.exitonclick()
