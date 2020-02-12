#!/usr/bin/env python3
import unittest
from Player import Player


class TestIsWithinBounds(unittest.TestCase):

	def test_correct_input(self):
		self.assertTrue(Player(1).is_within_bounds("0,2"))
		self.assertTrue(Player(1).is_within_bounds("1,2"))
		self.assertTrue(Player(1).is_within_bounds("2,1"))
		self.assertTrue(Player(1).is_within_bounds("0,0"))

	def test_three_tuple_input(self):
		self.assertFalse(Player(1).is_within_bounds("0,2,1"))
		self.assertFalse(Player(1).is_within_bounds("1,3,1"))

	def test_single_integer_input(self):
		self.assertFalse(Player(1).is_within_bounds("1"))
		self.assertFalse(Player(1).is_within_bounds("20"))
		self.assertFalse(Player(1).is_within_bounds("100"))

	def test_incorrect_char_input(self):
		self.assertFalse(Player(1).is_within_bounds("a"))
		self.assertFalse(Player(1).is_within_bounds(",,,"))
		self.assertFalse(Player(1).is_within_bounds("$"))
		self.assertFalse(Player(1).is_within_bounds("\fkenvkd"))

	def test_empty_string_input(self):
		self.assertFalse(Player(1).is_within_bounds(""))

	def test_very_large_user_input(self):
		self.assertFalse(Player(1).is_within_bounds(
			"al;dkfjafiowjh;aosfna;oifjawo;fkas;ahjoaiwjfal;skdjfoawiejf;aldkfja;lsdkfja;weijfa;slkdfjaowiejf;alsdkfjawoiejf;asldfkja;weoifja;ldsfkjawe;oifjasdl;fkajwoe;ifja;lfkjawoe;ifjas;lfkjaweo;ifjasl;fkjawoefija;dfawleifja;faiwejf;oaijdf;lakjfo;aijwef;askdfj;aliwefja;oiefja;lsdkfja;oeijfa;lskfjao;wiefja;lskdfja;wiejfa;kfja;owiefja;slkdfja;woiefja;lskdfja;woiefj;alskdfja;owiefja;ldkfja;woeifja;lsdkfja;owiefja;lsdkfja;owiefj;aldkfja;lfewi;awejf;lawe;fj;fjoi69" * 10000))


class TestConvertUserInput(unittest.TestCase):

	def test_valid_input(self):
		self.assertEqual(Player(1).convert_user_input("0,2"), (0,2))
		self.assertEqual(Player(1).convert_user_input("1,2"), (1,2))
		self.assertEqual(Player(1).convert_user_input("2,1"), (2,1))
		self.assertEqual(Player(1).convert_user_input("0,0"), (0,0))


if __name__ == '__main__':
	unittest.main()
