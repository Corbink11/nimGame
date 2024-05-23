class NimGame:
    def __init__(self, rows):
        self.rows = rows

    def evaluate(self):
        return sum(self.rows)

    def make_move(self, row, stones):
        if 0 <= row < len(self.rows) and 0 < stones <= self.rows[row]:
            self.rows[row] -= stones
            return True
        return False

    def game_over(self):
        return all(row == 0 for row in self.rows)

def compute_optimal_move(game):
    xor_sum = 0
    for stones in game.rows:
        xor_sum ^= stones

    for i, stones in enumerate(game.rows):
        target = stones ^ xor_sum
        if target < stones:
            return i, stones - target

def play_nim():
    num_rows = int(input("Enter the number of rows: "))
    rows = []

    for i in range(num_rows):
        stones = int(input(f"Enter the number of stones in row {i}: "))
        rows.append(stones)

    game = NimGame(rows)
    player = 1

    while not game.game_over():
        if player == 1:
            print(f"Current state: {game.rows}")
            row = int(input(f"Player {player}, choose a row (0 to {len(game.rows) - 1}): "))
            stones = int(input(f"Player {player}, choose stones to remove: "))
            if game.make_move(row, stones):
                player = 2
            else:
                print("Invalid move. Try again.")
        else:
            row, stones = compute_optimal_move(game)
            print(f"Computer chooses row {row} and removes {stones} stones.")
            game.make_move(row, stones)
            player = 1

    winner = "Player" if player == 1 else "Computer"
    actual_winner = "Computer" if winner == "Player" else "Player"
    print(f"{actual_winner} wins!")

if __name__ == "__main__":
    play_nim()