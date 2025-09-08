#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Datei mit allen Routinen zusammen 

#Imports für die Funktionen
import numpy as np
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
#
#
#Parameter der Teilchen
q= 50
m= 1
g= -10
#
#
#Was fehlt?
#
#
class Teilchen:
    """
    definiert die Klasse Teilchen, welche auf Basis von Statevektoren existiert.
    """
    
    #Routine um Teilchen erstellen zu können
    def __init__(self, x, y ,vx ,vy):
        self.s= np.array([x, y, vx, vy], dtype= float)
    
    #Routinen um die Geschwindigkeit abzufragen und zu überschreiben
    @property
    def v(self):
         return self.v[2:]
    
    @v.setter
    def v(self, value):
         self.v[2:]= value
         
    #Routine um die Position abzufragen und zu überschreiben 
    @property
    def p(self):
        return self.p[:2]
    
    @p.setter
    def p(self, value):
        self.p[:2]= value 
        
    #Routine um Zustand zurück zu geben
    def state(self):
        return self.s
    
    #Routine um neuen Zustand zu übergeben
    def state_neu(self, s_neu):
        self.s= np.array(s_neu)      
#
#
class Box:   
    
    """
    definiert die Klasse Box, welche die Umgebungsstruktur der Teilchen bildet.
    """
    
    #Routine um Box erstellen zu können
    def __init__(self, teilchen,  grenzen):     
        
        #Liste der übergebenen Teilchen 
        if teilchen is None:
            teilchen= []
        self.teilchen= teilchen 
        
        #Boxgrenzen setzten 
        self.grenzen= grenzen 
        
#Routine bei der man prüft ob sich die Teilchen noch in der Box befinden 
def in_box(self, grenzen):
    """
    prüft ob sich die in die Box gefügten Teilchen noch 
    innerhalb der Box befinden, oder ob sie die Grenzen überschritten haben

    Returns
    -------
    innen:  
        True:
            wenn die Teilchen sich noch in der Box befinden 
    
        False: 
            wenn die Teilchen außerhalb der Grenzen liegen 
    wand:
        "außerhalb dem x oder y Min- oder Maximum "
        je nach Grenzüberschreitung
        
    """
    xmin, xmax, ymin, ymax = grenzen
    wand= None
    innen= None
    
    for s in self.teilchen:
        
        #Seitenwände
        if s.p[0] <= self.xmin:
             innen, wand= False, "außerhalb dem x-Minimum " 
             
        elif s.p[0] >= self.xmax:
            innen, wand= False, "außerhalb dem x-Maximum "
            
        else:
            innen,wand= True, None
        
        #Ober-/Unterseite
        if s.p[1] <= self.ymin:
            innen,wand= False, "außerhalb dem y-Minimum "
            
        elif s.p[1] >= self.ymax:
            innen, wand= False, "außerhalb dem y-Maximum "
            
        else:
             innen, wand= True, None
     
    return innen, wand
#
#
def f(si, alle_teilchen, i):
    """
    Routine, die die entsprechende Differetialgleichung des gegebenen 
    Statevektors si aufbaut und den Abgeleiteten Statevektor wiedergibt.

    Parameter
    ----------
    si :
        array
        Statevektor des ensprechenden Teilchens si
        
    alle_teilchen :
        array 
        Liste der Statevektoren der Teilchens 
        
    i: 
        index

    Returns
    -------
    sdot:
        array 
        Ableitung des gegebenen si Teilchens
    
    """
    
    # r und rdot vom gegebenen Teilchen 
    x= si[0]
    y= si[1]
    vx= si[2]
    vy= si[3]
    ri= np.array([x,y])
    ridot= np.array([vx, vy])
    
    #Gravitationsstate und der tatsächliche State für die Beschleunigung
    a= np.array([0.0, g])
    bes= m * a
    
    for j, sj in enumerate(alle_teilchen):
        
        if j== i:
            continue
        
        rj= sj[:2]
        rij= ri - rj
        betrag= np.linalg.norm(rij)
        a -= (q**2) * (rij / (betrag ** 3))
    
    #Finale Ableitung des gegebenen Teichens si
    sdot= np.array([ridot[0], ridot[1], bes[0], bes[1]])
    
    return sdot
#
#
def rk4_step(f, s, dt, alle_teilchen, i):  
    """
    Routine, die einen einzelen Schritt eines Teilchens berechenet 

    Parameter
    ----------
    f :
        Die Differentialgleichung des Teilchens
        
    s :
        Statevektor des Teilchen an diskretem Punkt
        
    dt :
        Zeitschritt
        
    alle_teilchen:
        Liste aller Teilchen
        
    i:
        Index

    Returns
    -------
    step:
        array
        Nächster Statevektor des gebeben Teilchen s

    """
    #Runge-Kutta-Koeffizienten
    k1= dt * f(s, alle_teilchen, i)
    k2= dt * f(s + (0.5 * k1), alle_teilchen, i)
    k3= dt * f(s + (0.5 * k2), alle_teilchen, i)
    k4= dt * f(s + k3, alle_teilchen, i)
    
    #Nächster Punkt des angegebenen Teilchens s
    step= s + (k1 / 6) + (k2 / 3) + (k3 / 3) + (k4 / 6)
    return step
