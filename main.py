from turtle import Turtle as t, Screen

tim = t()
my_screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def rotate_clockwise():
    tim.right(10)


def rotate_counter_clockwise():
    tim.left(10)


def clean_slate():
    tim.home()
    tim.clear()


my_screen.listen()

my_screen.onkey(fun=move_forward, key="w")
my_screen.onkey(fun=move_backwards, key="s")
my_screen.onkey(fun=rotate_clockwise, key="d")
my_screen.onkey(fun=rotate_counter_clockwise, key="a")
my_screen.onkey(fun=clean_slate, key="c")

my_screen.exitonclick()
