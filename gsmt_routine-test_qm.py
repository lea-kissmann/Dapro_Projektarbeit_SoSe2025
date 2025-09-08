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
q= 0
m= 0
g= -10
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
         return self.s[2:]
    
    @v.setter
    def v(self, value):
         self.s[2:]= value
         
    #Routine um die Position abzufragen und zu überschreiben 
    @property
    def p(self):
        return self.s[:2]
    
    @p.setter
    def p(self, value):
        self.s[:2]= value 
        
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
    
    for j, sj in enumerate(alle_teilchen):
        
        if j== i:
            continue
        
        rj= sj[:2]
        rij= ri - rj
        betrag= np.linalg.norm(rij)
        if betrag > 0:
            a -= (q**2) * (rij / (betrag ** 3))
    
    #Finale Ableitung des gegebenen Teichens si
    bes= m * a
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
       betrag_rij = betrag_rij[betrag_rij > 0]
      
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
            
    return treffer, wand_gesucht
#
#  
#Routine um zu testen ob ein Teilchen noch in der Box ist  
def ist_in_box(state, grenzen):
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
        
    """
    xmin, xmax, ymin, ymax = grenzen
    x, y = state[:2]
    return (xmin <= x <= xmax) and (ymin <= y <= ymax)
#
#       
def reflektieren(state, grenzen, alle_teilchen, i, dt):
    """
    Routine um die Reflextion der Teilchen an den Boxwänden herzustellen 
    """
    # Berechnung des nächsten Schritts
    neuer_state = rk4_step(f, state, dt, alle_teilchen, i)
    
    if ist_in_box(neuer_state, grenzen):
        return neuer_state
    
    # Finde wo das Teilchen die Wand trifft
    treffer, wand_getroffen = wo_durchquert(state, neuer_state, grenzen, dt)
    
    if treffer is None:
        return neuer_state
    
    # Berechne State bis zur Wand
    state_bis_wand = rk4_step(f, state, treffer, alle_teilchen, i)
    
    # Spiegele die entsprechende Geschwindigkeitskomponente
    if wand_getroffen in ("xmin", "xmax"):
        state_bis_wand[2] *= -1 
    if wand_getroffen in ("ymin", "ymax"):
        state_bis_wand[3] *= -1
        
    # Führe den Rest des Zeitschritts aus 
    dt_rest = dt - treffer
    alle_teilchen[i] = state_bis_wand.copy()
    neu_final_state = rk4_step(f, state_bis_wand, dt_rest, alle_teilchen, i)
        
    return neu_final_state
#
#
def step(teilchen_list, box, dt):
    """
    Führt einen Zeitschritt für alle Teilchen durch
    """
    # Sammlung der aktuellen States
    alle_states = [t.state() for t in teilchen_list]
    neue_states = []
    
    # Schleife um einen Durchlauf zu berechnen
    for i, state in enumerate(alle_states):
        state_neu = reflektieren(state, box.grenzen, alle_states, i, dt)
        neue_states.append(state_neu)
           
    # Überschreiben der Werte, sodass die neuen aktuell sind       
    for t, s_neu in zip(teilchen_list, neue_states):
        t.state_neu(s_neu)
#
#
def main():
    #gegebene Teilchen 
    teilchen = [Teilchen(1.0, 45.0, 10.0, 0.0), 
                Teilchen(99.0, 55.0, -10.0, 0.0),
                Teilchen(10.0, 50.0, 15.0, -15.0),
                Teilchen(20.0, 30.0, -15.0, -15.0),
                Teilchen(80.0, 70.0, 15.0, 15.0),
                Teilchen(80.0, 60.0, 15.0, 15.0),
                Teilchen(80.0, 50.0, 15.0, 15.0)]
    
    #Initialisierung der Box
    box= Box(teilchen, grenzen=(-100, 100, -100, 100))
    
    #Parameter der Simulation 
    dt= 0.001
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
            step(teilchen, box, dt) 
            
            states_array = np.array([t.s for t in teilchen])
            En= E(states_array)                     
            
            #Tatsächliche verfassung der Dateiinhalte pro Schritt
            f.write(f"Schritt {durchlaufe:4d}    | Systemenergie = {En:12.5f}\n")
            f.write("  Teilchen  |      x          y            vx           vy\n")
            f.write("----------------------------------------------------------------\n")
            
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
if __name__ == "__main__":
    systE, zeit, bes_x, bes_y, teilchen= main()

#Plotts
#Farben für Plots mit mehreren Farben
farben= ['b', 'g', 'r', 'c', 'm', 'y', 'k']

#1.Plott: E vs. zeit
plt.figure()
plt.plot(zeit, systE, label="Systemenergie im Verlauf der Zeit")
plt.xlabel("Zeit")
plt.ylabel("Systemenergie")
plt.legend()
plt.title("Energierhaltung")

#2.Plott: Die Flugbahn des ersten Teilchens
plt.figure()
plt.plot(bes_x[0], bes_y[0], label="1. Teilchen")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Bahn des ersten Teilchens")

#3.Plott: Flugbahnen aller Teilchen
plt.figure()
for i in range(len(teilchen)):
    plt.plot(bes_x[i], bes_y[i], label=f"{i+1}. Teilchen", color= farben[i])
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Flugbahnen aller Teilchen")

#Ausgabe der Plotts
plt.show()




