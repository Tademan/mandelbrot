
def mandela(x,y,limit=1000):
    a = x+y*1j
    b = 0
    for i in range(limit):
        b = b**2+a
        if b.imag**2+b.real**2>4:
            return i
    return 0
