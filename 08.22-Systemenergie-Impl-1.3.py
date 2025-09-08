#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#erster Versuch die funktion der Systemenergie aufzustellen
import numpy as np


def E(*args):
    """
    

    Parameters
    ----------
    *args : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    #Parameter der Teilchen
    q= 50
    m= 1
    g= -10
    
    
    
    sam_Ei=[] 

    for index, vektor in enumerate(args):
        
        x= vektor[0]
        y= vektor[1]
        vx= vektor[2]
        vy= vektor[3]
        
        ri = np.array([x,y])
        
        Ei= (- (m * g * y)) + ((m/2) * ((vx ** 2) + (vy ** 2)))
        sam_Ei.append(Ei)
        
            
            
            
            