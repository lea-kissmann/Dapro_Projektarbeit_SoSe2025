#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


s1= np.array([1.0, 45.0, 10.0, 0.0])
s2= np.array([99.0, 55.0, -10.0, 0.0])
s3= np.array([10.0, 50.0, 15.0, -15.0])
s4= np.array([20.0, 30.0, -15.0, -15.0])
s5= np.array([80.0, 70.0, 15.0, 15.0])
s6= np.array([80.0, 60.0, 15.0, 15.0])
s7= np.array([80.0, 50.0, 15.0, 15.0])


def main():
    
    #gegebene Teilchen 
    teilchen = [Teilchen(s1), 
                Teilchen(s2),
                Teilchen(s3),
                Teilchen(s4),
                Teilchen(s5),
                Teilchen(s6),
                Teilchen(s7),]
    
    #Initialisierung der Box
    box= Box([teilchen], grenzen=( -100, 100, -100, 100))
    
    #Parameter der Simulation 
    dt= 0.001
    zeit= 10
    durchlauf= zeit/ dt
    
    #Zwischenspeicher für Plotts
    systE= []
    zeit= []
    bes_x= [[] for w in teilchen]
    bes_y= [[] for u in teilchen]
    
    
    #Datei die Output verschriftlicht
    with open("Werte_Simulation.txt", "w") as f:

        #Durchläufe der Simulation
        for durchlaufe in range(durchlauf):
            schritt= step(teilchen, box, dt) 
            E= E(teilchen) 
            
        #Tatsächliche verfassung der Dateiinhalte pro Schritt
            f.write(f"Schritt {durchlaufe:4d}    | Systemenergie = {E:12.5f}\n")
            f.write("  Teilchen  |        x       y       vx       vy\n")
            f.write("-----------------------------------------------------\n")
            
            for i, t in enumerate(teilchen):
                x, y, vx, vy = t.s
                f.write(f"   {i}   |   {x:10.3f}   {y:10.3f}   {vx:10.3f}   {vy:10.3f}\n")
                
            f.write(" \n")
           
        #Übergeben der Werte an Listen
            zeit.append(durchlaufe * dt)
            systE.append(E)
            for i, t in enumerate(teilchen):
                bes_x[i].append(t.s[0])
                bes_y[i].append(t.s[1])
        
    print("Simulation ist abgeschlossen. Datei 'Werte_Simulation.txt' wurde erstellt")



    
    
    

