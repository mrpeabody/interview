"""
mySidewalk: Coding assignment #1


Task description
===============
The user has a file that is made up of short (less than 1000 character) strings, each on a different line
(assume any common character or character combination that means a newline to someone might be used
interchangeably in this file). Most of these strings will be preceded by numbers, i.e.
“2 Steaks”, “10 Chicken Wings”, “343GuiltySparks”.
Accept the file from the user and return them a file with the same items sorted first by the numeric value of
any leading number (2 < 10 < 343) and then alphabetically for the rest of the string.


Solution description
================
The solution is based on Python3 (3.5.1) and its standard library. No external dependencies required.
The following file can serve as module or a standalone script.

In case of a script mode, file name to process should be sent as an argument. There is also an optional second
parameter for the output file name.

Usage examples:
    python3 problem1 text.txt
    (The output will be placed in the output.txt)

    python3 problem1 text.txt out1.txt
    (The output will be placed in the out1.txt)


All the tests are placed in the test_problem1.py file.


Assumptions:
================
- If a string does not contain a number that precedes text, it'll be placed after all 'numbered' strings in the sorted
output file, sorted alphabetically with other strings without a number;
- A 'numbered' string may or may not contain a separator between the preceding number and the rest of the string:
“10 Chicken Wings”, “343GuiltySparks”;
- Accordingly with the previous statement and due to the lack of clearance how a separator (if any) between two parts
of a string should be treated, and what kinds of separators to expect, the 'text' part of the string will be starting
right after the end of the number part;
- all non-alphanumeric symbols in the text will be ignored while sorting;
- strings that don't follow the structure described above will be ignored (i.e. empty strings, or strings that only
contain a number);
- Alphabetical sorting is case-insensitive;
- number is assumed to be integer.

"""

import sys
import re


def read_input(filename):
    """
    This function reads the input from the text file into a dictionary that has string numbers as keys,
    and a list of (text_start_index, original_string) tuples as values. Example:
    { 10: [(2, '10 Chicken Wings'), ... ] }
    Returns None if something went wrong, printing the error description into stdout.
    :param filename: the name of the file to read
    :return: list of tuples if everything went well, None otherwise
    """
    items = {}

    # open and read the file line by line
    try:
        with open(filename, 'r') as input_file:
            for line in input_file:
                # save the original value
                original_value = line.rstrip()

                # getting the text start index (if no text found, ignoring the line)
                found_non_numeric = re.search(r'[^0-9]', original_value)
                if found_non_numeric:
                    text_start_index = found_non_numeric.start()
                else:
                    continue

                # getting the number (if any)
                try:
                    number = int(original_value[:text_start_index])
                except ValueError:
                    # don't have a number, therefore the string should be sorted after all 'numeric' ones
                    number = sys.maxsize

                # append the tuple into the current number's values list
                number_values = items.setdefault(number, [])
                number_values.append((text_start_index, original_value))
    # file read error, gracefully stop
    except IOError as io_error:
        print(io_error.strerror, ':', filename)
        items = None

    return items


def process_data(items):
    """
    This function processes the data dictionary (items) into a sorted list of original string values.
    :param items: the dictionary of a format: { 10: [(2, '10 Chicken Wings'), ... ] }
    :return: a sorted list with original string values, None if something went wrong and prints the error into stdout
    """
    if not isinstance(items, dict):
        print('Bad input: Data format is incorrect')
        return None

    # declare the final list to return
    final_result = []

    try:
        # sort the keys first
        sorted_numbers = sorted(items)

        # prepare the useful regex pattern for sorting
        alpha_num = re.compile(r'[\W_]+')

        # sort lists of values for each key alphabetically
        for number in sorted_numbers:
            # first, make it a list of texts and sort it
            # lambda converts a tuple (2, '10 Chicken Wings') into a string 'ChickenWings' for sorting purposes
            sorting_values = map(lambda item: (alpha_num.sub('', item[1][item[0]:]).lower(), item), items[number])

            # then add original values to the final list
            final_result += map(lambda value: value[1][1], sorted(sorting_values))
    except Exception as e:
        print(e)
        final_result = None

    return final_result


def write_values(values, filename='output.txt'):
    """
    This function writes a list of strings into a file. Prints an error to stdout, if something happens.
    :param values: a list of strings
    :param filename: the name of the file to write. The function will overwrite an existing file.
    :return: True if everything went well, False otherwise
    """
    try:
        with open(filename, 'w') as output_file:
            for value in values:
                if not isinstance(value, str):
                    raise TypeError

                # write the file to the file
                print(value, file=output_file)

    except IOError as io_error:
        print(io_error.strerror, ':', filename)
        return False
    except TypeError:
        print('Data input error')
        return False

    return True


# Standalone script mode
if __name__ == '__main__':
    # getting the number of arguments
    argc = len(sys.argv)

    # no args - can't work
    if argc < 2:
        print(
            'No arguments were sent. Please use as following:\n',
            '\t python3 problem1.py <required_input_filename> <optional_output_filename>'
        )
        sys.exit(1)

    # read input into the specific data format
    data = read_input(sys.argv[1])
    if data is None:
        sys.exit(1)

    # sort the data
    final_values = process_data(data)
    if not final_values:
        sys.exit(1)

    # write the results into a file
    # one argument - output filename will be 'output.txt'
    if argc == 2:
        result = write_values(final_values)
    # two arguments - output filename will be as set in second argument
    else:
        result = write_values(final_values, filename=sys.argv[2])

    # report the final result
    print('Data was successfully sorted' if result else 'Failed to sort data')
