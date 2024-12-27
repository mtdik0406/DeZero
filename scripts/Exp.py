from scripts.Function import Function
import numpy as np

class Exp(Function):
    def forword(self, x):
        return np.exp(x)
    
    def backward(self, gy):
        x = self.input.data
        gx = np.exp(x) * gy
        return gx