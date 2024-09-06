class RockPaperScissors:
    def __init__(self):
        self.Player1_score = 0
        self.Player2_score = 0

    def get_ready(self, player):
        ready = input(f"{player}, are you ready? (yes/no): ").strip().lower()
        if ready == "yes":
            print("Ok, let's go!")
        else:
            print("Clearly a born loser!" if player == "Player 1" else "I'm sorry, do you want your mummy? 👶")

    def get_move(self, player):
        return input(f"{player}, Select your move (R, P or S): ").strip().upper()

    def determine_winner(self, Player1, Player2):
        if Player1 == Player2:
            return "Draw"
        elif (Player1 == "R" and Player2 == "S") or (Player1 == "P" and Player2 == "R") or (Player1 == "S" and Player2 == "P"):
            return "Player 1"
        else:
            return "Player 2"

    def play_game(self):
        print("Epic 🥌, 📰, or ✂ Battle")
        print()
        print("""Welcome to this battle of Rock, Paper, Scissors! The winner of best of 3 
will be named 
The Ultimate Champion 🥇""")
        print()

        self.get_ready("Player 1")
        self.get_ready("Player 2")

        while self.Player1_score < 2 and self.Player2_score < 2:
            Player1 = self.get_move("Player 1")
            Player2 = self.get_move("Player 2")
            
            winner = self.determine_winner(Player1, Player2)
            
            if winner == "Draw":
                print("It's a draw!")
            elif winner == "Player 1":
                print("Player 1 wins this round!")
                self.Player1_score += 1
            else:
                print("Player 2 wins this round!")
                self.Player2_score += 1
            
            print(f"Current Score -> Player 1: {self.Player1_score}, Player 2: {self.Player2_score}")
            print()

        if self.Player1_score == 2:
            print("Player 1 is the Ultimate Champion 🥇!")
        else:
            print("Player 2 is the Ultimate Champion 🥇!")

game = RockPaperScissors()
game.play_game()
