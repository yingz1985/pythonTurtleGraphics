#The purpose of this exercise is to create a column chart based on the user's entered values. 
#Besides creating the columns, the program also highlights the value that has the largest value.

from turtle import*
bob= Turtle()
scr=bob.getscreen()
rent= int(scr.numinput("How much for rent?","How much will you spend on rent?"))
utilities= int(scr.numinput("How much for utilities?","How much will you spend on utilities?"))
food= int(scr.numinput("How much for food?", "How much will you spend on food?"))
fun= int(scr.numinput("How much for fun?", "How much will you spend on fun?"))


bob.penup()
bob.goto(-100,0)
bob.setheading(0)
bob.pendown()

#rent bar
if rent>utilities and rent>food and rent>fun:
    bob.color("black","red")
else:
    bob.color("black","blue")
bob.begin_fill()
for i in range(2):
    bob.forward(30)
    bob.left(90)
    bob.forward(rent/3)
    bob.left(90)
bob.end_fill()

val_rent=str(rent)
bob.penup()
bob.goto(-100, rent/3+5)
bob.setheading(0)
bob.write("$"+val_rent,font=("Calibri",12,"normal"))
bob.penup()
bob.goto(-100,-20)
bob.setheading(0)
bob.write("Rent",font=("Calibri",12,"normal"))

bob.penup()
bob.goto(-50,0)
bob.setheading(0)
bob.pendown()

#utilities bar
if utilities>rent and utilities>food and utilities>fun:
    bob.color("black","red")
else:
    bob.color("black","blue")
bob.begin_fill()
for i in range(2):
    bob.forward(30)
    bob.left(90)
    bob.forward(utilities/3)
    bob.left(90)
bob.end_fill()

val_utilities=str(utilities)
bob.penup()
bob.goto(-50, utilities/3+5)
bob.setheading(0)
bob.write("$"+val_utilities,font=("Calibri",12,"normal"))
bob.penup()
bob.goto(-50,-20)
bob.setheading(0)
bob.write("Utilities",font=("Calibri",12,"normal"))


bob.penup()
bob.goto(0,0)
bob.setheading(0)
bob.pendown()

#food bar
if food>utilities and food>rent and food>fun:
    bob.color("black","red")
else:
    bob.color("black","blue")
bob.begin_fill()
for i in range(2):
    bob.forward(30)
    bob.left(90)
    bob.forward(food/3)
    bob.left(90)
bob.end_fill()

val_food=str(food)
bob.penup()
bob.goto(0, food/3+5)
bob.setheading(0)
bob.write("$"+val_food,font=("Calibri",12,"normal"))
bob.penup()
bob.goto(0,-20)
bob.setheading(0)
bob.write("Food",font=("Calibri",12,"normal"))


bob.penup()
bob.goto(50,0)
bob.setheading(0)
bob.pendown()

#fun bar
if fun>utilities and fun>food and fun>rent:
    bob.color("black","red")
else:
    bob.color("black","blue")
bob.begin_fill()
for i in range(2):
    bob.forward(30)
    bob.left(90)
    bob.forward(fun/3)
    bob.left(90)
bob.end_fill()

val_fun=str(fun)
bob.penup()
bob.goto(50, fun/3+5)
bob.setheading(0)
bob.write("$"+val_fun,font=("Calibri",12,"normal"))
bob.penup()
bob.goto(50,-20)
bob.setheading(0)
bob.write("Fun",font=("Calibri",12,"normal"))

#title
title_height= max(rent,utilities,fun,food)/3
bob.penup()
bob.goto(-70,title_height+30)
bob.write("Monthly Expenses", font=("Times new roman",14,"bold"))


