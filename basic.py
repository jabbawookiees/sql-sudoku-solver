# This module constains the simplest way I could conceive to have an SQL engine solve sudoku


def generate_sql(sudoku, verbose=False):
    """
    Generates an SQL statement like so:

    SELECT a1.value, a2.value, a3.value ...
           b1.value, ...
           i1.value, ...
    FROM digits a1 CROSS JOIN digits a2 CROSS JOIN ... digits i9
    WHERE a1.value = 1 AND a2.value = 2 AND ... (the initial configuration)
          AND a1.value <> a2.value AND a1.value <> a3.value ...
          AND b1.value <> b2.value AND b1.value <> b3.value ... (the rows)
          ...
          AND a1.value <> b1.value AND a1.value <> c1.value ... (the columns)
          ...
          AND a1.value <> b2.value AND ... (the smaller squares)

    We denote the cells in the grid by a (letter, number) pair: a0 to i8.
    a0 is at the top-left, b0 is the cell below that, and i8 is the cell at the bottom-right.
    """
    positions = []
    letters = 'abcdefghi'
    numbers = '012345678'
    rows = {}
    columns = {}
    squares = {}

    for li, letter in enumerate(letters):
        for ni, number in enumerate(numbers):
            pos = letter + number
            positions.append(pos)

            if letter not in rows:
                rows[letter] = []
            rows[letter].append(pos)

            if number not in columns:
                columns[number] = []
            columns[number].append(pos)

            if (li / 3, ni / 3) not in squares:
                squares[li / 3, ni / 3] = []
            squares[li / 3, ni / 3].append(pos)

    query = "SELECT " + \
        ", ".join(["{}.value".format(p) for p in positions]) + \
        " FROM " + \
        " CROSS JOIN ".join(["digits {}".format(p) for p in positions]) + \
        " WHERE "

    column_constraints = []
    for column in columns.values():
        for p1 in column:
            for p2 in column:
                if p1 >= p2:
                    continue
                column_constraints.append("{}.value <> {}.value".format(p1, p2))

    row_constraints = []
    for row in rows.values():
        for p1 in row:
            for p2 in row:
                if p1 >= p2:
                    continue
                row_constraints.append("{}.value <> {}.value".format(p1, p2))

    square_constraints = []
    for square in squares.values():
        for p1 in square:
            for p2 in square:
                if p1 >= p2:
                    continue
                square_constraints.append("{}.value <> {}.value".format(p1, p2))

    initial_constraints = []
    for (i, j), value in sudoku.items():
        if value is not None:
            letter = letters[i]
            number = numbers[j]
            pos = letter + number
            initial_constraints.append("{}.value = {}".format(pos, value))

    query += " AND ".join(initial_constraints)
    query += " AND " + " AND ".join(column_constraints)
    query += " AND " + " AND ".join(row_constraints)
    query += " AND " + " AND ".join(square_constraints)
    return query
