# This module constains the simplest way I could conceive to have an SQL engine solve sudoku


def generate_sql(sudoku, verbose=False):
    """
    The same as basic, but instead of cross joining all tables, we fill in the tables with the possibilities first.
    """
    positions = []
    letters = 'abcdefghi'
    numbers = '012345678'

    position_to_rows = {}
    position_to_columns = {}
    position_to_squares = {}

    rows = {}
    columns = {}
    squares = {}

    # Construct the rows, columns, and squares
    for li, letter in enumerate(letters):
        for ni, number in enumerate(numbers):
            pos = letter + number
            positions.append(pos)

            if letter not in rows:
                rows[letter] = []
            rows[letter].append(pos)
            position_to_rows[pos] = rows[letter]

            if number not in columns:
                columns[number] = []
            columns[number].append(pos)
            position_to_columns[pos] = columns[number]

            if (li / 3, ni / 3) not in squares:
                squares[li / 3, ni / 3] = []
            squares[li / 3, ni / 3].append(pos)
            position_to_squares[pos] = squares[li / 3, ni / 3]

    possible_values = {}
    for pos in positions:
        possible_values[pos] = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    # Only doing initial logic in minimizing possible initial values.
    initial_values = {}
    for (i, j), value in sudoku.items():
        if value is None:
            continue
        letter = letters[i]
        number = numbers[j]
        pos = letter + number

        initial_values[pos] = value
        possible_values[pos] = set([value])

        row = position_to_rows[pos]
        column = position_to_columns[pos]
        square = position_to_squares[pos]

        for neighbor in row + column + square:
            if neighbor == pos:
                continue
            if value in possible_values[neighbor]:
                possible_values[neighbor].remove(value)

    query = ""
    # Delete all initial values
    query += "\n".join(["DELETE FROM {};".format(p) for p in positions])

    # Fill table with possible values
    aggregator = []
    for pos in positions:
        choices = ",".join(["({})".format(val) for val in possible_values[pos]])
        aggregator.append("INSERT INTO {} VALUES {};".format(pos, choices))
    query += "\n".join(aggregator)

    query += "COMMIT;\n"

    select_clause = "SELECT " + ", ".join(["{}.value".format(p) for p in positions])
    from_clause = "FROM " + " CROSS JOIN ".join(["{}".format(p) for p in positions])
    where_clause = "WHERE "

    column_constraints = []
    for column in columns.values():
        for p1 in column:
            for p2 in column:
                # We don't bother with the constraints between pre-initialized values
                if p1 >= p2 or (p1 in initial_values and p2 in initial_values):
                    continue
                column_constraints.append("{}.value <> {}.value".format(p1, p2))

    row_constraints = []
    for row in rows.values():
        for p1 in row:
            for p2 in row:
                if p1 >= p2 or (p1 in initial_values and p2 in initial_values):
                    continue
                row_constraints.append("{}.value <> {}.value".format(p1, p2))

    square_constraints = []
    for square in squares.values():
        for p1 in square:
            for p2 in square:
                if p1 >= p2 or (p1 in initial_values and p2 in initial_values):
                    continue
                square_constraints.append("{}.value <> {}.value".format(p1, p2))

    where_clause += " AND ".join(column_constraints)
    where_clause += " AND " + " AND ".join(row_constraints)
    where_clause += " AND " + " AND ".join(square_constraints)

    query += select_clause + " " + from_clause + " " + where_clause

    return query
