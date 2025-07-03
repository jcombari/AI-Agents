from game import TicTacToe
from agent import AIPlayer

class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            try:
                square = int(input(f"{self.letter}'s turno. Ingresa un movimiento (0-8): "))
                if square not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Movimiento inválido. Intenta de nuevo.")
        return square

def play(game, x_player, o_player):
    game.print_board()
    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            print(f"\n{letter} hace una jugada en el cuadrado {square}")
            game.print_board()
            print('')

            if game.current_winner:
                print(f"¡{letter} gana!")
                return letter
            letter = 'O' if letter == 'X' else 'X'
    print("¡Empate!")

if __name__ == '__main__':
    print("Elige modo de juego:")
    print("1: Humano vs IA")
    print("2: IA vs IA")
    mode = input("Selecciona (1 o 2): ").strip()

    if mode == '1':
        x_player = HumanPlayer('X')
        o_player = AIPlayer('O')
    else:
        x_player = AIPlayer('X')
        o_player = AIPlayer('O')

    game = TicTacToe()
    play(game, x_player, o_player)