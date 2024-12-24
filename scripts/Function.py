from scripts.Variable import Variable

class Function:
    def __call__(self, input):
        # input が Variable のインスタンスであることを仮定
        x = input.data
        y = x ** 2
        output = Variable(y)
        return output
