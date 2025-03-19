from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)  # Move off screen

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """Add a new segment to the snake at the position of the last segment."""
        self.add_segment(self.segments[-1].position())

    def move_forward(self):
        """Move the snake forward by shifting each segment to the position of the one ahead."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Change direction to UP if not currently moving DOWN."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change direction to DOWN if not currently moving UP."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change direction to LEFT if not currently moving RIGHT."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change direction to RIGHT if not currently moving LEFT."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
