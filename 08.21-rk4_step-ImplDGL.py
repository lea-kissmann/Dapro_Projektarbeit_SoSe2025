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
        if si is not args == True:      #nur si zu arg oder alle von einander?
            x_j= args[0]
            y_j= args[1]
            
            rij_x= si[0] - x_j
            rij_x += werte_rij_x
            
            rij_y= si[1] - y_j
            rij_y += werte_rij_y
        else:
            continue
    
    #WAS WENN NUR EIN TEILCHEN?
    
    #Zwischenspeicher des rij abhänigen Teils der elektrischen Abstoßung 
    sam_rij=[]
    
    #Berechnung zu Sammlung des rij abhänigen Teils der elektrischen Abstoßung
    for x, y in zip(werte_rij_x, werte_rij_y):
        rij= np.array([x ,y ,0 ,0])
        sum_rij= rij / ((abs(rij)) ** 3)
        sum_rij += sam_rij
    
    #Zwischenspeicher von den Summen der x-,y-,vx-,vy-Werte des 
    #rij abhänigen Teils der elektrischen Abstoßung
    sum_x= 0
    sum_y= 0
    sum_vx= 0
    sum_vy= 0
    
    #Loop der die einzelen gesammelten x-,y-,vx-,vy-Werte aufaddiert
    for vektor in sam_rij:
        sum_x += vektor[0]
        sum_y += vektor[1] 
        sum_vx += vektor[2] 
        sum_vy += vektor[3] 
        
    #Array aus den Summen des rij abhänigen Teils der elektrischen Abstoßung   
    elAbr= np.array([sum_x ,sum_y ,sum_vx ,sum_vy])
    
    #Elektrische Abstoßung 
    elAb= (q ** 2) * elAbr 
        
    #Ermittlung der r"-Werte für x und y, bzw. ax, ay des gegebenen Teilchens
    ai_x= m * 0 - elAb[0]
    ai_y= m * g - elAb[1]
    
    return np.array([ridot[0] ,ridot[1] ,ai_x ,ai_y])



def rk4_step(dgl, s, dt):   #ist dgl doch f? / was ist s? 
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


s1= np.array([1.0 ,45.0 ,10.0 ,0.0])
s2= np.array([99.0 ,55.0 ,-10.0, 0.0])

s1dot= f(s1,s2)
print(s1dot)
