from tkinter import *

import tkinter.font as tkFont

from tkinter import ttk

import chemical

import edm

import gz

import nuclear

import res

import radiac

import damage

import route

import prediction

from functools import partial

import math

import matplotlib.pyplot as plt

import os

window = Tk()

window.title("201 Engineer Regiment")

window.wm_iconbitmap('img/cbrn.ico')

default_font = tkFont.nametofont("TkDefaultFont")

default_font.configure(size=15)

window.option_add("*Font", default_font)

# window.attributes('-fullscreen', True)

window.state('zoomed')

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
 
tab2 = ttk.Frame(tab_control)

tab3 = ttk.Frame(tab_control)

tab4 = ttk.Frame(tab_control)

tab5 = ttk.Frame(tab_control)

tab6 = ttk.Frame(tab_control)

tab7 = ttk.Frame(tab_control)

tab8 = ttk.Frame(tab_control)
 
tab_control.add(tab1, text = '    CHP     ')
 
tab_control.add(tab2, text='     EDM    ')

tab_control.add(tab3, text = '     GZ     ')

tab_control.add(tab4, text = '    NHP    ' )

tab_control.add(tab5, text = '    RES    ' )

tab_control.add(tab6, text = '   RADIAC  ')

tab_control.add(tab7, text = '   DAMAGE  ')

tab_control.add(tab8, text = '   ROUTE  ')

tab_control.pack(expand=1, fill='both')

class chem:
    def argsToChemical(self):
        self.a = int(guiChem.eAtkGr.get())
        self.b = int(guiChem.eAtkArea.get())
        self.c = int(guiChem.eDwd.get())
        self.d = int(guiChem.eWs.get())
        self.e = str(guiChem.eWindCond.get())
        self.f = str(guiChem.eWindStab.get())
        self.g = str(guiChem.mapSheet.get())
        self.h = int(guiChem.eMapOrigin.get())
        self.j = int(guiChem.eOwnGr.get())
        self.k = int(guiChem.eDtg.get())
        # print(self.a, self.b, self.c, self.d, self.e, self.f,self.g, self.h,self.j, self.k)
        chemical.display(self.a, self.b, self.c, self.d, self.e, self.f,self.j, self.k, mapSheet = self.g, mapOrigin=self.h)


    def argsToChemicalKml(self):
        self.a = int(guiChem.eAtkGr.get())
        self.b = int(guiChem.eAtkArea.get())
        self.c = int(guiChem.eDwd.get())
        self.d = int(guiChem.eWs.get())
        self.e = str(guiChem.eWindCond.get())
        self.f = str(guiChem.eWindStab.get())
        # print(self.a, self.b, self.c, self.d, self.e, self.f,self.g, self.h,self.j, self.k)
        chemical.display3(self.a, self.b, self.c, self.d, self.e, self.f)


    def argsToPreview(self):
        self.a = int(guiChem.eAtkGr.get())
        self.b = int(guiChem.eAtkArea.get())
        self.c = int(guiChem.eDwd.get())
        self.d = int(guiChem.eWs.get())
        self.e = str(guiChem.eWindCond.get())
        self.f = str(guiChem.eWindStab.get())
        self.g = str(guiChem.mapSheet.get())
        self.h = int(guiChem.eMapOrigin.get())
        self.j = int(guiChem.eOwnGr.get())
        self.k = int(guiChem.eDtg.get())
        self.l = int(guiChem.eAtkGr2.get())
        # print(self.a, self.b, self.c, self.d, self.e, self.f,self.g, self.h,self.j, self.k, self.l)
        chemical.display2(self.a, self.b, self.c, self.d, self.e, self.f,self.j, self.k,self.l, mapSheet = self.g, mapOrigin=self.h)



    def argsToChemCheck(self):
        self.a = int(guiChem.eAtkGr.get())
        self.b = int(guiChem.eAtkArea.get())
        self.c = int(guiChem.eDwd.get())
        self.d = int(guiChem.eWs.get())
        self.e = str(guiChem.eWindCond.get())
        self.f = str(guiChem.eWindStab.get())
        self.g = int(guiChem.eOwnGr.get())
        self.h = int(guiChem.eDtg.get())

        # print(self.a, self.b, self.c, self.d, self.e, self.f,self.g, self.h)
        a = chemical.check(self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h)
        guiChem.bWarning.delete(0, END)
        guiChem.bWarning.insert(0, a)
        

    def previewMap(self):
        # print(guiChem.zone.get())
        # print(guiChem.mapSheet.get())
        self.a = int(guiChem.eAtkGr.get())
        self.b = int(guiChem.eMapOrigin.get())

        self.grRef = prediction.splitGr(self.a)
        self.mapRef = prediction.splitGr(self.b)


        image = "img/jpgColour/"+guiChem.mapSheet.get()+".jpg"
        
        # print(image)

        img = plt.imread(image)
        fig, ax = plt.subplots(1,1, figsize=(45,30), dpi=20)
        plt.subplots_adjust(top=1, bottom=0, left=0, right=1)
        # ax.imshow(img, extent=[0, 720, 0, 480])
        ax.imshow(img, extent=[-25, 1775, -25, 1175])
        
        circle4 = plt.Circle((self.grRef[0]-self.mapRef[0], self.grRef[1]-self.mapRef[1]), 4, color='red', linewidth=4)
        ax.add_artist(circle4)

        plt.show()

class edmClass:
    def argsToEdm(self):
        self.ws1 = float(guiEdm.eWs1.get())
        self.ws2 = float(guiEdm.eWs2.get())
        self.ws3 = float(guiEdm.eWs3.get())
        self.ws4 = float(guiEdm.eWs4.get())
        self.ws5 = float(guiEdm.eWs5.get())
        self.ws6 = float(guiEdm.eWs6.get())
        self.ws7 = float(guiEdm.eWs7.get())
        self.ws8 = float(guiEdm.eWs8.get())
        self.ws9 = float(guiEdm.eWs9.get())
        self.ws10 = float(guiEdm.eWs10.get())

        self.wd1 = float(guiEdm.eWd1.get())
        self.wd2 = float(guiEdm.eWd2.get())
        self.wd3 = float(guiEdm.eWd3.get())
        self.wd4 = float(guiEdm.eWd4.get())
        self.wd5 = float(guiEdm.eWd5.get())
        self.wd6 = float(guiEdm.eWd6.get())
        self.wd7 = float(guiEdm.eWd7.get())
        self.wd8 = float(guiEdm.eWd8.get())
        self.wd9 = float(guiEdm.eWd9.get())
        self.wd10 = float(guiEdm.eWd10.get())

        self.ct = float(guiEdm.eCt.get())
        self.cb = float(guiEdm.eCb.get())
        self.sh = float(guiEdm.eSh.get())


        # print(self.ws1, self.ws2, self.ws3, self.ws4, self.ws5, self.ws6, self.ws7, self.ws8, self.ws9, self.ws10)
        # print(self.wd1, self.wd2, self.wd3, self.wd4, self.wd5, self.wd6, self.wd7, self.wd8, self.wd9, self.wd10)
        # print(self.ct, self.cb, self.sh)
        a = edm.display(self.ws1, self.wd1, self.ws2, self.wd2, self.ws3,self.wd3, self.ws4,self.wd4, self.ws5,self.wd5, self.ws6,self.wd6, self.ws7, self.wd7,self.ws8,self.wd8, self.ws9, self.wd9,self.ws10,self.wd10, self.ct, self.cb, self.sh)

        guiEdm.bBounds.delete(0, END)
        guiEdm.bBounds.insert(0, a) 

    def changeCloudDim(self):
        
        if guiEdm.cloudDim.get() == "2 KT":

            guiEdm.eCt.delete(0, END)  
            guiEdm.eCt.insert(0, '4.9')

            guiEdm.eCb.delete(0, END)  
            guiEdm.eCb.insert(0, '2.6')   

            guiEdm.eSh.delete(0, END)  
            guiEdm.eSh.insert(0, '1.7')       


        elif guiEdm.cloudDim.get() == "5 KT":

            guiEdm.eCt.delete(0, END)  
            guiEdm.eCt.insert(0, '7.1')

            guiEdm.eCb.delete(0, END)  
            guiEdm.eCb.insert(0, '4.4')   

            guiEdm.eSh.delete(0, END)  
            guiEdm.eSh.insert(0, '2.9') 

        elif guiEdm.cloudDim.get() == "30 KT":

            guiEdm.eCt.delete(0, END)  
            guiEdm.eCt.insert(0, '11.6')

            guiEdm.eCb.delete(0, END)  
            guiEdm.eCb.insert(0, '7.7')   

            guiEdm.eSh.delete(0, END)  
            guiEdm.eSh.insert(0, '5.1')

        elif guiEdm.cloudDim.get() == "100 KT":

            guiEdm.eCt.delete(0, END)  
            guiEdm.eCt.insert(0, '14.4')

            guiEdm.eCb.delete(0, END)  
            guiEdm.eCb.insert(0, '9.3')   

            guiEdm.eSh.delete(0, END)  
            guiEdm.eSh.insert(0, '6.2')



