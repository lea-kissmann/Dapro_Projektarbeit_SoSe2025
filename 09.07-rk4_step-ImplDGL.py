#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Versuch der Implementierung der Runge-Kutta-Methode

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
    r_i= np.array([x,y])
    ridot= np.array([vx, vy])
    
    #Zwischenspeicher der rij-Werte für x und y 
    werte_rij_x= []
    werte_rij_y= []
    
    #Zwischenspeicher des rij abhänigen Teils der elektrischen Abstoßung 
    sam_rij=[]
    
    #Zwischenspeicher von den Summen der x-,y-,vx-,vy-Werte des 
    #rij abhänigen Teils der elektrischen Abstoßung
    sum_x= 0.0
    sum_y= 0.0
    
    for j, sj in enumerate(alle_teilchen):
        if j== i:
            ai_x= m * 0.0 - 0.0
            ai_y= m * g - 0.0
        else:
        #loop um die rij-Werte ermitteln zu können zwischen 
        #dem gegebenen Teilchen si und den beliebig vielen Teilchen des Systems
            x_j= sj[0]
            y_j= sj[1]
            
            rij_x= si[0] - x_j
            werte_rij_x.append(rij_x) 
            
            rij_y= si[1] - y_j
            werte_rij_y.append(rij_y)
        
        #Berechnung zu Sammlung des rij abhänigen Teils der elektrischen Abstoßung
        for x, y in zip(werte_rij_x, werte_rij_y):
            rij= np.array([x ,y])
            betrag= np.linalg.norm(rij)
            sum_rij= rij / (betrag ** 3)
            sam_rij.append(sum_rij) 
        
        #Loop der die einzelen gesammelten x-,y-,vx-,vy-Werte aufaddiert
        for vektor in sam_rij:
            sum_x += vektor[0]
            sum_y += vektor[1] 
            
        #Array aus den Summen des rij abhänigen Teils der elektrischen Abstoßung   
        elAbr= np.array([sum_x ,sum_y ,0 ,0])
        
        #Elektrische Abstoßung 
        elAb= (q ** 2) * elAbr 
            
        #Ermittlung der r"-Werte für x und y, bzw. ax, ay des gegebenen Teilchens
        ai_x= m * 0.0 - elAb[0]
        ai_y= m * g - elAb[1]
    
    #Finale Ableitung des gegebenen Teichens si
    sdot= np.array([ridot[0], ridot[1], ai_x, ai_y])
    return sdot



def rk4_step(f, s, dt, *args):  #*args --> alle_teilchen
    """
    Routine, die einen einzelen Schritt eines Teilchens berechenet 

    Parameter
    ----------
    f : Die Differentialgleichung des Teilchens
    
    s : Statevektor des Teilchen an diskretem Punkt
    
    dt : Zeitschritt

    Returns
    -------
    array--> Nächster Statevektor des gebeben Teilchen s

    """
    #Runge-Kutta-Koeffizienten
    k1= dt * f(s, args)
    k2= dt * f(s + (0.5 * k1), args)
    k3= dt * f(s + (0.5 * k2), args)
    k4= dt * f(s + k3, args)
    
    #Nächster Punkt des angegebenen Teilchens s
    step= s + (k1 / 6) + (k2 / 3) + (k3 / 3) + (k4 / 6)
    return step


s1= np.array([1.0 ,45.0 ,10.0 ,0.0])
s2= np.array([99.0 ,55.0 ,-10.0, 0.0])
s3= np.array([10.0,50.0,15.0,-15.0])

s1dot= f(s1,s2)
print(s1dot)
