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

#Mod. 3.3 Damped Pendulum Motion
#Problem Parameters
t_0 = 0.0   #seconds
m = 0.2     #kg (usually does not matter)
g = 9.81    #m/s^2
length = 1.0   #meters
k = 0.7     #1/s damping coeff
init_angle_degrees = 45.0 #angle in degrees
init_angle = init_angle_degrees*2*pi/360.0  #init angle in radians
ang_v_0 = 0 #init ang velocity
ang_a_0 = -g*sin(init_angle)/length-k*ang_v_0

delta_t=0.02    #seconds

t = [t_0]
angle = [init_angle]
ang_v = [ang_v_0]
ang_a = [ang_a_0]

delta_ang_v = 0
delta_ang = 0
t_max = 6.0 #s how long to run the sim
#epsilon_stop = 1e-2
#epsilon = 1.1*epsilon_stop
counter=0

while t[counter] < t_max:
    counter+=1                              #increment counter (0->1 on first trip through
    t_curr=t[counter-1]+delta_t             #get the current time by adding delta_t
    t.append(t_curr)                        #add this time to the time list
    delta_ang_v = ang_a[counter-1] * delta_t        #calc delta_v based on previous accel
    ang_v.append(ang_v[counter - 1] + delta_ang_v)      #add new v to v list
    delta_ang = ang_v[counter] * delta_t          #calc delta_s based on current v
    angle.append(angle[counter - 1] + delta_ang)      #add new s to s list
    ang_a.append(-g*sin(angle[counter])/length-k*ang_v[counter])                       #add new a to a list


title_base = "Damped Pendulum "
title = title_base + " delta_t = " + str(delta_t)
filename = "mod33_damped_pendulum_" + str(delta_t) + "_all.png"
xlabel = "t (s)"
y1label = "ang a (rad/s^2)"
y2label = "ang v (rad/s)"
y3label = "angle (rad)"

myPlot3x(t,ang_a,ang_v,angle,xlabel,y1label,y2label,y3label,title,filename)
