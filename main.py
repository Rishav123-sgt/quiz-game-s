class QuizGame:
    def __init__(self):
        self.questions = [
            {"q": "What is the capital of India?", "a": "Delhi"},
            {"q": "What is 5 + 3?", "a": "8"},
            {"q": "Who developed Python?", "a": "Guido van Rossum"},
        ]
        self.score = 0

    def start(self):
        print("Welcome to Quiz Game!\n")
        for i, item in enumerate(self.questions, 1):
            ans = input(f"Q{i}. {item['q']} ")
            if ans.strip().lower() == item["a"].lower():
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! Answer: {item['a']}\n")

        print(f"Final Score: {self.score}/{len(self.questions)}")

if __name__ == "__main__":
    game = QuizGame()
    game.start()
