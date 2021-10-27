import numpy as np


class Game:
    def __init__(self, board=None):

        if board is None:
            self.board = np.zeros((3, 3), dtype=int)

        else:
            self.board = board

        self.game_over = False
        self.winner = 0
        self.score = 0

    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.game_over = False
        self.winner = 0
        self.score = 0

    def play_move(self, move, player):

        if move is not None:
            board_flat = self.board.flatten()
            board_flat[move - 1] = player
            self.board = np.reshape(board_flat, (self.board.shape[0], self.board.shape[1]))

    def is_terminal(self):

        # verificando se o jogador 1 venceu
        if any(np.sum(self.board, axis=0) == 3) or \
                any(np.sum(self.board, axis=1) == 3) or \
                sum(np.diag(self.board)) == 3 or \
                sum(np.diag(self.board[::-1])) == 3:

            self.game_over = True
            self.winner = 1
            self.score = (len(self.get_availables()) + 1)

        # verificando se o jogador 2 venceu
        elif any(np.sum(self.board, axis=0) == -3) or \
                any(np.sum(self.board, axis=1) == -3) or \
                sum(np.diag(self.board)) == -3 or \
                sum(np.diag(self.board[::-1])) == -3:

            self.game_over = True
            self.winner = -1
            self.score = -(len(self.get_availables()) + 1)

        # verificando se houve empate
        else:
            if len(self.get_availables()) == 0:
                self.score = 0
                self.game_over = True
                self.winner = 0

            else:
                self.score = 0
                self.game_over = False
                self.winner = 0

        return self.game_over

    def get_availables(self):
        return np.where(self.board.flatten() == 0)[0] + 1

    def is_available(self, move):
        return self.board.flatten()[move - 1] == False

    def print_game(self):

        A = []

        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                if self.board[i, j] == -1:
                    A.append('O')
                elif self.board[i, j] == 1:
                    A.append('X')
                else:
                    A.append(' ')

        print(f' {A[0]} | {A[1]} | {A[2]}')
        print('---+---+---')
        print(f' {A[3]} | {A[4]} | {A[5]}')
        print('---+---+---')
        print(f' {A[6]} | {A[7]} | {A[8]}')
