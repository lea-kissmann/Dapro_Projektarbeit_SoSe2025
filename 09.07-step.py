#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def step(teilchen_sam, box, dt):
    neue_states= []
    alle_teilchen= [t.s.copy() for t in teilchen_sam]
    
    for i, state in enumerate(teilchen_sam):
        state_neu= rk4_step(f, t.s, dt, alle_teilchen, i)
        if in_box(state_neu) == True:
            neue_states.append(state_neu)
        else:
           getroffen, wand_gesucht= wo_durchquert(state, state_neu, grenzen , dt)
           state_final= reflektieren(state, rk4_step, f, dt, grenzen, alle_teilchen, i)
           neue_states.append(state_final)
           
    for teilchen, state in zip(teilchen_sam, neue_states):
        t.s= s
        
    
        