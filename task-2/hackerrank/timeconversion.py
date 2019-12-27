#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    t = s[8:10]
    p = ''
    if t == 'AM':
        if s[0:2] == '12':
            p += '00' + s[2:8]
        else:
            p += s[0:8]
    else:
        if s[0:2] == '01':
            p += '13' + s[2:8]
        if s[0:2] == '02':
            p += '14' + s[2:8]
        if s[0:2] == '03':
            p += '15' + s[2:8]
        if s[0:2] == '04':
            p += '16' + s[2:8]
        if s[0:2] == '05':
            p += '17' + s[2:8]
        if s[0:2] == '06':
            p += '18' + s[2:8]
        if s[0:2] == '07':
            p += '19' + s[2:8]
        if s[0:2] == '08':
            p += '20' + s[2:8]
        if s[0:2] == '09':
            p += '21' + s[2:8]
        if s[0:2] == '10':
            p += '22' + s[2:8]
        if s[0:2] == '11':
            p += '23' + s[2:8]
        if s[0:2] == '12':
            p += '12' + s[2:8]

    return p

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