class gzClass:
    def argsToGz(self):
        self.gr1 = int(guiGz.eGr1.get())
        self.gr2 = int(guiGz.eGr2.get())
        self.gr3 = int(guiGz.eGr3.get())
        self.cb1 = int(guiGz.eCb1.get())
        self.cb2 = int(guiGz.eCb2.get())
        self.cb3 = int(guiGz.eCb3.get())
        # print(self.gr1, self.gr2, self.gr3, self.cb1, self.cb2, self.cb3)
        a = gz.display(self.gr1, self.cb1, self.gr2, self.cb2, self.gr3, self.cb3)

        guiGz.bBounds.delete(0, END)
        guiGz.bBounds.insert(0, a)

class nucClass:
    def argsToNuc(self):
        self.atkGr = int(guiChem.eAtkGr.get())
        self.cr = float(guiNuc.eCr.get())
        self.dwd = int(guiNuc.eDwd.get())
        self.ws = float(guiNuc.eWs.get())
        self.zone = float(guiNuc.eZone.get())
        self.extent = int(guiNuc.eExtent.get())
        self.ownGr = int(guiChem.eOwnGr.get())
        self.mapSheet = str(guiChem.mapSheet.get())
        self.mapOrigin = int(guiChem.eMapOrigin.get())
        self.dtg = int(guiChem.eDtg.get())
        # print(self.atkGr, self.cr, self.dwd, self.ws, self.zone, self.extent, self.ownGr,self.mapSheet, self.mapOrigin)
        nuclear.display(self.atkGr, self.cr, self.dwd, self.ws, self.zone, self.extent,self.ownGr, self.dtg, mapSheet=self.mapSheet, mapOrigin=self.mapOrigin)        

    def argsToNucKml(self):
        self.atkGr = int(guiChem.eAtkGr.get())
        self.cr = float(guiNuc.eCr.get())
        self.dwd = int(guiNuc.eDwd.get())
        self.ws = float(guiNuc.eWs.get())
        self.zone = float(guiNuc.eZone.get())
        self.extent = int(guiNuc.eExtent.get())
        # print(self.atkGr, self.cr, self.dwd, self.ws, self.zone, self.extent, self.ownGr,self.mapSheet, self.mapOrigin)
        nuclear.display3(self.atkGr, self.cr, self.dwd, self.ws, self.zone, self.extent)  

    def argsToNucGis(self):
        os.startfile("hazard.qgz")
             





class resClass:
    

    def changeRiskValue(self):
      
        if guiRes.riskValue.get() == "Negligible Risk":

            guiRes.eCb1.delete(0, END)  
            guiRes.eCb1.insert(0, '5')     

        elif guiRes.riskValue.get() == "Increased Risk":

            guiRes.eCb1.delete(0, END)  
            guiRes.eCb1.insert(0, '25')

        elif guiRes.riskValue.get() == "Significant Risk":

            guiRes.eCb1.delete(0, END)  
            guiRes.eCb1.insert(0, '70')          

        elif guiRes.riskValue.get() == "High Risk":

            guiRes.eCb1.delete(0, END)  
            guiRes.eCb1.insert(0, '100')

        elif guiRes.riskValue.get() == "Very High Risk":

            guiRes.eCb1.delete(0, END)  
            guiRes.eCb1.insert(0, '125')

    
    def changeSpeedValue(self):
      
        if guiRes.speedValue.get() == "FSMO":

            guiRes.eTpt.delete(0, END)  
            guiRes.eTpt.insert(0, '2.5')     

        elif guiRes.speedValue.get() == "Single Belt":

            guiRes.eTpt.delete(0, END)  
            guiRes.eTpt.insert(0, '5')

        elif guiRes.speedValue.get() == "B Veh":

            guiRes.eTpt.delete(0, END)  
            guiRes.eTpt.insert(0, '25')          

        elif guiRes.speedValue.get() == "A Veh":

            guiRes.eTpt.delete(0, END)  
            guiRes.eTpt.insert(0, '40')


    def argsToRes(self):
        self.gr1 = int(guiRes.eGr1.get())
        self.cb1 = int(guiRes.eCb1.get())
        self.zone = float(guiNuc.eZone.get())
        self.extent = int(guiNuc.eExtent.get())
        self.tpt = float(guiRes.eTpt.get())
        # print(self.gr1, self.cb1, self.zone)
        a = res.display(self.gr1, self.cb1, self.zone, self.extent, self.tpt)

        guiRes.bBounds.delete('1.0', END)

        b= "Total number of Troops available is : "+str(a[1])+"\n"

        guiRes.bBounds.insert(INSERT, b)
        guiRes.bBounds.insert(INSERT, a[0])



