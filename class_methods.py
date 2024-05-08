# What will the code below output? Why?

class A:

    b = None

    def __init__(self):
        self.c = None

    @classmethod
    def set_c(cls, value):
        cls.c = value

    def set_b(self, value):
        self.b = value

inst_A = A()
inst_B = A()

inst_A.set_c(5)
inst_A.set_b(3)

inst_B.set_c(10)
inst_B.set_b(8)

print(inst_A.c)
print(inst_A.b)

print(inst_B.c)
print(inst_B.b)