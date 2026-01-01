INPUTADRESS = "05_01_input.txt"
#TESTGOAL = 707 #Level 1 Goal
TESTGOAL = 361615643045059 #Level 2 Goal
#INPUTADRESS = "05_01_input_test.txt"
#TESTGOAL = 3 #Level 1 Testgoal
#TESTGOAL = 14 #Level 2 Testgoal

# Read input file
def read_input():
    with open(INPUTADRESS, 'r') as file:
        data = file.read().split('\n')
        index = data.index('')
        ranges, ids = [data[:index], data[index + 1:]]
        return ranges, ids

def get_ids(old_ranges, new_ranges):
    for new_interval in new_ranges:
        low_new, high_new = new_interval.split('-')

        for old_interval in old_ranges:
            low_old, high_old = old_interval.split('-')

            # low_new in between old Intervall
            if ((int(low_new))>=int(low_old) and (int(low_new))<=int(high_old)):
            # low_new in between old Intervall & high_new over high_old -> (low_old - high_new)   
                if (int(high_new))>int(high_old):
                    old_ranges[old_ranges.index(old_interval)] = f"{low_old}-{high_new}"

            # low_new under old Intervall
            elif ((int(low_new))<int(low_old)):
                # low_new under old Intervall & high_new over high_old -> (low_new - high_new)   
                if (int(high_new))>=int(high_old):
                    old_ranges[old_ranges.index(old_interval)] = f"{low_new}-{high_new}"

                # low_new under old Intervall & high_new in old Intervall -> (low_new - high_old)   
                elif ((int(high_new))>=int(low_old) and (int(low_new))<=int(high_old)):
                    old_ranges[old_ranges.index(old_interval)] = f"{low_new}-{high_old}"

                # low_new under old Intervall & high_new under old Intervall -> (low_old - high_old, low_new - high_new))   
                elif ((int(high_new))<int(low_old)):
                    if (old_ranges.index(old_interval) + 1) == len(old_ranges):
                        if new_interval not in old_ranges:
                            old_ranges.append(new_interval)

            # low_new over old Intervall
            elif ((int(low_new))>int(high_old)):
                if (old_ranges.index(old_interval) + 1) == len(old_ranges):
                    if new_interval not in old_ranges:
                            old_ranges.append(new_interval)

            new_ranges = old_ranges.copy()
            new_ranges.sort(key=lambda x: int(x.split('-')[0]))
        
    return new_ranges

def get_sum(fresh_ids):
    sum = 0
    for element in fresh_ids:
        low, high = element.split('-')
        sum += (int(high) - int(low) + 1)
    return sum

def get_answer(ranges):
    old_ranges = []
    new_ranges = ranges.copy()
    old_ranges.append(new_ranges[0])
    old_ranges = get_ids(old_ranges, new_ranges)

    while (old_ranges != new_ranges):
        new_ranges = old_ranges.copy()
        old_ranges = []
        old_ranges.append(new_ranges[0])
        old_ranges = get_ids(old_ranges, new_ranges)


    sum = get_sum(old_ranges)
    return sum


def main():
    ranges, ids = read_input()
    #fresh_ids = get_ids(ranges)
    sum = get_answer(ranges)
    print("ranges", ranges)
    #print("ids", ids)
    #print("fresh_ids", fresh_ids)
    print(f"Sum: {sum}")
    print(f"Powerlevel: {TESTGOAL} (expected)")
    print(f"Difference: {sum - TESTGOAL}")


if __name__ == "__main__":
    main()