class radiacClass:  

    def argsToRate(self):
        self.time = float(guiRadiac.eTime.get())
        self.radiation = float(guiRadiac.eRadiation.get())
        self.timeReq = float(guiRadiac.eTimeReq.get())

        # print(self.time, self.radiation, self.timeReq)

        a = radiac.displayRate(self.time, self.radiation, self.timeReq)

        guiRadiac.bBoundsRate.delete(0, END)
        guiRadiac.bBoundsRate.insert(0, a)

    
    def argsToRad(self):
        self.time = float(guiRadiac.eTime.get())
        self.radiation = float(guiRadiac.eRadiation.get())
        self.radReq = float(guiRadiac.eRadReq.get())

        # print(self.time, self.radiation, self.radReq)

        a = radiac.displayRad(self.time, self.radiation, self.radReq)

        guiRadiac.bBoundsRad.delete(0, END)
        guiRadiac.bBoundsRad.insert(0, a)

    def argsToDose(self):
        self.time = float(guiRadiac.eTime.get())
        self.radiation = float(guiRadiac.eRadiation.get())
        self.timeEntry = float(guiRadiac.eTimeEntry.get())
        self.timeExit = float(guiRadiac.eTimeExit.get())

        # print(self.timeEntry, self.timeExit)
        a = radiac.displayDose(self.time  ,self.radiation ,self.timeEntry, self.timeExit)

        guiRadiac.bBoundsDose.delete(0, END)
        guiRadiac.bBoundsDose.insert(0, a) 

    def argsToTime(self):
        self.time = float(guiRadiac.eTime.get())
        self.radiation = float(guiRadiac.eRadiation.get())
        self.radLimit = float(guiRadiac.eRadLimit.get())
        self.timeReqMsn = float(guiRadiac.eTimeReqMsn.get())

        # print(self.time, self.radiation, self.radLimit, self.timeReqMsn)
        a = radiac.displayTime(self.time  ,self.radiation ,self.radLimit, self.timeReqMsn)

        guiRadiac.bBoundsTime.delete(0, END)
        guiRadiac.bBoundsTime.insert(0, a)   

    def argsToExit(self):
        self.time = float(guiRadiac.eTime.get())
        self.radiation = float(guiRadiac.eRadiation.get())
        self.radLimit = float(guiRadiac.eRadLimit.get())
        self.timeEntry = float(guiRadiac.eTimeEntry.get())

        # print(self.time, self.radiation, self.radLimit, self.timeEntry)
        a = radiac.displayExit(self.time  ,self.radiation ,self.radLimit, self.timeEntry)

        guiRadiac.bBoundsExit.delete(0, END)
        guiRadiac.bBoundsExit.insert(0, a)  


class damageClass:
    def argsToDamage(self):
        self.atkGr = int(guiChem.eAtkGr.get())
        self.burst = str(guiDamage.eBurst.get())
        self.yd = float(guiDamage.eYd.get())
        # print(self.burst, self.yd)
        damage.display3(self.atkGr, self.burst, self.yd)

    def argsToDamageKml(self):
        self.atkGr = int(guiChem.eAtkGr.get())
        self.burst = str(guiDamage.eBurst.get())
        self.yd = float(guiDamage.eYd.get())
        # print(self.burst, self.yd)
        damage.display3(self.atkGr, self.burst, self.yd)
          

    def argsToDamageGis(self):
        os.startfile("hazard.qgz") 

class routeClass:
    def argsToRoute(self):
        self.atkGr = int(guiChem.eAtkGr.get())
        self.burst = str(guiDamage.eBurst.get())
        self.yd = float(guiDamage.eYd.get())
        # print(self.burst, self.yd)
        damage.display3(self.atkGr, self.burst, self.yd)

    def argsToRouteKml(self):
        self.atkGr = int(guiChem.eAtkGr.get())
        self.dwd = int(guiNuc.eDwd.get())
        self.extent = int(guiNuc.eExtent.get())        
        self.time = float(guiRoute.eTime.get())
        self.rad = float(guiRoute.eRadiation.get())
        self.dist = float(guiRoute.eDist.get())
        self.timeEntry = float(guiRoute.eTimeEntry.get())
        self.timeExit = float(guiRoute.eTimeExit.get())
        self.distEntry = float(guiRoute.eDistEntry.get())
        self.distExit = float(guiRoute.eDistExit.get())
        # print(self.atkGr, self.dwd, self.extent, self.time, self.rad, self.dist, self.timeEntry, self.timeExit, self.distEntry, self.distExit)
        route.display(self.atkGr, self.dwd, self.extent, self.time, self.rad, self.dist, self.timeEntry, self.timeExit, self.distEntry, self.distExit)
          

    def argsToRouteGis(self):
        os.startfile("hazard.qgz") 

