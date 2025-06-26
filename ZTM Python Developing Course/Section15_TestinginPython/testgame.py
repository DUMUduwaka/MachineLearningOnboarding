'''test file'''
import unittest
import script


class TestGame(unittest.TestCase):
    '''Unit testing'''

    def test_input(self):
        '''test 1: correct guess'''
        result = script.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        '''test 2: incorrect guess'''
        result = script.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_invalid_number(self):
        '''test 3: invalid number'''
        result = script.run_guess(5, 11)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
