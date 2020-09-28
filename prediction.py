import math

def splitGr(gr):
    x = int(gr) // 1000
    y = int(gr) % 1000
    z = [x, y]
    return (z)


def toRadians(windDir):
    a = 90+360-int(windDir)
    p = math.radians(a)
    return(p)

def toDegree(windDir):
    a = 90+360-int(windDir)
    if a > 360:
        a = a - 360
    return(a)

def distBetPts(gr1, gr2):
    a = splitGr(gr1)
    b = splitGr(gr2)
    dist = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)  
    return (dist/10) 


def epicenter(atkArea, atkGr, windDir):
    x = splitGr(atkGr)
    y = toRadians(windDir+180)

    if atkArea > 1 :
        A = int(x[0] + 40*math.cos(y))
        AA = int(x[1] + 40*math.sin(y))
    else:
        A = int(x[0] + 20*math.cos(y))
        AA = int(x[1] + 20*math.sin(y))

    epi = [A,AA]

    return(epi)

def epicenterNuc(atkArea, atkGr, windDir, zone, extent):
    x = splitGr(atkGr)
    y = toRadians(windDir+180)

    theta = math.degrees(math.asin(atkArea/zone))
    alpha = extent/2-theta
    epiDist = atkArea/math.sin(math.radians(alpha))

    A = int(x[0] + 10*epiDist*math.cos(y))
    AA = int(x[1] + 10*epiDist*math.sin(y))

    epi = A*1000+AA

    return(epi)

def angle (atkGr, atkArea, windDir, yourGr):
    a = epicenter(atkArea, atkGr, windDir)
    b = splitGr(yourGr)
    p = b[0]-a[0]
    q = b[1]-a[1]
    r = math.degrees(math.atan2(q,p))

    if p < 0 and q < 0:
        r = r+360
    elif p > 0 and q < 0:
        r = r+360

    if r > 300:
        r = 360 - r

    return(r)

def angleBet2Gr (epiGr, yourGr):
    a = splitGr(epiGr)
    b = splitGr(yourGr)
    p = b[0]-a[0]
    q = b[1]-a[1]
    r = math.degrees(math.atan2(q,p))

    if p < 0 and q < 0:
        r = r+360
    elif p > 0 and q < 0:
        r = r+360

    if r > 300:
        r = 360 - r

    return(r)

def timeTaken( atkGr, yourGr, windSpeed, dtg):
    a = distBetPts(atkGr, yourGr)
    b = a/windSpeed
    c = b - int(b)
    d = c*60
    time = dtg%10000
    hr = time//100
    min = time%100
    hr = hr+int(b)
    min = min+int(d)
    if min >=60:
        min = min-60
        hr = hr+1
    e = [int(b), int(d), hr, min]
    return(e)

def interSecPt( x1, y1, m1, x2, y2, m2):
    p = ((y1-x1*math.tan(math.radians(m1)))-(y2-x2*math.tan(math.radians(m2))))/(math.tan(math.radians(m2))-math.tan(math.radians(m1)))
    q = math.tan(math.radians(m1))*p + (y1-x1*math.tan(math.radians(m1)))
    
    return ([p, q])

def vectorLength( windSpeed, time):
    x = windSpeed*1.85*time
    return(x)

def xcord( vecLen, convVecDeg):
    x = vecLen*math.cos(math.radians(convVecDeg))
    return(x)

def ycord( vecLen, convVecDeg):
    x = vecLen*math.sin(math.radians(convVecDeg))
    return(x)


def outDanger():
    a = "You are Out of the Hazard Area"
    return(a)

def inDanger( atkGr, yourGr, windSpeed, dtg):
    a = timeTaken(atkGr, yourGr, windSpeed, dtg)
    b = str(a[0])
    c = str(a[1])
    hr = str(a[2])
    min = str(a[3])
    d = "You are In Hazard Area Estimated Arrival of Contamination is  " + b + " hrs  " + c + " mins i.e.,"+hr+min+"hrs"
    return(d)
