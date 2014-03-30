#!/usr/bin/env python

#game is a state machine, with event -> actions -> new state as edges
game = {}

class State:
    def __init__(self):
        self.events = []
    
    def on(self, event):
        self.events.append(event)

    def step(self):
        for e in self.events:
            if e.is_true():
                return e.action()


if __name__ == "__main__":
    current_state = State()
    final_states = [State()]
    
    while current_state not in final_states:
        current_state = current_state.step()
    

class GameKernel:
    players
    objects
    board
    possible moves
    
