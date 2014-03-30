#!/usr/bin/env python
import random
from physics import *

player = PhysicsObject()
wall = PhysicsObject()

def init():
    def start():
        return play
    return {"play": start}

def play():
    def explode():
        print "EXPLODE"
        return win
    if player.is_colliding(wall):
        return {"explode": explode}

    return {"nothing": lambda : play}

def win():
    print "WIN"
    return None


def player1(actions):
    print "Available actions:"
    
    for act in actions:
        print act + " " + ' '.join(actions[act].func_code.co_varnames)
    take_action = raw_input("Pick:")
    action_name = take_action.split(' ')[0]
    args = take_action.split(' ')[1:]
    
    action = actions[action_name]
    return action, args


def AI(actions):
    if "play" in actions:
        return actions["play"], []
    else:
        return actions["nothing"], []


if __name__ == "__main__":
    state = init
    while state is not None:
        actions = state()
        if actions is None:
            break
        action, args = AI(actions)
        state = action(*args)
        
    print "Game Over"
    
            
            
