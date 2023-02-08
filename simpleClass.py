class ABC:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = 0

    def add(self):
        self.c = self.a + self.b
        return 4

obj1 = ABC(1, 2)
print(obj1.add())