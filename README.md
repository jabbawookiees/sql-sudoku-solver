# Getting Started

Hi! This is the SQL-based sudoku solver Professor Roland asked me to make.

To use it, you need to install the required libraries in `requirements.txt`.

For Linux users, you will also need to install `postgresql-9.3` and `postgresql-client-9.3`. I think you will also need to have the `python-dev` package to install psycopg2.

You will also need to create the database and fill in the tables. Please see `initialize.sql` for what to do.

To run it, simply type `python main.py samples/problem0.txt`. You can replace the file to be solved as long as you follow the prescribed format for sudoku files -- 9 lines, 9 characters each, and spaces for empty cells. See the other files for examples.

There is a faster SQL-based constraint solver that first removes all the impossible choices before doing the joins and removes useless constraints (pre-filled cells not equal to other pre-filled cells) that significantly speeds up the solver. We get over 100x speedups on the more difficult problems. In fact, for problem 5 and onwards, I have given up trying to wait for the basic solver.

To use the faster solver, use `python main.py samples/problem0.txt --generator faster`.

Note that as of this writing, problem99.txt took longer than one minute on my machine to solve (so I gave up on that).

## Sudoku sources

Problem 0 was created by me for debugging.

Unless specified otherwise, the other problems are from here:
http://www.printable-sudoku-puzzles.com/wfiles/

Problem 1 and 2 are from:
These are the first two with 45 pre-filled numbers in each sudoku.

Problem 3 and 4 are from:
These are the first two with 35 pre-filled numbers in each sudoku.
The basic solver takes about 2 to 10 seconds on these. I gave up on using that to solve further problems.
These problems and the easier ones take me less than one second to solve using the faster solver.

Problem 5 and 6 are from:
These are the first two with 30 pre-filled numbers in each sudoku.
Problem 5 takes me about 10 seconds to solve on my machine, while problem 6 takes me about 0.5 to 1 second.

Problem 7 and 8 are from:
These are the first two with 25 pre-filled numbers in each sudoku.
These take me about 10-15 seconds to solve on my machine.

Problem 99 is from Peter Norvig's sudoku page:
http://norvig.com/sudoku.html
I can't figure out how to solve this with a single SQL statement. :(
