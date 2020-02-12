import unittest

from Board import Board


class TestRows(unittest.TestCase):
	def setUp(self):
		self.board = Board()

	def test_row1_player1(self):
		self.board.board = [['X', 'X', 'X'],
							['_', '_', '_'],
							['_', '_', '_']]

		self.assertEqual(self.board.check_rows(), 1)

	def test_row1_player2(self):
		self.board.board = [['O', 'O', 'O'],
					  ['_', '_', '_'],
					  ['_', '_', '_']]

		self.assertEqual(self.board.check_rows(), 2)

	def test_row2_player1(self):
		self.board.board = [['_', '_', '_'],
					  ['X', 'X', 'X'],
					  ['_', '_', '_']]

		self.assertEqual(self.board.check_rows(), 1)

	def test_row2_player2(self):
		self.board.board= [['_', '_', '_'],
					  ['O', 'O', 'O'],
					  ['_', '_', '_']]

		self.assertEqual(self.board.check_rows(), 2)

	def test_row3_player1(self):
		self.board.board = [['_', '_', '_'],
					  ['_', '_', '_'],
					  ['X', 'X', 'X']]

		self.assertEqual(self.board.check_rows(), 1)

	def test_row3_player2(self):
		self.board.board = [['_', '_', '_'],
					  ['_', '_', '_'],
					  ['O', 'O', 'O']]

		self.assertEqual(self.board.check_rows(), 2)

	def test_empty(self):
		self.board.board = [['_', '_', '_'],
					  ['_', '_', '_'],
					  ['_', '_', '_']]
		self.assertEqual(self.board.check_rows(), 0)

	def test_no_rows(self):
		self.board.board = [['X', '_', 'O'],
					  ['_', 'X', 'O'],
					  ['_', 'X', 'O']]
		self.assertEqual(self.board.check_rows(), 0)


class TestColumns(unittest.TestCase):
	def setUp(self):
		self.board = Board()

	def test_column1_player1(self):
		self.board.board = [['X', '_', '_'],
					  ['X', '_', '_'],
					  ['X', '_', '_']]

		self.assertEqual(self.board.check_columns(), 1)

	def test_column1_player2(self):
		self.board.board = [['O', '_', '_'],
					  ['O', '_', '_'],
					  ['O', '_', '_']]

		self.assertEqual(self.board.check_columns(), 2)

	def test_column2_player1(self):
		self.board.board = [['_', 'X', '_'],
					  ['_', 'X', '_'],
					  ['_', 'X', '_']]

		self.assertEqual(self.board.check_columns(), 1)

	def test_column2_player2(self):
		self.board.board = [['_', 'O', '_'],
					  ['_', 'O', '_'],
					  ['_', 'O', '_']]

		self.assertEqual(self.board.check_columns(), 2)

	def test_column3_player1(self):
		self.board.board = [['_', '_', 'X'],
					  ['_', '_', 'X'],
					  ['_', '_', 'X']]

		self.assertEqual(self.board.check_columns(), 1)

	def test_column3_player2(self):
		self.board.board = [['_', '_', 'O'],
					  ['_', '_', 'O'],
					  ['_', '_', 'O']]

		self.assertEqual(self.board.check_columns(), 2)

	def test_empty(self):
		self.board.board = [['_', '_', '_'],
					  ['_', '_', '_'],
					  ['_', '_', '_']]
		self.assertEqual(self.board.check_columns(), 0)

	def test_no_cols(self):
		self.board.board = [['X', 'X', 'X'],
					  ['_', 'O', 'O'],
					  ['_', 'X', 'O']]
		self.assertEqual(self.board.check_columns(), 0)


class TestDiagonal(unittest.TestCase):
	def setUp(self):
		self.board = Board()

	def test_diagonal1_player1(self):
		self.board.board = [['X', '_', '_'],
					  ['_', 'X', '_'],
					  ['_', '_', 'X']]

		self.assertEqual(self.board.check_diagonals(), 1)

	def test_diagonal1_player2(self):
		self.board.board = [['O', '_', '_'],
					  ['_', 'O', '_'],
					  ['_', '_', 'O']]

		self.assertEqual(self.board.check_diagonals(), 2)

	def test_diagonal2_player1(self):
		self.board.board = [['_', '_', 'X'],
					  ['_', 'X', '_'],
					  ['X', '_', '_']]

		self.assertEqual(self.board.check_diagonals(), 1)

	def test_empty(self):
		self.board.board = [['_', '_', '_'],
					  ['_', '_', '_'],
					  ['_', '_', '_']]
		self.assertEqual(self.board.check_diagonals(), 0)

	def test_no_cols(self):
		self.board.board = [['X', 'X', 'X'],
					  ['_', 'O', 'O'],
					  ['_', 'X', 'O']]
		self.assertEqual(self.board.check_diagonals(), 0)


class TestHasThreeInARow(unittest.TestCase):
	def setUp(self):
		self.board = Board()

	def test_player1_threeInARow(self):
		self.board.board = [['X', '_', 'O'],
					  ['X', 'O', '_'],
					  ['X', '_', '_']]
		self.assertEqual(self.board.has_three_in_a_row(), 1)

	def test_player2_threeInARow(self):
		self.board.board = [['X', '_', 'O'],
					  ['O', 'O', 'O'],
					  ['X', 'X', '_']]
		self.assertEqual(self.board.has_three_in_a_row(), 2)

	def test_empty(self):
		self.board.board = [['_', '_', '_'],
					  ['_', '_', '_'],
					  ['_', '_', '_']]
		self.assertEqual(self.board.has_three_in_a_row(), 0)

	def test_cats_board(self):
		self.board.board = [['X', 'O', 'X'],
					  ['X', 'O', 'O'],
					  ['O', 'X', 'O']]
		self.assertEqual(self.board.has_three_in_a_row(), 0)


class TestBoardFull(unittest.TestCase):
	def setUp(self):
		self.board = Board()

	def test_board_full(self):
		self.board.board = [['X', 'O', 'X'],
					  ['X', 'O', 'O'],
					  ['O', 'X', 'O']]
		self.assertTrue(self.board.board_full())

	def test_board_not_empty(self):
		self.board.board = [['X', 'O', 'X'],
					  ['X', 'O', 'O'],
					  ['O', 'X', '_']]
		self.assertFalse(self.board.board_full())


# class TestboardOver(unittest.TestCase):
# 	def setUp(self):
# 		self.board = Board()

if __name__ == '__main__':
	unittest.main()
