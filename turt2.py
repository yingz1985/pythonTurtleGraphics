#Name: Ying Zhang


from turtle import*
bob = Turtle()
screen = bob.getscreen()
seed_string = screen.textinput("Seed String", "Enter seed string: ")
angle = screen.numinput("Angle", "Enter angle: ")
distance = screen.numinput("Distance", "Enter distance: ")
production_rule = screen.numinput("Production Rule", "Enter the number of production rules: ")

target = []
replacement = []
while production_rule >0:
    val = screen.textinput("Target Character", "Enter target character: ")
    target.append(val)
    rep = screen.textinput("Replacement Character", "Enter replacement character: ")
    replacement.append(rep)
    production_rule-=1
    
ini_depth = screen.numinput("Depth", "Enter desired depth: ")
bob.speed(0)

bob.penup()
bob.goto(-150,-100)         #different starting point to fit prompt image
bob.pendown()


def drawLSystem (string,angle,distance):
    global bob
    for letter in string:
        if letter == "F":
            bob.forward(distance)


        elif letter == "+":
            bob.right(angle)

        elif letter == "-":
            bob.left(angle)

def productionRules(old_val,new_val):  #take in two lists
    productionRules = {o:n for o, n in zip(old_val,new_val)}

    return productionRules
            
def deriveLSystem(seed,productions,depth):
    if depth <=0:
        return seed
    else:
        result_seed= ""
        for char in seed:
            if char in productions.keys():
                result_seed += productions[char]
            else:
                result_seed +=char

    return deriveLSystem(result_seed,productions,depth-1)


rule = productionRules(target,replacement)
end_string = deriveLSystem(seed_string,rule,ini_depth)
drawLSystem(end_string,angle,distance)

    
    
        
