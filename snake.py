from turtle import Turtle

# Initial positions for the snake segments
positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in positions:
            self.add_segment(position)

    def add_segment(self,position):
        new_turtle = Turtle("square")  # Create a new Turtle object for each segment
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtles.append(new_turtle)
    def reset(self):
        for turtle in self.turtles:
            turtle.goto(1000,1000)
        self.turtles.clear()
        self.create_snake()
        self.head=self.turtles[0]
    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def move(self):
        # Move segments starting from the tail to the head
        for segment in range(len(self.turtles) - 1, 0, -1):
            new_x_cord = self.turtles[segment - 1].xcor()
            new_y_cord = self.turtles[segment - 1].ycor()
            self.turtles[segment].goto(new_x_cord, new_y_cord)
        self.head.forward(move_distance)

    # Snake movement functions
    def up(self):
        if self.head.heading() != 270:  # Prevent moving in the opposite direction
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
