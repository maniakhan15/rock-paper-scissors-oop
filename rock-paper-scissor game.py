import random
class Player:
    def __init__(self, name):
        self.name = name
        self.choice = ""
        self.score = 0

    def make_choice(self):
        """Get and validate the player's choice."""
        while True:
            choice = input("Choose rock, paper or scissors: ").lower()

            if choice in ["rock", "paper", "scissors"]:
                self.choice = choice
                break
            else:
                print("Invalid choice! Please choose rock, paper or scissors.")

class Computer(Player):
    def __init__(self):
        super().__init__("Computer")

    def make_choice(self, choices):
        """Randomly select a choice for the computer."""
        self.choice = random.choice(choices)

class Game:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.player = Player("Player")
        self.computer = Computer()

    def determine_winner(self):
        """Determine the winner of the current round."""
        if self.player.choice == self.computer.choice:
            return "tie"

        if (
            (self.player.choice == "rock" and self.computer.choice == "scissors")
            or
            (self.player.choice == "paper" and self.computer.choice == "rock")
            or
            (self.player.choice == "scissors" and self.computer.choice == "paper")
        ):
            return "player"

        return "computer"

    def display_score(self):
        """Display the current score."""
        print(
            "Score: Player", self.player.score,
            "-", "Computer", self.computer.score
        )

    def play_round(self):
        """Play one round of the game."""

        print("\n" + "=" * 35)
        print("           NEW ROUND")
        print("=" * 35)

        self.player.make_choice()
        self.computer.make_choice(self.choices)

        print("\nYou chose:", self.player.choice)
        print("Computer chose:", self.computer.choice)

        winner = self.determine_winner()

        if winner == "tie":
            print("\nIt's a tie!")

        elif winner == "player":
            print(
                "\nYou win!",
                self.player.choice,
                "beats",
                self.computer.choice + "."
            )
            self.player.score += 1

        else:
            print(
                "\nComputer wins!",
                self.computer.choice,
                "beats",
                self.player.choice + "."
            )
            self.computer.score += 1

        self.display_score()

    def start(self):
        """Start and manage the game."""

        print("=" * 35)
        print("      ROCK PAPER SCISSORS")
        print("=" * 35)

        while True:
            self.play_round()

            play_again = input("\nPlay again? (yes/no): ").lower()

            if play_again != "yes":
                break

        print("\n" + "=" * 35)
        print("           FINAL SCORE")
        print("=" * 35)

        self.display_score()
        print("Thanks for playing!")

game = Game()
game.start()
