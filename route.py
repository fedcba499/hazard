import math
from prediction import *
import matplotlib.pyplot as plt
from matplotlib import patches

from lxml import etree
from pykml.parser import Schema
from pykml.factory import KML_ElementMaker as KML
from pykml.factory import GX_ElementMaker as GX
import os

def display(gridRef, windDir, extentDeg, time, radiation, dist, timeEntry, timeExit, distEntry, distExit):
    print(gridRef,windDir, extentDeg, time, radiation, dist, timeEntry, timeExit, distEntry, distExit )
    print(type(gridRef),type(windDir), type(extentDeg), type(time), type(radiation), type(dist), type(timeEntry), type(timeExit), type(distEntry), type(distExit) )


    gridRef = splitGr(gridRef)
    windDir = toDegree(windDir)

    deg_2 = [windDir-extentDeg/2, windDir+extentDeg/2]
    dist_2 = [distEntry, distExit]

    boundX = []
    boundY = []

    
    doseTaken = (radiation*float(math.pow(time, 1.2))*dist*dist/0.2)*(1/float(math.pow(timeEntry, 0.2))-1/float(math.pow(timeExit, 0.2)))*(1/distEntry-1/distExit)

    doseTaken = float("%.2f" % doseTaken)

    for x in range(2):

        p = gridRef[0]+10*dist_2[x]*math.cos(math.radians(deg_2[x]))
        q = gridRef[1]+10*dist_2[x]*math.sin(math.radians(deg_2[x]))
        boundX.append(p)
        boundY.append(q)

    b = []
    for x in range(2):
        p = str(str(77+boundX[x]/1000)+","+str(34+boundY[x]/1000)+","+str(0)+" ")
        b.append(p)

    c = str(str(77+((boundX[0]+boundX[1])/2)/1000)+","+str(34+((boundY[0]+boundY[1])/2)/1000)+","+str(0)+" ")

    
    doc = KML.kml( 
        KML.Folder(
            KML.name("Dose Taken"),
            KML.LookAt(
                KML.longitude(77+gridRef[0]/1000),
                KML.latitude(34+gridRef[1]/1000),
                KML.heading(0),
                KML.tilt(0),
                KML.range(50000),
                GX.altitudeMode("relativeToSeaFloor"),
            ),
            KML.Placemark( 
                KML.name(str(doseTaken)+" Rads"), 
                KML.Style(
                KML.LineStyle(
                    KML.color('ff501400'),
                    GX.physicalWidth('80'),
                ),
                id="street",
                ),          
                KML.styleUrl('#street'),
                KML.Point(
                    KML.coordinates(
                        str(c)
                    )
                )        
            ),
            KML.Placemark( 
                KML.name("line"), 
                KML.Style(
                KML.LineStyle(
                    KML.color('ff5014E7'),
                    GX.physicalWidth('100'),
                ),
                id="street",
                ),          
                KML.styleUrl('#street'),
                KML.MultiGeometry(
                    KML.LineString(
                        KML.extrude(0),
                        GX.altitudeMode("relativeToSeaFloor"),
                        KML.coordinates(                        
                            str(b[0]),
                            str(b[1])                                       
                        )
                    )
                )            
            )
        )     
    )

    

    # doc = KML.kml( 
       
    #     KML.Placemark( 
    #         KML.name(str(doseTaken)), 
    #         KML.Style(
    #         KML.LineStyle(
    #             KML.color('ff501400'),
    #             GX.physicalWidth('80'),
    #         ),
    #         id="street",
    #         ),          
    #         KML.LookAt(
    #             KML.longitude(77+gridRef[0]/1000),
    #             KML.latitude(34+gridRef[1]/1000),
    #             KML.heading(0),
    #             KML.tilt(0),
    #             KML.range(25000),
    #             GX.altitudeMode("relativeToSeaFloor"),
    #         ),
    #         KML.styleUrl('#street'),
    #         KML.Point(
    #             KML.coordinates(
    #                 str(b[0])
    #             )
    #         ),
    #         KML.MultiGeometry(
    #             KML.LineString(
    #                 KML.extrude(0),
    #                 GX.altitudeMode("relativeToSeaFloor"),
    #                 KML.coordinates(                       
    #                     str(b[0]),
    #                     str(b[1])                                      
    #                 )
    #             )
    #         )            
    #     )
    # )

    print(etree.tostring(etree.ElementTree(doc), pretty_print=True).decode())

    # output a KML file (named based on the Python script)
    outfile = open(__file__.rstrip('.py')+'.kml','w')
    outfile.write(etree.tostring(etree.ElementTree(doc), pretty_print=True).decode())

    # assert Schema('kml22gx.xsd').validate(doc)

    # This validates:
    # xmllint --noout --schema ../../pykml/schemas/kml22gx.xsd altitudemode_reference.kml

    os.startfile("route.kml")

    