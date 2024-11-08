import turtle
import random

class Canvas:

    def __init__(self, speed: int = 0,
                 bgcolor: str = 'black',
                 tracer: int = 0,
                 colormode: int = 255):
        """
        Create the canvas with the given values

        Args:
            speed (int): How fast to draw, 10-1 for fast-slow, 0 for fastest.
            bgcolor (str): The bankground color of the canvas.
            tracer (int): Set delay for update drawings, must be a non-negative integer.
            colormode (int): Set the RGB value scale, 1.0 or 255.
        """
        turtle.speed(speed)
        turtle.bgcolor(bgcolor)
        turtle.tracer(tracer)
        turtle.colormode(colormode)

    def melody(self,
               range_num_layers: list,
               range_num_sides: list,
               range_num_polygon: list):
        """
        Create the artwork with the given randomize range of layers, sides and shapes.
        (the artist's melody)

        Args: Range of values, for example [a, b] is 'from a to b inclusively'
            range_num_layers (list): Range for randomizing number of indented polygon layers. 
            range_num_sides (list): Range for randomizing number of polygon sides.
            range_num_polygon (list): Range for randomizing number of polygon.
        """
        self.__range_num_layers = range_num_layers
        self.__range_num_sides = range_num_sides
        self.__range_num_polygon = range_num_polygon

        self.randomize_values()
        for _ in range(self.__num_shapes):
            self.randomize_values()
            self.setup_polygon()
            for _ in range(self.__num_layers):
                self.draw_polygon()
                self.move_to_next_layer()

    def setup_polygon(self):
        """
        Set the color, location, orientation and the border size 
        of the shape before drawing.
        """
        turtle.penup()
        turtle.goto(self.__location[0], self.__location[1])
        turtle.setheading(self.__orientation)
        turtle.color(self.__color)
        turtle.pensize(self.__border_size)

    def draw_polygon(self):
        """ Draw the polygon with the indicated shape onto the canvas."""
        turtle.pendown()
        for _ in range(self.__num_sides):
            turtle.forward(self.__size)
            turtle.left(360/self.__num_sides)
        turtle.penup()

    def move_to_next_layer(self):
        """ Go reposition into the inner layer of the polygon."""
        turtle.penup()
        turtle.forward(self.__size*(1-self.__reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(self.__size*(1-self.__reduction_ratio)/2)
        turtle.right(90)

        self.__location[0] = turtle.pos()[0]
        self.__location[1] = turtle.pos()[1]

        self.__size *= self.__reduction_ratio


    def randomize_values(self):
        """ Randomize all the value to get ready to draw the next shape."""
        self.__num_layers = random.randint(self.__range_num_layers[0], self.__range_num_layers[1])
        self.__num_sides = random.randint(self.__range_num_sides[0], self.__range_num_sides[1])
        self.__num_shapes = random.randint(self.__range_num_polygon[0], self.__range_num_polygon[1])

        self.__color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.__location = [random.randint(-250, 250), random.randint(-170, 170)]
        self.__size = random.randint(50, 150)
        self.__orientation = random.randint(0, 90)
        self.__border_size = random.randint(1, 10)
        self.__reduction_ratio = 0.618
    
    def clear(self):
        """ Clear the paintings from the canvas"""
        turtle.clear()


class Painter:

    def __init__(self, canvas: Canvas = Canvas()) -> None:
        """
        A painter
        
        Args:
            canvas (Canvas): Canvas that the painter will be painting on.
        """
        self.__canvas = canvas

    def hear(self):
        """ Tell Painter what to do, will ask for an input"""
        while True:
            self.__task_set = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
            if not (1 <= self.__task_set <= 9):
                print(f"{self.__task_set} is not between 1 to 9")
                continue
            self.brain()

    def brain(self):
        """ Painter's vital organs for processing given task and will paint accordingly."""
        self.__canvas.clear()

        if self.__task_set % 4 != 0 and self.__task_set != 9:
            range_num_sides = [self.__task_set % 4 + 2, self.__task_set % 4 + 2]
        else:
            range_num_sides = [3, 5]
        
        if self.__task_set <= 4:
            range_num_layers = [1, 1]
        elif self.__task_set <= 8:
            range_num_layers = [3, 3]
        else:
            range_num_layers = [1, 3]
        
        range_num_polygon = [20, 30]
        self.__canvas.melody(range_num_layers, range_num_sides, range_num_polygon)


# Main 
Josh = Painter()
Josh.hear()

turtle.done()
