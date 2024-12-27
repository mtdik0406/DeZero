class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None
        self.creator = None
        
    def set_creator(self, func):
        self.creator = func
        
    def backward(self):
        f = self.creator
        if f is not None:
            x = f.input # 関数の入力を取得
            x.grad = f.backward(self.grad) # 関数のbackwardメソッドを呼ぶ
            x.backward() # 自分より1つ前の変数のbackwardメソッドを呼ぶ（再帰）