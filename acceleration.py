import numpy as np

g = 9.8

x = np.linspace(0, 100, 101)
y = np.linspace(0, 100, 101)

for i in np.linspace(0, 98, 99):

    r = int(i)
    s = int(i + 1)
    t = int(i + 2)

    y[t] = (2 * y[s] - y[r] - g * ((0.1) ** 2))

    print "\ni:", int(i)
    print "t:", t

    print "y[t]:", y[t]
    print "x[r]:", x[r]
