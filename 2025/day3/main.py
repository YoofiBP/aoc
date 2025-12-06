# In a bank, look for the highest digit, note its index and look for the second highest digit after it

def get_largest_jolt(battery: str):
    current_max = 0
    max_idx = 0
    for i in range(len(battery) - 1):
        if int(battery[i]) > current_max:
            current_max = int(battery[i])
            max_idx = i
    second_max = 0
    second_idx = max_idx + 1
    for i in range(second_idx, len(battery)):
        if int(battery[i]) > second_max:
            second_max = int(battery[i])
    return str(current_max) + str(second_max)

def get_largest_jolt2(battery: str, max_num_digits: int):
    battery_length = len(battery)
    full_number = ''
    last_idx_to_check = battery_length - (max_num_digits - len(full_number))
    current_idx = 0
    current_max = -1
    current_max_idx = 0
    print(f"starting last idx: {last_idx_to_check}")
    while len(full_number) != max_num_digits:
        current_digit = int(battery[current_idx])
        print(f"Comparing {current_digit} and {current_max}")
        if current_digit > current_max:
            print(f"{current_digit} is larger than {current_max}")
            current_max = current_digit
            current_max_idx = current_idx
        if current_idx == last_idx_to_check:
            # We have reached the end of the possible numbers and need to start again from the index of the last max_number
            print(f"we have finished checking. Current index is {current_idx}")
            full_number += str(current_max)
            print(f"Current full number {full_number}")
            current_idx = current_max_idx + 1
            print(f"New current index: {current_idx}")
            last_idx_to_check = battery_length - (max_num_digits - len(full_number))
            print(f"New last index: {last_idx_to_check}")
            current_max = -1
        else:
            current_idx += 1
    return int(full_number)


def main():
    total_output = 0
    with open("input.txt", "r") as f:
        batteries = [ln.strip() for ln in f.readlines()]
        for battery in batteries:
            total_output += int(get_largest_jolt2(battery, 12))
    print(total_output)

main()