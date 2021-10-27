class HumanPlayer:

    @staticmethod
    def human_play(game):
        print('From function:\nHuman playing...')

        # checking the availables moves
        print(game.get_availables())
        while True:
            move = int(input('Select move:'))
            if move < 1 or move > 9 or not game.is_available(move):
                move = int(input('Invalide move:'))
            else:
                break

            print(f'move: {move}')

        return move

