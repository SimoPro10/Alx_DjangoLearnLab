# generate_secret_key.py
import random
import string

print(''.join(random.choice(string.ascii_letters + string.digits) for i in range(50)))
