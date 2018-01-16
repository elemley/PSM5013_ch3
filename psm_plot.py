from math import *
import numpy as np
import matplotlib.pyplot as plt

"""
UCO PSM Plotting Library

Form of functions are:

xxyyzzPlot###

xxyyzz = Plot type (Line, Scatter, etc...)

Multiple types are meant to be series on a single plot... arguments are in this same order

### =

first digit = # of rows
second digit = # of cols
third digit = # of series per plot

Arguments are in row, then column order

"""
#

def LinePlot111(x,y,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlim(min(x),max(x))
    plt.ylim(min(y), max(y))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.plot(x,y)
    plt.savefig(filename)
    plt.show()

def ScatterPlot111(x,y,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlim(min(x),max(x))
    plt.ylim(min(y), max(y))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.scatter(x,y)
    plt.savefig(filename)
    plt.show()

def LineScatterPlot111(x,y1,y2,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlim(min(x),max(x))
    if min(y1)<min(y2):
        ymin = min(y1)
    else:
        ymin = min(y2)
    if max(y1) > max(y2):
        ymax = max(y1)
    else:
        ymax = max(y2)
    plt.ylim(ymin, ymax)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.plot(x,y1)
    plt.scatter(x,y2)
    plt.savefig(filename)
    plt.show()


def LinePlot211(x,y1,y2,xlabel,y1label,y2label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(211)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.ylabel(y1label)
    plt.title(title)
    plt.plot(x,y1)

    ax2 = plt.subplot(212,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.xlabel(xlabel)
    plt.ylabel(y2label)
    plt.plot(x, y2)

    plt.savefig(filename)
    plt.show()

def LinePlot121(x,y1,y2,xlabel,y1label,y2label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(121)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.xlabel(xlabel)
    plt.ylabel(y1label)
    plt.title(title)
    plt.plot(x,y1)

    ax2 = plt.subplot(122,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.xlabel(xlabel)
    plt.ylabel(y2label)
    plt.plot(x, y2)

    plt.savefig(filename)
    plt.show()



def LinePlot311(x,y1,y2,y3,xlabel,y1label,y2label,y3label,title,filename):
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

def LinePlot131(x,y1,y2,y3,xlabel,y1label,y2label,y3label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(131)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.xlabel(xlabel)
    plt.ylabel(y1label)
    plt.title(title)
    plt.plot(x,y1)

    ax2 = plt.subplot(132,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.xlabel(xlabel)
    plt.ylabel(y2label)
    plt.plot(x, y2)

    ax3 = plt.subplot(133,sharex=ax1)
    plt.ylim(min(y3), max(y3))
    plt.xlabel(xlabel)
    plt.ylabel(y3label)
    plt.plot(x, y3)
    plt.savefig(filename)
    plt.show()





def ScatterPlot211(x,y1,y2,xlabel,y1label,y2label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(211)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.ylabel(y1label)
    plt.title(title)
    plt.scatter(x,y1)

    ax2 = plt.subplot(212,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.xlabel(xlabel)
    plt.ylabel(y2label)
    plt.scatter(x, y2)

    plt.savefig(filename)
    plt.show()

def ScatterPlot121(x,y1,y2,xlabel,y1label,y2label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(121)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.xlabel(xlabel)
    plt.ylabel(y1label)
    plt.title(title)
    plt.scatter(x,y1)

    ax2 = plt.subplot(122,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.xlabel(xlabel)
    plt.ylabel(y2label)
    plt.scatter(x, y2)

    plt.savefig(filename)
    plt.show()



def ScatterPlot311(x,y1,y2,y3,xlabel,y1label,y2label,y3label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(311)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.ylabel(y1label)
    plt.title(title)
    plt.scatter(x,y1)

    ax2 = plt.subplot(312,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.ylabel(y2label)
    plt.scatter(x, y2)

    ax3 = plt.subplot(313,sharex=ax1)
    plt.ylim(min(y3), max(y3))
    plt.xlabel(xlabel)
    plt.ylabel(y3label)
    plt.scatter(x, y3)

    plt.savefig(filename)
    plt.show()

def ScatterPlot131(x,y1,y2,y3,xlabel,y1label,y2label,y3label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(131)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.xlabel(xlabel)
    plt.ylabel(y1label)
    plt.title(title)
    plt.scatter(x,y1)

    ax2 = plt.subplot(132,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.xlabel(xlabel)
    plt.ylabel(y2label)
    plt.scatter(x, y2)

    ax3 = plt.subplot(133,sharex=ax1)
    plt.ylim(min(y3), max(y3))
    plt.xlabel(xlabel)
    plt.ylabel(y3label)
    plt.scatter(x, y3)
    plt.savefig(filename)
    plt.show()

