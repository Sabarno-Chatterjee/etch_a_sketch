from turtle import Turtle as t, Screen


tim = t()
my_screen = Screen()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)



my_screen.listen()
my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="s", fun = move_backwards)

my_screen.exitonclick()