def main():
    
    print('')
    print("----------------------")
    print("Let's play Py-Pac-Poe!")
    print("----------------------")
    print('')


    global board, turn

    board = {
        'a1': ' ', 'b1': ' ', 'c1': ' ', 
        'a2': ' ', 'b2': ' ', 'c2': ' ',
        'a3': ' ', 'b3': ' ', 'c3': ' '
    }

    turn = 'X'
    # count = 1
    
    # if count % 2 == 0:
    #     turn = 'O'
    # else:
    #     turn = 'X'

    player_choice = []

    def gridPrint():
        header = ['  ', 'A', 'B', 'C']
        row_1 = ['1)', board['a1'], board['b1'], board['c1']]
        row_2 = ['2)', board['a2'], board['b2'], board['c2']]
        row_3 = ['3)', board['a3'], board['b3'], board['c3']]
        print('')
        print(*header, sep="   ")
        print('')
        print(*row_1, sep="   ")
        print("    -----------")
        print(*row_2, sep="   ")
        print("    -----------")
        print(*row_3, sep="   ")
        print('')

    gridPrint()

    def playerOTurn():
        while True:
            move = input("Player O's move (example B2): ")
            if move in board:
                break
            else:
                print('Please enter a valid move. Player')
        return [move.lower(), 'O']
    
    def playerXTurn():
        while True:
            move = input("Player X's move (example B2): ")
            if move in board:
                break
            else:
                print('Please enter a valid move. ')
        return [move.lower(), 'X']

    count = 1
    while True:
        if count % 2 == 0:
            player_choice = playerOTurn()
        else:
            player_choice = playerXTurn()            

        def gridInsert(choice):
            print(choice)
            for i in board:
                if choice[0] == i and board[i] == ' ':
                    board[i] = choice[1]
            print(board)
            gridPrint()
                
        gridInsert(player_choice)
        count += 1
    
main()