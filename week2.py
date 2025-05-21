# === PART 1: Tic-Tac-Toe AI Game ===

# Define the game board
board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        print('|'.join(board[i*3:(i+1)*3]))
        if i < 2:
            print('-'*5)

def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    return any(all(board[i] == player for i in cond) for cond in win_conditions)

def check_tie():
    return all(cell != ' ' for cell in board)

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("That spot is taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Choose a number from 1 to 9.")

def ai_move():
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_win('O'):
                return
            board[i] = ' '
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_win('X'):
                board[i] = 'O'
                return
            board[i] = ' '
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            return

def play_game():
    print("Tic-Tac-Toe Game! You are X. AI is O.")
    print_board()
    while True:
        player_move()
        print_board()
        if check_win('X'):
            print("You win!")
            break
        if check_tie():
            print("It's a tie!")
            break
        ai_move()
        print("AI's move:")
        print_board()
        if check_win('O'):
            print("AI wins!")
            break
        if check_tie():
            print("It's a tie!")
            break

# Uncomment the line below to play the game
# play_game()

# === PART 2: Matplotlib Data Visualization ===

import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV data
data = pd.read_csv("C:/Users/Welcome Sir/Downloads/company_sales_data.csv")


# Exercise 1: Line plot of Total Profit
months = data['month_number']
profit = data['total_profit']

plt.figure(figsize=(10, 5))
plt.plot(months, profit, marker='o', color='green', linestyle='-', linewidth=2)
plt.title('Company Profit per Month')
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.grid(True)
plt.savefig("profit_line_plot.png")  # Save plot as image
plt.show()

# Exercise 2: Subplot for Bathing Soap and Facewash Sales
soap_sales = data['bathingsoap']
facewash_sales = data['facewash']

plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(months, soap_sales, label='Bathing Soap', color='blue', marker='o')
plt.title('Bathing Soap Sales')
plt.ylabel('Sales Units')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(months, facewash_sales, label='Facewash', color='red', marker='x')
plt.title('Facewash Sales')
plt.xlabel('Month')
plt.ylabel('Sales Units')
plt.grid(True)

plt.tight_layout()
plt.savefig("soap_facewash_subplots.png")
# Save subplot image
plt.show()
