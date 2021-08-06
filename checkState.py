def checkWin(cells):
    win = []
    for i in range(3):
        if (cells[i * 3] == cells[i * 3 + 1] and cells[i * 3] == cells[i * 3 + 2]):
            win.append(cells[i * 3])
        if (cells[i] == cells[i + 3] and cells[i] == cells[i + 6]):
            win.append(cells[i])
    if (cells[0] == cells[4] and cells[0] == cells[8]):
        win.append(cells[0])
    if (cells[2] == cells[4] and cells[2] == cells[6]):
        win.append(cells[0])
    return (win)


cells = input('Enter cells:')
print('---------')
for index in range(3):
    line = '| ' + cells[index * 3] + ' ' + cells[index * 3 + 1] + ' ' + cells[index * 3 + 2] + ' |'
    print(line)
print('---------')
number_of_X = len([x for x in cells if x == "X"])
number_of_O = len([x for x in cells if x == "O"])

if abs(number_of_X - number_of_O) > 1:
    print("Impossible")
else:
    win = (checkWin(cells))
    if len(win) == 0:
        if "_" in cells:
            print("Game not finished")
        else:
            print("Draw")
    elif len(win) == 1:
        print(win[0] + " wins")
    else:
        print("Impossible")
