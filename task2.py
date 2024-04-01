import random
import string


def gen_password(length=5):
    symbols = string.ascii_letters + string.digits + string.punctuation
    while True:
        yield "".join(random.choice(symbols) for _ in range(length))


if __name__ == '__main__':
    password = gen_password(10)
    print(next(password))
