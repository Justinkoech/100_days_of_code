from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Define starting positions

class Snake:
    def __init__(self):
        self.segments = []
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0]  # Move this line after segments are created

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)  # Use the position passed to the method
        self.segments.append(new_segment)

    def extend(self):
        # Add a new segment to the snake at the position of the last segment
        self.add_segment(self.segments[-1].position())

    def move_forwards(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
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
