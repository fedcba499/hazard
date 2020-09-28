import math
from prediction import *
import matplotlib.pyplot as plt
from matplotlib import patches

from lxml import etree
from pykml.parser import Schema
from pykml.factory import KML_ElementMaker as KML
from pykml.factory import GX_ElementMaker as GX
import os

def display3(atkGr, burst,yd):
    # GROUNDBURST
    if burst == 's' or burst == 'S':
        thermalfirstConstant = 0.318870
        thermalsecondConstant = 0.24955
        thermalthirdConstant = 0.20142
        twentypsiConstant = 0.22049
        fivepsiConstant = 0.46631
        onepsiConstant = 1.4221

    # AIRBURST
    if burst == 'a' or burst == 'A':
        thermalfirstConstant = 0.90705
        thermalsecondConstant = 0.70125
        thermalthirdConstant = 0.549
        twentypsiConstant = 0.24596
        fivepsiConstant = 0.57832
        onepsiConstant = 1.6639
    
    thermalfirst = math.pow(yd, 0.525)*thermalfirstConstant
    thermalsecond = math.pow(yd, 0.525)*thermalsecondConstant
    thermalthird = math.pow(yd, 0.525)*thermalthirdConstant
    twentypsi = math.pow(yd, 0.33)*twentypsiConstant
    fivepsi = math.pow(yd, 0.33)*fivepsiConstant
    onepsi = math.pow(yd, 0.33)*onepsiConstant

    gridRef = splitGr(atkGr)

    p = ''
    for x in range(37):
        p = p+str(str("%.4f" % float(77+(gridRef[0]+thermalfirst*10*math.cos(math.radians(x*10)))/1000))+","+str("%.4f" % float(34+(gridRef[1]+thermalfirst*10*math.sin(math.radians(x*10)))/1000))+","+str(0)+" \n")

    q = ''
    for x in range(37):
        q = q+str(str("%.4f" % float(77+(gridRef[0]+thermalsecond*10*math.cos(math.radians(x*10)))/1000))+","+str("%.4f" % float(34+(gridRef[1]+thermalsecond*10*math.sin(math.radians(x*10)))/1000))+","+str(0)+" \n")

    r = ''
    for x in range(37):
        r = r+str(str("%.4f" % float(77+(gridRef[0]+thermalthird*10*math.cos(math.radians(x*10)))/1000))+","+str("%.4f" % float(34+(gridRef[1]+thermalthird*10*math.sin(math.radians(x*10)))/1000))+","+str(0)+" \n")

    s = ''
    for x in range(37):
        s = s+str(str("%.4f" % float(77+(gridRef[0]+twentypsi*10*math.cos(math.radians(x*10)))/1000))+","+str("%.4f" % float(34+(gridRef[1]+twentypsi*10*math.sin(math.radians(x*10)))/1000))+","+str(0)+" \n")

    t = ''
    for x in range(37):
        t = t+str(str("%.4f" % float(77+(gridRef[0]+fivepsi*10*math.cos(math.radians(x*10)))/1000))+","+str("%.4f" % float(34+(gridRef[1]+fivepsi*10*math.sin(math.radians(x*10)))/1000))+","+str(0)+" \n")

    u = ''
    for x in range(37):
        u = u+str(str("%.4f" % float(77+(gridRef[0]+onepsi*10*math.cos(math.radians(x*10)))/1000))+","+str("%.4f" % float(34+(gridRef[1]+onepsi*10*math.sin(math.radians(x*10)))/1000))+","+str(0)+" \n")

      

    doc = KML.kml( 
        KML.Folder(
            KML.name("Damage"),
            KML.LookAt(
                KML.longitude(77+gridRef[0]/1000),
                KML.latitude(34+gridRef[1]/1000),
                KML.heading(0),
                KML.tilt(0),
                KML.range(5000),
                GX.altitudeMode("relativeToSeaFloor"),
            ),
            KML.Placemark( 
                KML.name("gx:altitudeMode Example2"), 
                KML.Style(
                KML.PolyStyle(
                    KML.color('48501400'),
                    KML.colorMode('random'),
                    KML.fill('1'),
                    KML.outline('1'),
                    # GX.physicalWidth('12'),
                ),
                id="street",
                ), 
                KML.styleUrl('#street'),
                KML.MultiGeometry(
                    KML.Polygon(
                        KML.outerBoundaryIs(
                            KML.LinearRing(
                                KML.extrude(0),
                                GX.altitudeMode("relativeToSeaFloor"),
                                KML.coordinates(                       
                                    str(p)                                                               
                                )
                            )
                        )
                    ),
                    KML.Polygon(
                        KML.outerBoundaryIs(
                            KML.LinearRing(
                                KML.extrude(0),
                                GX.altitudeMode("relativeToSeaFloor"),
                                KML.coordinates(                       
                                    str(q)                                                               
                                )
                            )
                        )
                    ),
                    KML.Polygon(
                        KML.outerBoundaryIs(
                            KML.LinearRing(
                                KML.extrude(0),
                                GX.altitudeMode("relativeToSeaFloor"),
                                KML.coordinates(                       
                                    str(r)                                                               
                                )
                            )
                        )
                    )
                )            
            ),
            KML.Placemark( 
                KML.name("1st Deg"), 
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
                        str(str("%.4f" % float(77+(gridRef[0]+thermalfirst*10*math.cos(math.radians(90)))/1000))+","+str("%.4f" % float(34+(gridRef[1]+thermalfirst*10*math.sin(math.radians(90)))/1000))+","+str(0)+" \n")
                    )
                )        
            ),
            KML.Placemark( 
                KML.name("2nd Deg"), 
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
                        str(str("%.4f" % float(77+(gridRef[0]+thermalsecond*10*math.cos(math.radians(45)))/1000))+","+str("%.4f" % float(34+(gridRef[1]+thermalsecond*10*math.sin(math.radians(45)))/1000))+","+str(0)+" \n")
                    )
                )        
            ),
            KML.Placemark( 
                KML.name("3rd Deg"), 
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
                        str(str("%.4f" % float(77+(gridRef[0]+thermalthird*10*math.cos(math.radians(0)))/1000))+","+str("%.4f" % float(34+(gridRef[1]+thermalthird*10*math.sin(math.radians(0)))/1000))+","+str(0)+" \n")
                    )
                )        
            ),
            KML.Placemark( 
                KML.name("Concrete"), 
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
                        str(str("%.4f" % float(77+(gridRef[0]+twentypsi*10*math.cos(math.radians(270)))/1000))+","+str("%.4f" % float(34+(gridRef[1]+twentypsi*10*math.sin(math.radians(270)))/1000))+","+str(0)+" \n")
                    )
                )        
            ),
            KML.Placemark( 
                KML.name("Wooden"), 
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
                        str(str("%.4f" % float(77+(gridRef[0]+fivepsi*10*math.cos(math.radians(325)))/1000))+","+str("%.4f" % float(34+(gridRef[1]+fivepsi*10*math.sin(math.radians(325)))/1000))+","+str(0)+" \n")
                    )
                )        
            ),
            KML.Placemark( 
                KML.name("Glass"), 
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
                        str(str("%.4f" % float(77+(gridRef[0]+onepsi*10*math.cos(math.radians(0)))/1000))+","+str("%.4f" % float(34+(gridRef[1]+onepsi*10*math.sin(math.radians(0)))/1000))+","+str(0)+" \n")
                    )
                )        
            ),
            KML.Placemark( 
                KML.name("gx:altitudeMode Example3"), 
                KML.Style(
                KML.LineStyle(
                    KML.color('ff5014E7'),
                    GX.physicalWidth('12'),
                ),
                id="street",
                ),
                KML.styleUrl('#street'),
                KML.MultiGeometry(
                    KML.LineString(
                        KML.extrude(0),
                        GX.altitudeMode("relativeToSeaFloor"),
                        KML.coordinates(                        
                            str(s)                                        
                        )
                    ),
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

    os.startfile("damage.kml")