class guiChem:

    title = Label(tab1, text = "Chemical Hazard Prediction", fg = 'green', bg = "yellow", width = 56)
    title.config(font=("Courier", 30, "bold"))
    title.grid(row = 0, column = 0, sticky = N, columnspan = 4)

    maps = LabelFrame(tab1, text = "Maps")
    maps.grid(row = 1, column = 0, sticky = W+E, columnspan=  4, padx = 5)

    mapSel = Label(maps, text = "Maps Selection", width = 30, anchor = W)
    mapSel.grid(row=0, column = 0, sticky = W, padx = 10)

    zone = StringVar(maps)
    mapSheet = StringVar(maps)

    dict = {'Zone 0': ['nj-43-13', 'nj-43-14', 'nj-43-15'], 
        'Zone 1A': ['nh-42-01','nh-42-02','nh-42-03','nh-42-04','nh-42-05','nh-42-06','nh-42-07','nh-42-08','nh-42-09','nh-42-10','nh-42-11','nh-42-12','nh-42-13','nh-42-14','nh-42-15', 'nh-42-16','nh-42-5a','nh-43-01','nh-43-02','nh-43-03','nh-43-04','nh-43-05','nh-43-06','nh-43-07','nh-43-08','nh-43-09','nh-43-10','nh-43-11','nh-43-12','nh-43-13','nh-43-14', 'nh-43-15','nh-43-16','ni-42-12','ni-42-16','ni-43-01','ni-43-02','ni-43-03','ni-43-04', 'ni-43-05','ni-43-06', 'ni-43-07','ni-43-08','ni-43-09','ni-43-10','ni-43-11','ni-43-12', 'ni-43-13','ni-43-14','ni-43-15','ni-43-16','ni-44-01','ni-44-05','ni-44-09','ni-44-13'], 
        'Zone 1B': ['nh-44-01','nh-44-05','nh-44-06','nh-44-09','nh-44-10','nh-44-11','nh-44-12', 'nh-44-13','nh-44-14','nh-44-15','nh-44-16','nh-45-13','nh-46-15','nh-46-16','ni-44-01', 'ni-44-05','ni-44-09','ni-44-13'], 
        'Zone 2A': ['nf-42-02','nf-42-03','nf-42-04','nf-42-07','nf-42-08','nf-42-11','nf-42-12', 'nf-42-16','nf-43-01','nf-43-02','nf-43-03','nf-43-04','nf-43-05','nf-43-06','nf-43-07', 'nf-43-08','nf-43-09','nf-43-10','nf-43-11','nf-43-12','nf-43-13','nf-43-14','nf-43-15', 'nf-43-16','nf-44-01','nf-44-02','nf-44-03','nf-44-04','nf-44-05','nf-44-06','nf-44-07', 'nf-44-08','nf-44-09','nf-44-10','nf-44-11','nf-44-12','nf-44-13', 'ng-42-01','ng-42-02','ng-42-03','ng-42-04','ng-42-05','ng-42-06','ng-42-07','ng-42-08', 'ng-42-09','ng-42-10','ng-42-11','ng-42-12','ng-42-13','ng-42-14','ng-42-15','ng-42-16', 'ng-43-01','ng-43-02','ng-43-03','ng-43-04','ng-43-05','ng-43-06','ng-43-07','ng-43-08', 'ng-43-09','ng-43-10','ng-43-11','ng-43-12','ng-43-13','ng-43-14','ng-43-15','ng-43-16'], 
        'Zone 2B': ['nf-44-14','nf-44-15','nf-44-16','nf-45-01','nf-45-02','nf-45-03','nf-45-04', 'nf-45-05','nf-45-06','nf-45-07','nf-45-08','nf-45-09','nf-45-10','nf-45-11','nf-45-12', 'nf-45-13','nf-45-14','nf-46-01','nf-46-02','nf-46-05','nf-46-06','nf-46-09','nf-46-10', 'ng-44-01','ng-44-02','ng-44-03','ng-44-04','ng-44-05','ng-44-06','ng-44-07','ng-44-08', 'ng-44-09','ng-44-10','ng-44-11','ng-44-12','ng-44-13','ng-44-14','ng-44-15','ng-44-16', 'ng-45-01','ng-45-02','ng-45-03','ng-45-04','ng-45-05','ng-45-06','ng-45-07','ng-45-08', 'ng-45-09','ng-45-10','ng-45-11','ng-45-12','ng-45-13','ng-45-14','ng-45-15','ng-45-16', 'ng-46-01','ng-46-02','ng-46-03','ng-46-04','ng-46-05','ng-46-06','ng-46-07','ng-46-09', 'ng-46-10','ng-46-11','ng-46-13','ng-46-14','ng-46-15'], 
        'Zone 3A': ['ne-43-01','ne-43-02','ne-43-03','ne-43-04','ne-43-05','ne-43-06','ne-43-07', 'ne-43-08','ne-43-09','ne-43-10','ne-43-11','ne-43-12','ne-43-13','ne-43-14','ne-43-15', 'ne-43-16', 'nd-43-02','nd-43-03','nd-43-04','nd-43-06','nd-43-07','nd-43-08','nd-43-11', 'nd-43-12','nd-43-15','nd-43-16', 'ne-44-01','ne-44-02','ne-44-03','ne-44-04','ne-44-05','ne-44-06','ne-44-07', 'ne-44-08','ne-44-09','ne-44-10','ne-44-11','ne-44-12','ne-44-13','ne-44-14','ne-44-15', 'ne-45-01','ne-45-02','ne-45-05','nd-44-01','nd-44-02','nd-44-03','nd-44-05','nd-44-06','nd-44-09','nd-44-10','nd-44-13','nd-44-14'], 
        'Zone 4A': ['nc-43-03','nc-43-04','nc-43-07','nc-43-08','nc-43-11','nc-43-12','nc-43-16', 'nc-44-01','nc-44-02','nc-44-05','nc-44-09','nc-44-13']}

    zoneOption = OptionMenu(maps,zone, *dict.keys())
    zone.set('Zone 0')    
    zoneOption.grid(row=0, column = 1)

    mapSheetOption = OptionMenu(maps, mapSheet, '')
    mapSheet.set('nc-43-03')
    mapSheetOption.grid(row=0, column =2)

    def menuObj(self, *args):

        self.zone.trace('w', self.update_options)
    
    def update_options(self, *args):
        mapSheetsLog = self.dict[self.zone.get()]
        self.mapSheet.set(mapSheetsLog[0])

        menu = self.mapSheetOption['menu']
        menu.delete(0, 'end')

        for mapSheetNo in mapSheetsLog:
            menu.add_command(label=mapSheetNo, command=lambda nation=mapSheetNo: self.mapSheet.set(nation))


    chemObj = chem()

    bPreview = Button(maps, text="Preview",width = 20, command = chemObj.previewMap)
    bPreview.grid(row= 0, column = 3)

    mapOrigin = Label(maps, text = "Enter 6 Digit GR of Map Sheet Origin", width = 30, anchor = W)
    mapOrigin.grid(row=1, column=0, sticky = W, padx = 10)

    vMapOrigin = StringVar(maps, value='0')
    eMapOrigin = Entry(maps,textvariable=vMapOrigin, width = 20)
    eMapOrigin.grid(row=1, column = 1)
    
    atkGr = Label(maps, text = "Enter 6 Digit GR of Area Attacked", width = 30, anchor = W)
    atkGr.grid(row = 1, column = 2, sticky = W, padx = 10)

    vAtkGr = StringVar(maps, value='200200')
    eAtkGr = Entry(maps, textvariable=vAtkGr, width = 20)
    eAtkGr.grid(row = 1, column = 3)

    optinal = LabelFrame(maps, text = "Optional")
    optinal.grid(row = 2, column = 0, sticky = W+E, columnspan=  4, padx = 10, pady = 5)

    extraMap = Label(optinal, text = "Direction for Placing Extra Map Sheets", width = 30, anchor = W)
    extraMap.grid(row=0, column=0, sticky = W, padx = 10)

    place = StringVar(optinal)
    placeOption = OptionMenu(optinal,place,"North", "East", "South", "West", "NorthEast", "NorthWest", "SouthEast", "SoutWest")
    place.set('North')    
    placeOption.grid(row=0, column = 1, padx = 20)

    bExtraAdd = Button(optinal, text="Add")
    bExtraAdd.grid(row= 0, column = 2, padx = 100)

    bExtraPreview = Button(optinal, text="Preview")
    bExtraPreview.grid(row= 0, column = 3, padx = 60)


    parameters = LabelFrame(tab1, text = "Parameters")
    parameters.grid(row = 2, column = 0,sticky = W+E, columnspan=  4, padx = 5)

    atkArea = Label(parameters, text = "Enter Attack Area in KM", width = 30, anchor = W)
    dwd = Label(parameters, text = "Enter Downwind direction in Degree", width = 30, anchor = W)
    ws = Label(parameters, text = "Enter Wind Speed in KMPH", width = 30, anchor = W)
    windCond = Label(parameters, text = "Enter P - Presistant, N - NonPersistant" , width = 30, anchor = W)
    windStab = Label(parameters, text = "Enter U - Unstable, N - Neutal, S - Stable", width = 30, anchor = W)
    dtg = Label(parameters, text = "Enter Date Time Group", width = 30, anchor = W)

    vAtkArea = StringVar(parameters, value='1')
    eAtkArea = Entry(parameters, textvariable=vAtkArea, width = 20)

    vDwd = StringVar(parameters, value='0')
    eDwd = Entry(parameters, textvariable=vDwd, width = 20)

    vWs = StringVar(parameters, value='10')
    eWs = Entry(parameters, textvariable=vWs, width = 20)

    vWindCond = StringVar(parameters, value='p')
    eWindCond = Entry(parameters, textvariable=vWindCond, width = 20)

    vWindStab = StringVar(parameters, value='u')
    eWindStab = Entry(parameters, textvariable=vWindStab, width = 20)

    vDtg = StringVar(parameters, value='061000')
    eDtg = Entry(parameters, textvariable=vDtg, width = 20)

    atkArea.grid(row = 0, column = 0, sticky = W, padx = 10)
    eAtkArea.grid(row = 0, column = 1)

    dwd.grid(row = 0, column = 2, sticky = W, padx = 10)
    eDwd.grid(row = 0, column = 3)

    ws.grid(row = 1, column = 0, sticky = W, padx = 10)
    eWs.grid(row = 1, column = 1)

    windCond.grid(row = 1, column = 2, sticky = W, padx = 10)
    eWindCond.grid(row = 1, column = 3)

    windStab.grid(row = 2, column = 0, sticky = W, padx = 10)
    eWindStab.grid(row = 2, column = 1)

    dtg.grid(row = 2, column = 2, sticky = W, padx = 10)
    eDtg.grid(row = 2, column = 3)


    optional = LabelFrame(tab1, text= "Optional")
    optional.grid(row = 3, column = 0, sticky = W+E, columnspan=  4, padx = 5)

    ownGr = Label(optional, text = "Enter Your Location GR", width = 30, anchor = W)
    eOwnGr = Entry(optional)

    ownGr.grid(row = 0, column = 0, sticky = W, padx = 10)
    eOwnGr.grid(row = 0, column = 1) 

    bCheck = Button(optional, text="Check",width = 20, command = chemObj.argsToChemCheck)
    bCheck.grid(row= 0, column = 3, padx = 100) 

    atkGr2 = Label(optional, text = "Enter GR of Second Attk Area", width = 30, anchor = W)
    eAtkGr2 = Entry(optional)

    atkGr2.grid(row = 1, column = 0, sticky = W, padx = 10)
    eAtkGr2.grid(row = 1, column = 1) 

    bPreview2 = Button(optional, text="Preview",width = 20, command = chemObj.argsToChemicalKml)
    bPreview2.grid(row= 1, column = 3, padx = 100) 
    
    btnBounds = Button(tab1, text = "Click to get CHP GR Bounds",bg = "green", command = chemObj.argsToChemical)
    btnBounds.grid(row = 4, column = 1, columnspan = 2) 
    
    

    result = LabelFrame(tab1, text= "Result")
    result.grid(row = 5, column = 0, sticky = W+E, columnspan=  4, padx = 5)

    bounds = Label(result, text = "Hazard area GR Bounds are as follows", bg = "yellow", width = 30, anchor = W)
    warning = Label(result, text = "Warning", bg = "red", width = 30, anchor = W)

    bBounds = Entry(result, width=85)
    bWarning = Entry(result, width=85)     

    bounds.grid(row = 0, column = 0, sticky = W, padx = 10)
    bBounds.grid(row = 0, column = 1, columnspan = 3)

    warning.grid(row = 1, column = 0, sticky = W, padx = 10)
    bWarning.grid(row = 1, column = 1, columnspan = 3)

