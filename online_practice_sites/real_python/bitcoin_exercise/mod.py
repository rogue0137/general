# https://realpython.com/python-modules-packages/

s = "If Comrade Napoleon says it, it must be right."
a = [100,200,300]

def foo(arg):
    print(f'arg = {arg}')

class Foo:
    pass

if __name__ == '__main__':
    print('Executing standalone script')
    print(s)
    print(a)
    foo('quux')
    x = Foo()
    print(x)