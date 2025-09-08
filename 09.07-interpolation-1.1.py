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
#
#           
def reflektieren(teilchen, rk4_step, f, sn, dt, grenzen, alle_teilchen, i): #BRAUCHT MAN SN??????
    """
    Routine um die Reflextion der Teilchen an den Boxwänden herzustellen 

    Parameters
    ----------
    teilchen : 
        das entsprechende Teilchen
    rk4_step : 
        Routine um nächsten Schritt zu berechen 
    f : 
        Routine um Statevektor abzuleiten
    sn : 
        momentane Statevektor des Teilchens 
    dt : 
        Zeitschritt
    grenzen : 
        Boxgrenzen
    alle_Teilchen : 
        restlichen Teilchen des Systems 
    i:
        Index

    Returns
    -------
    neu_final_state:
        der wenn nötig überarbeitete Statevektor

    """
    #Genereller Stand des Teilchens bisher
    alter_state= teilchen.state()
    position_alt= alter_state[:2]
    
    #Berechnung neuer Stand
    neuer_state= rk4_step(f, alter_state, dt, alle_teilchen, i)
    position_neu= neuer_state[:2]
    
    #Testen ob Teilchen nach Zeit in Box geblieben ist 
    
    innen, wand= in_box(position_neu)
    treffer, wand_getroffen= wo_durchquert(position_alt, position_neu, grenzen, dt)
    
    if innen == True or treffer is None:
        neu_final_state= neuer_state
    else:
        state_bis_wand= rk4_step(f, alter_state, treffer, alle_teilchen, i) #index sache anpassen !!!!!
        
    #Spiegelung der Betroffenen Werte
        if wand_getroffen in ("xmin", "xmax"):
            state_bis_wand[2] *= -1 
        if wand_getroffen in ("ymin", "ymax"):
            state_bis_wand[3] *= -1
            
    #Rest des Zeitschrittes ausführen 
        dt_rest= dt - treffer
        alle_teilchen[i]= state_bis_wand
        neu_final_state= rk4_step(f, state_bis_wand, dt_rest, alle_teilchen, i)
        
    return neu_final_state
        
            
    



