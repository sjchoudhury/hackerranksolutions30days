

import math
import os
import random
import re
import sys



N = int(input())

if N%2 != 0:  # is to check the value of integer "N" is odd or not
    print("Weird")
else:
    if N>=2 and N<5: # for n between 2 to 5
        print("Not Weird")

    if N>=6 and N<=20:# for n between 6 to 20
        print("Weird")

    if N>20:
        print("Not Weird")
