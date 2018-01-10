#Ying Zhang


from turtle import*
bob= Turtle()
scr=bob.getscreen()
rows=int(scr.numinput("# of rows", "How many rows would you like?",5,1,10))
columns=int(scr.numinput("# of columns", "How many columns would you like?",5,1,10))
size=int(scr.numinput("length of a side of a square", "Length of a side of a square",25,10,50))
c1=scr.textinput("first color","Choose your first color")
c2=scr.textinput("second color","Choose your second color")
c3=scr.textinput("third color", "Choose your third color")

def draw_square(size):
    global bob
    bob.setheading(0)
    bob.begin_fill()
    for i in range(4):
        bob.forward(size)
        bob.left(90)
        bob.speed(0)
    bob.end_fill()
        

def draw_checker_board():
    global bob
    bob.goto(0,0)
    for r in range(rows):
        for c in range(columns):
            if (r+c)%3==0:
                color=c1
            if (r+c)%3==1:
                color=c2
            if (r+c)%3==2:
                color=c3
            bob.color("black",color)
            bob.begin_fill()
            bob.penup()
            bob.goto(c*size,r*size)
            bob.pendown()
            draw_square(size)
draw_checker_board()
    
