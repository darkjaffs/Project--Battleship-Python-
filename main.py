import random

from os import system, name

# Declaring Global Variable

array_size = None
background_array = [[0 for x in range(9)] for y in range(9)]
output_array = [[0 for x in range(9)] for y in range(9)]
input_choice = [0 for x in range(2)]


# clear function to clear screen


def clear():
    if name == "nt":
        x = system("cls")
    else:
        x = system("clear")


# Declaring Main Function where all the functions are called


def main():
    global array_size
    start = 10

    while start != 1:

        start = start_menu()

        if start == 2:
            return 0

        elif start == 3:
            print(" 1. Four Ships Have Been Hidden In Grid \n")
            print(" 2. A Carrier Ship Which Occupies 5 Spaces Has Been Hidden \n")
            print(" 3. A BattleShip Which Occupies 4 Spaces Has Been Hidden \n")
            print(" 4. Two Frigate Ships Which Occupies 2 Spaces Has Been Hidden \n")
            print(
                " 5. You Will Be Assigned Limited Number Of Shells To Complete The Task Of Destroying Them All \n"
            )
            print("  GoodLuck!!  ")

    while True:
        array_size = input(" Enter the size of array between 6 and 9: ")
        array_size = int(array_size)

        if int(array_size) >= 6 and int(array_size) <= 9:
            break

        else:
            print(" INVALID INPUT \n RETRY")

    print("\n")

    grid_size()

    print("")
    carrier_assignment()
    battleship_assignment()
    frigate_assignment()
    frigate_assignment()


    shells = prompt_statements()
    count = game_mechanics(shells)

    if count[0] == 4 and count[2] >= 4 and count[1] >= 3:
        final_ship_location()
        win_check(count)
        return 0

    final_ship_location()
    win_check(count)

    return 0


def start_menu():
    choice = 0

    print("-------- WELCOME TO THE BATTLESHIP --------")
    print("-_-_-_-_-_-_-_-   1. START GAME   -_-_-_-_-_-_-_-_-")
    print("-_-_-_-_-_-_-_-   2.    EXIT      -_-_-_-_-_-_-_-_-")
    print("-_-_-_-_-_-_-_-   3. Instructions -_-_-_-_-_-_-_-_-")

    choice = input("Enter Your Prefered Option: ")

    clear()

    return int(choice)


def grid_size():
    ASCII = 65
    global array_size
    global output_array
    column_array = [[0 for x in range(9)] for y in range(9)]
    row_array = [[0 for x in range(9)] for y in range(9)]
    index_number = 1

    # This will print index for columns

    for x in range(array_size):
        if ASCII == 65:
            # To get space before the first index

            print("    ", end="")

        column_array[0][x] = chr(ASCII)

        # Here we are printing the column grid

        print(f"{chr(ASCII)}   ", end="")

        ASCII = ASCII + 1

    for x in range(array_size):
        row_array[x][0] = index_number
        index_number = index_number + 1

    print("")

    for x in range(array_size):
        print(f"{row_array[x][0]}   ", end="")

        for y in range(array_size):
            output_array[x][y] = "-"
            print(f"{output_array[x][y]}   ", end="")

        print("")


# To assign carrier the spaces


def carrier_assignment():
    global array_size
    global background_array

    while True:
        random_carrier = random.randrange(array_size)

        # To confirm we don't go off grid
        try:
            if random_carrier + 1 < array_size:
                if random_carrier + 2 < array_size:
                    if random_carrier + 3 < array_size:
                        if random_carrier + 4 < array_size:
                            break
        except (ValueError, IndexError):
            continue

    random_number = random_carrier

    # randomly checking whether we should assign vertically or horizontally
    vh_choice = random.random()

    if vh_choice == 1:
        for x in range(5):
            background_array[random_carrier][random_number] = 2

            random_number = random_number + 1

    else:
        for x in range(5):
            background_array[random_number][random_carrier] = 2
            random_number = random_number + 1


# To assign the battleship spaces


def battleship_assignment():
    global array_size
    global background_array

    while True:
        random_battleship = random.randrange(0, array_size)
        random_number = random_battleship
        try:
            if background_array[random_battleship][random_number] == 0:
                if background_array[random_battleship][random_number + 2] == 0:
                    if background_array[random_battleship][random_number + 3] == 0:
                        if background_array[random_battleship][random_number + 4] == 0:
                            if random_battleship + 1 < array_size:
                                if random_battleship + 2 < array_size:
                                    if random_battleship + 3 < array_size:
                                        if random_battleship + 4 < array_size:
                                            break
        except (ValueError, IndexError):
            continue

    random_number = random_battleship

    vh_choice = random.random()

    if vh_choice == 1:
        for x in range(4):
            background_array[random_battleship][random_number] = 3

            random_number = random_number + 1

    else:
        for x in range(4):
            background_array[random_number][random_battleship] = 3
            random_number = random_number + 1


def frigate_assignment():
    global array_size
    global background_array

    while True:
        random_frigate = random.randrange(0, array_size)

        random_number = random_frigate

        try:
            if background_array[random_frigate][random_number] == 0:
                if background_array[random_frigate][random_number + 1] == 0:
                    if random_frigate + 1 < array_size:
                        break
        except (ValueError, IndexError):
            continue

    vh_choice = random.random()

    if vh_choice == 1:
        for x in range(2):
            background_array[random_frigate][random_number] = 1

            random_number = random_number + 1

    else:
        for x in range(2):
            background_array[random_number][random_frigate] = 1
            random_number = random_number + 1


