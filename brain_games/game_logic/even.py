import prompt
from random import randint


def welcome_user():
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}')
    main(username)


def generate_number():
    """
    Generates random number in range 1...100,
    passes it to function is_even() and returns a tuple
    containing number and True/False for Even
    """

    number = randint(1, 100)
    number_is_even = is_even(number)
    correct_answer = number_is_even
    return number, correct_answer


def is_even(number):
    if number % 2 == 0:
        return "yes"
    return "no"


def main(username):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(0, 3):
        result = generate_number()
        (value, correct_answer) = result
        print(f'Question: {value}')
        answer = prompt.string('Answer: ')
        if answer.lower() == correct_answer:
            print('Correct!')
            continue
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            print(f'Let\'s try again, {username}!')
            return
    print(f'Congratulations, {username}')
