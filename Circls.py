import turtle
window = turtle.Screen()
r = 50

europa = turtle.Turtle()
africa = turtle.Turtle()
america = turtle.Turtle()
asia = turtle.Turtle()
australia = turtle.Turtle()

for i in [europa, africa, america, asia, australia]:
    i.up()

europa.goto(-2*r,2*r)
africa.goto(0,2*r)
america.goto(2*r,2*r)
asia.goto(-r,r)
australia.goto(r,r)

for i in [europa, africa, america, asia, australia]:
    i.down()
    i.pensize(6)

europa.color("blue")
africa.color("black")
america.color("red")
asia.color("yellow")
australia.color("green")

for i in [europa, africa, america, asia, australia]:
    i.circle(r)
window.mainloop()