#
#
def E(alle_teilchen):
    """
    Berechnet die Systemenergie der angegebenen anzahl an Teilchen 

    Parameters
    ----------
    *args : Die angegebenen Statevektoren der Teilchen 

    Returns
    -------
    E : Die gesamte Energie der angegebenen Teilchen 

    """
    
    #Array aus allen angegebenen Teilchen 
    matrix= alle_teilchen
    
    #N ist die Anzahl der angegebenen Teilchen
    N= matrix.shape[0]
    
    #Sammlung der x-, y-, vx-, vy-Werte aller angegebenen Teilchen 
    x= matrix[:,0]
    y= matrix[:,1]
    vx= matrix[:,2]
    vy= matrix[:,3]
    
    #Berechnung der Energie anhand Gravitationsenergie + Kienetische Energie 
    #+ Energie der Teilchen untereinander 

    #Gravitationsenergie mit -m * g * y
    Eg= -m * g * np.sum(y)   
    
    #Berechnung der Kinietische Energie mit 1/2*m*(vx^2+vy^2)
    sam_v= ((vx ** 2) + (vy ** 2))
    Ek= (m/2) * np.sum(sam_v)
    
    #Berechnung der Energie der Teilchen 
    #Fall für mehrere Teilchen: 
    if N > 1:
       r= matrix[:,:2]
       
       betrag_rij= pdist(r)
      
       Et= (q ** 2) * np.sum(1.0 / betrag_rij) 
    
    # Fall für ein Teilchen
    else:
       Et= 0.0
    
    #Berechnung der gesamten Energie
    E= np.sum(Eg + Ek) + Et
    
    return E
#
#
def wo_durchquert(sn, sn1, grenzen, dt):
    """
    Routine die durch Interpolation mit 
    
    treffer= dt * ((Bel wand - Bel sn) / (Bel sn+1 - Bel sn))
    
    den neuen Zeitpunkt zurückgibt bevor das Teilchen die Box verlässt 

    Parameters
    ----------
    sn : 
        vorheriger Standort (Statevektor des Teilchens)
    sn1 :
        neuer  Standort (Statevektor des Teilchens)
    grenzen : 
        Boxgrenzen 
    dt : 
        Größe des Zeitschrittes
        
    Returns
    -------
    treffer:
        Zeitpunkt (float) bis zu dem das Teilchen in der Box ist 
    wand_gesucht:
        an welcher wand das Teilchen die Box trifft
        
    """
    xmin, xmax, ymin, ymax= grenzen
    
    treffer= None
    wand_gesucht= None
    
    #Gucken ob x-Grenze überschritten
    if sn1[0] < xmin:
        getroffen= dt * (xmin - sn[0]) / (sn1[0] - sn[0])
        if 0 <= getroffen <= dt:
            treffer, wand_gesucht= getroffen, "xmin"
            
    elif sn1[0] > xmax:
        getroffen= dt * (xmax - sn[0]) / (sn1[0] - sn[0])
        if 0 <= getroffen <= dt:
            treffer, wand_gesucht= getroffen, "xmax"
            
    #Gucken ob y-Grenze überschritten
    if sn1[1] < ymin:
        getroffen= dt * (ymin - sn[1]) / (sn1[1] - sn[1])
        if 0 <= getroffen <= dt and (treffer is None or getroffen < treffer):
            treffer, wand_gesucht= getroffen, "ymin"
            
    elif sn1[1] > ymax:
        getroffen= dt * (ymax - sn[1]) / (sn1[1] - sn[1])
        if 0 <= getroffen <= dt and (treffer is None or getroffen < treffer):
            treffer, wand_gesucht= getroffen, "ymax"
            
    return getroffen, wand_gesucht
#
#           
def reflektieren(teilchen, rk4_step, f, sn, dt, grenzen, alle_teilchen, i): #BRAUCHT MAN SN??????
    """
    Routine um die Reflextion der Teilchen an den Boxwänden herzustellen 

    Parameters
    ----------
    teilchen : 
        das entsprechende Teilchen
    rk4_step : 
        Routine um nächsten Schritt zu berechen 
    f : 
        Routine um Statevektor abzuleiten
    sn : 
        momentane Statevektor des Teilchens 
    dt : 
        Zeitschritt
    grenzen : 
        Boxgrenzen
    alle_Teilchen : 
        restlichen Teilchen des Systems 
    i:
        Index

    Returns
    -------
    neu_final_state:
        der wenn nötig überarbeitete Statevektor

    """
    #Genereller Stand des Teilchens bisher
    alter_state= teilchen.state()
    position_alt= alter_state[:2]
    
    #Berechnung neuer Stand
    neuer_state= rk4_step(f, alter_state, dt, alle_teilchen, i)
    position_neu= neuer_state[:2]
    
    #Testen ob Teilchen nach Zeit in Box geblieben ist 
    
    innen, wand= in_box(position_neu)
    treffer, wand_getroffen= wo_durchquert(position_alt, position_neu, grenzen, dt)
    
    if innen == True or treffer is None:
        neu_final_state= neuer_state
    else:
        state_bis_wand= rk4_step(f, alter_state, treffer, alle_teilchen, i) #index sache anpassen !!!!!
        
    #Spiegelung der Betroffenen Werte
        if wand_getroffen in ("xmin", "xmax"):
            state_bis_wand[2] *= -1 
        if wand_getroffen in ("ymin", "ymax"):
            state_bis_wand[3] *= -1
            
    #Rest des Zeitschrittes ausführen 
        dt_rest= dt - treffer
        alle_teilchen[i]= state_bis_wand
        neu_final_state= rk4_step(f, state_bis_wand, dt_rest, alle_teilchen, i)
        
    return neu_final_state
