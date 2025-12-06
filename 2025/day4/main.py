def create_grid():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]
    
def roll_present(shelf: str):
    return shelf == '@'

def roll_can_be_picked(roll_row_idx, row_col_idx, grid):
    adjacent_coordinates = generate_adjacent_coordinates(roll_row_idx, row_col_idx)
    number_of_rolls_adjacent = 0
    for coords in adjacent_coordinates:
        try:
            row, col = coords
            if row < 0 or col < 0:
                continue
            if roll_present(grid[row][col]):
                number_of_rolls_adjacent += 1
        except:
            print(f"Nothing at coordinates: {coords}")
    return number_of_rolls_adjacent < 4
    
def generate_adjacent_coordinates(row_idx, col_idx):
    #Given an index, generate the coordinates of all the surrounding positions
    coordinates = [
        [row_idx - 1, col_idx - 1], [row_idx-1, col_idx], [row_idx -1, col_idx + 1],
        [row_idx, col_idx - 1], [row_idx, col_idx + 1],
        [row_idx + 1, col_idx - 1], [row_idx + 1, col_idx], [row_idx + 1, col_idx + 1]
        ]
    return coordinates

def main():
    grid = create_grid()
    number_of_rolls_that_can_be_fetched = 0
    roll_removed = True
    while roll_removed:
        print("Restarting with another grid")
        roll_removed = False
        rebuilt_row = ''
        rebuilt_grid = []
        current_row_idx = 0
        current_col_idx = 0
        last_row_idx = len(grid) - 1
        max_col_size = len(grid[0])
        while current_row_idx < last_row_idx + 1:
            shelf_item = grid[current_row_idx][current_col_idx]
            if roll_present(shelf_item) and roll_can_be_picked(current_row_idx, current_col_idx, grid):
                roll_removed = True
                rebuilt_row += "x"
                number_of_rolls_that_can_be_fetched += 1
            elif shelf_item == 'x':
                rebuilt_row += '.'
            else:
                rebuilt_row += shelf_item
            if len(rebuilt_row) == max_col_size:
                rebuilt_grid.append(rebuilt_row)
                rebuilt_row = ''
            current_col_idx += 1
            if current_col_idx == max_col_size:
                current_row_idx += 1
                current_col_idx = 0
        print(number_of_rolls_that_can_be_fetched)
        grid = rebuilt_grid
main()