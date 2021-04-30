#!/usr/bin/env python3
import crayons
# range is required because an int cannot be looped
for fb in range(1,101):
    if (fb % 3) == 0 and (fb % 5) == 0:
        print('{} {}'.format(crayons.white(fb), crayons.yellow('FizzBuzz')))
    elif(fb % 3) == 0:
        print('{} {}'.format(crayons.white(fb), crayons.red('Fizz')))
    elif (fb % 5) == 0:
        print('{} {}'.format(crayons.white(fb), crayons.blue('Buzz')))
    else:
        print('{}'.format(crayons.white(fb)))


