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

def kmlCheck(atkGr, atkArea, dwd, ws, windCond, windStab):

    a = coOrdinates(atkGr, atkArea, dwd, ws, windCond, windStab)
    b = []
    grRef = splitGr(atkGr)
    for x in range(5):
        p = str(str(77+a[2*x]/1000)+","+str(34+a[2*x+1]/1000)+","+str(400)+" ")
        print(p)
        b.append(p)
    
    print(b)

    

    doc = KML.kml(
        KML.Placemark(
            KML.name("gx:altitudeMode Example"),
            KML.LookAt(
                KML.longitude(77.577),
                KML.latitude(34.152),
                KML.heading(-60),
                KML.tilt(70),
                KML.range(6300),
                GX.altitudeMode("relativeToSeaFloor"),
            ),
            KML.LineString(
                KML.extrude(1),
                GX.altitudeMode("relativeToSeaFloor"),
                KML.coordinates(
                    # "77.825,34.233,400 "
                    # "77.820,34.222,400 "
                    # "77.812,34.212,400 "
                    # "77.796,34.209,400 "
                    # "77.788,34.205,400"
                  str(b[0]),
                  str(b[1]),
                  str(b[2]),
                  str(b[3]),
                  str(b[4]),
                  str(b[0])                    
                )
            )
        )
    )

    print(etree.tostring(doc, pretty_print=True))

    # output a KML file (named based on the Python script)
    outfile = open(__file__.rstrip('.py')+'.kml','wb')
    outfile.write(etree.tostring(doc, pretty_print=True))

    assert Schema('kml22gx.xsd').validate(doc)

    # This validates:
    # xmllint --noout --schema ../../pykml/schemas/kml22gx.xsd altitudemode_reference.kml

    

kmlCheck(577152, 1, 0, 10, 'p', 'u')
os.startfile("chemicalKml.kml")


