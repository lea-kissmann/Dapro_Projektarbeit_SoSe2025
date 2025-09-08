#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np 

class Teilchen:
    
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
         return self.s[2:]
    
    #Routine um die Position abzufragen
    def position(self):
        return self.s[:2]

    
    
     


