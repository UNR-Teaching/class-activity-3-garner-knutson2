import re


class Board(object):

	def __init__(self):
		"""
		Initializes the Board of size 3x3
		"""
		self.board = [['_', '_', '_'],
					  ['_', '_', '_'],
					  ['_', '_', '_']]
		self.player1 = True

	def check_rows(self):
		# Check for three in a row in the rows
		for row in self.board:
			if row[0] == row[1] == row[2] and row[0] != '_':
				return 1 if row[0] == 'X' else 2
		return 0

	def check_columns(self):
		# Check for 3 in a row in a column
		for column in list(map(list, zip(*self.board))):
			if column[0] == column[1] == column[2] and column[0] != '_':
				return 1 if column[0] == 'X' else 2
		return 0

	def check_diagonals(self):
		# Check for 3 in a row in a diagonal
		if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '_':
			return 1 if self.board[0][0] == 'X' else 2
		elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '_':
			return 1 if self.board[0][2] == 'X' else 2
		else:
			return 0

	def has_three_in_a_row(self):
		"""
				Checks to see if there is a current winner of the game

				:return: 1 if player 1 has won, 2 if player 2 has won or 0 if no one has won
		"""
		results = [self.check_rows(), self.check_columns(), self.check_diagonals()]
		for result in results:
			if result != 0:
				return result
		return 0

	def board_full(self):
		for row in self.board:
			for i in row:
				if i == '_':
					return False

		return True

	def game_over(self):
		three_in_a_row = self.has_three_in_a_row()
		if three_in_a_row:
			return three_in_a_row
		else:
			return self.board_full()

	def is_marked(self, row, column):
		return self.board[row][column] != '_'

	def check_bounds(self, move):
		return move.location[0] >= 0 or move.location[0] <= 2 or move.location[1] >= 0 or move.location[1] <= 2

	def add_move(self, move):
		if not move or not self.check_bounds(move) or self.is_marked(move.location[0], move.location[1]):
			return False
		self.board[move.location[0]][move.location[1]] = move.player.player_symbol
		return True

	def print_board(self):
		for row in self.board:
			print(f'{row[0]} {row[1]} {row[2]}')
