import prompt
from brain_games.games import even, calc, gcd, prime, progression

GAMES = {
    'even': even.main,
    'calc': calc.main,
    'gcd': gcd.main,
    'progression': progression.main,
    'prime': prime.main
}

GAMES_DESCRIPTION = {
    'even': 'Answer "yes" if the number is even, otherwise answer "no".',
    'calc': 'What is the result of the expression?',
    'gcd': 'Find the greatest common divisor of given numbers.',
    'progression': 'What number is missing in the progression?',
    'prime': 'Answer "yes" if given number is prime. Otherwise answer "no".'
}


def play_games(game, username):
    for i in range(0, 3):
        result = GAMES[game]()

        (question, correct_answer) = result
        print(f'Question: {question}')
        answer = prompt.string('Answer: ')

        if answer.lower() == correct_answer.lower():
            print('Correct!')
            continue
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {username}!')
            return

    print(f'Congratulations, {username}!')


def main(game):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}')

    game_welcome_message = GAMES_DESCRIPTION[game]\
        if game in GAMES_DESCRIPTION else 'Game not found'
    print(game_welcome_message)
    play_games(game, username)


if __name__ == '__main__':
    main('even')
