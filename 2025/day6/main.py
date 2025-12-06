def perform_operation(operation, numbers):
    """
    Perform a mathematical operation on a list of numbers.

    Args:
        operation (str): The operation to perform (+, -, *, /, ^)
        numbers (list): List of numbers to operate on

    Returns:
        float: Result of the operation
    """
    if not numbers:
        return None

    # Initialize result with the first number
    result = float(numbers[0])

    # Process remaining numbers
    for num in numbers[1:]:
        num = float(num)
        if operation == '+':
            result += num
        elif operation == '-':
            result -= num
        elif operation == '*':
            result *= num
        elif operation == '/':
            if num == 0:
                return None  # Avoid division by zero
            result /= num
        elif operation == '^':
            result **= num

    return result

def get_input1():
    with open("input.txt", "r") as f:
        return [ln.split() for ln in f.readlines()]

def get_largest_number_in_col(homework):
    mapping_of_col_to_max_width: dict[int, int] = {}
    num_of_cols = len(homework[0])
    num_of_rows = len(homework)
    for col in range(num_of_cols):
        numbers = []
        for row in range(num_of_rows):
            numbers.append(homework[row][col])
        numbers.sort(key=lambda x: len(x))
        mapping_of_col_to_max_width[col] = len(numbers[-1])
    return mapping_of_col_to_max_width

def get_input2():
    cleaned_homework = get_input1()
    num_of_cols = len(cleaned_homework[0])
    col_largest_mapping = get_largest_number_in_col(cleaned_homework)
    new_homework: list[list[str]] = []
    with open("input.txt", "r") as f:
        for ln in f.readlines():
            col = 0
            pointer = 0
            new_row = []
            for _ in range(num_of_cols):
                end_idx = pointer + col_largest_mapping[col]
                new_row.append(ln[pointer:end_idx].replace(" ", "0"))
                pointer = end_idx + 1
                col += 1 #Skip the empty column line
            new_homework.append(new_row)
        new_homework[-1] = cleaned_homework[-1]
        return new_homework

def part_1():
    homework = get_input1()
    num_of_cols = len(homework[0])
    num_of_rows = len(homework)
    overall_sum = 0
    for col in range(num_of_cols):
        operation = homework[-1][col]
        numbers = []
        for row in range(num_of_rows):
            if row != num_of_rows - 1:
                numbers.append(int(homework[row][col]))
        overall_sum += perform_operation(operation, numbers)
    print(overall_sum)

def part_2():
    homework = get_input2()
    num_of_cols = len(homework[0])
    num_of_rows = len(homework)
    overall_sum = 0
    for col in range(num_of_cols - 1, -1, -1):
        operation = homework[-1][col]
        numbers = []
        for row in range(num_of_rows):
            if row != num_of_rows - 1:
                numbers.append(list(homework[row][col]))
        output = add_sum_column(numbers, operation)
        overall_sum += output
    print(overall_sum)

def add_sum_column(numbers: list[list[str]], operation: str):
    num_of_cols = len(numbers[0])
    num_of_rows = len(numbers)
    new_numbers = []
    for col in range(num_of_cols - 1, -1, -1):
        number = ''
        for row in range(num_of_rows):
            if numbers[row][col] != '0':
                number += numbers[row][col]
        new_numbers.append(number)
    return perform_operation(operation, [int(x) for x in new_numbers])


part_2()