if __name__ == "__main__":
    optionMenuObj = guiChem()
    optionMenuObj.menuObj()


class guiEdm:

    title = Label(tab2, text = "Effective Downwind Message", fg = 'green', bg = "yellow", width = 56)
    title.config(font=("Courier", 30, "bold"))
    title.grid(row = 0, column = 0, sticky = N, columnspan = 4)

    parameters = LabelFrame(tab2, text = "Wind Parameters")
    parameters.grid(row = 1, column = 0, sticky = W+E, columnspan=  4, padx = 5)

    ws1 = Label(parameters, text = "Enter 0 - 2 km layer Wind Speed", width = 30, anchor = W)
    ws2 = Label(parameters, text = "Enter 2 - 4 km layer Wind Speed", width = 30, anchor = W)
    ws3 = Label(parameters, text = "Enter 4 - 6 km layer Wind Speed", width = 30, anchor = W)
    ws4 = Label(parameters, text = "Enter 6 - 8 km layer Wind Speed", width = 30, anchor = W)
    ws5 = Label(parameters, text = "Enter 8 - 10 km layer Wind Speed", width = 30, anchor = W)
    ws6 = Label(parameters, text = "Enter 10 - 12 km layer Wind Speed", width = 30, anchor = W)
    ws7 = Label(parameters, text = "Enter 12 - 14 km layer Wind Speed", width = 30, anchor = W)
    ws8 = Label(parameters, text = "Enter 14 - 16 km layer Wind Speed", width = 30, anchor = W)
    ws9 = Label(parameters, text = "Enter 16 - 18 km layer Wind Speed", width = 30, anchor = W)
    ws10 = Label(parameters, text = "Enter 18 - 20 km layer Wind Speed", width = 30, anchor = W)

    wd1 = Label(parameters, text = "Enter 0 - 2 km layer wind Direction", width = 30, anchor = W)
    wd2 = Label(parameters, text = "Enter 2 - 4 km layer wind Direction", width = 30, anchor = W)
    wd3 = Label(parameters, text = "Enter 4 - 6 km layer wind Direction", width = 30, anchor = W)
    wd4 = Label(parameters, text = "Enter 6 - 8 km layer wind Direction", width = 30, anchor = W)
    wd5 = Label(parameters, text = "Enter 8 - 10 km layer wind Direction", width = 30, anchor = W)
    wd6 = Label(parameters, text = "Enter 10 - 12 km layer wind Direction", width = 30, anchor = W)
    wd7 = Label(parameters, text = "Enter 12 - 14 km layer wind Direction", width = 30, anchor = W)
    wd8 = Label(parameters, text = "Enter 14 - 16 km layer wind Direction", width = 30, anchor = W)
    wd9 = Label(parameters, text = "Enter 16 - 18 km layer wind Direction", width = 30, anchor = W)
    wd10 = Label(parameters, text = "Enter 18 - 20 km layer wind Direction", width = 30, anchor = W)

    eWs1 = Entry(parameters, width = 20)
    eWs2 = Entry(parameters, width = 20)
    eWs3 = Entry(parameters, width = 20)
    eWs4 = Entry(parameters, width = 20)
    eWs5 = Entry(parameters, width = 20)
    eWs6 = Entry(parameters, width = 20)
    eWs7 = Entry(parameters, width = 20)
    eWs8 = Entry(parameters, width = 20)
    eWs9 = Entry(parameters, width = 20)
    eWs10 = Entry(parameters, width = 20)

    eWd1 = Entry(parameters, width = 20)
    eWd2 = Entry(parameters, width = 20)
    eWd3 = Entry(parameters, width = 20)
    eWd4 = Entry(parameters, width = 20)
    eWd5 = Entry(parameters, width = 20)
    eWd6 = Entry(parameters, width = 20)
    eWd7 = Entry(parameters, width = 20)
    eWd8 = Entry(parameters, width = 20)
    eWd9 = Entry(parameters, width = 20)
    eWd10 = Entry(parameters, width = 20)

    ws1.grid(row = 1, column = 0, sticky = W, padx = 10)
    eWs1.grid(row = 1, column = 1)

    ws2.grid(row = 2, column = 0, sticky = W, padx = 10)
    eWs2.grid(row = 2, column = 1)

    ws3.grid(row = 3, column = 0, sticky = W, padx = 10)
    eWs3.grid(row = 3, column = 1)

    ws4.grid(row = 4, column = 0, sticky = W, padx = 10)
    eWs4.grid(row = 4, column = 1)

    ws5.grid(row = 5, column = 0, sticky = W, padx = 10)
    eWs5.grid(row = 5, column = 1)

    ws6.grid(row = 6, column = 0, sticky = W, padx = 10)
    eWs6.grid(row = 6, column = 1)

    ws7.grid(row = 7, column = 0, sticky = W, padx = 10)
    eWs7.grid(row = 7, column = 1)

    ws8.grid(row = 8, column = 0, sticky = W, padx = 10)
    eWs8.grid(row = 8, column = 1)

    ws9.grid(row = 9, column = 0, sticky = W, padx = 10)
    eWs9.grid(row = 9, column = 1)

    ws10.grid(row = 10, column = 0, sticky = W, padx = 10)
    eWs10.grid(row = 10, column = 1)


    wd1.grid(row = 1, column = 2, sticky = W, padx = 10)
    eWd1.grid(row = 1, column = 3)

    wd2.grid(row = 2, column = 2, sticky = W, padx = 10)
    eWd2.grid(row = 2, column = 3)

    wd3.grid(row = 3, column = 2, sticky = W, padx = 10)
    eWd3.grid(row = 3, column = 3)

    wd4.grid(row = 4, column = 2, sticky = W, padx = 10)
    eWd4.grid(row = 4, column = 3)

    wd5.grid(row = 5, column = 2, sticky = W, padx = 10)
    eWd5.grid(row = 5, column = 3)

    wd6.grid(row = 6, column = 2, sticky = W, padx = 10)
    eWd6.grid(row = 6, column = 3)

    wd7.grid(row = 7, column = 2, sticky = W, padx = 10)
    eWd7.grid(row = 7, column = 3)

    wd8.grid(row = 8, column = 2, sticky = W, padx = 10)
    eWd8.grid(row = 8, column = 3)

    wd9.grid(row = 9, column = 2, sticky = W, padx = 10)
    eWd9.grid(row = 9, column = 3)

    wd10.grid(row = 10, column = 2, sticky = W, padx = 10)
    eWd10.grid(row = 10, column = 3)

    optional = LabelFrame(tab2, text = "Optional")
    optional.grid(row = 2, column = 0, sticky = W+E, columnspan=  4, padx = 5)

    cloudDim = StringVar(optional)
    cloudDimOption = OptionMenu(optional,cloudDim, "2 KT", "5 KT", "30 KT", "100 KT")
    cloudDim.set('2 KT')    
    cloudDimOption.grid(row=12, column = 2)    

    edmObj = edmClass()

    bPreview = Button(optional, text="Update",width = 20, command = edmObj.changeCloudDim)
    bPreview.grid(row=12, column = 3)

    ct = Label(optional, text = "Enter Height of Cloud Top in km", width = 30, anchor = W)
    cb = Label(optional, text = "Enter Height of Cloud Bottom in km", width = 30, anchor = W)
    sh = Label(optional, text = "Enter Height of 2/3 Stem in km", width = 30, anchor = W)

    eCt = Entry(optional, width = 20)
    eCb = Entry(optional, width = 20)
    eSh = Entry(optional, width = 20)

    ct.grid(row = 11, column = 0, sticky = W, padx = 10)
    eCt.grid(row = 11, column = 1)

    sh.grid(row = 11, column = 2, sticky = W, padx = 10)
    eSh.grid(row = 11, column = 3)

    cb.grid(row = 12, column = 0, sticky = W, padx = 10)
    eCb.grid(row = 12, column = 1)   

    btnBounds = Button(tab2, text = "Click to get EDM",bg = "green", command = edmObj.argsToEdm)

    btnBounds.grid(row = 3, column = 1, columnspan = 2)

    result = LabelFrame(tab2, text = "Result")
    result.grid(row = 4, column = 0, sticky = W+E, columnspan=  4, padx = 5)

    bounds = Label(result, text = "Effective Downwind Message is : ", bg = "yellow", width = 30, anchor = W)
    bBounds = Entry(result, width=85)

    bounds.grid(row = 13, column = 0, sticky = W, padx = 10)
    bBounds.grid(row = 13, column = 1, columnspan = 4)

