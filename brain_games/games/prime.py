from random import randint
from math import sqrt


def generate_number():
    """
    Generates random number in range 1...100,
    passes it to function is_even() and returns a tuple
    containing number and True/False for Even
    """

    number = randint(1, 100)
    correct_answer = is_prime(number)
    return number, correct_answer


def is_prime(number):
    for i in range(2, int(sqrt(number) + 1)):
        if number % i == 0:
            return 'no'
    return 'yes'


def main():
    result = generate_number()
    return result


if __name__ == '__main__':
    main()
