import unittest
from Player import Player
from Board import Board


class TestGame(unittest.TestCase):

	def test_add_player_move_to_board(self):
		board = Board()
		choice = "0,0"
		player1 = Player(1)
		move = player1.validate_input(choice)
		self.assertTrue(board.add_move(move))
		self.assertEqual(board.board[0][0],player1.player_symbol)

	def test_incorrect_move(self):
		board = Board()
		choice = "0,0,0"
		player1 = Player(1)
		move = player1.validate_input(choice)
		self.assertFalse(board.add_move(move))


	def test_cat_game(self):
		board = Board()
		player1 = Player(1)
		player2 = Player(2)
		choice = ["0,0","0,1","1,0","1,1","2,0","0,2","2,1","1,2","2,2"]

		move = player1.validate_input(choice[0])
		board.add_move(move)
		move = player2.validate_input(choice[1])
		board.add_move(move)
		move = player1.validate_input(choice[2])
		board.add_move(move)
		move = player2.validate_input(choice[3])
		board.add_move(move)
		move = player1.validate_input(choice[4])
		board.add_move(move)
		move = player2.validate_input(choice[5])
		board.add_move(move)
		move = player1.validate_input(choice[6])
		board.add_move(move)
		move = player2.validate_input(choice[7])
		board.add_move(move)
		move = player1.validate_input(choice[8])
		board.add_move(move)


if __name__ == '__main__':
	unittest.main()
