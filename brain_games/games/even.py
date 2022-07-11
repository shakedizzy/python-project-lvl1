from random import randint


def is_even(number):
    if number % 2 == 0:
        return "yes"
    return "no"


def main():
    number = randint(1, 100)
    correct_answer = is_even(number)
    return number, correct_answer


if __name__ == '__main__':
    main()
