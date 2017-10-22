import turtle
def draw_square(t,sz):
    for i in range (4):
        t.forward(20)
        t.left(90)


wn=turtle.Screen()
wn.bgcolor("lightgreen")

tess=turtle.Turtle()
tess.pensize(3)
tess.color("hotpink")

size=20
for i in range(5):
    draw_square(tess,size)
    tess.penup()
    tess.forward(40)
    tess.pendown()
    
wn.mainloop()
    
    