import turtle
import random
import winsound

# Screen
wnd = turtle.Screen()
wnd.title('Pong for 1 player')
wnd.tracer(0)
wnd._bgcolor('black')
wnd.setup(width=800, height=600)

#Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.shapesize(stretch_len=5,stretch_wid=1)
paddle.color('purple')
paddle.penup()
paddle.goto(0,-270)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = 1

#score & lives
score = 0
lives = 3

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("pink")
pen.penup()
pen.hideturtle()
pen.goto(0,263)
pen.write("Lives: 3   Score: 0", align="center", font=('Courier', 24, 'normal'))

#Functions
def paddle_right():
    x = paddle.xcor()
    x+=20
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x-=20
    paddle.setx(x)

def falling_block():
    for block in block_list:
        if block.state == 'falling':
            block.l = block.xcor()-10
            block.r = block.xcor()+10
            block.goto(block.xcor(),block.ycor()+block.dy)

#Keyboard Binding
wnd.listen()

wnd.onkeypress(paddle_right, "Right")
wnd.onkeypress(paddle_left, "Left")

#bricks
x_list = [-335, -225, -115, -5, 105, 215, 325]
y_list = [220, 190, 160, 130, 100]
block_list = list()

for i in y_list:
    for j in x_list:
        block = turtle.Turtle()
        block.shape('square')
        block.shapesize(stretch_len=5, stretch_wid=1)
        block.up()
        block.goto(j,i)
        block.color('white')
        block.state = 'ready'
        block.l = block.xcor()-50
        block.r = block.xcor()+50
        block_list.append(block)
    
block_count = len(block_list)
    
    

while lives>0 and block_count>0:
    wnd.update()
    falling_block()

    #Move the ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor() > 230:
        ball.sety(230)
        ball.dy *= -1
    

    if ball.ycor() < -280:
        ball.goto(0,0)
        lives -=1
        pen.clear()
        pen.write("Lives: {}  Score: {}".format(lives, score), align="center", font=('Courier', 24, 'normal'))
        ball.dy *= -1
        winsound.PlaySound("Bouncy_Bounce-Bugs_Bunny-1735935456.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

        
    # Paddle and ball collisions

    if (ball.ycor() < -240 and ball.ycor() > -250) and (ball.xcor() < paddle.xcor() + 55 and ball.xcor()> paddle.xcor() -55):
        ball.sety(-240)
        ball.dy *= -0.95
        winsound.PlaySound("Bouncy_Bounce-Bugs_Bunny-1735935456.wav", winsound.SND_ASYNC)

        

    for block in block_list:
                
        if (block.l - 10 <= ball.xcor() <= block.r + 10) and (block.ycor()-15 <= ball.ycor() <= block.ycor()+15) and block.state == 'ready':
                ball.dy *= -1
                block.state = 'falling'
                block.dy = -1
                score += 1
                pen.clear()
                pen.write('Lives: {}  Score: {}'.format(lives,score), align='center', font=('Courier', 24, 'normal'))

        
        if block.ycor()<0 or block.ycor()>240:
            block.hideturtle()
            block_list.remove(block)
            block_count = len(block_list)


#Game Over
pen.clear()
pen.goto(0,0)
pen.write('GAME OVER\nScore: {}'.format(score), align='center', font=('Courier', 40, 'normal'))