class guiGz:

    title = Label(tab3, text = "Ground Zero", fg = 'green', bg = "yellow", width = 56)
    title.config(font=("Courier", 30, "bold"))
    title.grid(row = 0, column = 0, sticky = N, columnspan = 4)

    parameters = LabelFrame(tab3, text = "Parameters")
    parameters.grid(row = 1, column = 0, sticky = W+E, columnspan=  4, padx = 5)

    gr1 = Label(parameters, text = "Enter Observer 1 Six Digit GR", width = 30, anchor = W)
    gr2 = Label(parameters, text = "Enter Observer 2 Six Digit GR", width = 30, anchor = W)
    gr3 = Label(parameters, text = "Enter Observer 3 Six Digit GR", width = 30, anchor = W)

    cb1 = Label(parameters, text = "Enter Observer 1 Cloud Bearing", width = 30, anchor = W)
    cb2 = Label(parameters, text = "Enter Observer 2 Cloud Bearing", width = 30, anchor = W)
    cb3 = Label(parameters, text = "Enter Observer 3 CLoud Bearing", width = 30, anchor = W)

    eGr1 = Entry(parameters, width = 20)
    eCb1 = Entry(parameters, width = 20)

    eGr2 = Entry(parameters, width = 20)
    eCb2 = Entry(parameters, width = 20)

    eGr3 = Entry(parameters, width = 20)
    eCb3 = Entry(parameters, width = 20)

    gr1.grid(row = 1, column = 0, sticky = W, padx = 10)
    eGr1.grid(row = 1, column = 1)

    cb1.grid(row = 1, column = 2, sticky = W, padx = 10)
    eCb1.grid(row = 1, column = 3)

    gr2.grid(row = 2, column = 0, sticky = W, padx = 10)
    eGr2.grid(row = 2, column = 1)

    cb2.grid(row = 2, column = 2, sticky = W, padx = 10)
    eCb2.grid(row = 2, column = 3)

    gr3.grid(row = 3, column = 0, sticky = W, padx = 10)
    eGr3.grid(row = 3, column = 1)

    cb3.grid(row = 3, column = 2, sticky = W, padx = 10)
    eCb3.grid(row = 3, column = 3)

    gzObj = gzClass()
    btnBounds = Button(tab3, text = "Click to get Ground Zero",bg = "green", command = gzObj.argsToGz)
    btnBounds.grid(row = 2, column = 0, columnspan = 4)
    
    result = LabelFrame(tab3, text = "Result")
    result.grid(row = 3, column = 0, sticky = W+E, columnspan=  4, padx = 5)

    bounds = Label(result, text = "GR of Attack Ground Zero is : ", bg = "yellow", width = 30, anchor = W)
    bounds.grid(row = 5, column = 0, sticky = W, padx = 10)

    bBounds = Entry(result, width=80)         
    bBounds.grid(row = 5, column = 1, columnspan = 3)

class guiNuc:

    title = Label(tab4, text = "Nuclear Hazard Prediction", fg = 'green', bg = "yellow", width = 56)
    title.config(font=("Courier", 30, "bold"))
    title.grid(row = 0, column = 0, sticky = N, columnspan = 4)

    parameters = LabelFrame(tab4, text = "Parameters")
    parameters.grid(row = 1, column = 0, sticky = W+E, columnspan=  4, padx = 5)

    cr = Label(parameters, text = "Enter Cloud Radius in KM", width = 30, anchor = W)
    dwd = Label(parameters, text = "Enter Downwind direction in Degree", width = 30, anchor = W)
    ws = Label(parameters, text = "Enter Wind Speed in KMPH", width = 30, anchor = W)
    zone = Label(parameters, text = "Enter Zone 1 distance in KM", width = 30, anchor = W)
    extent = Label(parameters, text = "Enter Extent in Degrees", width = 30, anchor = W)

    eWs = Entry(parameters, width = 20)
    eCr = Entry(parameters, width = 20)
    eDwd = Entry(parameters, width = 20)
    eZone = Entry(parameters, width = 20)
    eExtent = Entry(parameters, width = 20)

    dwd.grid(row = 1, column = 0, sticky = W, padx = 10)
    eDwd.grid(row = 1, column = 1)

    ws.grid(row = 1, column = 2, sticky = W, padx = 10)
    eWs.grid(row = 1, column = 3)

    cr.grid(row = 2, column = 0, sticky = W, padx = 10)
    eCr.grid(row = 2, column = 1)    

    zone.grid(row = 2, column = 2, sticky = W, padx = 10)
    eZone.grid(row = 2, column = 3)

    extent.grid(row = 3, column = 0, sticky = W, padx = 10)
    eExtent.grid(row = 3, column = 1) 

    nucObj = nucClass()    
    btnBounds = Button(tab4, text = "Click to get NHP GR Bounds",bg = "green", width = 30, anchor = N, command = nucObj.argsToNuc)
    btnBounds.grid(row = 2, column = 0, columnspan = 2)  

    btnBoundsKml = Button(tab4, text = "Google Earth",bg = "green", width = 30, anchor = N, command = nucObj.argsToNucKml)
    btnBoundsKml.grid(row = 2, column = 2, columnspan = 1)  

    btnBoundsGis = Button(tab4, text = "GIS",bg = "green", width = 30, anchor = N, command = nucObj.argsToNucGis)
    btnBoundsGis.grid(row = 2, column = 3, columnspan = 1)    

    result = LabelFrame(tab4, text = "Result")
    result.grid(row = 3, column = 0, sticky = W+E, columnspan=  4, padx = 5)

    bounds = Label(result, text = "Hazard area GR Bounds are as follows", bg = "yellow") 
    bBounds = Entry(result, width=85) 

    bounds.grid(row = 5, column = 0, sticky = W, padx = 10)
    bBounds.grid(row = 5, column = 1, columnspan = 3)

