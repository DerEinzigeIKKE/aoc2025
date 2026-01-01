INPUTADRESS = "input\input_01.txt"
#TESTGOAL = 1066 # Level 1 Goal
TESTGOAL = 6223 # Level 2 Goal
#INPUTADRESS = "input\input_test_01.txt"
#TESTGOAL = 3 # Level 1 Testgoal
#TESTGOAL = 6 # Level 2 Testgoal

# Read input file
def read_input():
    with open(INPUTADRESS, 'r') as file:
        return file.read()

def change_position(input):
    position_old = 50
    position_new = 0
    counter = 0
    for line in input.split('\n'):
        # If line starts with R, move right
        if line.startswith('R'):
            line = line.strip('R')
            for i in range(int(line)):
                position_new = position_old + 1
                position_old = position_new
                counter += check_position(position_new)
            

        # If line starts with L, move left
        elif line.startswith('L'):
            line = line.strip('L')
            for i in range(int(line)):
                position_new = position_old - 1
                position_old = position_new
                counter += check_position(position_new)
    return counter

def check_position(position):
    if (position % 100) == 0:
        return 1
    else:
        return 0

def main():
    raw_input = read_input()
    counter = change_position(raw_input)
    print(f"counter: {counter}")
    print(f"counter: {counter} (expected)")
    print(f"difference: {counter - TESTGOAL}")

if __name__ == "__main__":
    main()

