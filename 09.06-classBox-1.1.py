#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np

class Box:   # nochmal gucken ob jetzt rechnungen noch funktionieren --> liste überbergeben 
             # und nicht einzelne teilchen....
    
    """
    definiert die Klasse Box, welche die Umgebungsstruktur der Teilchen bildet.
    """
    
    #Routine um Box erstellen zu können
    def __init__(self, teilchen,  grenzen):     
        
        #Liste der übergebenen Teilchen 
        if teilchen is None:
            teilchen= []
        self.teilchen= teilchen 
        
        #Boxgrenzen setzten 
        self.grenzen= grenzen 
        
    #Routine bei der man prüft ob sich die Teilchen noch in der Box befinden 
    def in_box(self, grenzen):
        """
        prüft ob sich die in die Box gefügten Teilchen noch 
        innerhalb der Box befinden, oder ob sie die Grenzen überschritten haben

        Returns
        -------
        innen:  
            True:
                wenn die Teilchen sich noch in der Box befinden 
        
            False: 
                wenn die Teilchen außerhalb der Grenzen liegen 
        wand:
            "außerhalb dem x oder y Min- oder Maximum "
            je nach Grenzüberschreitung
            
        """
        xmin, xmax, ymin, ymax = grenzen
        wand= None
        innen= None
        
        for s in self.teilchen:
            
            #Seitenwände
            if s.p[0] <= self.xmin:
                 innen, wand= False, "außerhalb dem x-Minimum " 
                 
            elif s.p[0] >= self.xmax:
                innen, wand= False, "außerhalb dem x-Maximum "
                
            else:
                innen,wand= True, None
            
            #Ober-/Unterseite
            if s.p[1] <= self.ymin:
                innen,wand= False, "außerhalb dem y-Minimum "
                
            elif s.p[1] >= self.ymax:
                innen, wand= False, "außerhalb dem y-Maximum "
                
            else:
                 innen, wand= True, None
         
        return innen, wand
    