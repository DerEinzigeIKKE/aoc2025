INPUTADRESS = "01_1_input.txt"
#INPUTADRESS = "01_1_input_test.txt"


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
    print(counter)

if __name__ == "__main__":
    main()

