import turtle as tur

tur.title("Snake coding - Butterfly")
tur.width(2)
tur.speed(10)

color1 = "#f6aa0c"
color2 = "#0099ff"
color3 = "#f83079"
color4 = "#72e7fb"

def go_to(pos):
    tur.speed(0)
    tur.up()
    tur.goto(pos[0], pos[1])
    tur.down()
    tur.speed(10)

def rel_pos(x,y):
    tur.speed(0)
    tur.up()
    tur.goto(tur.pos()+(x,y))
    tur.down()
    tur.speed(10)

def draw_oval(width, height, color):
    tur.speed(0)
    tur.fillcolor(color)
    tur.begin_fill()
    for _ in range(2):
        tur.circle(height/2, 45)
        tur.circle(width/2, 135)
    tur.end_fill()
    tur.speed(10)

def draw_heart(size):
    tur.left(50)
    tur.forward(size)
    tur.circle(size * 0.5, 200)
    tur.right(140)
    tur.circle(size * 0.5, 200)
    tur.forward(size+5)
    tur.left(50)

def rightwings(top_pos):
    go_to(top_pos)
    tur.seth(-65)
    tur.circle(-200,35)
    cur_pos = tur.pos()
    tur.begin_fill()
    tur.fillcolor(color1)
    draw_heart(100)
    tur.end_fill()
    go_to((cur_pos[0],cur_pos[1] + 20))
    tur.begin_fill()
    tur.fillcolor(color2)
    draw_heart(80)
    tur.end_fill()

    rel_pos(60,-70)
    tur.seth(-45)
    draw_oval(20,50,color3)
    rel_pos(-25,30)
    draw_oval(10, 30, color3)
    rel_pos(-10, -15)
    draw_oval(10,20,color4)

    go_to(top_pos)
    tur.seth(-65)
    tur.circle(-200,20)
    cur_pos = tur.pos()
    tur.begin_fill()
    tur.fillcolor(color1)
    draw_heart(100)
    tur.end_fill()
    go_to(cur_pos)
    tur.begin_fill()
    tur.fillcolor(color2)
    draw_heart(80)
    tur.end_fill()

    rel_pos(50,30)
    tur.seth(10)
    draw_oval(10,60,color3)
    rel_pos(40,-5)
    draw_oval(20,60,color4)
    rel_pos(-10,-40)
    draw_oval(20,40,color3)
    tur.seth(-45)
    rel_pos(0,-45)
    draw_oval(10,80,color4)
    rel_pos(-30,20)
    draw_oval(10,30,color4)
    rel_pos(-30,30)
    draw_oval(25,30,color3)

def leftWings(top_pos):
    go_to(top_pos)
    tur.seth(-110)
    tur.circle(200,22)
    cur_pos = tur.pos()
    tur.seth(100)
    tur.begin_fill()
    tur.fillcolor(color1)
    draw_heart(100)
    tur.end_fill()
    go_to((cur_pos[0], cur_pos[1] + 10))
    tur.begin_fill()
    tur.fillcolor(color2)
    draw_heart(80)
    tur.end_fill()

    rel_pos(-80, -45)
    tur.seth(-135)
    draw_oval(20, 50, color3)
    rel_pos(25,30)
    draw_oval(10,30,color4)
    rel_pos(30,10)
    draw_oval(10,20,color3)

    go_to(top_pos)
    tur.seth(-110)
    tur.circle(200,5)
    cur_pos = tur.pos()
    tur.seth(90)
    tur.begin_fill()
    tur.fillcolor(color1)
    draw_heart(100)
    tur.end_fill()
    go_to((cur_pos[0], cur_pos[1] -15))
    tur.begin_fill()
    tur.fillcolor(color2)
    draw_heart(80)
    tur.end_fill()

    rel_pos(-90,50)
    tur.seth(110)
    draw_oval(10,60,color4)
    rel_pos(40,-5)
    draw_oval(20,60,color4)
    rel_pos(-10,-40)
    draw_oval(20,40,color3)
    tur.seth(-150)
    rel_pos(-29,-30)
    draw_oval(10,80,color4)
    rel_pos(-30,20)
    draw_oval(10,30, color3)
    rel_pos(90,15)
    draw_oval(10,30,color3)

def drawWings(top_pos):
    rightwings(top_pos)
    leftWings(top_pos)

def drawButterfly():
    tur.seth(70)
    tur.circle(200,45)
    top_pos = tur.pos()
    tur.seth(-110)
    tur.circle(200,45)
    go_to(top_pos)
    tur.seth(0)
    tur.begin_fill()
    tur.fillcolor(color2)
    tur.circle(10)
    tur.end_fill()
    tur.circle(10, 180)
    tur.width(3)
    cur_pos = tur.pos()
    tur.seth(90)
    tur.circle(50,60)
    go_to(cur_pos)
    tur.seth(90)
    tur.circle(-50,60)
    tur.width(2)

    drawWings(top_pos)
    go_to((0,0))
    tur.begin_fill()
    tur.fillcolor(color1)
    tur.seth(70)
    tur.circle(200,45)
    top_pos = tur.pos()
    tur.seth(-110)
    tur.circle(200,45)
    tur.end_fill()

    tur.begin_fill()
    tur.fillcolor(color3)
    tur.seth(70)
    tur.circle(200,20)
    tur.seth(180)
    tur.forward(30)
    tur.seth(-85)
    tur.circle(200,20)
    tur.end_fill()

    tur.begin_fill()
    tur.fillcolor(color1)
    tur.seth(70)
    tur.circle(200,15)
    tur.seth(180)
    tur.forward(27)
    tur.seth(-81)
    tur.circle(200,15)
    tur.end_fill()

    go_to((0,0))
    tur.begin_fill()
    tur.fillcolor(color4)
    tur.seth(70)
    tur.circle(200, 10)
    tur.seth(180)
    tur.forward(20)
    tur.seth(-75)
    tur.circle(200,10)
    tur.end_fill()

drawButterfly()
go_to((-180, -200))
tur.write("""Snake coding \n please subscribe!""",
          font=('Arial',40,'bold'))
tur.done()


























