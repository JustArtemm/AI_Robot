import os
import json
import sys

def get_config(path):
    with open(path, 'r') as f:
        return json.load(f)
    
def dump_config(path, config):
    with open(path, 'w') as f:
        json.dump(config, f, indent=4)

def get_input():
    return input("User: ")



