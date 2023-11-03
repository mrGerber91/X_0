from colorama import init
from colorama import Fore
from colorama import Back

# Инициализируем colorama
init()

# Создаем пустое игровое поле
board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

# Определяем игроков
player1 = Fore.RED +'X'+ Fore.RESET
player2 = Fore.GREEN +'O'+ Fore.RESET

# Функция для отображения игрового поля
def display_board(board):
    for row in board:
        print(Back.YELLOW +'|'.join(row)+Back.RESET)

# Функция для проверки выигрышной комбинации
def check_winner(board, player):
    # Проверяем горизонтальные и вертикальные линии
    for i in range(3):
        if (board[i] == [player, player, player] or
             [board[0][i], board[1][i], board[2][i]] == [player, player, player]):
            return True
    # Проверяем диагонали
    if ([board[0][0], board[1][1], board[2][2]] == [player, player, player] or
             [board[2][0], board[1][1], board[0][2]] == [player, player, player]):
        return True
    return False

# Основной игровой цикл
current_player = player1
while True:
    display_board(board)

    # Ход игрока
    print(f"Ходит игрок {current_player}")
    row = int(input("Введите номер строки (от 0 до 2): "))
    col = int(input("Введите номер столбца (от 0 до 2): "))

    # Проверка корректности введенных данных
    if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != '-':
        print("Некорректный ход, повторите попытку!")
        continue

    # Записываем ход игрока на игровое поле
    board[row][col] =  current_player

    # Проверяем победителей
    if check_winner(board, current_player):
        display_board(board)
        print(f"Игрок {current_player} победил!")
        break

    # Проверяем ничью
    if all([cell != '-' for row in board for cell in row]):
        display_board(board)
        print("Игра окончена вничью!")
        break

    # Переключаем игрока
    current_player = player1 if current_player == player2 else player2