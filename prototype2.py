#!/usr/bin/env python
import random

def init():
    def start():
        return play
    return {"play": start}

def play():
    target = 50
    def guess(num):
        num = int(num)
        if num < target:
            print "Below"
        if num > target:
            print "Above"
        if num == target:
            return win
        return play

    return {"guess": guess}

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
        return actions["guess"], [random.randint(1,100)]


if __name__ == "__main__":
    state = init
    while state is not None:
        actions = state()
        if actions is None:
            break

        action, args = player1(actions)

        state = action(*args)
        
    print "Game Over"
    
            
            