class guiRes:

    title = Label(tab5, text = "Radiation Exposure Status", fg = 'green', bg = "yellow", width = 56)
    title.config(font=("Courier", 30, "bold"))
    title.grid(row = 0, column = 0, sticky = N, columnspan = 4)

    
    parameters = LabelFrame(tab5, text = "Parameters")
    parameters.grid(row = 1, column = 0, sticky = W+E, columnspan=  4, padx = 5)

    gr1 = Label(parameters, text = "Enter Distance from Attack GR", width = 30, anchor = W)
    cb1 = Label(parameters, text = "Enter Acceptable Risk Dose ", width = 30, anchor = W)
    tpt = Label(parameters, text = "Enter Troops Movement Speed ", width = 30, anchor = W)

    eGr1 = Entry(parameters, width = 20)
    eCb1 = Entry(parameters, width = 20)
    eTpt = Entry(parameters, width = 20)

    gr1.grid(row = 1, column = 0, sticky = W, padx = 10)
    eGr1.grid(row = 1, column = 1)

    cb1.grid(row = 2, column = 0, sticky = W, padx = 10)
    eCb1.grid(row = 2, column = 1)

    tpt.grid(row = 3, column = 0, sticky = W, padx = 10)
    eTpt.grid(row = 3, column = 1)

    # cloudDim = StringVar(optional)
    # cloudDimOption = OptionMenu(optional,cloudDim, "2 KT", "5 KT", "30 KT", "100 KT")
    # cloudDim.set('2 KT')    
    # cloudDimOption.grid(row=2, column = 2)  

    riskValue = StringVar(parameters)
    riskValueOption = OptionMenu(parameters,riskValue, "Negligible Risk", "Increased Risk", "Significant Risk", "High Risk", "Very High Risk")
    riskValue.set("Negligible Risk")    
    riskValueOption.grid(row=2, column = 2, padx = 40)     

    resObj = resClass()

    bPreview = Button(parameters, text="Update",width = 20, command = resObj.changeRiskValue)
    bPreview.grid(row=2, column = 3, padx = 20)

    speedValue = StringVar(parameters)
    speedValueOption = OptionMenu(parameters,speedValue, "FSMO", "Single Belt", "B Veh", "A Veh")
    speedValue.set("FSMO")    
    speedValueOption.grid(row=3, column = 2, padx = 40)     


    bPreviewSpeed = Button(parameters, text="Update",width = 20, command = resObj.changeSpeedValue)
    bPreviewSpeed.grid(row=3, column = 3, padx = 20)


    btnBounds = Button(tab5, text = "Click to get RES ",bg = "green", command = resObj.argsToRes)
    btnBounds.grid(row = 2, column = 0, columnspan = 4)

    result = LabelFrame(tab5, text = "Result")
    result.grid(row = 3, column = 0, sticky = W+E, columnspan=  4, padx = 5)

    bounds = Label(result, text = "Troops for Mission : ", bg = "yellow", width = 30, anchor = W)
    bounds.grid(row = 5, column = 0, sticky = W, padx = 10)

    bBounds = Text(result, wrap=WORD, width=80, height= 11)

    # bBounds = Entry(result, width=80)         
    bBounds.grid(row = 6, column = 0, columnspan = 4, padx = 10, pady = 5)


class guiRadiac:

    title = Label(tab6, text = "Radiac Calculator", fg = 'green', bg = "yellow", width = 56)
    title.config(font=("Courier", 30, "bold"))
    title.grid(row = 0, column = 0, sticky = N, columnspan = 4)

    
    parameters = LabelFrame(tab6, text = "Parameters")
    parameters.grid(row = 1, column = 0, sticky = W+E, columnspan=  4, padx = 5)

    time = Label(parameters, text = "Enter Time of Reading", width = 30, anchor = W)
    radiation = Label(parameters, text = "Enter Radiation Reading ", width = 30, anchor = W)
    timeReq = Label(parameters, text = "Enter Time at which Radiation Req ", width = 30, anchor = W)    
    radReq = Label(parameters, text = "Enter Radiatiion at which Time Req ", width = 30, anchor = W)
    timeEntry = Label(parameters, text = "Enter Troops Enter Time ", width = 30, anchor = W)
    timeExit = Label(parameters, text = "Enter Troops Exit Time", width = 30, anchor = W)
    radLimit = Label(parameters, text = "Enter Dose Limit ", width = 30, anchor = W)
    timeReqMsn = Label(parameters, text = "Enter Time Required", width = 30, anchor = W)

    eTime = Entry(parameters, width = 20)
    eRadiation= Entry(parameters, width = 20)
    eTimeReq = Entry(parameters, width = 20)    
    eRadReq = Entry(parameters, width = 20)
    eTimeEntry = Entry(parameters, width = 20)
    eTimeExit = Entry(parameters, width = 20)
    eRadLimit = Entry(parameters, width = 20)
    eTimeReqMsn = Entry(parameters, width = 20)

    time.grid(row = 1, column = 0, sticky = W, padx = 10)
    eTime.grid(row = 1, column = 1)

    radiation.grid(row = 1, column = 2, sticky = W, padx = 10)
    eRadiation.grid(row = 1, column = 3)

    timeReq.grid(row = 2, column = 0, sticky = W, padx = 10)
    eTimeReq.grid(row = 2, column = 1)
    
    radReq.grid(row = 2, column = 2, sticky = W, padx = 10)
    eRadReq.grid(row = 2, column = 3)

    timeEntry.grid(row = 3, column = 0, sticky = W, padx = 10)
    eTimeEntry.grid(row = 3, column = 1)

    timeExit.grid(row = 3, column = 2, sticky = W, padx = 10)
    eTimeExit.grid(row = 3, column = 3)

    radLimit.grid(row = 4, column = 0, sticky = W, padx = 10)
    eRadLimit.grid(row = 4, column = 1)

    timeReqMsn.grid(row = 4, column = 2, sticky = W, padx = 10)
    eTimeReqMsn.grid(row = 4, column = 3)
  

    radiacObj = radiacClass()


    btnBoundsRate = Button(tab6, text = "Click to get DoseRate ",bg = "green", command = radiacObj.argsToRate)
    btnBoundsRate.grid(row = 2, column = 0, columnspan = 1)

    btnBoundsRad = Button(tab6, text = "Click to get Radiation Time ",bg = "green", command = radiacObj.argsToRad)
    btnBoundsRad.grid(row = 2, column = 1, columnspan = 1)

    btnBoundsDose = Button(tab6, text = "Click to get Dose Taken ",bg = "green", command = radiacObj.argsToDose)
    btnBoundsDose.grid(row = 2, column = 2, columnspan = 1)
    
    btnBoundsTime = Button(tab6, text = "Click to get Start Time ",bg = "green", command = radiacObj.argsToTime)
    btnBoundsTime.grid(row = 2, column = 3, columnspan = 1)

    btnBoundsTime = Button(tab6, text = "Click to get Exit Time ",bg = "green", command = radiacObj.argsToExit)
    btnBoundsTime.grid(row = 3, column = 1, columnspan = 2)

    result = LabelFrame(tab6, text = "Result")
    result.grid(row = 4, column = 0, sticky = W+E, columnspan=  4, padx = 5)

    boundsRate = Label(result, text = "Dose Rate is : ", bg = "yellow", width = 30, anchor = W)
    boundsRate.grid(row = 5, column = 0, sticky = W, padx = 10)

    bBoundsRate = Entry(result, width=80)         
    bBoundsRate.grid(row = 5, column = 1, columnspan = 3)    
    
    boundsRad = Label(result, text = "Radiation Time is : ", bg = "yellow", width = 30, anchor = W)
    boundsRad.grid(row = 6, column = 0, sticky = W, padx = 10)

    bBoundsRad = Entry(result, width=80)         
    bBoundsRad.grid(row = 6, column = 1, columnspan = 3)  

    boundsDose = Label(result, text = "Dose Taken by Troops : ", bg = "red", width = 30, anchor = W)
    boundsDose.grid(row = 8, column = 0, sticky = W, padx = 10)

    bBoundsDose = Entry(result, width=80)         
    bBoundsDose.grid(row = 8, column = 1, columnspan = 3)

    boundsTime = Label(result, text = "Start Time : ", bg = "red", width = 30, anchor = W)
    boundsTime.grid(row = 9, column = 0, sticky = W, padx = 10)

    bBoundsTime = Entry(result, width=80)         
    bBoundsTime.grid(row = 9, column = 1, columnspan = 3)

    boundsExit = Label(result, text = "Exit Time : ", bg = "red", width = 30, anchor = W)
    boundsExit.grid(row = 10, column = 0, sticky = W, padx = 10)

    bBoundsExit = Entry(result, width=80)         
    bBoundsExit.grid(row = 10, column = 1, columnspan = 3)

