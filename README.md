# OO code using turtle graphics
> *This is a part of my University assignment.*

## Files
- `polygon_art_original.py` is the original unedited code provided by the instructor.
- `polygon_art.py` is the program I wrote.
- `/example art pieces` contains the art pieces output from my program.

## Overview
- I completed the program and there's no bug in it (according to the scope of the program)
```
class Canvas:
    def melody()
    def setup_polygon()
    def draw_polygon()
    def move_to_next_layer()
    def randomize_values()
    def clear()

class Painter
    def hear()
    def think()
```

## How it works

### Basic
- Declare an object with the `Painter` class. and use the `hear` method to get inputs.
```
Keen = Painter()
Keen.hear()

turtle.done()
```
- The output will ask you for a number between 1 to 9, you can input as many time as you want **without having to re-run** the program.
```
Which art do you want to generate? Enter a number between 1 to 9 inclusive: 6
Which art do you want to generate? Enter a number between 1 to 9 inclusive: 10
10 is not between 1 to 9
Which art do you want to generate? Enter a number between 1 to 9 inclusive: _<
```

### Extra
> *I did this purely for fun haha*
- You can create a **custom canvas** with different paint speed and background color and give it to the painter. For example this will make the background of the canvas blue:
```
c = Canvas(bgcolor='blue')

Keen = Painter(c)
Keen.hear()

turtle.done()
```
