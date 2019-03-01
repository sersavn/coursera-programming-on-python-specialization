#aim is to draw "ladder"

'''
import sys
num_steps = int(sys.argv[1])

python ladder.py 4

   #
  ##
 ###
####
'''

import sys
num_steps = int(sys.argv[1])

for i in range(1, num_steps+1):
    print(' ' * (num_steps - i) + '#' * i)
