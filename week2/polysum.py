from math import pi as pi, tan as tan
def polysum(n, s):
    return round((0.25 * n * s * s) / tan(pi / n) + (s * n)**2, 4)
print(polysum(52, 79))