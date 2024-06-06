import random

class Ship:
    def __init__(self, coordinates):
        self.coordinates = coordinates

class Board:
    def __init__(self, size):
        self.size = size
        self.ships = []

    def place_ship(self, ship):
        self.ships.append(ship)

def print_board(board):
    for row in board:
        print(" ".join(row))

def generate_board(size):
    return [["O" for _ in range(size)] for _ in range(size)]

def is_valid_move(board, x, y):
    return 0 <= x < len(board) and 0 <= y < len(board)

def is_hit(board, x, y, ships):
    for ship in ships:
        if (x, y) in ship.coordinates:
            return True
    return False

def check_victory(board):
    for row in board:
        if any(cell == "O" for cell in ship.cells):
            return False
    return True

def main():
    board_size = 6
    player_board = generate_board(board_size)
    computer_board = generate_board(board_size)

    player_ships = [Ship([(0, 0), (1, 0), (2, 0)]), Ship([(0, 1), (0, 2)])]
    computer_ships = [Ship([(random.randint(0, 3), random.randint(0, 5)) for _ in range(3)]),
Ship([(random.randint(0, 5), random.randint(0, 5)) for _ in range(2)])]

    player_board_obj = Board(board_size)    
    computer_board_obj = Board(board_size)  

    for ship in player_ships:
        player_board_obj.place_ship(ship)

    for ship in computer_ships:
        computer_board_obj.place_ship(ship)

    while True:
        print("---- Player's Turn ----")
        print("Player's Board:")
        print_board(player_board)
        input_coords = input("Enter coordinates to shoot (x y): ")
        x, y = map(int, input_coords.replace(',', '').split())

        if is_hit(computer_board_obj, x, y, computer_board_obj.ships):
            print("Hit!")
            computer_board[y][x] = "X"
            if check_victory(computer_board_obj.ships):
                print("Player wins!")
                break
        else:
            print("Miss!")
            computer_board[y][x] = "T"  

        print("---- Computer's Turn ----")
        computer_x, computer_y = random.randint(0, 5), random.randint(0, 5)
        if is_hit(player_board_obj, computer_x, computer_y, player_board_obj.ships):
            print("Computer hit at", (computer_x, computer_y))
            player_board_obj[computer_y][computer_x] = "X"
            if check_victory(player_board_obj):
                print("Computer wins!")
                break
        else:
            print("Computer missed at", (computer_x, computer_y))
            player_board[computer_y][computer_x] = "T"

if __name__ == "__main__":
 main()