# for giving prompt statements


def prompt_statements():
    global array_size

    ammo = (array_size * array_size) / 2

    print(
        f"---- Four Ships Have Been Hidden In The Grid And You Have Been Given {ammo} Shells To Destroy Them All ----"
    )
    print("---- Specify The Location Of The Ship According To The Grid Index ----")
    print("---- Good Luck!! ----")

    return int(ammo)


def user_input(user_index):
    input_column_index = 0
    input_row_index = 0

    list_index = [0 for x in range(2)]

    for x in range(2):
        ascii_input = user_index[x]

        ASCII_input = ord(ascii_input)

        if ASCII_input >= 65 and ASCII_input <= 90:
            for y in range(65, ASCII_input):
                input_column_index = input_column_index + 1

        elif ASCII_input >= 97 and ASCII_input <= 122:
            for z in range(97, ASCII_input):
                input_column_index = input_column_index + 1

        elif ASCII_input >= 49 and ASCII_input <= 57:
            for i in range(49, ASCII_input):
                input_row_index = input_row_index + 1

    list_index[0] = int(input_row_index)
    list_index[1] = int(input_column_index)

    return list_index


# This is used to print the updated grid everytime


def updated_grid():
    clear()

    global array_size
    global output_array

    column_array = [[0 for x in range(9)] for y in range(9)]
    row_array = [[0 for x in range(9)] for y in range(9)]
    index_number = 1
    ASCII = 65

    for x in range(array_size):
        if ASCII == 65:
            # To get space before the first index

            print("    ", end="")

        column_array[0][x] = chr(ASCII)

        # Here we are printing the column grid

        print(f"{chr(ASCII)}   ", end="")

        ASCII = ASCII + 1

    for x in range(array_size):
        row_array[x][0] = index_number
        index_number = index_number + 1

    print("")

    for x in range(array_size):
        print(f"{row_array[x][0]}   ", end="")

        for i in range(array_size):
            print(f"{output_array[x][i]}   ", end="")

        print("")


def game_mechanics(shells):
    global input_choice
    global background_array
    global output_array
    frigate_count = 0
    carrier_count = 0
    battleship_count = 0

    count = [0 for x in range(3)]

    for i in range(shells + 1):
        while True:
            try:
                input_choice[0], input_choice[1] = input(
                    "Enter the position you want to target with space: "
                ).split()
                index = user_input(input_choice)
            except (ValueError, IndexError, TypeError):
                print("INVALID INPUT, Try Again")
            else:
                break

        if background_array[index[0]][index[1]] == 0:
            output_array[index[0]][index[1]] = "m"
            print("")

            updated_grid()

            print(f" \n You Missed! (Remaining Shot: {shells - i} )")

        elif background_array[index[0]][index[1]] == 1:
            output_array[index[0]][index[1]] = "f"
            background_array[index[0]][index[1]] = 0
            frigate_count = frigate_count + 1

            print("")

            updated_grid()

            print(f" \n You HIT! (Remaining Shot: {shells - i} )")

            if frigate_count == 2 or frigate_count == 4:
                print("\n YOU DESTROYED A FRIGATE!!")

        elif background_array[index[0]][index[1]] == 2:
            output_array[index[0]][index[1]] = "c"
            background_array[index[0]][index[1]] = 0
            carrier_count = carrier_count + 1

            print("")

            updated_grid()

            print(f" \n You HIT! (Remaining Shot: {shells - i} )")

            if carrier_count == 3:
                print("YOU DESTROYED A CARRIERSHIP!!")

        elif background_array[index[0]][index[1]] == 3:
            output_array[index[0]][index[1]] = "b"
            background_array[index[0]][index[1]] = 0
            battleship_count = battleship_count + 1

            print("")

            updated_grid()

            print(f" \n You HIT! (Remaining Shot: {shells - i} )")

            if battleship_count == 4:
                print("YOU DESTROYED A BATTLESHIP!!")

        if frigate_count == 4 and battleship_count >= 4 and carrier_count >= 3:
            break

    count[0] = int(frigate_count)
    count[1] = int(battleship_count)
    count[2] = int(carrier_count)
    return count


def final_ship_location():
    global array_size
    global output_array
    global background_array

    for i in range(array_size):
        for j in range(array_size):
            if background_array[i][j] == 1:
                output_array[i][j] = "f"

            elif background_array[i][j] == 2:
                output_array[i][j] = "c"

            elif background_array[i][j] == 3:
                output_array[i][j] = "b"

    ASCII = 65

    column_array = [[0 for x in range(9)] for y in range(9)]
    row_array = [[0 for x in range(9)] for y in range(9)]
    index_number = 1

    # This will print index for columns

    for x in range(array_size):
        if ASCII == 65:
            # To get space before the first index

            print("    ", end="")

        column_array[0][x] = chr(ASCII)

        # Here we are printing the column grid

        print(f"{chr(ASCII)}   ", end="")

        ASCII = ASCII + 1

    for x in range(array_size):
        row_array[x][0] = index_number
        index_number = index_number + 1

    print("")

    for x in range(array_size):
        print(f"{row_array[x][0]}   ", end="")

        for y in range(array_size):
            print(f"{output_array[x][y]}   ", end="")

        print("\n")


def win_check(count):

    if count[0] == 4 and count[2] >= 4 and count[1] >= 3:
        print("\n CONGRATULATION YOU HAVE WON!!!")

    else:
        print("\n Unfortunately, you lost. Better luck next time!")


main()