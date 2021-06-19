#!/user/bin/env python
import sys

def double(number):
    return f'Here is your result: {number * 2}\n see you bro.'

# imput is always a string, you need to convert it to the correct data type
number =  int(sys.argv[1])
print(double(number))