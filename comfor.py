import turtle as tr

colors = ['blue', 'black', 'red','yellow','green']
positions = [-220, 0, 220, -110, 105]

tr.pensize(5)
tr.speed(15)

def draw_circle(color, position):
    tr.color(color)
    tr.penup()
    if color == 'yellow':  
        tr.goto(position,-80)
    elif color == 'green':
        tr.goto(position,-80)
    else:
        tr.goto(position, 0)
    tr.pendown()
    tr.circle(100)

for color, position in zip(colors, positions):
    draw_circle(color, position)


