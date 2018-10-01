"""
File : TriHexFractal.py
Language : python3
Author : Steven Hulbert <sdh2110@rit.edu>
Purpose : Recursively generates a glowing hexagonal shaped fractal with user
determined settings
"""

import turtle

# Declare defaults for the global variables determining the hexagons settings
HEX_SIZE = 250
GAP_SIZE = 5
LAYER_COUNT = 4
GLOW_LAYERS = 30
CENTER_EDGE_WIDTH = 0.3
GLOW_WIDTH = 60
GLOW_MULTIPLIER = (GLOW_WIDTH / CENTER_EDGE_WIDTH) ** (1.0 / GLOW_LAYERS)


def initialize_turtle():
    """ Position turtle so that the hexagon will be centered in window
    """
    turtle.hideturtle()
    turtle.up()
    turtle.right(90)
    turtle.forward(HEX_SIZE)
    turtle.left(120)


def draw_single_triangle(length):
    """
    Draws a single triangle counterclockwise in the direction the turtle is facing.
    :param length: the length of each side of the triangle
    """
    # Assume pen was left up, so place pen down
    turtle.down()

    # Draw triangle
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)

    # Return the pen to its lifed position
    turtle.up()


def draw_single_hexagon(length):
    """
    Draws a single hexagon counterclockwise in the direction the turtle is facing.
    :param length: the length of each side of the hexagon
    """
    # Assume pen was left up, so place pen down
    turtle.down()

    # Draw triangle
    for i in range(6):
        turtle.forward(length)
        turtle.left(60)

    # Return the pen to its lifed position
    turtle.up()


def fractal_triangle(length, recursions):
    """
    Recursively fractals out a single triangle counterclockwise in the
    direction the turtle is facing. A single hexagon will be drawn within the
    center of the triangle with three additional triangles filling in the
    remaining corners of the larger triangle. Each of these inner shapes will
    be recursively fractaled as well.
    :param length: the length of each side of the main triangle
    :param recursions: the amount of recursions left for this triangle
    """
    # Set length for inner triangles
    # The length of the hexagons will = new_length + (GAP_SIZE * 0.87735)
    new_length = ((length - (4.6188 * GAP_SIZE)) / 3) - (0.57735 * GAP_SIZE)

    # Fractal out this triangle if not the last recursion and if the inner shapes will be visible
    if recursions > 1 and new_length + (GAP_SIZE * 0.87735) > 0:
        # Iteratively draw each side of the triangle and the inner triangles
        for side in range(3):
            # Draw one side
            turtle.down()
            turtle.forward(length)
            turtle.up()

            # Move turtle towards center of triangle to draw inner triangle
            turtle.left(150)
            turtle.forward(GAP_SIZE * 2)
            turtle.right(30)

            # Only draw the inner triangle if it will be visible
            if new_length > 0:
                fractal_triangle(new_length, recursions - 1)

            # Also draw inner hexagon if this is the last side of the triangle to draw
            if side == 2:
                turtle.forward(new_length + (GAP_SIZE * 1.0547))
                fractal_hexagon(new_length + (GAP_SIZE * 0.87735), recursions - 1)
                turtle.backward(new_length + (GAP_SIZE * 1.0547))

            # Return turtle to a vertex of the outer triangle in position to draw next side
            turtle.left(30)
            turtle.backward(GAP_SIZE * 2)
            turtle.right(30)
    # Draw regular triangle if its the last recursion or if the inner shapes will not be visible
    elif recursions == 1 or new_length + (GAP_SIZE * 0.87735) <= 0:
        draw_single_triangle(length)


