#!/usr/bin/env python

class player:
    def can(self, action):
        pass
    def will(self, action):
        pass


def win(state):
    print "WIN"
    return None

def lose(state):
    print "LOSE"
    return None

def play(state):
    choice = raw_input("Lets Play!:")
    if choice == "Hello":
        state["score"] = state["score"] + 1

    if state["score"] >= 3:
        return win
    return play

def initial(state):
    print "INITIAL"
    return play

def run_game(state, env):
    while state != None:
        state = state(env)

if __name__=="__main__":
    run_game(initial, {"score": 0})
