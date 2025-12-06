def parse_input():
    with open("test.txt", "r") as f:
        ranges, ids = f.read().split("\n\n")
        ids = [int(x) for x in ids.split("\n")]
        ranges = [[int(y) for y in x.split('-')] for x in ranges.split('\n')]
        
    return ranges, ids

def count_fresh_ids(ranges, ids):
    fresh_count = 0
    for id in ids:
        for range in ranges:
            lower, upper = range
            if id >= lower and id <= upper:
                fresh_count += 1
                break
    print(fresh_count)

def count_total_number_of_ids(ranges: list[list[int, int]]):
    total = 0
    ranges.sort(key=lambda x: x[0])
    print(ranges)
    previous = None
    for i in ranges:
        lower, upper = i
        total += (upper - lower) + 1
        if previous is not None:
            _, previous_upper = previous
            if lower < previous_upper:
                num_to_remove = (previous_upper - lower) + 1
                total -= num_to_remove
        previous = i
    print(total)

def count_total_number_of_ids2(ranges: list[list[int, int]]):
    total = 0
    ranges.sort()
    previous = None
    new_ranges = []
    print(ranges)
    for i in range(len(ranges)):
        curr_lower, curr_higher = ranges[i]
        if previous is not None:
            _, prev_higher = previous
            if curr_lower <= prev_higher:
                new_ranges.append([prev_higher + 1, curr_higher])
                previous = [prev_higher + 1, curr_higher]
            else:
                new_ranges.append(ranges[i])
                previous = ranges[i]
        else:
            new_ranges.append(ranges[i])
            previous = ranges[i]
        
    
    for l, h in new_ranges:
        total += (h - l) + 1

    print(new_ranges)

def main():
    ranges, ids = parse_input()
    count_total_number_of_ids2(ranges)
    
main()

#346240317247002