import turtle
import math
import random
import time

s = turtle.getscreen()
s.bgcolor("grey")
s.title("Maze Game")
s.setup(700,700)
s.tracer(0)

# Register shapes 
images = ["img/player.gif", "img/treasure.gif", "img/wall.gif", "img/enemy.gif"]

for image in images:
    turtle.register_shape(image)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("img/player.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        # Calculate the spot to move to 
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24

        # Check if the space has a wall 
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
    
    def go_down(self):
        # Calculate the spot to move to 
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        # Check if the space has a wall 
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        # Calculate the spot to move to 
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor() 

        # Check if the space has a wall 
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        # Calculate the spot to move to 
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor() 

        # Check if the space has a wall 
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
    
    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        d = math.sqrt((a ** 2) + (b ** 2))
        if d < 5:
            return True
        else:
            return False
    
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("img/treasure.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
        
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("img/enemy.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0 
        else:
            dx = 0
            dy = 0

        # Check if player is close 
        # If so, go in that direction 
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        # Calculate the spot to move to 
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            # Choose a different direction 
            self.direction = random.choice(["up", "down", "left", "right"])

        # Self timer to move next time 
        turtle.ontimer(self.move, t=random.randint(100, 300)) 
    
    def is_close(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        d = math.sqrt((a ** 2) + (b ** 2))
        if d < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle() 

levels = [""]

level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXP XXXXXXX          XXXX",
    "XX  XXXXXXX  XXXXXX  XXXX",
    "XX       XX  XXXXXX  XXXX",
    "XX       XX  XX        XX",
    "XXXXXXX  XX  XX        XX",
    "XXXXXXX  XX  XXXXX  XXXXX",
    "XXXXXXX  XX    XXX  XXXXX",
    "XX  XXX       EXXX TXXXXX",
    "XX  XXX  XXXXXXXXXXXXXXXX",
    "XX  XXX    XXXXXXXXXXXXXX",
    "XX               EXXXXXXX",
    "XXXXXXXXXXXXX     XXXX  X",
    "XXXXXXXXXXXXXXXX  XXXX  X",
    "XX  XXXXXXXXXXXX        X",
    "XX                      X",
    "XX           XXXXXXXXXXXX",
    "XXXXXXXXXXX  XXXXXXXXXXXX",
    "XXXXXXXXXXX            EX",
    "X    XXXXXX             X",
    "X    XXXXXXXXXXXX  XXXXXX",
    "X      XXXXXXXXXX  XXXXXX",
    "X           XXX         X",
    "XXXXE                   X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

turtle.hideturtle()

# Add a treasures list 
treasures = []

# Add enemies list
enemies = [] 

# Add maze to mazes list
levels.append(level_1)

# Create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            sc_x = -288 + (x*24)
            sc_y = 288 - (y*24)

            # Check if it is an X (representing a wall)
            if character == "X":
                pen.goto(sc_x, sc_y)
                pen.shape("img/wall.gif")
                pen.stamp()
                # add coordinate to wall list 
                walls.append((sc_x,sc_y))
            
            # Check if it is an P (representing the player)
            if character == "P":
                player.goto(sc_x, sc_y)

            # Check if it is a T (representing Treasure) 
            if character == "T":
                treasures.append(Treasure(sc_x, sc_y))

            # Check if it is a E (representing Enemy) 
            if character == "E":
                enemies.append(Enemy(sc_x, sc_y))

pen = Pen()
player = Player()


# Create wall coordinate List 
walls = []

# Set up levels 
setup_maze(levels[1])

# keyboard Binding
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

# turn off screen updates
s.tracer(0)

# Start moving enemies 
for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

while True: 
    # Check for player collision with treasure 
    # Iterate through treasure list 
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            s.clear()
            s.bgcolor("grey")
            turtle.hideturtle()
            turtle.write("You Win!! Score: {}".format(player.gold), align="center", font= ("Arial", 40, "bold"))
            time.sleep(3)
            exit()

    for enemy in enemies:
        if player.is_collision(enemy):
            s.clear()
            s.bgcolor("grey")
            turtle.hideturtle()
            turtle.write("You Lose!! Score: {}".format(player.gold), align="center", font= ("Arial", 40, "bold"))
            time.sleep(3)
            exit()

    s.update()
