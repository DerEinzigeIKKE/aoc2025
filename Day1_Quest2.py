INPUTADRESS = "01_1_input.txt"
#INPUTADRESS = "01_1_input_test.txt"


# Read input file
def read_input():
    with open(INPUTADRESS, 'r') as file:
        return file.read()

def check_position(input):
    position_alt = 50
    position_neu = 0
    counter = 0
    for line in input.split('\n'):
        # If line starts with R, move right
        if line.startswith('R'):
            line = line.strip('R')                  #505
            counter += (int(line) // 100)           #5
            steps = int(line) % 100                 #5      
            position_neu = position_alt + steps

        # If line starts with L, move left
        elif line.startswith('L'):
            line = line.strip('L')
            counter += (int(line) // 100)
            steps = int(line) % 100
            position_neu = position_alt - steps

    # Check if Click 
        if ((position_neu < 0 or position_neu >= 100) and (position_alt >=0 and position_alt < 100)):
            counter += 1
        elif ((position_alt < 0 or position_alt >= 100) and (position_neu >=0 and position_neu < 100)):
            counter += 1
    
    # Correct position to be within 0-99
        if (position_neu < 0):
            print(position_neu)
            position_neu %= 100
            print(position_neu)
        elif (position_neu >= 100):
            #print(position_neu)
            position_neu %= 100
            #print(position_neu)
        
        position_alt = position_neu
    return counter

def main():
    raw_input = read_input()
    counter = check_position(raw_input)
    print(counter)

if __name__ == "__main__":
    main()

