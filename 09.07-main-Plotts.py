#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

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
    systE= []
    sam_states= []
    
    
    #Durchläufe der Simulation
    for durchlauf in range(durchlauf):
        schritt= step(teilchen, box, dt) #speichern und durchlaufen?
        sam_states.append(schritt)
        
        E= E(teilchen) #speicher und durchlaufen? 
        systE.append(E)
        
        
    return systE, sam_states


if __name__ == "__main__":
    Sytemenergie, Sammlung_Teilchen= main() 
    
    
    

