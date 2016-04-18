## mySidewalk: Coding assignment #1


### Task description
The user has a file that is made up of short (less than 1000 character) strings, each on a different line
(assume any common character or character combination that means a newline to someone might be used
interchangeably in this file). Most of these strings will be preceded by numbers, i.e.
“2 Steaks”, “10 Chicken Wings”, “343GuiltySparks”.
Accept the file from the user and return them a file with the same items sorted first by the numeric value of
any leading number (2 < 10 < 343) and then alphabetically for the rest of the string.


### Solution description
The solution is built using Python3 (3.5.1) and its standard library. No external dependencies required.
The following file can serve as module or a standalone script.


In case of a script mode, file name to process should be sent as an argument. There is also an optional second
parameter for the output file name.


##### Usage example:

    python3 problem1 text.txt
*The output will be placed in the output.txt*


Also possible to set the output file name (optional)

    python3 problem1 text.txt out1.txt
*The output will be placed in the out1.txt*


All the tests are placed in the test_problem1.py file under the __tests__ directory:

    python3 -m unittest test_problem1


### Assumptions
* If a string does not contain a number that preceeds text, it'll be placed after all 'numbered' strings in the sorted
output file, sorted alphabetically with other strings without a number;

* A 'numbered' string may or may not contain a separator between the preceeding number and the rest of the string:
“10 Chicken Wings”, “343GuiltySparks”;

* Accordingly with the previous statement and due to the lack of clearance how a separator (if any) between two parts
of a string should be treated, and what kinds of separators to expect, the 'text' part of the string will be starting
right after the end of the number part;

* all non-alphanumeric symbols in the text will be ignored while sorting;

* strings that don't follow the structure described above will be ignored (i.e. empty strings, or strings that only
contain a number);

* Alphabetical sorting is case-insensitive;

* number is assumed to be integer.


---

## mySidewalk: Coding assignment #2


### Task description
The user wants a responsive web interface to see a particular comment from the mySidewalk engagement comments API.
Load the comment with ID 100 (https://mysidewalk.com/api/engagement/v1/comments/100.json) from the API,
redirect the window’s location to a path that represents a human friendly portion of the comment, and display
the comment in a device response and visually pleasing manner.


### Solution description
The solution is built using Flask web framework + Python3 (3.5.1) and its standard library.
The following solution works as a standalone web app.
Web stack only includes HTML5 and CSS3, no frameworks or libraries required.


### Installation

    pip3 install -r requirements.txt


##### Usage example:

Start the app:

    python3 problem2

Access it in a browser:

    http://127.0.0.1:5000/comment/<comment_id>
   *<comment_id> might be replaced with an actual id, say 100*


All the tests are placed in the test_problem2.py file under the __tests__ directory:

    python3 -m unittest test_problem2

---