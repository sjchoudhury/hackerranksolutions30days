#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here

   # there must be an indent Here
   tip = meal_cost/100*tip_percent

   tax = tax_percent/100*meal_cost

   total_cost = meal_cost+tip+tax
   total_cost = round(total_cost)
   # we're using round(total_cost) to convert decimanl number to non decimal number.
   # the original value is 15.36 but by using round(total_cost) we're converting them to a round number.
   print(total_cost)

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
