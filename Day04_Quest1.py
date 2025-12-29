#INPUTADRESS = "04_01_input.txt"
#TESTGOAL = 1460 #Level 1 Goal
INPUTADRESS = "04_01_input_test.txt"
TESTGOAL = 13 #Level 1 Testgoal

# Read input file
def read_input():
    with open(INPUTADRESS, 'r') as file:
        return file.read().split('\n')


def data_to_matrice(input):
    matrice = [] 
    rows = len(input)
    col = len(input[0])
    for i in range(rows):   
        row = []
        for j in range(col):
            row.append(input[i][j])
        matrice.append(row)
    return matrice


def select_place(matrice):
    count = 0
    rows = len(matrice)
    col = len(matrice[0])
    for i in range(0, rows):
        for j in range(0, col):
            if matrice[i][j] == '@':
                count += check_neighbors(matrice, i, j)
    return count


def check_neighbors(matrice, i, j):
    count = 0
    rows = len(matrice) - 1
    col = len(matrice[0]) - 1
    if (i != 0):
        if ((matrice[i-1][j] == '@') or (matrice[i-1][j] == 'X')):
            count += 1
    if ((i != 0) and (j != 0)):
        if ((matrice[i-1][j-1] == '@') or (matrice[i-1][j-1] == 'X')):
            count += 1
    if ((i != 0) and (j != col)):
        if ((matrice[i-1][j+1] == '@') or (matrice[i-1][j+1] == 'X')):
            count += 1
    if (i != rows):
        if ((matrice[i+1][j] == '@') or (matrice[i+1][j] == 'X')):
            count += 1
    if (j != 0):
        if ((matrice[i][j-1] == '@') or (matrice[i][j-1] == 'X')):
            count += 1
    if (j != col):
        if ((matrice[i][j+1] == '@') or (matrice[i][j+1] == 'X')):
            count += 1
    if ((i != rows) and (j != 0)):
        if ((matrice[i+1][j-1] == '@') or (matrice[i+1][j-1] == 'X')):
            count += 1
    if ((i != rows) and (j != col)):
        if ((matrice[i+1][j+1] == '@') or (matrice[i+1][j+1] == 'X')):
            count += 1
    
    if count < 4:
        matrice[i][j] = 'X'
        return 1
    elif count >= 4:
        return 0   


def print_data(matrice):
    rows = len(matrice)
    col = len(matrice[0])
    for i in range(rows):
        for j in range(col):
            print(matrice[i][j], end=" ")
        print()


def main():
    data = read_input()
    data = data_to_matrice(data)
    sum = select_place(data)
    print_data(data)
    print(f"Sum: {sum}")
    print(f"Powerlevel: {TESTGOAL} (expected)")
    print(f"Difference: {sum - TESTGOAL}")


if __name__ == "__main__":
    main()