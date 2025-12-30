INPUTADRESS = "05_01_input.txt"
TESTGOAL = 707 #Level 1 Goal
#INPUTADRESS = "05_01_input_test.txt"
#TESTGOAL = 3 #Level 1 Testgoal

# Read input file
def read_input():
    with open(INPUTADRESS, 'r') as file:
        data = file.read().split('\n')
        index = data.index('')
        ranges, ids = [data[:index], data[index + 1:]]
        return ranges, ids

def check_ids(ranges, ids):
    fresh_ids = []
    for element in ids:
        for range_element in ranges:
            low, high = range_element.split('-')
            if int(element) in range(int(low), int(high) + 1):
                fresh_ids.append(int(element))
                print(f"Fresh ingredient found: {element}")
                #ids.remove(element)
                break
            
    return fresh_ids

def get_sum(fresh_ids):
    sum = 0
    for element in fresh_ids:
        sum += 1
    return sum

def main():
    ranges, ids = read_input()
    fresh_ids = check_ids(ranges, ids)
    sum = get_sum(fresh_ids)
    print("ranges", ranges)
    print("ids", ids)
    print("fresh_ids", fresh_ids)
    print(f"Sum: {sum}")
    print(f"Powerlevel: {TESTGOAL} (expected)")
    print(f"Difference: {sum - TESTGOAL}")


if __name__ == "__main__":
    main()