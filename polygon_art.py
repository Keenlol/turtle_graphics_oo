import turtle
import random

class Canvas:

    def __init__(self, speed: int = 0, 
                 bgcolor: str='black', 
                 tracer: int = 0, 
                 colormode: int = 255):
        turtle.speed(speed)
        turtle.bgcolor(bgcolor)
        turtle.tracer(tracer)
        turtle.colormode(colormode)
        self.__range_layers = [1,1]
        self.__range_num_sides = [3,6]
        self.__range_num_shapes = [30,40]
        self.randomize_values()

    def randomize_values(self):
        self.__layers = random.randint(self.__range_layers[0],self.__range_layers[1])
        self.__num_sides = random.randint(self.__range_num_sides[0], self.__range_num_sides[1])
        self.__num_shapes = random.randint(self.__range_num_shapes[0],self.__range_num_shapes[1])

        self.__color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.__location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.__size = random.randint(50, 150)
        self.__orientation = random.randint(0, 90)
        self.__location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.__border_size = random.randint(1, 10)
        self.__reduction_ratio = 0.618

    def melody(self,
                 range_layers : list, 
                 range_num_sides : list,
                 range_num_shapes : list):

        self.__range_layers = range_layers
        self.__range_num_sides = range_num_sides
        self.__range_num_shapes = range_num_shapes

        for _ in range(self.__num_shapes):
            self.randomize_values()
            self.setup_shape()
            for _ in range(self.__layers):
                self.draw()
                self.move_to_next_layer()

    def setup_shape(self):
        turtle.penup()
        turtle.goto(self.__location[0], self.__location[1])
        turtle.setheading(self.__orientation)
        turtle.color(self.__color)
        turtle.pensize(self.__border_size)

    def draw(self):
        turtle.pendown()
        for _ in range(self.__num_sides):
            turtle.forward(self.__size)
            turtle.left(360/self.__num_sides)
        turtle.penup()

    def move_to_next_layer(self):
        self.__size *= self.__reduction_ratio
        turtle.penup()
        turtle.forward(self.__size*(1-self.__reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(self.__size*(1-self.__reduction_ratio)/2)
        turtle.right(90)



# draw a polygon at a random location, orientation, color, and border line thickness


# specify a reduction ratio to draw a smaller polygon inside the one above

# reposition the turtle and get a new location


c = Canvas()
c.melody([1,4], [3,4], [10,10])
# adjust the size according to the reduction ratio

# draw the second polygon embedded inside the original 

# hold the window; close it by clicking the window close 'x' mark
turtle.done()