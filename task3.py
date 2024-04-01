import random
import string

symbols = string.ascii_letters + string.digits

password = ("".join(random.choice(symbols) for _ in range(10)))
print(password)
