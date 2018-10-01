import turtle

HEX_SIZE = 300
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
    turtle.down()
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.up()


def draw_single_hexagon(length):
    turtle.down()
    turtle.forward(length)
    turtle.left(60)
    turtle.forward(length)
    turtle.left(60)
    turtle.forward(length)
    turtle.left(60)
    turtle.forward(length)
    turtle.left(60)
    turtle.forward(length)
    turtle.left(60)
    turtle.forward(length)
    turtle.left(60)
    turtle.up()


def fractal_triangle(length, recursions):
    new_length = ((length - (4.6188 * GAP_SIZE)) / 3) - (0.57735 * GAP_SIZE)
    if recursions > 1 and new_length + (GAP_SIZE * 0.87735) > 0:
        for side in range(3):
            turtle.down()
            turtle.forward(length)
            turtle.up()
            turtle.left(150)
            turtle.forward(GAP_SIZE * 2)
            turtle.right(30)

            if new_length > 0:
                fractal_triangle(new_length, recursions - 1)

            if side == 2:
                turtle.forward(new_length + (GAP_SIZE * 1.0547))
                fractal_hexagon(new_length + (GAP_SIZE * 0.87735), recursions - 1)
                turtle.backward(new_length + (GAP_SIZE * 1.0547))

            turtle.left(30)
            turtle.backward(GAP_SIZE * 2)
            turtle.right(30)
    elif recursions == 1 or new_length + (GAP_SIZE * 0.87735) <= 0:
        draw_single_triangle(length)


def fractal_hexagon(length, recursions):
    # set length for inner triangles
    # the length of the hexagons will = new_length + (GAP_SIZE * 1.1547)
    new_length = ((length - (2.88675 * GAP_SIZE)) / 2) - (0.57735 * GAP_SIZE)

    # fractal out this hexagon if not the last recursion and if the inner shapes will be visible
    if recursions > 1 and new_length + (GAP_SIZE * 1.1547) > 0:
        for side in range(3):
            # draw two sides of the hexagon
            turtle.down()
            turtle.forward(length)
            turtle.left(60)
            turtle.forward(length)
            turtle.up()

            # move turtle towards center of hexagon to draw inner shapes
            turtle.left(120)
            turtle.forward(GAP_SIZE * 1.1547)

            # reposition turtle to draw an inner triangle, draw it, and move back as long as its visible
            if new_length > 0:
                turtle.right(120)
                turtle.backward((2 * new_length) + (GAP_SIZE * 2.3094))
                fractal_triangle(new_length, recursions - 1)
                turtle.forward((2 * new_length) + (GAP_SIZE * 2.3094))
                turtle.left(60)
            else:
                turtle.right(60)

            # reposition turtle to draw an inner hexagon and draw it
            fractal_hexagon(new_length + (GAP_SIZE * 1.1547), recursions - 1)

            # reposition turtle to draw an inner triangle, draw it, and move back as long as its visible
            if new_length > 0:
                turtle.forward(new_length + (GAP_SIZE * 2.3094))
                fractal_triangle(new_length, recursions - 1)
                turtle.backward(new_length + (GAP_SIZE * 2.3094))

            # return turtle to edge of hexagon in position to draw next edge
            turtle.left(60)
            turtle.backward(GAP_SIZE * 1.1547)
            turtle.right(60)
    # draw regular hexagon if its the last recursion or if the inner shapes will not be visible
    elif recursions == 1 or new_length + (GAP_SIZE * 1.1547) <= 0:
        draw_single_hexagon(length)


def main():
    turtle.bgcolor("black")
    turtle.tracer(0, 0)
    initialize_turtle()

    r_color = 0
    g_color = 1
    b_color = 0

    for i in range(GLOW_LAYERS + 1):
        turtle.width(CENTER_EDGE_WIDTH * (GLOW_MULTIPLIER ** (GLOW_LAYERS - i)))
        turtle.pencolor((r_color * (i / GLOW_LAYERS), g_color * (i / GLOW_LAYERS), b_color * (i / GLOW_LAYERS)))
        fractal_hexagon(HEX_SIZE, LAYER_COUNT)

    turtle.update()

    #turtle.getscreen().getcanvas().postscript(file='myfilename.eps', colormode='color')
    turtle.done()



main()