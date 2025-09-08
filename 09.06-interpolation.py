#!/usr/bin/env python3
# -*- coding: utf-8 -*-
   
def wo_durchquert(sn, sn1, grenzen, dt):
    """
    Routine die durch Interpolation mit 
    
    treffer= dt * ((Bel wand - Bel sn) / (Bel sn+1 - Bel sn))
    
    den neuen Zeitpunkt zurückgibt bevor das Teilchen die Box verlässt 

    Parameters
    ----------
    sn : 
        vorheriger Standort (Statevektor des Teilchens)
    sn1 :
        neuer  Standort (Statevektor des Teilchens)
    grenzen : 
        Boxgrenzen 
    dt : 
        Größe des Zeitschrittes
        
    Returns
    -------
    treffer:
        Zeitpunkt (float) bis zu dem das Teilchen in der Box ist 
    wand_gesucht:
        an welcher wand das Teilchen die Box trifft
        

    """
    xmin, xmax, ymin, ymax= grenzen
    
    treffer= None
    wand_gesucht= None
    
    #Gucken ob x-Grenze überschritten
    if sn1[0] < xmin:
        getroffen= dt * (xmin - sn[0]) / (sn1[0] - sn[0])
        if 0 <= getroffen <= dt:
            treffer, wand_gesucht= getroffen, "xmin"
            
    elif sn1[0] > xmax:
        getroffen= dt * (xmax - sn[0]) / (sn1[0] - sn[0])
        if 0 <= getroffen <= dt:
            treffer, wand_gesucht= getroffen, "xmax"
            
    #Gucken ob y-Grenze überschritten
    if sn1[1] < ymin:
        getroffen= dt * (ymin - sn[1]) / (sn1[1] - sn[1])
        if 0 <= getroffen <= dt and (treffer is None or getroffen < treffer):
            treffer, wand_gesucht= getroffen, "ymin"
            
    elif sn1[1] > ymax:
        getroffen= dt * (ymax - sn[1]) / (sn1[1] - sn[1])
        if 0 <= getroffen <= dt and (treffer is None or getroffen < treffer):
            treffer, wand_gesucht= getroffen, "ymax"
            
    return getroffen, wand_gesucht
            