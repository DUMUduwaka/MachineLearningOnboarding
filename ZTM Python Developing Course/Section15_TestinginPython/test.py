'''Text python file'''

import unittest
import main
print(__name__)


class Testmain(unittest.TestCase):
    '''Test class'''

    def test_do_stuff(self):
        '''test number 1'''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 100)

    # def test_do_stuff2(self):
    #     test_param = 'a name'
    #     result = main.do_stuff(test_param)
    #     self.assertEqual(result, ValueError)

    # def test_do_stuff2(self):
    #     test_param = 'a name'
    #     result = main.do_stuff(test_param)
    #     self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff2(self):
        '''test number 2'''
        test_param = 'a name'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        '''test number 3'''
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def test_do_stuff4(self):
        '''test number 4'''
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')


if __name__ == '__main__':
    unittest.main()
