from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot([], [], lw=2)

x = np.linspace(0, 10, 11)
y = []
g = 9.8

for i in np.linspace(0, 10, 11):
    r = int(i)
    s = int(r + 1)
    t = int(r + 2)
    y[r] = r
    print "\n", y[r]
    y[s] = s

    y[t] = int(2 * y[s] - y[r] - g * ((0.1) ** 2))
    return y[t]

line.set_data(x, y[t])

# Showing the figure and window
ax.plot(line)
plt.show()
