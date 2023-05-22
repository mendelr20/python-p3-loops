#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(f"{i}")
        i -= 1
    print("Happy New Year!")
        

def square_integers(int_list):
    square_integers = []
    for x in int_list:
        square_integers.append( x * x)
    return square_integers

def fizzbuzz():
    i = 1
    while i < 101:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            i += 1
        elif i % 3 == 0:
            print("Fizz")
            i += 1
        elif i % 5 == 0:
            print("Buzz")
            i += 1
        else:
            print(f"{i}")
            i += 1
