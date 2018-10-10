import numpy as np

class BanditArm:
    def __init__(self, mean = 0, variance = 1):
        self.mean = mean
        
    def draw(self):
        return np.random.normal(self.mean, self.variance)