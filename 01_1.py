INPUTADRESS = "01_1_input.txt"
#INPUTADRESS = "01_1_input_test.txt"


# Read input file
def read_input():
    with open(INPUTADRESS, 'r') as file:
        return file.read()

def check_position(input):
    position = 50
    counter = 0
    count = 0
    for line in input.split('\n'):

        if line.startswith('R'):
            line = line.strip('R')
            position += int(line)

        elif line.startswith('L'):
            line = line.strip('L')
            position -= int(line)

        if (position < 0):
            position %= 100

        if (position >= 100):
            position %= 100
        
        print(f"Current position: {position}")
        if position == 0:
            counter += 1
            print(f"Lap completed at instruction {count}")
        count += 1
    return counter

def main():
    raw_input = read_input()
    counter = check_position(raw_input)
    print(counter)

if __name__ == "__main__":
    main()
