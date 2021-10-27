import random, copy
import numpy as np


class Computer:

    def __init__(self, algorithm='Random'):

        self.algorithm = algorithm

    def get_availables(self, board):
        return np.where(board.flatten() == 0)[0] + 1

    def is_terminal(self, board):

        score = 0
        game_over = 0
        winner = 0

        # verificando se o jogador 1 venceu
        if any(np.sum(board, axis=0) == 3) or \
                any(np.sum(board, axis=1) == 3) or \
                sum(np.diag(board)) == 3 or \
                sum(np.diag(board[::-1])) == 3:

            game_over = True
            winner = 1
            score = (len(self.get_availables(board)) + 1)

        # verificando se o jogador 2 venceu
        elif any(np.sum(board, axis=0) == -3) or \
                any(np.sum(board, axis=1) == -3) or \
                sum(np.diag(board)) == -3 or \
                sum(np.diag(board[::-1])) == -3:

            game_over = True
            winner = -1
            score = -(len(self.get_availables(board)) + 1)

        # verificando se houve empate
        else:
            if len(self.get_availables(board)) == 0:
                score = 0
                game_over = True
                winner = 0

            else:
                score = 0
                game_over = False
                winner = 0

        return game_over, score, winner

    def play_move(self, board, move, player):

        if move is not None:
            board_flat = board.flatten()
            board_flat[move - 1] = player
            board = np.reshape(board_flat, (board.shape[0], board.shape[1]))

        return board

    def play(self, game):
        print('From class:\nComputer playing...')

        if self.algorithm == 'Random':
            print('Random game')
            return self.random(game)

        if self.algorithm == 'Minimax':
            return self.minimax(game)

        if self.algorthm == 'Alpha_Beta':
            return self.alpha_beta()

        if self.algorthm == 'MonteCarlo':
            return self.montecarlo()

    def random(self, game):

        # getting available moves
        move = random.choice(game.get_availables())

        return move

    def minimax(self, board, minimizing=True):

        if minimizing:
            print('Minimizando')
            ply = -1
            value, move = self.min_value(board, ply)

        else:
            print('Maximizando')
            ply = 1
            value, move = self.max_value(board, ply)

        return move

    def max_value(self, board, ply):
        # Verificando se é um estado terminal
        if self.is_terminal(board)[0]:
            return self.is_terminal(board)[1], None

        v = -np.inf

        avl = self.get_availables(board)
        for a in avl:
            new_board = self.play_move(board, a, ply)
            v2, _ = self.min_value(new_board, -ply)
            if v2 > v:
                v, move = v2, a

        return v, move

    def min_value(self, board, ply):
        # Verificando se é um estado terminal
        if self.is_terminal(board)[0]:
            return self.is_terminal(board)[1], None

        v = np.inf
        avl = self.get_availables(board)
        for a in avl:
            new_board = self.play_move(board, a, ply)
            v2, _ = self.max_value(new_board, -ply)

            if v2 < v:
                v, move = v2, a

        return v, move

    def montecarlo(self):
        pass

    def alpha_beta(self):
        pass
