import turtle as tr

colors = []
positions = [-220, 0, 220, -110, 105]

tr.pensize(5)
tr.speed(15)

def draw_circle(color, position):
    tr.color(color)
    tr.penup()
    tr.goto(position, -80)
    tr.pendown()
    tr.circle(100)

for c in range(1, 5):  # Correção: A função range() começa em 1 e vai até 4
    cor = input("Digite a {}ª cor: ".format(c))
    colors.append(cor)

for color, position in zip(colors, positions):
    draw_circle(color, position)

tr.done()
