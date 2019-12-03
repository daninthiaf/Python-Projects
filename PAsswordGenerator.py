#imported libraries
import random
import string
import hashlib

#SSHA algorithm
def hash_password(password):
    Salt = ''.join(
        [random.choice(string.ascii_letters + string.digits) for n in xrange(10)])

    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

#hashed password
def hashedPW(hashed_password):
    Password, Salt = hashed_password.split('-')
    return password

#salted password
def getSalt(hashed_password):
    Password, Salt = hashed_password.split('-')
    return Salt


# username 
userName = raw_input('Enter your username: ')
# password 
Password = raw_input('Enter a password: ')
# compute hashed and salted password and concatenate
hashedPassword = hashPassword(password)
print('SSHA password concatenation complete.')

# write info to pwd.txt
pwdTXT = open("pwd.txt", "w")
pwdTXT.write(userName + ',' + getSalt(hashed_password) + ',' + hashedPW(hashedPassword))
