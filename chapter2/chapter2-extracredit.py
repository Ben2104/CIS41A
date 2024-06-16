import turtle
import math

# Prompt the user for the width and height of the graphics window
width = int(input("Enter the width of the graphics window: "))
height = int(input("Enter the height of the graphics window: "))

# Prompt the user for the radius of the circle
radius = int(input("Enter the radius of the circle: "))

# Prompt the user for the outline and fill colors
outline_color = input("Enter the outline color of the circle: ")
fill_color = input("Enter the fill color of the circle: ")

# Set up the graphics window
turtle.setup(width, height)
window = turtle.Screen()
window.title("Circle Drawer")

# Create a turtle to draw the circle
circle_turtle = turtle.Turtle()

# Move the turtle to the starting position
circle_turtle.penup()
circle_turtle.goto(0, -radius)
circle_turtle.pendown()

# Set the outline and fill colors
circle_turtle.color(outline_color, fill_color)

# Begin filling the circle
circle_turtle.begin_fill()

# Draw the circle
circle_turtle.circle(radius)

# End filling the circle
circle_turtle.end_fill()

# Calculate the circumference and area of the circle
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Print the circumference and area
print(f"Circumference of the circle: {circumference:.2f}")
print(f"Area of the circle: {area:.2f}")

# Hide the turtle and display the window
circle_turtle.hideturtle()
turtle.done()

"""
Example Results:
Enter the width of the graphics window: 500
Enter the height of the graphics window: 500
Enter the radius of the circle: 100
Enter the outline color of the circle: black
Enter the fill color of the circle: red
Circumference of the circle: 628.32
Area of the circle: 31415.93

Enter the width of the graphics window: 500
Enter the height of the graphics window: 500
Enter the radius of the circle: 150
Enter the outline color of the circle: blue
Enter the fill color of the circle: yellow
Circumference of the circle: 942.48
Area of the circle: 70685.83
"""
