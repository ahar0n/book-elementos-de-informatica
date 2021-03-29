def hex2bin(x):
    pattern = ''
    for i in x:
        dec = hex2dec(i)
        pattern += dec2bin(dec)
    return pattern

def hex2dec(x):
    hexa = '0123456789ABCDEF'
    return hexa.index(x)

def dec2hex(x):
    hexa = '0123456789ABCDEF'
    return hexa[x]

def dec2bin(x, npattern=4):
    pattern = 0
    exp = 0
    while x > 0:
        rest = x % 2
        x //= 2
        pattern += rest * 10**exp
        exp += 1
    pattern = str(pattern)
    while len(pattern) < npattern:
        pattern = '0' + pattern
    return pattern

def word2charlist(word):
    chars = []
    for i in word:
        chars.append(i)
    return chars

def bin2dec(x):
    suma = 0
    exp = 0
    while len(x) > 0:
        suma += int(x[-1]) * (2**exp)
        x = x[0:-1]
        exp += 1
    return suma