import turtle
wn=turtle.Screen()
tess=turtle.Turtle()
for i in range(12):
    tess.color("blue")
    tess.shape("turtle")
    tess.penup()
    tess.forward(100)
    tess.pendown()
    tess.forward(10)
    tess.penup()
    tess.forward(20)
    tess.stamp()
    tess.backward(130)
    tess.left(30)
    
    
wn.mainloop()