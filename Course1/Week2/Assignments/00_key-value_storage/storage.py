# creation of key-value storage with reading and writing

'''
Writing of the value according to the key
> storage.py --key key_name --val value_1

Reading in case if key is single
> storage.py --key key_name
value_1

Writing of the additional value to the same key. Order of writing matters.
> storage.py --key key_name --val value_2

Reading in case of multiple keys
> storage.py --key key_name
value_1, value_2
'''


import os
import json
import argparse
import tempfile

# creating file if not created
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if storage_path == False:
    with open(storage_path, 'w') as f:
        f.close()

#  creating dictionary or retrieving dictionary content
def dict_creation():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", type = str)
    parser.add_argument("--val")
    args = parser.parse_args()
    the_dict = dict()
    if args.key and args.val:
        the_dict[args.key] = [args.val]
    elif args.key:
        try:
            print(*reading()[args.key], sep=", ")
        except:
            print('None')
    return the_dict

# reading data from file
def reading():
    with open(storage_path, 'r') as f:
        result = json.loads(f.read())
        return result

# combining initial_dict from file and new one
try:
    initial_dict = reading()
except:
    initial_dict = dict()
updated_dict = dict_creation()
for k,v in updated_dict.items():
    if k in initial_dict:
        if v[0] not in initial_dict[k]:
            merged_list = initial_dict[k] + v
            updated_dict[k] = merged_list
        else:
            updated_dict[k] = initial_dict[k]
initial_dict.update(updated_dict)
with open(storage_path, 'w') as f:
    json_out = json.dumps(initial_dict)
    f.write(json_out)
