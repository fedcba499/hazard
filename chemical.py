import math
from prediction import *
import matplotlib.pyplot as plt
from matplotlib import patches

from lxml import etree
from pykml.parser import Schema
from pykml.factory import KML_ElementMaker as KML
from pykml.factory import GX_ElementMaker as GX
import os

def distance( windCond, windStab, atkArea):

    dis = 10
    if windCond == 'P'or windCond == 'p':
        if atkArea > 1 :
            dis = 14
        else:
            dis = 12
    elif windCond == 'N' or windCond == 'n':
        if windStab == 'U' or windStab == 'u':
            dis = 12
        elif windStab == 'N' or windStab == 'n':
            dis = 32
        elif windStab == 'S' or windStab == 's':
            dis = 52

    return(dis)

def coOrdinates(atkGr, atkArea, windDir, windSpeed, agent, airStability):

    a = windDir
    deg_1 = [a-120, a+180, a+120]
    deg_2 = [a+30, a-30]
    deg_3 = [45, 225]

    gr = splitGr(atkGr)
    epi = epicenter(atkArea, atkGr, windDir)
    dis = distance(agent, airStability, atkArea)

    coOrd = []

    if windSpeed >= 10:
        for x in deg_1:
            y = toRadians(x)
            A = int(gr[0]+int(atkArea+0.9)*10*math.cos(y))
            AA = int(gr[1]+int(atkArea+0.9)*10*math.sin(y))
            coOrd.append(A)
            coOrd.append(AA)

        for x in deg_2:
            y = toRadians(x)
            A = int(epi[0]+11.5*dis*math.cos(y))
            AA = int(epi[1]+11.5*dis*math.sin(y))
            coOrd.append(A)
            coOrd.append(AA)
    elif windSpeed < 10:
        for x in deg_3:
            y = toRadians(x)
            A = int(gr[0]+141*math.cos(y))
            AA = int(gr[1]+141*math.sin(y))
            coOrd.append(A)
            coOrd.append(AA)    

    return(coOrd)


def display(atkGr, atkArea, dwd, ws, windCond, windStab,ownGr, dtg, mapSheet="ne-43-06", mapOrigin = 0):

    # print(atkGr, atkArea, dwd, ws, windCond, windStab)

    mapRef = splitGr(mapOrigin)

    grRef = splitGr(atkGr)

    ownGrRef = splitGr(ownGr)

    checkStr = check(atkGr, atkArea, dwd, ws, windCond, windStab,ownGr, dtg)

    if windCond == 'N' or windCond == 'n':
        atkArea = 1

    if atkArea > 2:
        atkArea = 2

    
    a = coOrdinates(atkGr, atkArea, dwd, ws, windCond, windStab)
    blankStr = [] 

    image = "img/jpgColour/"+mapSheet+".jpg"
    # print(image)
    img = plt.imread(image)

    fig, ax = plt.subplots(1,1, figsize=(45,30), dpi=20)
    plt.subplots_adjust(top=1, bottom=0, left=0, right=1)
    # ax.imshow(img, extent=[0, 720, 0, 480])
    ax.imshow(img, extent=[-25, 1775, -25, 1175])   

    if len(a) == 10:

        x = [ a[0], a[2], a[4], a[6], a[8], a[0]]
        y = [ a[1], a[3], a[5], a[7], a[9], a[1]]

        x1 = [ a[0]-mapRef[0], a[2]-mapRef[0], a[4]-mapRef[0], a[6]-mapRef[0], a[8]-mapRef[0], a[0]-mapRef[0]]
        y1 = [ a[1]-mapRef[1], a[3]-mapRef[1], a[5]-mapRef[1], a[7]-mapRef[1], a[9]-mapRef[1], a[1]-mapRef[1]]


        # print(x,y)


        ax.plot(x1,y1, color='blue', linewidth=4)

        ax.text(x1[0], y1[0], str(x[0])+str(y[0]),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
        ax.text(x1[1], y1[1], str(x[1])+str(y[1]),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
        ax.text(x1[2], y1[2], str(x[2])+str(y[2]),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
        ax.text(x1[3], y1[3], str(x[3])+str(y[3]),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
        ax.text(x1[4], y1[4], str(x[4])+str(y[4]),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)

        circle2 = plt.Circle((grRef[0]-mapRef[0], grRef[1]-mapRef[1]), atkArea*10, color='blue', fill=False, linewidth=4)
        ax.add_artist(circle2)



    else:
        b = splitGr(atkGr)
        circle1 = plt.Circle((b[0], b[1]), 100,  color='blue', fill=False, linewidth=4)
        ax.add_artist(circle1)

    

    circle3 = plt.Circle((ownGrRef[0]-mapRef[0], ownGrRef[1]-mapRef[1]), 5, color='red', linewidth=4)
    ax.add_artist(circle3)

    
    circle4 = plt.Circle((grRef[0]-mapRef[0], grRef[1]-mapRef[1]), 2, color='green', linewidth=4)
    ax.add_artist(circle4)

    
    ax.text(ownGrRef[0]-mapRef[0], ownGrRef[1]-mapRef[1], checkStr,color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)




    plt.show()


def check( atkGr, atkArea, windDir, windSpeed, agent, airStability, yourGr, dtg):
    dist = distBetPts(atkGr, yourGr)
    ang = angle(atkGr,atkArea, windDir, yourGr)
    deg = toDegree(windDir)
    a = "hello"

    if windSpeed < 10:
        if dist <= 10:
            a = inDanger(atkGr, yourGr, windSpeed, dtg)
        else:
            a = outDanger()
        

    elif windSpeed >= 10 :
        if deg > 300:
            deg = 360-deg
        if ang > deg+30 or ang < deg-30:
            a = outDanger()
        else:
            if agent == 'N' or agent == 'n':
                if airStability == 'U' or airStability == 'u':
                    if dist < 10:
                        a = inDanger(atkGr, yourGr, windSpeed, dtg)
                    else:
                        a = outDanger()
                elif airStability == 'N' or airStability == 'n':
                    if dist < 30:
                        a = inDanger(atkGr, yourGr, windSpeed, dtg)
                    else:
                        a = outDanger()
                elif airStability == 'S' or airStability == 's':
                    if dist < 50:
                        a = inDanger(atkGr, yourGr, windSpeed, dtg)
                    else:
                        a = outDanger()

            elif agent == 'P' or agent == 'p':
                if dist < 10:
                    a = inDanger(atkGr, yourGr, windSpeed, dtg)
                else:
                    a = outDanger()
    
    return(a)  


def display2(atkGr, atkArea, dwd, ws, windCond, windStab,ownGr, dtg,atkGr2, mapSheet="ne-43-06", mapOrigin = 0):
    # print(atkGr, atkArea, dwd, ws, windCond, windStab)

    mapRef = splitGr(mapOrigin)

    grRef = splitGr(atkGr)

    ownGrRef = splitGr(ownGr)

    # checkStr = check(atkGr, atkArea, dwd, ws, windCond, windStab,ownGr, dtg)

    if windCond == 'N' or windCond == 'n':
        atkArea = 1

    if atkArea > 2:
        atkArea = 2

    
    a = coOrdinates(atkGr, atkArea, dwd, ws, windCond, windStab)
    b = coOrdinates(atkGr2, atkArea, dwd, ws, windCond, windStab)
    blankStr = [] 

    image = "img/jpgColour/"+mapSheet+".jpg"
    # print(image)
    img = plt.imread(image)

    fig, ax = plt.subplots(1,1, figsize=(45,30), dpi=20)
    plt.subplots_adjust(top=1, bottom=0, left=0, right=1)
    # ax.imshow(img, extent=[0, 720, 0, 480])
    ax.imshow(img, extent=[-25, 1775, -25, 1175])   

    if len(a) == 10:

        x = [ a[0], a[2], a[4], a[6], a[8], a[0]]
        y = [ a[1], a[3], a[5], a[7], a[9], a[1]]

        x1 = [ a[0]-mapRef[0], a[2]-mapRef[0], a[4]-mapRef[0], a[6]-mapRef[0], a[8]-mapRef[0], a[0]-mapRef[0]]
        y1 = [ a[1]-mapRef[1], a[3]-mapRef[1], a[5]-mapRef[1], a[7]-mapRef[1], a[9]-mapRef[1], a[1]-mapRef[1]]


        # print(x,y)


        ax.plot(x1,y1, color='blue', linewidth=4)

        ax.text(x1[0], y1[0], str(x[0])+str(y[0]),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
        ax.text(x1[1], y1[1], str(x[1])+str(y[1]),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
        ax.text(x1[2], y1[2], str(x[2])+str(y[2]),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
        ax.text(x1[3], y1[3], str(x[3])+str(y[3]),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
        ax.text(x1[4], y1[4], str(x[4])+str(y[4]),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)

        circle2 = plt.Circle((grRef[0]-mapRef[0], grRef[1]-mapRef[1]), atkArea*10, color='blue', fill=False, linewidth=4)
        ax.add_artist(circle2)



    else:
        b = splitGr(atkGr)
        circle1 = plt.Circle((b[0], b[1]), 100,  color='blue', fill=False, linewidth=4)
        ax.add_artist(circle1)



    if len(b) == 10:

        x = [ b[0], b[2], b[4], b[6], b[8], b[0]]
        y = [ b[1], b[3], b[5], b[7], b[9], b[1]]

        x1 = [ b[0]-mapRef[0], b[2]-mapRef[0], b[4]-mapRef[0], b[6]-mapRef[0], b[8]-mapRef[0], b[0]-mapRef[0]]
        y1 = [ b[1]-mapRef[1], b[3]-mapRef[1], b[5]-mapRef[1], b[7]-mapRef[1], b[9]-mapRef[1], b[1]-mapRef[1]]


        # print(x,y)


        ax.plot(x1,y1, color='blue', linewidth=4)

        ax.text(x1[0], y1[0], str(x[0])+str(y[0]),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
        ax.text(x1[1], y1[1], str(x[1])+str(y[1]),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
        ax.text(x1[2], y1[2], str(x[2])+str(y[2]),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
        ax.text(x1[3], y1[3], str(x[3])+str(y[3]),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
        ax.text(x1[4], y1[4], str(x[4])+str(y[4]),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)

        circle2 = plt.Circle((grRef[0]-mapRef[0], grRef[1]-mapRef[1]), atkArea*10, color='blue', fill=False, linewidth=4)
        ax.add_artist(circle2)



    else:
        b = splitGr(atkGr)
        circle1 = plt.Circle((b[0], b[1]), 100,  color='blue', fill=False, linewidth=4)
        ax.add_artist(circle1)

    if len(a) == 10 and len(b)==10:

        p1 = [a[2], b[2]]
        q1 = [a[3], b[3]]

        ax.plot(p1,q1, color='blue', linewidth=4)

        p2 = [a[6], b[6]]
        q2 = [a[7], b[7]]

        ax.plot(p2,q2, color='blue', linewidth=4)

        p3 = [a[8], b[8]]
        q3 = [a[9], b[9]]

        ax.plot(p3,q3, color='blue', linewidth=4)

  

    plt.show()

def display3(atkGr, atkArea, dwd, ws, windCond, windStab):

    a = coOrdinates(atkGr, atkArea, dwd, ws, windCond, windStab)
    b = []
    grRef = splitGr(atkGr)
    for x in range(5):
        p = str(str(77+a[2*x]/1000)+","+str(34+a[2*x+1]/1000)+","+str(0)+" ")
        # print(p)
        b.append(p)

    q = ''
    for x in range(37):
        q = q+str(str("%.4f" % float(77+(grRef[0]+10*math.cos(math.radians(x*10)))/1000))+","+str("%.4f" % float(34+(grRef[1]+10*math.sin(math.radians(x*10)))/1000))+","+str(0)+" \n")

    print(q)
       

    doc = KML.kml(        
        KML.Placemark( 
            KML.name("gx:altitudeMode Example"), 
            KML.Style(
            KML.LineStyle(
                KML.color('ff501400'),
                GX.physicalWidth('80'),
            ),
            id="street",
            ),          
            KML.LookAt(
                KML.longitude(77+grRef[0]/1000),
                KML.latitude(34+grRef[1]/1000),
                KML.heading(0),
                KML.tilt(0),
                KML.range(25000),
                GX.altitudeMode("relativeToSeaFloor"),
            ),
            KML.styleUrl('#street'),
            KML.MultiGeometry(
                KML.LineString(
                    KML.extrude(0),
                    GX.altitudeMode("relativeToSeaFloor"),
                    KML.coordinates(                       
                        str(b[2]),
                        str(b[3]),
                        str(b[4]),
                        str(b[0])                                        
                    )
                ),
                KML.LineString(
                    KML.extrude(0),
                    GX.altitudeMode("relativeToSeaFloor"),
                    KML.coordinates(                        
                        str(q)                                        
                    )
                )
            )            
        )
    )

    print(etree.tostring(etree.ElementTree(doc), pretty_print=True).decode())

    # output a KML file (named based on the Python script)
    outfile = open(__file__.rstrip('.py')+'.kml','w')
    outfile.write(etree.tostring(etree.ElementTree(doc), pretty_print=True).decode())

    # assert Schema('kml22gx.xsd').validate(doc)

    # This validates:
    # xmllint --noout --schema ../../pykml/schemas/kml22gx.xsd altitudemode_reference.kml

    os.startfile("chemical.kml")

    





