#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Versuch der Implementierung der Runge-Kutta-Methode

import numpy as np 

def f(si, *args):
    """
    Routine, die die entsprechende Differetialgleichung des gegebenen 
    Statevektors si aufbaut und den Abgeleiteten Statevektor wiedergibt.

    Parameter
    ----------
    si : array --> Statevektor des ensprechenden Teilchens si
    args : array --> Statevektoren der restlichen Teilchens 

    Returns
    -------
    array -->  Ableitung des gegebenen si Teilchens

    """
    #Parameter der DGL
    q= 50
    m= 1
    g= -10
    
    # r und rdot vom gegebenen Teilchen 
    ri= np.array([si[0],si[1]])
    ridot= np.array([si[2],si[3]])
    
    #Zwischenspeicher der rij-Werte für x und y 
    werte_rij_x= []
    werte_rij_y= []
    
    #loop um die rij-Werte ermitteln zu können zwischen 
    #dem gegebenen Teilchen si und den beliebig vielen Teilchen des Systems
    for arg in args:
        if si != args:
            x_j= args[0]
            y_j= args[1]
            
            rij_x= si[0] - x_j
            rij_x += werte_rij_x
            
            rij_y= si[1] - y_j
            rij_y += werte_rij_y
        else:
            continue
    
    #Zweichenspeicher des rij-Werte abhänigen Teil der elektischen Abstoßung 
    sum_eAb_x= []
    sum_eAb_y= []
    
    #Berechnung des rij-abhänigen Teils der el. Abstoßung in x- und y-Richtung 
    for xwert in werte_rij_x:
        eAb_x= xwert / ((abs(xwert)) ** 3 )
        sum_eAb_x += eAb_x
        
    for ywert in werte_rij_y:
        eAb_y= ywert / ((abs(ywert)) ** 3 )
        sum_eAb_y += eAb_y
    
    #Ermittlung der r"-Werte für x und y, bzw. ax, ay des gegebenen Teilchens
    ai_x= m * 0 - ((q ** 2) * sum(sum_eAb_x))
    ai_y= m * g - ((q ** 2) * sum(sum_eAb_y))
    
    return np.array([ridot[0]],[ridot[1]],[ai_x], [ai_y])



def rk4_step(dgl, s, dt):   #ist dgl doch f?
    """
    Routine, die einen einzelen Schritt eines Teilchens berechenet 

    Parameter
    ----------
    dgl : Die Differentialgleichung des Teilchens
    
    s : Statevektor des Teilchen an diskretem Punkt
    
    dt : Zeitschritt

    Returns
    -------
    array--> Nächster Statevektor des gebeben Teilchen s

    """
    #Runge-Kutta-Koeffizienten
    k1= dt * f(s)
    k2= dt * f(s + (0.5 * k1))
    k3= dt * f(s + (0.5 * k2))
    k4= dt * f(s + k3)
    
    return s + (k1 / 6) + (k2 / 3) + (k3 / 3) + (k4 / 6)


    
    
    
    
    
    
    
    