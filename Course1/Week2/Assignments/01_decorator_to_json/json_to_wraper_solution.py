# Write a decorator applicable to different functions \
# in order to convert its output to JSON format

# soulution

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

import functools
import json


def to_json(func):

    @functools.wraps(func)
     #*args and **kwargs gives ability to apply wraper to any function
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapped
