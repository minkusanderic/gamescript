
class PhysicsObject:
    def __init__(self):
        self.position = (0, 0)
        self.velocity = (0, 0)

    def is_colliding(self, other):
        return False
