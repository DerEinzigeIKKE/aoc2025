INPUTADRESS = "03_01_input.txt"
#INPUTADRESS = "03_01_input_test.txt"
TESTGOAL = 357


# Read input file
def read_input():
    with open(INPUTADRESS, 'r') as file:
        return file.read().split('\n')
    
def get_power_level(input):
    power_level = 0
    for element in input:
       power_level += analyze_pack(element)
    return power_level

def analyze_pack(input):
    i = 0
    battery_1 = 0
    battery_2 = 0
    length = len(input)
    while i < length:
        char = input[i]
        if int(char) > battery_2:
            battery_2 = int(char)
        if i != (length - 1):
            if ((battery_2 > battery_1)):
                battery_1 = battery_2 
                battery_2 = 0 
        i += 1
        power_level = (10 * battery_1) + battery_2
    print(f"Pack {input} has power level {power_level}")
    return power_level

def main():
    input = read_input()
    sum_power = get_power_level(input)
    print(f"Powerlevel: {sum_power}")
    print(f"Powerlevel: {TESTGOAL} (expected)")
    print(f"Difference: {sum_power - TESTGOAL}")
    


if __name__ == "__main__":
    main()