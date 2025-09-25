import os 


with open('day3\input.txt', 'r') as file:
    s = file.read()

# Part one 

i = 0
sum_result = 0  # This will hold the sum of all valid multiplications
while i < len(s):
    if s[i:i+4] == 'mul(':
        a, b = '', ''
        i = i + 4
        # extract all of a
        while i < len(s) and s[i].isdigit():
            a = a + s[i]
            i = i + 1
        # see if comma is the next caracter after a is a string of digits
        if i < len(s) and s[i] == ',':
            i = i + 1
            # extract second number (b)
            while i < len(s) and s[i].isdigit():
                b = b + s[i]
                i = i + 1
            # if b is a string of digits, look for closing )
            if i < len(s) and s[i] == ')':
                if a != '' and b != '':
                    result = int(a) * int(b)
                    sum_result += result
                i = i + 1 
                continue 
    else:
        i = i + 1  # move to next character if not 'mul('

print("Final sum:", sum_result)

    
