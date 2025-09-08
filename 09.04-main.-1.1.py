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
    
    #Parameter der Simulation 
    dt= 0.001
    zeit= 10
    durchlauf= zeit/ dt
    
    box= Box([teilchen], grenzen=( -100, 100, -100, 100))
    
    #Durchläufe der Simulation
    for durchlauf in range(durchlauf):
        step(box, rk4_step, f ,dt) #speichern und durchlaufen?
        E(teilchen) #speicher und durchlaufen? 
        
        
    

