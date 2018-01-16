from math import *
import numpy as np
import matplotlib.pyplot as plt

def myPlot(t,P,x1,x2,y1,y2,title,filename):
    fig1 = plt.figure()
    plt.xlim(x1,x2)
    plt.ylim(y1, y2)
    plt.xlabel('t')
    plt.ylabel('P')
    plt.title(title)
    plt.plot(t,P)
    plt.savefig(filename)
    plt.show()

#Mod. 3.1 Falling Sphere
#Problem Parameters
s_0_m = 0.0
v_0_m_per_s = 0.0
t_0_s=0
m_kg = 0.5
g_m_per_s2 = 9.81
diameter_m = 0.10
A_p = pi/4*diameter_m**2
Weight = m_kg*g_m_per_s2
Drag = 0
a_m_s2=g_m_per_s2

#t_s = current time (put units here)
delta_t_s=0.1
t = [t_0_s]
s = [s_0_m]
v = [v_0_m_per_s]
delta_v = 0
delta_s=0
t_max = 10000
epsilon_stop = 1e-5
epsilon = 1.1*epsilon_stop
counter=0

while epsilon>epsilon_stop:
    counter+=1
    Drag = 0.65 * v[counter-1]**2 * A_p
    a_m_s2 = (Weight-Drag)/m_kg
    t_curr = t[counter-1]+delta_t_s
    t.append(t_curr)
    delta_s=v[counter-1]*delta_t_s
    s_curr = s[counter-1]+delta_s
    delta_v=a_m_s2*delta_t_s
    v_curr = v[counter-1]+delta_v
    epsilon = (v_curr-v[counter-1])/v_curr
    s.append(s_curr)
    v.append(v_curr)














