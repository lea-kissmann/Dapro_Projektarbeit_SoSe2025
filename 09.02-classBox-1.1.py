#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np

class Box:
    
    """
    definiert die Klasse Box, welche die Umgebungsstruktur der Teilchen bildet.
    """
    
    #Routine um Box erstellen zu können
    def __init__(self, teilchen,  xmin= 0, ymin= 0, xmax= 100, ymax= 100):
        
        #Liste der übergebenen Teilchen 
        if teilchen is None:
            teilchen= []
        self.teilchen= teilchen 
        
        #Boxgrenzen 
        self.xmin, self.xmax= xmin, xmax
        self.ymin, self.ymax= ymin, ymax
        
    def in_box(self):
        
        for s in self.teilchen:
            
            if s.p <= self.xmin:
                return False, f"Teilchen {s} ist außerhalb dem x-Minimum " #vielleicht dict fü abfrage im code später?
            elif s.p >= self.xmax:
                return False, f"Teilchen {s} ist außerhalb dem x-Maximum "
            else:
                return True 
            
            if s.p <= self.ymin:
                return  False, f"Teilchen {s} ist außerhalb dem y-Minimum "
            elif s.p >= self.ymax:
                return False, f"Teilchen {s} ist außerhalb dem y-Maximum "
            else:
                return True
                
        
    