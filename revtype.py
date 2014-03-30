#!/usr/bin/env python

class revint:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def less_than(self, val):
        return revint(self.a, min(self.b - 1, val))

    def greater_than(self, val):
        return revint(max(self.a + 1, val), self.b)

    def add(self, other):
        return revint(self.a + other.a, self.b + other.b)
    
    def __repr__(self):
        return "[{0}, {1}]".format(self.a, self.b)

x = 2
if x < 4:
    y = 4
