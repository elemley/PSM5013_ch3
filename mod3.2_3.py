from math import *
import numpy as np
import matplotlib.pyplot as plt

def myPlot(t,P,x1,x2,xlabel,y1,y2,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlim(x1,x2)
    plt.ylim(y1, y2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.plot(t,P)
    plt.savefig(filename)
    plt.show()


def myPlot3x(x,y1,y2,y3,xlabel,y1label,y2label,y3label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(311)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.ylabel(y1label)
    plt.title(title)
    plt.plot(x,y1)

    ax2 = plt.subplot(312,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.ylabel(y2label)
    plt.plot(x, y2)

    ax3 = plt.subplot(313,sharex=ax1)
    plt.ylim(min(y3), max(y3))
    plt.xlabel(xlabel)
    plt.ylabel(y3label)
    plt.plot(x, y3)

    plt.savefig(filename)
    plt.show()


#damping coeff function -- here it's a function of v^2
def f_damp(c,v):
    tmp = 0.0
    if v > 0:
        tmp = -c*v**2
    else:
        tmp = c*v**2
    return tmp


#Mod. 3.2 Undamped Harmonic Oscillator
#Problem Parameters
t_0 = 0.0   #seconds
m = 0.2     #kg
g = 9.81    #m/s^2
k = 10.0    #N/m spring const
c = 0.1     #N/m/s damping coefficient
s_1 = 1.0   #meters
s_2 = s_1 + m*g/k   #meters
init_displacement = 0.3     #meters the amount we perturb the system
s_0 = s_2 + init_displacement   #meters this is the starting location of the mass
v_0 = 0.0   #m/s the mass starts from rest

delta_t=0.02    #seconds

f_restore = -k*(s_0-s_2)                  #N the force that the spring exerts to return to equiquilibrium
#f_damp = -c*v_0                          #damping force (always opposite motion
f_net = f_restore + m*g+f_damp(c,v_0)     #N the net force of the spring and the weight
a_0 = f_net/m                             #m/s^2 this is the accel due to net force of weight and spring

t = [t_0]
s = [s_0]
v = [v_0]
a = [a_0]

delta_v = 0
delta_s=0
t_max = 75.0 #s how long to run the sim
#epsilon_stop = 1e-2
#epsilon = 1.1*epsilon_stop
counter=0

while t[counter] < t_max:
    counter+=1                              #increment counter (0->1 on first trip through
    t_curr=t[counter-1]+delta_t             #get the current time by adding delta_t
    t.append(t_curr)                        #add this time to the time list
    delta_v = a[counter-1] * delta_t        #calc delta_v based on previous accel
    v.append(v[counter - 1] + delta_v)      #add new v to v list
    delta_s = v[counter] * delta_t          #calc delta_s based on current v
    s.append(s[counter - 1] + delta_s)      #add new s to s list
    f_restore = -k * (s[counter] - s_2)     #N the force that the spring exerts to return to equiquilibrium
    #f_damp = -c * v[counter]                #N damping force (always opposite motion
    f_net = f_restore + f_damp(c,v[counter]) + m * g      #N the net force of the spring and the weight
    a.append(f_net/m)                       #add new a to a list


title_base = "Damped Harmonic Oscillator --v^2 damping"
title = title_base + " delta_t = " + str(delta_t)
filename = "mod32_v2_damped_oscillator_" + str(delta_t) + "_all.png"
xlabel = "t (s)"
y1label = "a (m/s^2)"
y2label = "v (m/s)"
y3label = "s (m)"

myPlot3x(t,a,v,s,xlabel,y1label,y2label,y3label,title,filename)

"""
title_base = "Damped Harmonic Oscillator"
title = title_base + " delta_t = " + str(delta_t)
filename = "mod32_damped_oscillator_" + str(delta_t) + "_a.png"
xlabel = "t (s)"
ylabel = "a (m/s^2)"
myPlot(t,a,min(t),max(t),xlabel, min(a),max(a),ylabel, title,filename)


filename = "mod32_damped_oscillator_" + str(delta_t) + "_v.png"
ylabel = "v (m/s)"
myPlot(t,v,min(t),max(t),xlabel, min(v),max(v),ylabel, title,filename)

filename = "mod32_damped_oscillator_" + str(delta_t) + "_s.png"
ylabel = "s (m)"
myPlot(t,s,min(t),max(t),xlabel, min(s),max(s),ylabel, title,filename)

"""




