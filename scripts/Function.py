from scripts.Variable import Variable

class Function:
    def __call__(self, input):
        # input が Variable のインスタンスであることを仮定
        x = input.data
        y = self.forword(x)
        output = Variable(y)
        
        output.set_creator(self)
        self.input = input
        self.output = output
        
        return output

    def forword(self, x):
        raise NotImplementedError()

    def backward(self, gy):
        raise NotImplementedError()