def fractal_hexagon(length, recursions):
    """
    Recursively fractals out a single hexagon counterclockwise in the direction
    the turtle is facing. Three additional hexagons will be drawn within the
    the main hexagon with six triangles filling in the remaining corners of the
    main hexagon. Each of these inner shapes will be recursively fractaled as well.
    :param length: the length of each side of the main hexagon
    :param recursions: the amount of recursions left for this hexagon
    """
    # Set length for inner triangles
    # The length of the hexagons will = new_length + (GAP_SIZE * 1.1547)
    new_length = ((length - (2.88675 * GAP_SIZE)) / 2) - (0.57735 * GAP_SIZE)

    # Fractal out this hexagon if not the last recursion and if the inner shapes will be visible
    if recursions > 1 and new_length + (GAP_SIZE * 1.1547) > 0:
        # Iteratively draw two sides of the hexagon, two inner triangles and one inner hexagon
        for side in range(3):
            # Draw two sides of the hexagon
            turtle.down()
            turtle.forward(length)
            turtle.left(60)
            turtle.forward(length)
            turtle.up()

            # Move turtle towards center of hexagon to draw inner shapes
            turtle.left(120)
            turtle.forward(GAP_SIZE * 1.1547)

            # Draw an inner triangle if it will be visible
            if new_length > 0:
                # Reposition turtle to draw the triangle
                turtle.right(120)
                turtle.backward((2 * new_length) + (GAP_SIZE * 2.3094))

                # Draw the triangle
                fractal_triangle(new_length, recursions - 1)

                # Begin repositioning turtle to draw an inner hexagon
                turtle.forward((2 * new_length) + (GAP_SIZE * 2.3094))
                turtle.left(60)
            else:# Otherwise still begin repositioning turtle to draw an inner hexagon
                turtle.right(60)

            # Draw an inner hexagon
            fractal_hexagon(new_length + (GAP_SIZE * 1.1547), recursions - 1)

            # As long as the triangle will be visible, reposition turtle, draw it, and move back
            if new_length > 0:
                turtle.forward(new_length + (GAP_SIZE * 2.3094))
                fractal_triangle(new_length, recursions - 1)
                turtle.backward(new_length + (GAP_SIZE * 2.3094))

            # Return turtle to edge of hexagon in position to draw next edge
            turtle.left(60)
            turtle.backward(GAP_SIZE * 1.1547)
            turtle.right(60)
    # Draw regular hexagon if its the last recursion or if the inner shapes will not be visible
    elif recursions == 1 or new_length + (GAP_SIZE * 1.1547) <= 0:
        draw_single_hexagon(length)


def set_globals():
    """
    Sets the global settings for the drawing of the hexagon based on user input.
    """
    # Call in global variables for use
    global HEX_SIZE
    global GAP_SIZE
    global LAYER_COUNT
    global GLOW_LAYERS
    global CENTER_EDGE_WIDTH
    global GLOW_WIDTH
    global GLOW_MULTIPLIER

    # Declare an variable to hold the input well it is accessed
    hold = ""

    # Inform user of what they are entering and how to enter it
    print("Input the desired settings for the drawing of the fractaled")
    print("hexagon. All values can be any float value greater than")
    print("zero. Enter 'D' to use the default value of a setting.\n")

    # Set each of the global variables to user input or leave them at their
    # default value if the user enters 'D'
    hold = input("Enter the length of the main hexagon's sides: ")
    if hold != 'D':
        HEX_SIZE = float(hold)

    hold = input("Enter the width of the gap between different shapes: ")
    if hold != 'D':
        GAP_SIZE = float(hold)

    hold = input("Enter amount of layers(integer) in the recursion: ")
    if hold != 'D':
        LAYER_COUNT = int(hold)

    hold = input("Enter the width of the lines in the drawing: ")
    if hold != 'D':
        CENTER_EDGE_WIDTH = float(hold)

    hold = input("Enter the radius of the glow: ")
    if hold != 'D':
        GLOW_WIDTH = float(hold)

    hold = input("Enter the amount of steps(integer) in the glow's gradient: ")
    if hold != 'D':
        GLOW_LAYERS = int(hold)

    GLOW_MULTIPLIER = (GLOW_WIDTH / CENTER_EDGE_WIDTH) ** (1.0 / GLOW_LAYERS)


def main():
    """
    Determines the traits of the fractaled hexagon and then draws the fractal
    with a glow.
    """
    # Determine traits of fractal by user input
    set_globals()

    # Determine color of fractal
    print("\nEnter the RGB value of the color of the fractal as")
    print("floats between 0 and 1.")
    r_color = float(input("Enter the red value: "))
    g_color = float(input("Enter the green value: "))
    b_color = float(input("Enter the blue value: "))

    # Set up the turtle and the turtle window
    turtle.bgcolor("black")
    turtle.tracer(0, 0)
    initialize_turtle()

    # Draw each glow layer, progressively making each layer thinner and brighter
    for i in range(GLOW_LAYERS + 1):
        turtle.width(CENTER_EDGE_WIDTH * (GLOW_MULTIPLIER ** (GLOW_LAYERS - i)))
        turtle.pencolor((r_color * (i / GLOW_LAYERS), g_color * (i / GLOW_LAYERS), b_color * (i / GLOW_LAYERS)))
        fractal_hexagon(HEX_SIZE, LAYER_COUNT)

    # Update the window and leave it open until user closes it
    turtle.update()
    turtle.done()


main()