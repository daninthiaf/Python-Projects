#imported libraries
import time
import hashlib
import string
from brute import brute


# read from pwd.txt
f = open("pwd.txt", "r")
pwd = f.read()
username, salt, hashed_password = pwd.split(',')

#pick a brute algorithm
Options = raw_input(
    'Pick from choices 1, 2, 3, 4 to use for brute. \n')

#option 1
if Options == '1':
    count = 0
    start = time.time()
    for s in brute(length = 3, letters = True, numbers = False, symbols = False):
        if s.islower():
            count += 1
            if hashlib.sha256(salt.encode() + s.encode()).hexdigest() == hashed_password:
                end = time.time()
                print('Password found: ' + s)
                print('Attempts: ')
                print(count)
                print('Runtime:')
                print(end-start)
                continue
#option 2        
if Options == '2':
    count1 = 0
    start = time.time()
    for s in brute(length = 3, letters = True, numbers = False, symbols = False):
        count1 += 1
        if hashlib.sha256(salt.encode() + s.encode()).hexdigest() == hashed_password:
            end = time.time()
            print('Password found: ' + s)
            print('Attempts: ')
            print(count1)
            print('Runtime:')
            print(end-start)
            continue
#option 3
if Options == '3':
    count2 = 0
    start = time.time()
    for s in brute(length = 3, letters = True, numbers = True, symbols = False):
        count2 += 1
        if hashlib.sha256(salt.encode() + s.encode()).hexdigest() == hashed_password:
            end = time.time()
            print('Password found: ' + s)
            print('Attempts: ')
            print(count2)
            print('Runtime:')
            print(end-start)
            continue
#option 4
if Options == '4':
    count3 = 0
    start = time.time()
    for s in brute():
        count3+= 1
        if hashlib.sha256(salt.encode() + s.encode()).hexdigest() == hashed_password:
            end = time.time()
            print('Password found: ' + s)
            print('Attempts: ')
            print(count3)
            print('Runtime:')
            print(end-start)
            continue
