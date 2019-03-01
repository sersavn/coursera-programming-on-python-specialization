# aim is to find roots of quadratic equation based on a,b,c coefficients

'''
python roots.py 1 -3 -4

-1 4
'''

import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

r1 = (-b + (b**2 - 4 * a * c)**(0.5))/2 * a
r2 = (-b - (b**2 - 4 * a * c)**(0.5))/2 * a

try:
    print(int(r1))
except:
    pass

try:
    print(int(r2))
except:
    pass
