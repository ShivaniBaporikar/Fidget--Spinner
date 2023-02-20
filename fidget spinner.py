from turtle import *

# import tkinter
# from tkinter import messagebox 
# m=tkinter.Tk()
# def hellocallback():
#     messagebox.showInfo('hello World')
# w = tkinter.Button(m, text= 'hello', command= hellocallback)
# w.pack()
# m.mainloop()

state = {'turn':0}
def spinner():
    clear()
    angle=state['turn']/10
    right(angle)
    forward(100)
    dot(120, 'purple')
    back(100)
    right(120)
    forward(100)
    dot(120, 'grey')
    back(100)
    right(120)
    forward(100)
    dot(120, 'gold')
    back(100)
    right(120)
    update()

def animate():
    if state['turn']>0:
        state['turn']-=1

    spinner()
    ontimer(animate,120)

def flick():
    state['turn']+=10

setup(420,420,370,0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()
    

