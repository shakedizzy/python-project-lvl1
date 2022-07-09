import operator
from random import choice, randint


allowed_operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def calculate_exp():

    operand_1 = randint(1, 50)
    operand_2 = randint(1, 50)
    operation = choice(list(allowed_operators.keys()))

    expr = str(operand_1) + ' ' + operation + ' ' + str(operand_2)
    print(expr)
    correct_answer = str(allowed_operators[operation](operand_1, operand_2))
    return expr, correct_answer


def main():
    result = calculate_exp()
    return result
