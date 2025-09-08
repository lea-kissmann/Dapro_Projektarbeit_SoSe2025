#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#erster Versuch die funktion der Systemenergie aufzustellen
import numpy as np


def E(*args):
    """
    Berechnet die Systemenergie der angegebenen anzahl an Teilchen 

    Parameters
    ----------
    *args : Die angegebenen Statevektoren der Teilchen 

    Returns
    -------
    E : Die gesamte Energie der angegebenen Teilchen 

    """
    #Parameter der Teilchen
    q= 50
    m= 1
    g= -10
    
    #Matrix aus allen angegebenen Teilchen 
    matrix= np.asarray(args)
    
    #N ist die Anzahl der angegebenen Teilchen
    N= matrix.shape[0]
    
    #Sammlung der x-, y-, vx-, vy-Werte aller angegebenen Teilchen 
    x, y, vx, vy = matrix.T 
    
    #Berechnung der Energie anhand Gravitationsenergie + Kienetische Energie 
    #+ Energie der Teilchen untereinander 

    #Gravitationsenergie mit -m * g * y
    Eg= -m * g * y    
    
    #Berechnung der Kinietische Energie mit 1/2*m*(vx^2+vy^2)
    Ek= (m/2) * ((vx ** 2)+ (vy ** 2))
    
    #Berechnung der Energie der Teilchen 
    #Fall für mehrere Teilchen: 
    if N > 1:
       r= matrix[:,:2]
       
       rij_x= r[:,0][:, None] - r[:,0][None, :]
       rij_y= r[:,1][:, None] - r[:,1][None, :]
       
       rij= np.array([rij_x, rij_y])
       betrag= np.linalg.norm(rij)
       
       in_rij= 1 / betrag               #hier noch fehler ff.
       
       Et= (q ** 2) * np.sum(in_rij) 
    
    # Fall für ein Teilchen
    else:
       Et= 0.0
    
    #Berechnung der gesamten Energie
    E= np.sum(Eg + Ek) + Et
    
    return E
    
    
    
s1= np.array([1.0 ,45.0 ,10.0 ,0.0])
s2= np.array([99.0 ,55.0 ,-10.0, 0.0])
s3= np.array([10.0,50.0,15.0,-15.0])

print(E(s1,s2,s3))         
    