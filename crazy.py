import random
import string

pwd = ''
length = 10
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols
temp = random.sample(all, length)
pwd = "".join(temp)
print(pwd)