import math
import scipy.integrate



# x= 4.05**1.2

# print(x)

def integrand(x, a):
    return a/x**1.2

# a = 68.7

# i = scipy.integrate.quad(integrand, 0.5, 6, args=(a))

# print(i[0])


def displayRate(time, radiation, timeReq):

    a = (radiation*time**1.2)/timeReq**1.2

    return a


def displayRad(time, radiation, radReq):

    a = (radiation*time**1.2)/radReq

    a = a**(1/1.2)

    return a

def displayDose(time, radiation, timeEntry, timeExit):

    a = radiation*time**1.2

    i = scipy.integrate.quad(integrand, timeEntry, timeExit, args=(a))

    return i[0]

def displayTime(time, radiation, radLimit, timeForMsn):
    p = 0

    for i in range(1, 384):

        p = p+0.25

        a = displayDose( time, radiation,p, p+timeForMsn)
        if a < radLimit:
            # print(i)
            break

    return p

def displayExit(time, radiation, radLimit, timeEntry):
    
    p = timeEntry

    for i in range(1, 384):

        p = p+0.25

        a = displayDose(time, radiation, timeEntry, p)
        if a > radLimit:
            # print(i)
            break

    return p-0.25
