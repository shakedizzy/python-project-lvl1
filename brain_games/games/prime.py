from random import randint
from math import sqrt


def is_prime(number):
    for i in range(2, int(sqrt(number) + 1)):
        if number % i == 0:
            return 'no'
    return 'yes'


def main():
    number = randint(1, 100)
    correct_answer = is_prime(number)
    return number, correct_answer


if __name__ == '__main__':
    main()
