#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np 

class Teilchen:
    """
    definiert die Klasse Teilchen, welche auf Basis von Statevektoren existiert.
    """
    
    #Routine um Teilchen erstellen zu können
    def __init__(self, x, y ,vx ,vy):
        self.s= np.array([x, y, vx, vy], dtype= float)
    
    #Routie um Teilchen neu anlegen zu können        
    def __repr__(self):
        return f"Teilchen:[{str(self.x)} , {str(self.y)}, {str(self.vx)} , {str(self.vy)}]"
     
    #Rotine um die Ausgabe als Teilchen zuermöglichen
    def __str__(self):
        return f"{self.s}"
    
    #Routinen um die Geschwindigkeit abzufragen und zu überschreiben
    @property
    def v(self):
         return self.v[2:]
    
    @v.setter
    def v(self, value):
         self.v[2:]= value
         
    #Routine um die Position abzufragen und zu überschreiben 
    @property
    def p(self):
        return self.p[:2]
    
    @p.setter
    def p(self, value):
        self.p[:2]= value 
        
    #Routine um Zustand zurück zu geben
    def state(self):
        return self.s
    
    #Routine um neuen Zustand zu übergeben
    def state_neu(self, s_neu):
        self.s= np.array(s_neu)
        

     


