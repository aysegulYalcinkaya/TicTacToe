cells = "_ _ _ _ _ _ _ _ _".split()


def checkWin():
    win = []
    for i in range(3):
        if (cells[i * 3] == cells[i * 3 + 1] and cells[i * 3] == cells[i * 3 + 2] and cells[i * 3] != "_"):
            win.append(cells[i * 3])
        if (cells[i] == cells[i + 3] and cells[i] == cells[i + 6] and cells[i] != "_"):
            win.append(cells[i])
    if (cells[0] == cells[4] and cells[0] == cells[8] and cells[0] != "_"):
        win.append(cells[0])
    if (cells[2] == cells[4] and cells[2] == cells[6] and cells[2] != "_"):
        win.append(cells[2])
    return (win)


def print_cells():
    print('---------')
    for index in range(3):
        line = '| ' + cells[index * 3] + ' ' + cells[index * 3 + 1] + ' ' + cells[index * 3 + 2] + ' |'
        print(line)
    print('---------')


def check_state():
    number_of_X = len([x for x in cells if x == "X"])
    number_of_O = len([x for x in cells if x == "O"])

    if abs(number_of_X - number_of_O) > 1:
        return False
        # print("Impossible")
    else:
        win = (checkWin())
        if len(win) == 0:
            if "_" in cells:
                return False
                # print("Game not finished")
            else:
                print("Draw")
                return True
        elif len(win) == 1:
            print(win[0] + " wins")
            return True
        else:
            return False
            # print("Impossible")


def check_coordinates(coordinates):
    if coordinates[0].isnumeric() == False:
        print("You should enter numbers!")
        return False
    if len(coordinates) != 2:
        print("You should enter 2 numbers!")
        return False
    if int(coordinates[0]) < 1 or int(coordinates[0]) > 3 or int(coordinates[1]) < 1 or int(coordinates[1]) > 3:
        print("Coordinates should be from 1 to 3!")
        return False
    if cells[(int(coordinates[0]) - 1) * 3 + (int(coordinates[1]) - 1)] != "_":
        print("This cell is occupied! Choose another one!")
        return False
    return True


print_cells()
mark = "X"
while True:
    coordinates = input('Enter the coordinates:').split()
    while check_coordinates(coordinates) == False:
        coordinates = input('Enter the coordinates:').split()
    cells[(int(coordinates[0]) - 1) * 3 + (int(coordinates[1]) - 1)] = mark
    print_cells()
    if check_state():
        break
    else:
        if mark == "X":
            mark = "O"
        else:
            mark = "X"
