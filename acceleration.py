import matplotlib.pyplot as plt
import numpy as np
import math

fig = plt.figure("From Earth and Beyond!")
ax = fig.add_subplot(111)

g = 9.81                    # Force of gravity
dt = 0.1                    # Delta of time
rE = 6371                   # Radius of Earth
G = 6.674 * (10 ** -11)     # Gravitational constant
M = 5.972 ** 24             # Mass of Earth

x = np.linspace(0, 100, 101)    # X range
y = np.linspace(0, 100, 101)    # Y range

a = np.linspace(1, 101, 102)    # X range
b = np.linspace(3, 103, 104)    # Y range

vx = np.linspace(2, 102, 103)   # Velocity X range
vy = np.linspace(5, 105, 106)   # Velocity Y range

# The new part regarding the velocity...

x[0] = 1    # Initial quantities
y[0] = 3 + rE    # Initial quantities

vx[0] = 2   # V = m / s
vy[0] = 5   # V = m / s

x[1] = (x[0] + vx[0] * dt)
y[1] = (y[0] + vy[0] * dt)

for i in np.linspace(0, 98, 99):

    r = int(i)
    s = int(i + 1)
    t = int(i + 2)

    # Radius squared
    rSq = x[s] ** 2 + y[s] ** 2

    # The new calculation of 'g'
    g = G * M / rSq

    # Debugging --> Note: when the new g is used,
    # the program terminates after printing out
    # the 'rSq' and 'g' ...
    print "rSq:", math.sqrt(rSq)
    print "g:", g

    # Old program
    x[t] = (2 * x[s] - x[r] + 0)
    y[t] = (2 * y[s] - y[r] - g * ((dt) ** 2))

    # Stops program when reaches 0 because the Earth is solid,
    # eliminate for gas planets...
    if y[t] < 0:
        break

    # Debugging
    print "\ni:", int(i)
    print "t:", t

    print "y[t]:", y[t]
    print "x[t]:", x[t]

    # Plotting the result
    ax.scatter(x[t], y[t])

# Showing the diagram
plt.show()

# Velocity = change in location / change in time

# m --> mass
# g --> gravity (the force of)
# f = m * a
# f = m * g
#            ==> mg = ma
#                ==> a = g = 9.81 (m / s ** 2)

# a =   y(n+2) - y(n+1)   y(n+1) - y(n)     = g
#       --------------- - -------------
#              t                t
#     -----------------------------------
#                     t ** 2

# a =   y(n+2) - 2y(n+1) + y(n)     = g
#       -----------------------
#               t ** 2

# y(n+2) - 2y(n+1) + y(n) = g * (t ** 2)

# y(n+2) = 2y(n+1) - y(n) - g * (t ** 2)
# x(n+2) = 2x(n+1) - x(n)

"""
        |          x    x
        |      x           x
    y(1)|____.                x
    y(0)|__.'|                   x
      __|__|_|_____                x
        |x(0) x(1)

"""
