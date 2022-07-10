from random import randint


def calculate(number_1, number_2):
    min_number = min(number_1, number_2)
    max_number = max(number_1, number_2)
    if max_number % min_number == 0:
        return min_number

    for i in range(min_number // 2, 0, -1):
        if max_number % i == 0 and min_number % i == 0:
            return i


def main():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    question = str(number_1) + ' ' + str(number_2)
    correct_answer = str(calculate(number_1, number_2))
    return question, correct_answer
