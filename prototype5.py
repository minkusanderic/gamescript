#!/usr/bin/env python
import random

def init():
    def start():
        return play, [random.randint(1, 100), "below", 0]
    return {"play": start}

def play(target, last_guess, the_last):
    def guess(num):
        num = int(num)
        if num < target:
            return play, [target, "below", num]
        if num > target:
            return play, [target, "above", num]
        if num == target:
            return win, []

    return {"guess": guess}

def win():
    print "WIN"
    return None


def player1(actions, game_space):
    if "last_guess" in game_space:
        print game_space["last_guess"]

    print "Available actions:"
    
    for act in actions:
        print act + " " + ' '.join(actions[act].func_code.co_varnames)
    take_action = raw_input("Pick:")
    action_name = take_action.split(' ')[0]
    args = take_action.split(' ')[1:]
    
    action = actions[action_name]
    return action, args


lower_bound = 0
upper_bound = 100
current_guess = 0
def AI(actions, game_space):
    global current_guess
    global lower_bound
    global upper_bound
    if "play" in actions:
        return actions["play"], []
    else:
        if game_space["last_guess"] == "above":
            upper_bound = current_guess - 1
        else:
            lower_bound = current_guess + 1
        current_guess = random.randint(lower_bound, upper_bound)
        return actions["guess"], [current_guess]

def make_dot_graph(filename, trans):
    with open(filename, 'w') as f:
        f.write("digraph G {")

        for t in trans:
            f.write("\"{0}\" -> \"{1}\"\n".format(t[0], t[1]))
        
        f.write("}")


if __name__ == "__main__":
    state = init
    game_space = {}
    trans = set()
    last_state = '(init)'

    while state is not None:

        params = {}
        for v in state.func_code.co_varnames[:state.func_code.co_argcount]:
            params[v] = game_space[v]

        actions = state(**params)
        if actions is None:
            break

        action, args = AI(actions, game_space)

        state, params = action(*args)
        current_trans = (last_state,
                   str((state.__name__, tuple(params))))
        trans.add(current_trans)
        last_state = current_trans[1]

        for v in state.func_code.co_varnames[:state.func_code.co_argcount]:
            game_space[v] = params[0]
            params = params[1:]


    make_dot_graph("./graph.dot", trans)
    print "Game Over"
    
            
            
