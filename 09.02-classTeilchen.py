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
     
    #Rotine um die Ausgabe als Teiolchen zuermöglichen
    def __str__(self):
        return f"{self.s}"
    
    #Routine um die Geschwindigkeit abzufragen
    def geschwindigkeit(self):
         return self.v[2:]
    
    #Routine um die Position abzufragen
    def position(self):
        return self.p[:2]

    
    
     


