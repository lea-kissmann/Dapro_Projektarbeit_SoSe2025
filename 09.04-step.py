#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def step(box, rk4_step, f ,dt):
    neue_states= []
    alle_teilchen= [teilchen.state() for t in box.teilchen]
    

    for index, t in enumerate(box.teilchen):
        sdot= rk4_step(f, teilchen.state() , dt, alle_teilchen)
        if sdot.in_box == True:
            neue_states.append(sdot)
        else:
            reflextion und reflextion.append(sdot)
            
    for t, sdot in zip(box.teilchen, neue_states):
        t.state_neu(sdot)
        
        