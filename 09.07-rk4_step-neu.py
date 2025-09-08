#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np 
from  konstanten import m, g, q 

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
    x, y, vx, vy= si
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



def rk4_step(f, s, dt, alle_teilchen, i):  #*args --> alle_teilchen
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