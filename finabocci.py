
def fiboncci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

class Fibonacci:
    '''iterator that yields numbers in the Fibonacci sequence'''

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

for n in fiboncci(100):
    print(n, end = " ")

for n in Fibonacci(100):
    print(n, end = " ")