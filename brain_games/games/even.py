from random import randint


def generate_number():
    """
    Generates random number in range 1...100,
    passes it to function is_even() and returns a tuple
    containing number and True/False for Even
    """

    number = randint(1, 100)
    correct_answer = is_even(number)
    return number, correct_answer


def is_even(number):
    if number % 2 == 0:
        return "yes"
    return "no"


def main():
    result = generate_number()
    return result


if __name__ == '__main__':
    main()
