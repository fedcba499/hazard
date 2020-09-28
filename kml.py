#!/usr/bin/env python
'''Generate a KML string that matches the altitudemode example.

References:
http://code.google.com/apis/kml/documentation/kmlreference.html#gxaltitudemode
http://code.google.com/apis/kml/documentation/kmlfiles/altitudemode_reference.kml
'''

from lxml import etree
from pykml.parser import Schema
from pykml.factory import KML_ElementMaker as KML
from pykml.factory import GX_ElementMaker as GX
import os

doc = KML.kml(
    KML.Placemark(
        KML.name("gx:altitudeMode Example"),
        KML.LookAt(
            KML.longitude(77.806),
            KML.latitude(34.219),
            KML.heading(-60),
            KML.tilt(70),
            KML.range(6300),
            GX.altitudeMode("relativeToSeaFloor"),
        ),
        KML.LineString(
            KML.extrude(1),
            GX.altitudeMode("relativeToSeaFloor"),
            KML.coordinates(
              "77.825,34.233,400 "
              "77.820,34.222,400 "
              "77.812,34.212,400 "
              "77.796,34.209,400 "
              "77.788,34.205,400"
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

os.startfile("kml.kml")
