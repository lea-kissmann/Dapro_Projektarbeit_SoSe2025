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
    matrix= np.array(args)
    
    #N ist die Anzahl der angegebenen Teilchen
    N= matrix.shape[0]
    
    #Sammlung der x-, y-, vx-, vy-Werte aller angegebenen Teilchen 
    x, y, vx, vy = [], [], [], []
    
    #loop der die Werte aus den Vektoren extrahiert und den Sammlungen übergibt
    for werte in matrix :
        x_i, y_i, vx_i, vy_i= werte 
        x.append(x_i)
        y.append(y_i)
        vx.append(vx_i)
        vy.append(vy_i)
        
    
        
    