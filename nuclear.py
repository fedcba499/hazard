import math
from prediction import *
import matplotlib.pyplot as plt
from matplotlib import patches

from lxml import etree
from pykml.parser import Schema
from pykml.factory import KML_ElementMaker as KML
from pykml.factory import GX_ElementMaker as GX
import os


def display(gridRef,cloudRad, windDir, windSpeed, zoneDist, extentDeg, ownGr, dtg, mapSheet="ne-43-06", mapOrigin = 0):

    mapRef = splitGr(mapOrigin)

    ownGrRef = splitGr(ownGr)

    grRef = splitGr(gridRef)

    checkStr = check( gridRef, cloudRad, windDir, windSpeed, zoneDist, extentDeg, ownGr, dtg)

    gridRef = splitGr(gridRef)
    windDir = toDegree(windDir)

    tanAng = math.degrees(math.asin(cloudRad/zoneDist))    
    tanAng = extentDeg/2+90-tanAng

    deg_1 = [windDir+tanAng, windDir+180, windDir-tanAng]
    deg_2 = [windDir-extentDeg/2, windDir+extentDeg/2]

    boundX = []
    boundY = []

    for x in range(3):
        p = gridRef[0]+10*cloudRad*math.cos(math.radians(deg_1[x]))
        q = gridRef[1]+10*cloudRad*math.sin(math.radians(deg_1[x]))
        boundX.append(p)
        boundY.append(q)

    for x in range(2):
        p = gridRef[0]+10*zoneDist*math.cos(math.radians(deg_2[x]))
        q = gridRef[1]+10*zoneDist*math.sin(math.radians(deg_2[x]))
        boundX.append(p)
        boundY.append(q)

    for x in range(2):
        p = gridRef[0]+20*zoneDist*math.cos(math.radians(deg_2[x]))
        q = gridRef[1]+20*zoneDist*math.sin(math.radians(deg_2[x]))
        boundX.append(p)
        boundY.append(q)

    p = " "
    for x in range(7):
        p = p + str(round(boundX[x]))+str(round(boundY[x]))+", "

    # print(p)

    image = "img/jpgColour/"+mapSheet+".jpg"
    # print(image)
    img = plt.imread(image)

    fig, ax = plt.subplots(1,1, figsize=(45,30), dpi=20)
    plt.subplots_adjust(top=1, bottom=0, left=0, right=1)
    # ax.imshow(img, extent=[0, 720, 0, 480])
    ax.imshow(img, extent=[-25, 1775, -25, 1175])

    if windSpeed < 8:
        circle5 = plt.Circle((gridRef[0]-mapRef[0], gridRef[1]-mapRef[1]), cloudRad*10, color='blue', fill=False, linewidth=4)
        ax.add_artist(circle5)
    
    else:


        x = [ boundX[0]-mapRef[0], boundX[4]-mapRef[0] ]
        y = [ boundY[0]-mapRef[1], boundY[4]-mapRef[1] ]

        # print(x,y)

        ax.plot(x,y, color='blue', linewidth=4)

        x1 = [ boundX[2]-mapRef[0], boundX[3]-mapRef[0] ]
        y1 = [ boundY[2]-mapRef[1], boundY[3]-mapRef[1] ]

        # print(x1,y1)

        ax.plot(x1,y1, color='blue', linewidth=4)

        x2 = [ gridRef[0]-mapRef[0], boundX[5]-mapRef[0] ]
        y2 = [ gridRef[1]-mapRef[1], boundY[5]-mapRef[1] ]

        # print(x2,y2)

        ax.plot(x2,y2, color='blue', linewidth=4)

        x3 = [ gridRef[0]-mapRef[0], boundX[6]-mapRef[0] ]
        y3 = [ gridRef[1]-mapRef[1], boundY[6]-mapRef[1] ]

        # print(x3,y3)

        ax.plot(x3,y3, color='blue', linewidth=4)


        circle2 = plt.Circle((gridRef[0]-mapRef[0], gridRef[1]-mapRef[1]), cloudRad*10, color='blue', fill=False, linewidth=4)
        ax.add_artist(circle2)


        arc = patches.Arc((gridRef[0]-mapRef[0], gridRef[1]-mapRef[1]), zoneDist*20, zoneDist*20, 0, deg_2[0], deg_2[1], color='blue', linewidth=4)
        ax.add_patch(arc)

        arc1 = patches.Arc((gridRef[0]-mapRef[0], gridRef[1]-mapRef[1]), zoneDist*40, zoneDist*40, 0,  deg_2[0], deg_2[1],color='blue', linewidth=4)    
        ax.add_patch(arc1)   

        
        arc2 = patches.Arc((gridRef[0]-mapRef[0], gridRef[1]-mapRef[1]), windSpeed*20, windSpeed*20, 0,  deg_2[0], deg_2[1],color='blue', linewidth=4, linestyle= '--')    
        ax.add_patch(arc2)   

        arc3 = patches.Arc((gridRef[0]-mapRef[0], gridRef[1]-mapRef[1]), windSpeed*40, windSpeed*40, 0,  deg_2[0], deg_2[1],color='blue', linewidth=4, linestyle= '--')    
        ax.add_patch(arc3)  

        ax.text(boundX[0]-mapRef[0], boundY[0]-mapRef[1], str(round(boundX[0]))+str(round(boundY[0])),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
        ax.text(boundX[1]-mapRef[0], boundY[1]-mapRef[1], str(round(boundX[1]))+str(round(boundY[1])),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
        ax.text(boundX[2]-mapRef[0], boundY[2]-mapRef[1], str(round(boundX[2]))+str(round(boundY[2])),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
        ax.text(boundX[3]-mapRef[0], boundY[3]-mapRef[1], str(round(boundX[3]))+str(round(boundY[3])),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
        ax.text(boundX[4]-mapRef[0], boundY[4]-mapRef[1], str(round(boundX[4]))+str(round(boundY[4])),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
        ax.text(boundX[5]-mapRef[0], boundY[5]-mapRef[1], str(round(boundX[5]))+str(round(boundY[5])),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
        ax.text(boundX[6]-mapRef[0], boundY[6]-mapRef[1], str(round(boundX[6]))+str(round(boundY[6])),color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)
    

    circle3 = plt.Circle((ownGrRef[0]-mapRef[0], ownGrRef[1]-mapRef[1]), 5, color='red', linewidth=4)
    ax.add_artist(circle3)
    
    circle4 = plt.Circle((grRef[0]-mapRef[0], grRef[1]-mapRef[1]), 2, color='green', linewidth=4)
    ax.add_artist(circle4)
    
    ax.text(ownGrRef[0]-mapRef[0], ownGrRef[1]-mapRef[1], checkStr,color='blue', horizontalalignment='center',verticalalignment='center', size=50, fontdict=None)


    plt.show()

    
def check( atkGr, atkArea, windDir, windSpeed,zone, extent, yourGr, dtg):
    dist = distBetPts(atkGr, yourGr)
    # print('dist',dist)
    angFromCenter = angleBet2Gr(atkGr, yourGr)
    # print("angFromCenter", angFromCenter)
    deg = toDegree(windDir)
    # print("deg", deg)

    a = "hello"

    if windSpeed < 8:
        if dist <= atkArea:
            a = inDanger(atkGr, yourGr, windSpeed, dtg)
        else:
            a = outDanger()        

    elif windSpeed >= 8 :
        if deg > 300:
            deg = 360-deg
        if dist < atkArea:
            a = inDanger(atkGr, yourGr, windSpeed, dtg)
        else:
            if angFromCenter > deg+(extent/2) or angFromCenter < deg-(extent/2):
                a = outDanger()
            else:        
                a = inDanger(atkGr, yourGr, windSpeed, dtg)   

    
    return(a)  


# print(check( 200200, 2.2, 0, 10, 9, 40, 225270))

def display3(gridRef,cloudRad, windDir, windSpeed, zoneDist, extentDeg):

    # mapRef = splitGr(mapOrigin)

    # ownGrRef = splitGr(ownGr)

    # grRef = splitGr(gridRef)

    # checkStr = check( gridRef, cloudRad, windDir, windSpeed, zoneDist, extentDeg, ownGr, dtg)

    gridRef = splitGr(gridRef)
    windDir = toDegree(windDir)

    tanAng = math.degrees(math.asin(cloudRad/zoneDist))    
    tanAng = extentDeg/2+90-tanAng

    deg_1 = [windDir+tanAng, windDir+180, windDir-tanAng]
    deg_2 = [windDir-extentDeg/2, windDir+extentDeg/2]

    boundX = []
    boundY = []

    for x in range(3):
        p = gridRef[0]+10*cloudRad*math.cos(math.radians(deg_1[x]))
        q = gridRef[1]+10*cloudRad*math.sin(math.radians(deg_1[x]))
        boundX.append(p)
        boundY.append(q)

    for x in range(2):
        p = gridRef[0]+10*zoneDist*math.cos(math.radians(deg_2[x]))
        q = gridRef[1]+10*zoneDist*math.sin(math.radians(deg_2[x]))
        boundX.append(p)
        boundY.append(q)

    for x in range(2):
        p = gridRef[0]+20*zoneDist*math.cos(math.radians(deg_2[x]))
        q = gridRef[1]+20*zoneDist*math.sin(math.radians(deg_2[x]))
        boundX.append(p)
        boundY.append(q)

    # a = coOrdinates(atkGr, atkArea, dwd, ws, windCond, windStab)
    b = []
    # grRef = splitGr(atkGr)
    for x in range(7):
        p = str(str(77+boundX[x]/1000)+","+str(34+boundY[x]/1000)+","+str(0)+" ")
        # print(p)
        b.append(p)

    q = ''
    for x in range(37):
        q = q+str(str("%.4f" % float(77+(gridRef[0]+cloudRad*10*math.cos(math.radians(x*10)))/1000))+","+str("%.4f" % float(34+(gridRef[1]+cloudRad*10*math.sin(math.radians(x*10)))/1000))+","+str(0)+" \n")

    r = ''
    for x in range(int(extentDeg/2+1)):
        r = r+str(str("%.4f" % float(77+(gridRef[0]+zoneDist*10*math.cos(math.radians((windDir-extentDeg/2)+x*2)))/1000))+","+str("%.4f" % float(34+(gridRef[1]+zoneDist*10*math.sin(math.radians((windDir-extentDeg/2)+x*2)))/1000))+","+str(0)+" \n")

    s = ''
    for x in range(int(extentDeg/2+1)):
        s = s+str(str("%.4f" % float(77+(gridRef[0]+zoneDist*20*math.cos(math.radians((windDir-extentDeg/2)+x*2)))/1000))+","+str("%.4f" % float(34+(gridRef[1]+zoneDist*20*math.sin(math.radians((windDir-extentDeg/2)+x*2)))/1000))+","+str(0)+" \n")

    t = ''
    for x in range(int(extentDeg/2+1)):
        t = t+str(str("%.4f" % float(77+(gridRef[0]+windSpeed*10*math.cos(math.radians((windDir-extentDeg/2)+x*2)))/1000))+","+str("%.4f" % float(34+(gridRef[1]+windSpeed*10*math.sin(math.radians((windDir-extentDeg/2)+x*2)))/1000))+","+str(0)+" \n")

    u = ''
    for x in range(int(extentDeg/2+1)):
        u = u+str(str("%.4f" % float(77+(gridRef[0]+windSpeed*20*math.cos(math.radians((windDir-extentDeg/2)+x*2)))/1000))+","+str("%.4f" % float(34+(gridRef[1]+windSpeed*20*math.sin(math.radians((windDir-extentDeg/2)+x*2)))/1000))+","+str(0)+" \n")


    # print(q)

    grStr = str(str(77+gridRef[0]/1000)+","+str(34+gridRef[1]/1000)+","+str(0)+" ")
       

    doc = KML.kml( 
        KML.Folder(
            KML.name("NHP"),
            KML.LookAt(
                KML.longitude(77+(gridRef[0]+zoneDist*10*math.cos(math.radians(windDir)))/1000),
                KML.latitude(34+(gridRef[1]+zoneDist*10*math.sin(math.radians(windDir)))/1000),
                KML.heading(0),
                KML.tilt(0),
                KML.range(50000),
                GX.altitudeMode("relativeToSeaFloor"),
            ),
            KML.Placemark( 
                KML.name("gx:altitudeMode Example2"), 
                KML.Style(
                KML.LineStyle(
                    KML.color('ff501400'),
                    GX.physicalWidth('80'),
                ),
                id="street",
                ),          
                KML.LookAt(
                    KML.longitude(77+(gridRef[0]+zoneDist*10*math.cos(math.radians(windDir)))/1000),
                    KML.latitude(34+(gridRef[1]+zoneDist*10*math.sin(math.radians(windDir)))/1000),
                    KML.heading(0),
                    KML.tilt(0),
                    KML.range(50000),
                    GX.altitudeMode("relativeToSeaFloor"),
                ),
                KML.styleUrl('#street'),
                KML.MultiGeometry(
                    KML.LineString(
                        KML.extrude(0),
                        GX.altitudeMode("relativeToSeaFloor"),
                        KML.coordinates(                       
                            str(grStr),
                            str(b[5])                                                               
                        )
                    ),
                    KML.LineString(
                        KML.extrude(0),
                        GX.altitudeMode("relativeToSeaFloor"),
                        KML.coordinates(                       
                            str(grStr),
                            str(b[6])                                                               
                        )
                    ),
                    KML.LineString(
                        KML.extrude(0),
                        GX.altitudeMode("relativeToSeaFloor"),
                        KML.coordinates(                       
                            str(b[2]),
                            str(b[3])                                                               
                        )
                    ),
                    KML.LineString(
                        KML.extrude(0),
                        GX.altitudeMode("relativeToSeaFloor"),
                        KML.coordinates(                       
                            str(b[0]),
                            str(b[4])                                                               
                        )
                    ),
                    KML.LineString(
                        KML.extrude(0),
                        GX.altitudeMode("relativeToSeaFloor"),
                        KML.coordinates(                        
                            str(q)                                        
                        )
                    ),
                    KML.LineString(
                        KML.extrude(0),
                        GX.altitudeMode("relativeToSeaFloor"),
                        KML.coordinates(                        
                            str(r)                                        
                        )
                    ),
                    KML.LineString(
                        KML.extrude(0),
                        GX.altitudeMode("relativeToSeaFloor"),
                        KML.coordinates(                        
                            str(s)                                        
                        )
                    )
                )            
            ),
            KML.Placemark( 
                KML.name("gx:altitudeMode Example3"), 
                KML.Style(
                KML.LineStyle(
                    KML.color('ff5014E7'),
                    GX.physicalWidth('100'),
                ),
                id="street",
                ),          
                KML.LookAt(
                    KML.longitude(77+(gridRef[0]+zoneDist*10*math.cos(math.radians(windDir)))/1000),
                    KML.latitude(34+(gridRef[1]+zoneDist*10*math.sin(math.radians(windDir)))/1000),
                    KML.heading(0),
                    KML.tilt(0),
                    KML.range(50000),
                    GX.altitudeMode("relativeToSeaFloor"),
                ),
                KML.styleUrl('#street'),
                KML.MultiGeometry(
                    KML.LineString(
                        KML.extrude(0),
                        GX.altitudeMode("relativeToSeaFloor"),
                        KML.coordinates(                        
                            str(t)                                        
                        )
                    ),
                    KML.LineString(
                        KML.extrude(0),
                        GX.altitudeMode("relativeToSeaFloor"),
                        KML.coordinates(                        
                            str(u)                                        
                        )
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

    os.startfile("nuclear.kml")



