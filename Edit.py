class A():
    def __init__(self) -> None:
        pass
    def foo(self, b, c):
        self.bc = b+c
        print('b \ c -',b,' ',c)

a = A()
a.foo(1,2)
print(a.bc)
