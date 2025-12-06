# Separated by commas
# First ID - Last ID
# None of the IDs start with 0
# Invalid IDs follow a pattern. They are a sequence repeated twice

"""
If the number of digits is not even there is no pattern

Check the length
Starting from that length till 0, divide the string by that length, expect them all to be the same

111 - 3
1010 - 4
1188511885 - 10
222222 - 6

Check how many time we can get equal divisions

"""

def get_range(input: str):
    return input.split("-")

def is_invalid2(number: str):
    length = len(number)
    for x in range(length-1, 0, -1):
        if(length % x == 0):
            bucket = []
            idx = 0
            word = ''
            while len(bucket) != length//x:
                word += number[idx]
                if(len(word) == x and len(word) > 0):
                    bucket.append(word)
                    word = ''
                idx+=1
                if idx >= length and len(word) > 0:
                    bucket.append(word)
                    break
            invalid = bucket.count(bucket[0]) == len(bucket)
            if invalid:
                return True
            

def is_invalid(number: str):
    if(len(number) % 2) != 0:
        return False
    middle = len(number)//2
    first = number[middle::]
    second = number[:middle:]
    return first == second

def main():
    total_invalid = 0
    with open("input.txt", "r") as f:
        lines = f.read()
        ranges = lines.split(",")
        for r in ranges:
            lower, upper = get_range(r)
            for x in range(int(lower), int(upper) + 1):
                if(is_invalid2(str(x))):
                    total_invalid += x
                    # print(x)
    print(f"Total invalid ids are {total_invalid}")

main()