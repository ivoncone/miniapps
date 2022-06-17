import random
import string

password = ''

def new_password():

    length = 10
    pw = ''
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols

    temp = random.sample(all, length)
    pw = "".join(temp)

    return pw

print(new_password())

