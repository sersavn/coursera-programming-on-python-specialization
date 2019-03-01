# aim is to find sum of digits in input str

'''
import sys
digit_string = sys.argv[1]

python solution.py 873

18
'''

import sys

digit_string = sys.argv[1]

result = 0
for i in digit_string:
    result += int(i)
print(result)
