import prompt
import brain_games.games.even

games_description = {
    'even': 'Answer "yes" if the number is even, otherwise answer "no".',
}


def play_games(game):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}')

    game_welcome_message = games_description[game] if game in games_description else 'Game not found'
    print(game_welcome_message)

    for i in range(0, 3):
        if game == 'even':
            result = brain_games.games.even.main()

        (question, correct_answer) = result
        print(f'Question: {question}')
        answer = prompt.string('Answer: ')

        if answer.lower() == correct_answer.lower():
            print('Correct!')
            continue
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            print(f'Let\'s try again, {username}!')
            return

    print(f'Congratulations, {username}')
