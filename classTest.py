class A:
    def __init__(self, name):
        self.name = name

    def f(self):
        print('father' + self.name)


class B(A):
    def __init__(self, age):
        super(B, self).__init__('huhuhhrhrhr')
        self.age = age

    def f(self):
        print('son' + str(self.age))
        print('son' + self.name)


if __name__ == '__main__':
    a = A('huhuhr')
    b = B(18)
    a.f()
    b.f()
