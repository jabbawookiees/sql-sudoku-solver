import click
import psycopg2
import basic
import faster


POSTGRES_DBNAME = "something"
POSTGRES_USERNAME = "somebody"
POSTGRES_PASSWORD = "password"
POSTGRES_HOST = "127.0.0.1"


def run_sql(sql):
    """Runs an SQL statement against our database and returns a generator of answers."""
    conn = psycopg2.connect(dbname=POSTGRES_DBNAME, user=POSTGRES_USERNAME, password=POSTGRES_PASSWORD, host=POSTGRES_HOST)
    cursor = conn.cursor()
    cursor.execute(sql)
    while True:
        answer = cursor.fetchone()
        if answer:
            yield answer
        else:
            break
    conn.close()


def construct_sudoku(result):
    """Construct a sudoku board out of the result of an SQL query"""
    sudoku = {}
    k = 0
    for i in xrange(9):
        for j in xrange(9):
            sudoku[i, j] = result[k]
            k += 1
    return sudoku


def load_sudoku(filename):
    """Load a sudoku board from a file"""
    ff = open(filename)
    sudoku = {}
    for i in xrange(9):
        s = ff.readline()
        for j in xrange(9):
            if s[j] != ' ':
                sudoku[i, j] = int(s[j])
            else:
                sudoku[i, j] = None
    ff.close()
    return sudoku


def verify_sudoku(sudoku):
    """Checks if all rows, columns, and subsquares have unique initial values (or empty)"""
    columns = [set() for i in xrange(9)]
    rows = [set() for i in xrange(9)]
    squares = [[set() for i in xrange(3)] for j in xrange(3)]
    errors = []

    for (i, j), value in sudoku.items():
        if value is None:
            continue
        if value in rows[i]:
            errors.append("{} was doubled at row {}".format(value, i))
        else:
            rows[i].add(value)
        if value in columns[j]:
            errors.append("{} was doubled at column {}".format(value, j))
        else:
            columns[j].add(value)

        if value in squares[i / 3][j / 3]:
            errors.append("{} was doubled at square ({}, {})".format(value, i / 3, j / 3))
        else:
            squares[i / 3][j / 3].add(value)
    return errors


def check_answer(initial, answer):
    """Takes an initial sudoku board and the answer and checks if they match and if the answer is correct."""
    errors = verify_sudoku(answer)
    if errors:
        return False
    for i in xrange(9):
        for j in xrange(9):
            if initial[i, j] is not None and initial[i, j] != answer[i, j]:
                return False
    return True


def print_sudoku(sudoku):
    """Debugging function to print out the sudoku board"""
    for i in xrange(9):
        print ''.join([str(sudoku[i, j]) if sudoku[i, j] is not None else ' ' for j in xrange(9)])


@click.command()
@click.argument('filename', default='samples/problem0.txt')
@click.option('--generator', default='basic', show_default=True,
              help='The SQL generator we will use. Options are: basic, faster')
@click.option('--verbose', default=False, is_flag=True, type=bool,
              help='Whether we want to print the SQL query. It can be very long.')
def main(filename, generator, verbose):
    sudoku = load_sudoku(filename)
    print "Loaded the sudoku board:"
    print_sudoku(sudoku)

    errors = verify_sudoku(sudoku)
    if errors:
        print "Sudoku file has inconsistencies:"
        print '\n'.join(errors)
        raise Exception("Sudoku file has inconsistencies")

    if generator == 'basic':
        sql = basic.generate_sql(sudoku, verbose=verbose)
    elif generator == 'faster':
        sql = faster.generate_sql(sudoku, verbose=verbose)
    else:
        raise Exception("Unsupported SQL generator")

    if verbose:
        print sql

    for result in run_sql(sql):
        answer = construct_sudoku(result)
        correct = check_answer(sudoku, answer)
        print "Answered the sudoku board:"
        print_sudoku(answer)
        if not correct:
            print "WRONG ANSWER!"


if __name__ == '__main__':
    main()
