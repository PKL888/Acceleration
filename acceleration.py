# This program is an ongoing creation attempting
# to represent the position, accelleration and other
# objectives of objects in space and otherwhere...

# By Peleg Kark-Levin

import matplotlib.pyplot as plt
import numpy as np
import math

# Creating the figure
fig = plt.figure("Youston!")
ax = fig.add_subplot(111)

fig2 = plt.figure("Distance")
ax2 = fig2.add_subplot(111)

steps = 60                  # Number of steps per run

g = 9.81                    # Force of gravity
dt = 86400	                # Delta of time in seconds
rEarth = 6371000            # Radius of Earth in metres
G = 6.674 * (10 ** -11)     # Gravitational constant
M = 5.972 * (10 ** 24) 		# Mass of Earth

# Moon statistics
vMoon = 1022 				# Average orbital speed in m/s
rMoon = 384402 * 1000		# Average orbital distance in meters
tMoon = 27					# Average orbital journey in days

"""
x = np.linspace(0, 7, 8)    # X range
y = np.linspace(0, 7, 8)    # Y range

a = np.linspace(1, 101, 102)    # X range
b = np.linspace(3, 103, 104)    # Y range

vx = np.linspace(2, 9, 10)   # Velocity X range
vy = np.linspace(5, 11, 12)   # Velocity Y range
"""

# The new part regarding the velocity...

x = np.zeros(steps + 4)
y = np.zeros(steps + 4)

x[0] = 1        	  	# Initial quantities
y[0] = 3 + rMoon	    # Initial quantities

vx = vMoon	  			# V = m / s
vy = 0  	  			# V = m / s

# New stuff --> increasing initial velocity
# vx *= 100
# vy *= 100

x[1] = (x[0] + vx * dt)
y[1] = (y[0] + vy * dt)

for i in np.linspace(0, steps, (steps + 1)):

    # Printing out the run number
    print "run", i

    r = int(i)
    s = int(i + 1)
    t = int(i + 2)

    # Adjusting the dt based on the distance (t)
    # if t > 200 & r % 100 == 0:
    #     print "Yay!"
    #     dt /= 10

    print "dt:", dt

    # Deberes
    # For every say 100 t,
    # dt decreases by say /10 or /2 -->
    # I need to decide by how much
    # my goal is to create an ellipse around the Earth and back
    # proportionally related
    # create a summary
    # cheack what happens if say g = blaga blaga / r
    # not rSq
    # what would happen then?
    # try this out

    # Deberes 18 June
    # Check program with moon height (as in distance from Earth),
    # Moon speed, and moon time (as in 30 days to lap the Earth),
    # See if it actually is... 30 days
    # Check if I can instantiate the graph's x and y so that they are equal

    # Radius squared
    rSq = x[s] ** 2 + y[s] ** 2

    # The new calculation of 'g'
    # g is another name for 'a' and the 'F' - Force
    g = G * M / rSq
    # g = k * M / R
    # if r == 0:
    #     g = 9.8
    # else:
    #     g = G * M / rSq

    # Debugging --> Note: when the new g is used,
    # the program terminates after printing out
    # the 'rSq' and 'g' ...
    print "rSq:", math.sqrt(rSq)
    print "g:", g

    # Distance undertaken by the object
    xTravel = x[s]
    yTravel = y[s]

    # Pythagoras calculation to figure out the distance
    # between the objectives
    theDistance = math.sqrt((x[s] ** 2) + (y[s]) ** 2)

    # Debugging the new additions
    print "\nthe Distance:", theDistance
    print "xTravel:", xTravel
    print "yTravel:", yTravel

    # Variables to come ... the new addition
    my_cos = xTravel / theDistance
    my_sin = yTravel / theDistance

    # More debugging...
    print "my_cos:", my_cos
    print "my_sin:", my_sin
    print my_cos - my_sin

    # Old program
    x[t] = (2 * x[s] - x[r] - g * my_cos * ((dt) ** 2))  # Fx
    y[t] = (2 * y[s] - y[r] - g * my_sin * ((dt) ** 2))  # Fy

    # Fx = F * cos(a) --> x / r
    # Fy = F * sin(a) --> y / r

    # Stops program when reaches 0 because the Earth is solid,
    # eliminate for gas planets...
    # if y[t] < 0:
    #     break

    # Debugging
    print "\ni:", int(i)
    print "t:", t

    print "y[t]:", y[t]
    print "x[t]:", x[t]

    # Plotting the result
    ax.scatter(x[t], y[t])

    ax2.bar(i, rSq)

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

"""
v(t) = x(t + dt) - x(t)
     --------------------
			 dt

x(t) --> location of x in time t
x(t + dt) --> location at the next point in time

velocity --> how quickly one changes position
accelleration --> how quickly one changes velocity

a(t) = v(t + dt) - v(t)
      -------------------
             dt

a(t) --> accelleration at time t

a(t) = | x(t + dt * 2) - x(t + dt) |         |   x(t + dt) - x(t) |
       |---------------------------|    -    | -------------------|
       |           dt              |         |         dt         |
    ------------------------------------------------------------------
                                        dt

a(t) = x(t + dt * 2) - 2 * x(t + dt) + x(t)
      --------------------------------------
                    dt ** 2

f = m * a

m --> the mass of the object moving

a = f / m

f / m =  x(t + dt * 2) - 2 * x(t + dt) + x(t)
        --------------------------------------
                      dt ** 2

f / m * (dt ** 2) = x(t + dt * 2) - 2 * x(t + dt) + x(t)

f / m * (dt ** 2) + 2 * x(t + dt) - x(t) = x(t + dt * 2)
                           [s]      [r]         [t]

* Why did we move these two? 
    A. Because we want to know the position of THE NEXT POSITION

y[t] = (2 * y[s] - y[r] - g * my_sin * ((dt) ** 2))  # Fy

* Why is there a negative?
    A. Depending on the direction of movement and the forces involved
       --> On normal Earth we only have f = m * a
       --> But in this formula we have y going AWAY FROM EARTH,
           NOT TOWARDS IT, and that's why the f is a negative

* Why is this all useful?
    A. Because from our home Earth, when we see a spacial object in the sky,
       we can know its orbit distance, velocity, and time
       --> Then we can understand its orbit
       --> But there are also other physical formulas to understand more things

This was all the summary from the 21 of June 2018

"""
