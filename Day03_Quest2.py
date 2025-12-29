INPUTADRESS = "03_01_input.txt"
#TESTGOAL = 17311 # 2 digits normal input
TESTGOAL = 171419245422055 # 12 digits normal input
#INPUTADRESS = "03_01_input_test.txt"
#TESTGOAL = 357 # 2 digits test input
#TESTGOAL = 3121910778619 # 12 digits test input


# Read input file
def read_input():
    with open(INPUTADRESS, 'r') as file:
        return file.read().split('\n')
    
def get_power_level(input):
    power_level = 0
    for element in input:
       power_level += get_single_power(element)
    return power_level

def get_single_power(input):
    power_level = 0
    battery = analyze_pack(input)
    for i in range(12):
        power_level += battery[i] * (10 ** (11 - i))
    return power_level

def analyze_pack(input):
    i = 0
    battery = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # max 12 batteries
    length = len(input) - 1
    while i <= length:
        char = input[i]
        if int(char) > battery[11]:
            battery[11] = int(char)
            if (i == length):
                i += 1
                continue
            if (i == length - 1):
                change_battery(battery, 1)
                i += 1
                continue
            if (i == length - 2):
                change_battery(battery, 2)
                i += 1
                continue
            if (i == length - 3):
                change_battery(battery, 3)
                i += 1
                continue
            if (i == length - 4):
                change_battery(battery, 4)
                i += 1
                continue
            if (i == length - 5):
                change_battery(battery, 5)
                i += 1
                continue
            if (i == length - 6):
                change_battery(battery, 6)
                i += 1
                continue
            if (i == length - 7):
                change_battery(battery, 7)
                i += 1
                continue
            if (i == length - 8):
                change_battery(battery, 8)
                i += 1
                continue
            if (i == length - 9):
                change_battery(battery, 9)
                i += 1
                continue
            if (i == length - 10):
                change_battery(battery, 10)
                i += 1
                continue
            
            change_battery(battery, 11)
        i += 1
    print(f"Pack {input} has battery {battery}")
    return battery

def change_battery(battery, depth):
    for i in range(11, 11 - depth, -1):
        if battery[i] > battery[i - 1]:
            battery[i - 1] = battery[i]
            battery[i] = 0
        else:
            return

def main():
    input = read_input()
    sum_power = get_power_level(input)
    print(f"Powerlevel: {sum_power}")
    print(f"Powerlevel: {TESTGOAL} (expected)")
    print(f"Difference: {sum_power - TESTGOAL}")
    


if __name__ == "__main__":
    main()

"""
Ändeung im Vergleich zu Quest 1:
Es werden 12 statt 2 Batterien betrachtet.
Die Ergebnisse werden weiterhin aufsummiert
"""