# random password generator

import random
import string
import os
import subprocess

if __name__ == '__main__':
    random_pass = ''
    for ii in range(1):
        random_pass = ''
        for i in range(25):
            random_pass += ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation)])
        print(random_pass)
