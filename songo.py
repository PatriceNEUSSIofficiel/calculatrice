class Songo:
    def __init__(self):
        self.board = [[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4]]
        self.current_player = 0

    def display_board(self):
        print('     1  2  3  4  5  6')
        print('  +--------------------+')
        for row in range(2):
            print(str(row + 1) + ' | ', end='')
            for col in range(6):
                print(str(self.board[row][col]).rjust(2), end=' ')
            print('|')
        print('  +--------------------+')
        print('    A  B  C  D  E  F')

    def make_move(self, col):
        if col < 1 or col > 6:
            print('Invalid column')
            return False
        col -= 1
        if self.board[self.current_player][col] == 0:
            print('Empty hole')
            return False
        stones = self.board[self.current_player][col]
        self.board[self.current_player][col] = 0
        while stones > 0:
            col = (col + 1) % 6
            if col == 0:
                self.current_player = 1 - self.current_player
            self.board[self.current_player][col] += 1
            stones -= 1
        return True

    def get_winner(self):
        p0_sum = sum(self.board[0])
        p1_sum = sum(self.board[1])
        if p0_sum == 0:
            return 1
        elif p1_sum == 0:
            return 0
        else:
            return -1

game = Songo()

while True:
    game.display_board()
    print('Player', game.current_player + 1, "'s turn")
    col = input('Enter column (A-F) to move from: ').upper()
    if col == 'QUIT':
        break
    col = ord(col) - ord('A')
    game.make_move(col)
    winner = game.get_winner()
    if winner >= 0:
        game.display_board()
        print('Player', winner + 1, 'wins!')
        break
