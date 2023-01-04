def print_tic_tac_toe(value):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

def single_game(cur_player):

    # Represents the Tic Tac Toe
    values = [' ' for x in range(9)]
    print(values)
    # Stores the positions occupied by X and O
    player_pos = {'X':[], 'O':[]}
    print("test")

    print_tic_tac_toe(values)

    while True:
        print_tic_tac_toe(values)

    #     try:
    #         print("Player ", cur_player, " turn. Which box? : ", end="")
    #         move = int(input())
    #     except ValueError:
    #         print("Wrong Input!!! Try Again")
    #         continue

    # # Sanity check for MOVE inout
    # if move < 1 or move > 9:
    #     print("Wrong Input!!! Try Again")
    #     continue

    # # Check if the box is not occupied already
    # if values[move-1] != ' ':
    #     print("Place already filled. Try again!!")
    #     continue

single_game(4)