#
#
def step(teilchen_sam, box, dt):
    #Sammlung der Statezustände
    neue_states= []
    alle_teilchen= [teilchen_sam.copy() for t in teilchen_sam]
    
    #Schleife um einen Durchlauf zu berechnen
    for i, state in enumerate(teilchen_sam):
        state_neu= rk4_step(f, state, dt, alle_teilchen, i)
        if in_box(state_neu) == True:
            neue_states.append(state_neu)
        else:
           getroffen, wand_gesucht= wo_durchquert(state, state_neu, grenzen , dt)
           state_final= reflektieren(state, rk4_step, f, dt, grenzen, alle_teilchen, i)
           neue_states.append(state_final)
           
    #Überschreiben der Werte, sodass die neuen aktuell sind       
    for werte in teilchen_sam and neue_states:
        teilchen_sam = Teilchen.state_neu(neue_states)
#
#
def main():
    #gegebene Teilchen 
    teilchen = [Teilchen.state(1.0, 45.0, 10.0, 0.0), 
                Teilchen.state(99.0, 55.0, -10.0, 0.0),
                Teilchen.state(10.0, 50.0, 15.0, -15.0),
                Teilchen.state(20.0, 30.0, -15.0, -15.0),
                Teilchen.state(80.0, 70.0, 15.0, 15.0),
                Teilchen.state(80.0, 60.0, 15.0, 15.0),
                Teilchen.state(80.0, 50.0, 15.0, 15.0),]
    
    #Initialisierung der Box
    box= Box([teilchen], grenzen=(-100, 100, -100, 100))
    
    #Parameter der Simulation 
    dt= 0.001
    zeit= 10
    durchlauf= 10000
    
    #Zwischenspeicher für Plotts
    systE= []
    zeit= []
    bes_x= [[] for w in teilchen]
    bes_y= [[] for u in teilchen]
    
    
    #Datei die Output verschriftlicht
    with open("Werte_Simulation.txt", "w") as f:

        #Durchläufe der Simulation
        for durchlaufe in range(durchlauf):
            for array in teilchen:
                schritt= step(array, box, dt) 
                En= E(teilchen) 
                
            #Tatsächliche verfassung der Dateiinhalte pro Schritt
                f.write(f"Schritt {durchlaufe:4d}    | Systemenergie = {En:12.5f}\n")
                f.write("  Teilchen  |        x       y       vx       vy\n")
                f.write("-----------------------------------------------------\n")
                
                for i, t in enumerate(teilchen):
                    x, y, vx, vy = t.s
                    f.write(f"   {i}   |   {x:10.3f}   {y:10.3f}   {vx:10.3f}   {vy:10.3f}\n")
                    
                f.write(" \n")
               
            #Übergeben der Werte an Listen
                zeit.append(durchlaufe * dt)
                systE.append(En)
                for i, t in enumerate(teilchen):
                    bes_x[i].append(t.s[0])
                    bes_y[i].append(t.s[1])
        
    return systE, zeit, bes_x, bes_y, teilchen

#Ausgabe der Werte 
systE, zeit, bes_x, bes_y, teilchen= main()

#Plotts
#Farben für Plots mit mehreren Farben
farben= ['b', 'g', 'r', 'c', 'm', 'y', 'k']
#1.Plott: E vs. zeit
plt.figure()
plt.plot(zeit, systE, lable= "Systemenergie im Verlauf der Zeit")
plt.xlabel("Zeit")
plt.ylabel("Systemenergie")
plt.legend()
plt.title("Energierhaltung")

#2.Plott: Die Flugbahn des ersten Teilchens
plt.figure()
plt.plot(bes_x[0], bes_y[0], lable= "1. Teilchen")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Bahn des ersten Teilchens")

#3.Plott: Flugbahnen aller Teilchen
plt.figure()
for i in range(len(teilchen)):
    plt.plot(bes_x[i], bes_y[i], lable= f"{i}. Teilchen", color= farben[i])
plt.xlabel("x")
plt.ylabel("x")
plt.legend()
plt.title("Flugbahnen aller Teilchen")

#Ausgabe der Plotts
plt.show()




