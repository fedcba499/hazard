import math
from prediction import *



def display(gr1, cb1, gr2, cb2, gr3, cb3):
    gridRef = [gr1, gr2, gr3]
        
    cloudBear = [cb1, cb2, cb3]

    cloudBearFinal = []

    gridRefX = []
    gridRefY = []
    interX = []
    interY = []

    for x in range(3):
        p = toDegree(cloudBear[x])
        cloudBearFinal.append(p)

    for x in range(3):
        p = splitGr(gridRef[x])
        gridRefX.append(p[0])
        gridRefY.append(p[1])   

    for x in range(3):
        if x == 2:
            p = interSecPt(gridRefX[x],gridRefY[x],cloudBearFinal[x],gridRefX[x-2],gridRefY[x-2], cloudBearFinal[x-2])
        else:
            p = interSecPt(gridRefX[x],gridRefY[x],cloudBearFinal[x],gridRefX[x+1],gridRefY[x+1], cloudBearFinal[x+1])
        # p[0]= round(p[0])
        # p[1] = round(p[1])
        interX.append(p[0])
        interY.append(p[1])  

    midPt = [(interX[1]+interX[2])/2, (interY[1]+interY[2])/2]

    centroid = [round(midPt[0]-(midPt[0]-interX[0])/3), round(midPt[1]-(midPt[1]-interY[0])/3)]

    a = str(centroid[0])+str(centroid[1])

    # testgz.blank.delete(0, END)
    # testgz.blank.insert(0, str(centroid[0])+str(centroid[1]))

    return(a)