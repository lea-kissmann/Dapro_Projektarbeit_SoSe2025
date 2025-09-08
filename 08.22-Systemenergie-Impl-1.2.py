#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#erster Versuch die funktion der Systemenergie aufzustellen

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
        
        Ei= (- (m * g * y)) + ((m/2) * ((vx ** 2) + (vy ** 2)))
        sam_Ei.append(Ei)
        
        
    ij= []    
    for vektor in args:
        if vektor not in ij:
            ij.append(vektor)
            
    for array in ij:
        x_i= array[0]
        y_i= array[1]
            
            
            