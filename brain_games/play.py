import prompt
import brain_games.games.even
import brain_games.games.calc
import brain_games.games.gcd
import brain_games.games.progression


games_description = {
    'even': 'Answer "yes" if the number is even, otherwise answer "no".',
    'calc': 'What is the result of the expression?',
    'gcd': 'Find the greatest common divisor of given numbers.',
    'progression': 'What number is missing in the progression?'
}


def play_games(game, username):
    for i in range(0, 3):
        if game == 'even':
            result = brain_games.games.even.main()
        elif game == 'calc':
            result = brain_games.games.calc.main()
        elif game == 'gcd':
            result = brain_games.games.gcd.main()
        elif game == 'progression':
            result = brain_games.games.progression.main()
        else:
            return

        (question, correct_answer) = result
        print(f'Question: {question}')
        answer = prompt.string('Answer: ')

        if answer.lower() == correct_answer.lower():
            print('Correct!')
            continue
        else:
            print(f'"{answer}" is wrong answer ;(. \
Correct answer was "{correct_answer}".')
            print(f'Let\'s try again, {username}!')
            return

    print(f'Congratulations, {username}')


def main(game):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}')

    game_welcome_message = games_description[game]\
        if game in games_description else 'Game not found'
    print(game_welcome_message)
    play_games(game, username)


if __name__ == '__main__':
    main('even')
