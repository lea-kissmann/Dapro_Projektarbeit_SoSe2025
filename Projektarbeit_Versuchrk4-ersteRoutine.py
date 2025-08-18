#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Versuch die Runge-Kutta-Methode zu implementieren für zwei Teilchen im System

import numpy as np 

def f(si, sj):
    """
    Routine, die die entsprechende Differetialgleichung des gegebenen 
    Statevektors si aufbaut.

    Parameter
    ----------
    si : array --> Statevektor des ensprechenden Teilchens i
    sj : array --> Statevektor des ensprechenden Teilchens j

    Returns
    -------
    array -->  Ableitung des gegebenen si

    """
    
    #Parameter der DGL
    q= 50
    m= 1
    g= -10
    
    # r und rdot und rij und der elektrischen Abstoßung
    ri= np.array([si[0],si[1]])
    
    rj= np.array([sj[0],sj[1]])
    
    ridot= np.array([si[2],si[3]])
    
    rjdot= np.array([sj[2],sj[3]])
    
    rij= ri - rj
    
    eAb= (q**2) * (rij / (abs(rij) **3))
    
    # rddot
    ax= m * 0 - eAb[0]
    av= m * g - eAb[1]
    riddot= np.array([ax],[av])
    
    return np.array([ridot],[riddot])

def rk4_step(dgl, s, dt):
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


    
    
    
    
    
    
    
    