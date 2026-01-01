#INPUTADRESS = "input\input_09.txt"
#TESTGOAL = 0 #Level 1 Goal
#TESTGOAL = 0 #Level 2 Goal
INPUTADRESS = "input\input_test_09.txt"
TESTGOAL = 50 #Level 1 Testgoal
#TESTGOAL = 0 #Level 2 Testgoal

# Read input file
def read_input():
    with open(INPUTADRESS, 'r') as file:
        data = file.read().split('\n')
        return data

# Count Sum
def get_sum(input):
    return 1

# Main function
def main():
    input_data = read_input()
    sum = get_sum(input_data)
    print("input_data", input_data)
    print(f"Sum: {sum}")
    print(f"Powerlevel: {TESTGOAL} (expected)")
    print(f"Difference: {sum - TESTGOAL}")


if __name__ == "__main__":
    main()