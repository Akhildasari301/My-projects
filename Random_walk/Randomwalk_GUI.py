from tkinter import *

from randomwalk_model import *


# Introduction to Randwom Walk 
rw_decription = """
In mathematics, a random walk is a mathematical object, known as a stochastic or random process, 
that describes a path that consists of a succession of random steps on some mathematical space such as the integers.

An elementary example of a random walk is the random walk on the integer number line, 
which starts at 0 and at each step moves +1 or −1 with equal probability. 
other examples include the path traced by a molecule as it travels in a liquid or a gas (Brownian motion), 
the search path of a foraging animal, the price of a fluctuating stock and the financial status of a gambler: 
all can be approximated by random walk models, even though they may not be truly random in reality.
"""


window = Tk()

window.title("Random walk model")

# function that get's triggered when the generate button is clicked
def clicked():

    num_points = points.get()
    if num_points == "":
        num_points = 1000
    rw = Randomwalk(int(num_points))
    rw.get_points()
    rw.plot_walk()

# heading 
lb = Label(window, text = "2D Random Walk", font=('Arial Bold', 25))


lb.grid(column=0, row=0)

desc = Label(window, text=rw_decription, font=('Arial', 15))
desc.grid(column=0, row=1)

window.geometry('1100x800')

warn = Label(window, text="If no input is given, 1000 will be taken as input", font=('Arial', 15))
warn.grid(column=0, row=2)
# input field to get the number of points

ask_points = Label(window, text="Enter the no.of points to plot the walk: ", font=('Arial', 15))
ask_points.grid(column=0, row=3)

points = Entry(window)
points.grid(column=0, row = 4)
points.focus_set()

# button to generate the plot

bt = Button(window, text="Generate the plot", bg="blue", fg="white", command=clicked, font=('Arial Bold', 15), pady=5)
bt.grid(column=0, row=5)



window.mainloop()

