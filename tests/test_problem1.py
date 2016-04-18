import os
import sys
import unittest
from problem1 import read_input, process_data, write_values


CURRENT_DIR = os.path.dirname(__file__)


class TestReadInput(unittest.TestCase):
    """
    This class is testing read_input() function from the problem1 module
    """
    def setUp(self):
        self.correct_result = {
            2: [(1, '2 Steaks'), (1, '2HamAndCheese'), (1, '2 zzz')],
            10: [(2, '10 Chicken Wings')],
            15: [(2, '15 alpha')],
            343: [(3, '343GuiltySparks')],
            sys.maxsize: [(0, 'BeachMiami'), (0, 'ALPHA'), (0, 'apple'), (0, 'mySideWalk'), (0, 'BdachMiami')]
        }

        # files
        self.sample_input = os.path.join(CURRENT_DIR, 'sample_input.txt')
        self.sample_bad_input = os.path.join(CURRENT_DIR, 'sample_bad_input.txt')

    def test_non_existing_file(self):
        self.assertIsNone(read_input('non_existing_file'))

    def test_correct_result(self):
        self.assertEqual(read_input(self.sample_input), self.correct_result)

    def test_bad_input_tolerance(self):
        self.assertEqual(read_input(self.sample_bad_input), self.correct_result)


class TestProcessData(unittest.TestCase):
    """
    This class is testing process_data() function from the problem1 module
    """

    def setUp(self):
        self.input = {
            2: [(1, '2 Steaks'), (1, '2HamAndCheese'), (1, '2 zzz')],
            10: [(2, '10 Chicken Wings')],
            15: [(2, '15 alpha')],
            343: [(3, '343GuiltySparks')],
            sys.maxsize: [(0, 'BeachMiami'), (0, 'ALPHA'), (0, 'apple'), (0, 'mySideWalk'), (0, 'BdachMiami')]
        }

        self.correct_result = [
            '2HamAndCheese',
            '2 Steaks',
            '2 zzz',
            '10 Chicken Wings',
            '15 alpha',
            '343GuiltySparks',
            'ALPHA',
            'apple',
            'BdachMiami',
            'BeachMiami',
            'mySideWalk',
        ]

    def test_wrong_input(self):
        self.assertIsNone(process_data('wrong'))

    def test_empty_input(self):
        self.assertEqual(process_data({}), [])

    def test_process_data(self):
        self.assertEqual(process_data(self.input), self.correct_result)


class TestWriteValues(unittest.TestCase):
    """
    This class is testing write_values() function from the problem1 module
    """
    def setUp(self):
        self.input = [
            '2HamAndCheese',
            '2 Steaks',
            '2 zzz',
            '10 Chicken Wings',
            '15 alpha',
            '343GuiltySparks',
            'ALPHA',
            'apple',
            'BdachMiami',
            'BeachMiami',
            'mySideWalk',
        ]

        # files
        self.test_output = os.path.join(CURRENT_DIR, 'test_output.txt')
        self.sample_output = os.path.join(CURRENT_DIR, 'sample_output.txt')

    def test_no_data(self):
        self.assertFalse(write_values(None))

    def test_bad_values(self):
        self.assertFalse(write_values([{}, None, 123, '']))

    def test_correct_file_output(self):
        # write the test file
        write_values(self.input, filename=self.test_output)

        # read the saved file into a list
        saved_file_list = []
        with open(self.test_output, 'r') as saved_file:
            for line in saved_file:
                saved_file_list.append(line.rstrip())

        # remove the test file
        os.remove(self.test_output)

        # read the correct output file
        correct_file_list = []
        with open(self.sample_output, 'r') as comp_file:
            for line in comp_file:
                correct_file_list.append(line.rstrip())

        self.assertEqual(saved_file_list, correct_file_list)


if __name__ == '__main__':
    unittest.main()
