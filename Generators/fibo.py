def fib():
    a=0
    b=1
    yield a 
    yield b
    while 1:
        c=a+b
        yield c
        a=b
        b=c