class guiDamage:

    title = Label(tab7, text = "Atomic Damage Template", fg = 'green', bg = "yellow", width = 56)
    title.config(font=("Courier", 30, "bold"))
    title.grid(row = 0, column = 0, sticky = N, columnspan = 4)

    parameters = LabelFrame(tab7, text = "Parameters")
    parameters.grid(row = 1, column = 0, sticky = W+E, columnspan=  4, padx = 5)

    burst = Label(parameters, text = "Enter S - Surface Burst, A - Air Burst", width = 30, anchor = W)
    yd = Label(parameters, text = "Enter KT of Weapon", width = 30, anchor = W)
    
    eBurst = Entry(parameters, width = 20)
    eYd = Entry(parameters, width = 20)

    burst.grid(row = 1, column = 0, sticky = W, padx = 10)
    eBurst.grid(row = 1, column = 1)

    yd.grid(row = 1, column = 2, sticky = W, padx = 10)
    eYd.grid(row = 1, column = 3)

    damageObj = damageClass()    
    btnBounds = Button(tab7, text = "Click to get Atomic Damage Template",bg = "green", width = 30, anchor = N, command = damageObj.argsToDamage)
    btnBounds.grid(row = 2, column = 0, columnspan = 2)  

    btnBoundsKml = Button(tab7, text = "Google Earth",bg = "green", width = 30, anchor = N, command = damageObj.argsToDamageKml)
    btnBoundsKml.grid(row = 2, column = 2, columnspan = 1)  

    btnBoundsGis = Button(tab7, text = "GIS",bg = "green", width = 30, anchor = N, command = damageObj.argsToDamageGis)
    btnBoundsGis.grid(row = 2, column = 3, columnspan = 1)    

    result = LabelFrame(tab7, text = "Result")
    result.grid(row = 3, column = 0, sticky = W+E, columnspan=  4, padx = 5)

    bounds = Label(result, text = "Atomic Damage Template", bg = "yellow") 
    bBounds = Entry(result, width=85) 

    bounds.grid(row = 5, column = 0, sticky = W, padx = 10)
    bBounds.grid(row = 5, column = 1, columnspan = 3)

class guiRoute:

    title = Label(tab8, text = "Radiation Dose Taken Enroute", fg = 'green', bg = "yellow", width = 56)
    title.config(font=("Courier", 30, "bold"))
    title.grid(row = 0, column = 0, sticky = N, columnspan = 4)

    parameters = LabelFrame(tab8, text = "Parameters")
    parameters.grid(row = 1, column = 0, sticky = W+E, columnspan=  4, padx = 5)

    time = Label(parameters, text = "Enter Time of Reading", width = 30, anchor = W)
    radiation = Label(parameters, text = "Enter Radiation Reading ", width = 30, anchor = W)
    dist = Label(parameters, text = "Enter Distance from Center of blast ", width = 30, anchor = W)    
    timeEntry = Label(parameters, text = "Enter Troops Enter Time ", width = 30, anchor = W)
    timeExit = Label(parameters, text = "Enter Troops Exit Time", width = 30, anchor = W)
    distEntry = Label(parameters, text = "Enter Entry Distance ", width = 30, anchor = W)
    distExit = Label(parameters, text = "Enter Exit Distance", width = 30, anchor = W)

    eTime = Entry(parameters, width = 20)
    eRadiation= Entry(parameters, width = 20)
    eDist = Entry(parameters, width = 20)    
    eTimeEntry = Entry(parameters, width = 20)
    eTimeExit = Entry(parameters, width = 20)
    eDistEntry = Entry(parameters, width = 20)
    eDistExit = Entry(parameters, width = 20)

    time.grid(row = 1, column = 0, sticky = W, padx = 10)
    eTime.grid(row = 1, column = 1)

    radiation.grid(row = 1, column = 2, sticky = W, padx = 10)
    eRadiation.grid(row = 1, column = 3)

    dist.grid(row = 2, column = 0, sticky = W, padx = 10)
    eDist.grid(row = 2, column = 1)    

    timeEntry.grid(row = 3, column = 0, sticky = W, padx = 10)
    eTimeEntry.grid(row = 3, column = 1)

    timeExit.grid(row = 3, column = 2, sticky = W, padx = 10)
    eTimeExit.grid(row = 3, column = 3)

    distEntry.grid(row = 4, column = 0, sticky = W, padx = 10)
    eDistEntry.grid(row = 4, column = 1)

    distExit.grid(row = 4, column = 2, sticky = W, padx = 10)
    eDistExit.grid(row = 4, column = 3)

    routeObj = routeClass()   

    btnBounds = Button(tab8, text = "Click to get Dose Taken Enroute",bg = "green", width = 30, anchor = N, command = routeObj.argsToRoute)
    btnBounds.grid(row = 2, column = 0, columnspan = 2)  

    btnBoundsKml = Button(tab8, text = "Google Earth",bg = "green", width = 30, anchor = N, command = routeObj.argsToRouteKml)
    btnBoundsKml.grid(row = 2, column = 2, columnspan = 1)  

    btnBoundsGis = Button(tab8, text = "GIS",bg = "green", width = 30, anchor = N, command = routeObj.argsToRouteGis)
    btnBoundsGis.grid(row = 2, column = 3, columnspan = 1)    

    result = LabelFrame(tab8, text = "Result")
    result.grid(row = 3, column = 0, sticky = W+E, columnspan=  4, padx = 5)

    bounds = Label(result, text = "Dose Taken Enroute", bg = "yellow") 
    bBounds = Entry(result, width=85) 

    bounds.grid(row = 5, column = 0, sticky = W, padx = 10)
    bBounds.grid(row = 5, column = 1, columnspan = 3)




window.mainloop()
