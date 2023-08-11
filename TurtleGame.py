import turtle
import random as rand


Running = True
t = turtle.Turtle()
rocks = turtle.Turtle()
rocks.color("gray")
rocks.hideturtle()
rocks.penup()
rocks.shape("square")
rock1 = rocks.clone()
rock2 = rocks.clone()
rock3 = rocks.clone()
rock4 = rocks.clone()
s = turtle.Screen()
s.bgcolor("black")
t.color("blue")
t.shape("turtle")
t.pencolor("blue")
t.pensize(5)
s.screensize(400, 400)
ValedMoves = ["w", "a", "s", "d"]
RocksPos = []

# rockx = rand.randrange(-400, 400)
# rocky = rand.randrange(-400, 400)
# RocksPos.append(list[int(rockx), int(rocky)])
# rock1.setx(RocksPos[0][0])
# rock1.sety(RocksPos[0][1])


def RockSetUp():
    result = {}
    rock1x = rand.randrange(-400, 400)
    rock1y = rand.randrange(-400, 400)
    result["r1"] = [int(rock1x), int(rock1y)]
    # RocksPos.append([int(rock1x), int(rock1y)])
    rock1.setx(rock1x)
    rock1.sety(rock1y)
    rock1.showturtle()
    rock2x = rand.randrange(-400, 400)
    rock2y = rand.randrange(-400, 400)
    result["r2"] = [int(rock2x), int(rock2y)]
    # RocksPos.append([int(rock2x), int(rock2y)])
    rock2.setx(rock2x)
    rock2.sety(rock2y)
    rock2.showturtle()
    rock3x = rand.randrange(-400, 400)
    rock3y = rand.randrange(-400, 400)
    result["r3"] = [int(rock3x), int(rock3y)]
    # RocksPos.append([int(rock3x), int(rock3y)])
    rock3.setx(rock3x)
    rock3.sety(rock3y)
    rock3.showturtle()
    rock4x = rand.randrange(-400, 400)
    rock4y = rand.randrange(-400, 400)
    result["r4"] = [int(rock4x), int(rock4y)]
    # RocksPos.append([int(rock4x), int(rock4y)])
    rock4.setx(rock4x)
    rock4.sety(rock4y)
    rock4.showturtle()
    return result


# RockSetUp()

rock_group = RockSetUp()
print(rock_group["r1"])

while Running:
    hasMadeMove = False
    move = input("Blue turn: \n")
    moveid = -1
    ValedMovesID = -1
    hasMadeMove = False
    for i in range(len(move)):
        moveid += 1
        if move[moveid] == "w" and hasMadeMove == False:
            heading = t.heading()
            posV = t.pos
            # pos = list(posV)
            # print(t.pos.__dict__)
            t.setheading(90)
            t.forward(20)
            hasMadeMove == True
        elif move[moveid] == "a" and hasMadeMove == False:
            t.setheading(180)
            t.forward(20)
            hasMadeMove == True
        elif move[moveid] == "s" and hasMadeMove == False:
            t.setheading(270)
            t.forward(20)
            hasMadeMove == True
        elif move[moveid] == "d" and hasMadeMove == False:
            t.setheading(0)
            t.forward(20)
            hasMadeMove == True
        if t.distance(rock_group["r1"][0], rock_group["r1"][1]) < 20.1:
            t.color("red")
            Running = False
        elif t.distance(rock_group["r2"][0], rock_group["r2"][1]) < 20.1:
            t.color("red")
            Running = False
        elif t.distance(rock_group["r3"][0], rock_group["r3"][1]) < 20.1:
            t.color("red")
            Running = False
        elif t.distance(rock_group["r4"][0], rock_group["r4"][1]) < 20.1:
            t.color("red")
            Running = False
