from time import ticks_ms

class Tempo:
    def __init__(self, duree_ms):
        self.t_start = ticks_ms()
        self.duree_ms = duree_ms

    def fin(self):
        if ticks_ms() - self.t_start > self.duree_ms:
            self.reset()
            return True
        return False

    def reset(self):
        self.t_start = ticks_ms()