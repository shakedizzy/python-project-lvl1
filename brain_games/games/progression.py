from random import randint


def generate_progression():
    start_number = randint(1, 20)
    step = randint(3, 15)
    numbers_list = [str(start_number)]
    current_number = start_number + step
    for i in range(1, 10):
        numbers_list.insert(i, str(current_number))
        current_number += step
    return numbers_list


def secure_progression(ar_progression):
    position = randint(0, 9)
    modified_number = ar_progression[position]
    ar_progression[position] = '..'
    return ar_progression, modified_number


def main():
    ar_progression = generate_progression()
    result = secure_progression(ar_progression)
    (secret_list, correct_answer) = result
    question = " ".join(secret_list)
    return question, correct_answer


if __name__ == '__main__':
    main()
