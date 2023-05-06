#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    for i in range(1,11): # for loop funtion  it will multiply from 1 to 10 with integer "n"
        result = n * i # to get multiplied result
        print(n, "x", i, "=", result) # to show th e multiplication table
