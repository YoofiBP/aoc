import math

LEFT = "LEFT"
RIGHT = "RIGHT"

starting_dial = 50

def read_numbers():
    with open("puzzle.txt", "r") as f:
        lines = [ln.strip() for ln in f.readlines()]
    # remove empty lines
    return [ln for ln in lines if ln]

def destructure_rotation(rotation: str):
    return LEFT if rotation.startswith("L") else RIGHT, int(rotation[1::])

def twist_dial(rotation, current):
    direction, amount = destructure_rotation(rotation)
    extra_rotations = None
    if direction == LEFT:
        if current != 0 and amount > current:
            extra_rotations = 1
            extra_rotations += math.floor((amount - current)/100)
            print(f"During rotation it pointed to zero {extra_rotations} times")
        return (current - amount) % 100, extra_rotations
    if direction == RIGHT:
        if current != 0 and 100 - current < amount:
            extra_rotations = 1
            extra_rotations += math.floor((amount - (100 - current))/100)
            print(f"During rotation it pointed to zero {extra_rotations} times")
        return (current + amount) % 100, extra_rotations
    raise ValueError("Unexpected direction")

def twist_dial2(rotation, current):
    direction, amount = destructure_rotation(rotation)
    crossings = 0
    if direction == LEFT:
        if amount > current:
            crossings = 1 + (amount - current) // 100
            print(f"During rotation it pointed to zero {crossings} times")
        return (current - amount) % 100, crossings
    if direction == RIGHT:
        crossings = (current + amount) // 100
        return (current + amount) % 100, crossings
    raise ValueError("Unexpected direction")

def main():
    current_dial = starting_dial
    landed_at_zero = 0
    during_rotations = 0
    print(f"The dial starts by pointing at {current_dial}")
    for rotation in read_numbers():
        current_dial, extra_rotations = twist_dial2(rotation, current_dial)
        print(f"The dial is rotated {rotation} to point at {current_dial}\n")
        if current_dial == 0:
            landed_at_zero += 1
        during_rotations += (extra_rotations or 0)
    print(f"Dial points at zero {landed_at_zero} times and during the rotations it reached zero {during_rotations} times")
    print(f"Total: {during_rotations + landed_at_zero} times")

# main()

def day1():
    part1 = 0
    part2 = 0
    curr_pos = 50
    with open('puzzle.txt', 'r') as file:
        for line in file:
            # direction of moving
            dir = line[0]   
            num = int(line[1:])
            # circles made
            part2 += num // 100
            num = num % 100
            if dir == 'L':
                num = num*(-1)
            # crossed the boundary or not
            if curr_pos+num >= 100 or curr_pos+num <= 0:
                # if the position was zero no need to count
                if curr_pos != 0:
                    part2 += 1
            curr_pos += num
            curr_pos %= 100
            if curr_pos == 0:
                part1 += 1
    return part1, part2


if __name__ == '__main__':
    print(day1())