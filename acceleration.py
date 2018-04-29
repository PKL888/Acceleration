import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure("Acceleration")
ax = fig.add_subplot(111)

g = 9.8

x = np.linspace(0, 100, 101)
y = np.linspace(0, 100, 101)

for i in np.linspace(0, 98, 99):

    r = int(i)
    s = int(i + 1)
    t = int(i + 2)

    x[t] = (2 * x[s] - x[r] + 0)
    y[t] = (2 * y[s] - y[r] - g * ((0.1) ** 2))

    if y[t] < 0:
        break

    print "\ni:", int(i)
    print "t:", t

    print "y[t]:", y[t]
    print "x[t]:", x[t]

    ax.scatter(x[r], y[t])

plt.show()

# Velocity = change in location / change in time

# m --> mass
# g --> gravity (the force of)
# f = m * a
# f = m * g
#            ==> mg = ma
#                ==> a = g = 9.81 (m / s ** 2)

# a = ((y(n+2) - y(n+1)) / delta of 't' - (y(n+1) - y(n)) /,
# delta of 't') / delta of 't' ** 2 = g

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
