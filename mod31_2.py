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

#Mod. 3.1 Falling Sphere
#Problem Parameters
s_0_m = 2000
v_0_m_per_s = 0.0
t_0_s=0
m_kg = 90
g_m_per_s2 = -9.81
A_p_person_m2 = 0.4
A_p_parachute_m2 = 28
Weight = m_kg*g_m_per_s2
Drag = 0
a_m_s2=g_m_per_s2
parachute_trigger_height_m = 1000

#t_s = current time (put units here)
delta_t_s=0.1
t = [t_0_s]
s = [s_0_m]
v = [v_0_m_per_s]
delta_v = 0
delta_s=0
t_max = 10000
#epsilon_stop = 1e-5
#epsilon = 1.1*epsilon_stop
counter=0

A_p = A_p_person_m2

while s[counter]>750:
    counter+=1
    t_curr=t[counter-1]+delta_t_s
    t.append(t_curr)
    #Drag = 0.65*v[counter-1]**2 * A_p
    Drag = 0.65 * (v[counter-1])*(v[counter-1]) * A_p
    a_m_s2 = (Weight+Drag)/m_kg
    delta_s = v[counter-1]*delta_t_s
    delta_v = a_m_s2*delta_t_s
    current_s = s[counter-1]+delta_s
    current_v = v[counter-1]+delta_v

    if current_s > parachute_trigger_height_m:
        A_p=A_p_person_m2
    else:
        A_p=A_p_parachute_m2

    s.append(current_s)
    v.append(current_v)
    #epsilon = (v[counter]-v[counter-1])/v[counter]
    #epsilon = (Weight-Drag) / Weight


title_base = "Skydiver"
title = title_base + " delta_t = " + str(delta_t_s)
filename = "mod31_skydiver_position" + str(delta_t_s) + ".png"
xlabel = "t (s)"
ylabel = "s (m)"
myPlot(t,s,min(t),max(t),xlabel, min(s),max(s),ylabel, title,filename)
title_base = "Skydiver"
title = title_base + " delta_t = " + str(delta_t_s)
filename = "mod31_skydiver_velocity" + str(delta_t_s) + ".png"
xlabel = "t (s)"
ylabel = "v (m/s)"
myPlot(t,v,min(t),max(t),xlabel, min(v),max(v),ylabel, title,filename)











