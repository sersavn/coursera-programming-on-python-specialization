# Write a decorator applicable to different functions \
# in order to convert its output to JSON format

'''
example of wraper application:

@to_json
def get_data():
  return {
    'data': 42
  }

get_data()

'{"data": 42}'
'''

import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs): #(check )
        result = func(*args, **kwargs)
        result_dumps = json.dumps(result)
        return result_dumps
    return wrapped
