import math
from prediction import *


   
def display(ws1, wd1, ws2, wd2, ws3, wd3, ws4, wd4, ws5, wd5, ws6, wd6, ws7, wd7, ws8, wd8, ws9, wd9, ws10, wd10, ct, cb, sh):

    windSpeed = [ws1, ws2, ws3, ws4, ws5, ws6, ws7, ws8, ws9, ws10]

    windDir = [wd1, wd2, wd3, wd4, wd5, wd6, wd7, wd8, wd9, wd10]

    cloud = [ct, cb, sh]

    convWindDir = []
    veclen = []
    xCordinates = []
    yCordinates = []
    finalxCord = []
    finalyCord = []
    cloudxCord = []
    cloudyCord = []
    cloudTime = []

    timeInLayer = [0.68, 0.59, 0.52, 0.50, 0.48, 0.45, 0.42, 0.40, 0.39, 0.38]


    for x in range(10):
        p = toDegree(windDir[x])
        convWindDir.append(p)
        q = vectorLength(windSpeed[x], timeInLayer[x])
        q = float("%.2f" % q)
        veclen.append(q)
        
    for x in range(10):
        p = xcord(veclen[x], convWindDir[x])
        p = float("%.2f" % p)
        q = ycord(veclen[x], convWindDir[x])
        q = float("%.2f" % q)
        xCordinates.append(p)
        yCordinates.append(q)

    p = 0
    q = 0

    for x in range(10):
        p = p + xCordinates[x]
        p = float("%.2f" % p)
        q = q + yCordinates[x]
        q = float("%.2f" % q)
        finalxCord.append(p)
        finalyCord.append(q)

    p = 0
    q = 0
    r = 0

    for x in range(3):

        for y in range(int(cloud[x]/2)):
            p = p + xCordinates[y]
            # p = float("%.2f" % p)
            q = q + yCordinates[y]
            # q = float("%.2f" % q)
            r = r + timeInLayer[y]
            # r = float("%.2f" % r)
        
        p = p + xCordinates[int(cloud[x]/2)]*float(cloud[x]%2)/2
        # p = float("%.2f" % p)
        q = q + yCordinates[int(cloud[x]/2)]*float(cloud[x]%2)/2
        # q = float("%.2f" % q)
        r = r + timeInLayer[int(cloud[x]/2)]*float(cloud[x]%2)/2
        # r = float("%.2f" % r)

        cloudxCord.append(p)
        cloudyCord.append(q)
        cloudTime.append(r)

        p = 0
        q = 0
        r = 0

    effWindSpeed = math.sqrt(cloudxCord[1]**2 + cloudyCord[1]**2)/cloudTime[1]
    effWindSpeed = float("%.2f" % effWindSpeed)

    ctDeg = math.degrees(math.atan2(cloudyCord[0],cloudxCord[0]))
    shDeg = math.degrees(math.atan2(cloudyCord[2],cloudxCord[2]))
    
    if ctDeg < 0:
        ctDeg = 360+ctDeg

    if shDeg < 0:
        shDeg = 360+shDeg

    if ctDeg-shDeg < 90:
        cbDeg = int((ctDeg+shDeg)/2)
        ctshDeg = abs(ctDeg-shDeg)
    else:
        if ctDeg-shDeg > 0:
            ctDeg = 360-ctDeg
            ctshDeg = abs(ctDeg-shDeg)
            cbDeg = int((shDeg+ctDeg)/2)
            if cbDeg<0:
                cbDeg = 360+cbDeg
        
        elif shDeg-ctDeg > 0:
            shDeg = 360-shDeg
            ctshDeg = abs(ctDeg-shDeg)
            cbDeg = int((shDeg+ctDeg)/2)
            if cbDeg<0:
                cbDeg = 360+cbDeg

    ctDeg = toDegree(ctDeg)
    shDeg = toDegree(shDeg)
    cbDeg = toDegree(cbDeg)

    if effWindSpeed < 7:
        effDownMsg = float("%03d" % int(cbDeg))    
    elif ctshDeg <= 40:
        effDownMsg = "%03d" % int(cbDeg) + "%03d" % int(effWindSpeed+1) 
    elif ctshDeg>40:
        effDownMsg = "%03d" % int(cbDeg) + "%03d" % int(effWindSpeed+1) + "%03d" % int(ctshDeg) 
    
    # testedm.blank.delete(0, END)
    # testedm.blank.insert(0, effDownMsg) 

    # # print(effDownMsg)

    return(effDownMsg)