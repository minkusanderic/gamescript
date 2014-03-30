#!/usr/bin/env python
import random

def init(game_space):
    game_space = {"target": random.randint(1,100), "last_guess": "below"}
    def start():
        return play, game_space
    return {"play": start}

def play(game_space):
    target = game_space["target"]
    def guess(num):
        num = int(num)
        if num < target:
            game_space["last_guess"] = "below"
            print "Below"
        if num > target:
            game_space["last_guess"] = "above"
            print "Above"
        if num == target:
            return win, game_space
        return play, game_space

    return {"guess": guess}

def win(game_space):
    print "WIN"
    return None


def player1(actions, game_space):
    print "Available actions:"
    
    for act in actions:
        print act + " " + ' '.join(actions[act].func_code.co_varnames)
    take_action = raw_input("Pick:")
    action_name = take_action.split(' ')[0]
    args = take_action.split(' ')[1:]
    
    action = actions[action_name]
    return action, args


current_guess = 0
def AI(actions, game_space):
    global current_guess
    if "play" in actions:
        return actions["play"], []
    else:
        if game_space["last_guess"] == "above":
            current_guess = current_guess - 1
        else:
            current_guess = current_guess + 1
        return actions["guess"], [current_guess]



if __name__ == "__main__":
    state = init
    game_space = None
    while state is not None:
        actions = state(game_space)
        if actions is None:
            break

        action, args = player1(actions, game_space)

        state, game_space = action(*args)
        
    print "Game Over"
    
            
            
