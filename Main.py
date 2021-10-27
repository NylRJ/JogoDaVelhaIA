from jogo_velha.Computer import Computer
from jogo_velha.Game import Game
from jogo_velha.HumanPlayer import HumanPlayer
import numpy as np


def main():
    print('Running ok!')
    board = np.array([[1, -1, 1], [-1, 1, -1], [1, -1, 1]])
    game = Game()  # board=board)
    player = 1  # human play
    computer = Computer(algorithm='Minimax')
    game_over = False

    while not game_over:
        game.print_game()
        if player == 1:
            print('Player 1')
            game.play_move(HumanPlayer.human_play(game), player)
        if player == -1:
            print('Player 2')
            print(game.board)
            game.play_move(computer.play(game.board), player)

        game_over = game.is_terminal()

        player = -player

    print(f'Fim de jogo.\nGanhador: {game.winner}\n{game.score}')
    game.print_game()


if __name__ == '__main__':
    main()
