import sys


def print_hi(name="sam", age=1):
    print(f'Hi, {name},i`m {age}')


if __name__ == '__main__':
    a1, a2 = sys.argv[1], sys.argv[2]
    print_hi(a1, a2)
