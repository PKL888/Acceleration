import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 100), ylim=(0, 100))
line, = ax.plot([], [], lw=2)


# Initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,


# Animation function. This is called sequentially
def animate(i):

    x = np.linspace(0, 100, 101)
    y = np.linspace(0, 100, 101)

    g = 9.8

    for i in np.linspace(0, 98, 99):
        r = int(i)			# n
        s = int(r + 1)		# n + 1
        t = int(r + 2)		# n + 2

        y[t] = (2 * y[s] - y[r] - g * ((0.1) ** 2))

        print "i:", i

        print "y[t]:", y[t]
        print "x[i]:", x[i]

        line.set_data(x[i], y[t])
        print x[i]
        print y[t]
        print "\n"

        return line,


# Call the animator. blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

plt.show()
