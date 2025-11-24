import random

money_tree = [
    "₹1,000", "₹2,000", "₹3,000", "₹5,000", "₹10,000",
    "₹20,000", "₹40,000", "₹80,000", "₹1,60,000", "₹3,20,000",
    "₹6,40,000", "₹12,50,000", "₹25,00,000", "₹50,00,000", "₹1 CRORE"
]

# 15 QUESTIONS
questions = [
    {
        "question": "Which is the largest continent in the world?",
        "options": ["A) Africa", "B) Asia", "C) Europe", "D) Australia"],
        "answer": "B"
    },
    {
        "question": "Who wrote the Indian National Anthem?",
        "options": ["A) Rabindranath Tagore", "B) Bankim Chandra", "C) Mahatma Gandhi", "D) Sarojini Naidu"],
        "answer": "A"
    },
    {
        "question": "Which gas do plants absorb?",
        "options": ["A) Oxygen", "B) Carbon dioxide", "C) Nitrogen", "D) Hydrogen"],
        "answer": "B"
    },
    {
        "question": "Who invented the telephone?",
        "options": ["A) Edison", "B) Alexander Graham Bell", "C) Tesla", "D) Einstein"],
        "answer": "B"
    },
    {
        "question": "Which is the smallest prime number?",
        "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
        "answer": "C"
    },
    {
        "question": "Which is the longest river in the world?",
        "options": ["A) Amazon", "B) Ganga", "C) Nile", "D) Yangtze"],
        "answer": "C"
    },
    {
        "question": "Which device is used to measure temperature?",
        "options": ["A) Barometer", "B) Thermometer", "C) Hygrometer", "D) Speedometer"],
        "answer": "B"
    },
    {
        "question": "Which is the fastest land animal?",
        "options": ["A) Cheetah", "B) Tiger", "C) Leopard", "D) Lion"],
        "answer": "A"
    },
    {
        "question": "Which country gifted the Statue of Liberty to the USA?",
        "options": ["A) France", "B) Germany", "C) Canada", "D) Italy"],
        "answer": "A"
    },
    {
        "question": "What is the chemical symbol of gold?",
        "options": ["A) Go", "B) Au", "C) Ag", "D) Gd"],
        "answer": "B"
    },
    {
        "question": "Where is the Taj Mahal located?",
        "options": ["A) Delhi", "B) Jaipur", "C) Agra", "D) Lucknow"],
        "answer": "C"
    },
    {
        "question": "Which planet has the most moons?",
        "options": ["A) Earth", "B) Mars", "C) Saturn", "D) Jupiter"],
        "answer": "C"
    },
    {
        "question": "Who is known as the Father of Computers?",
        "options": ["A) Alan Turing", "B) Charles Babbage", "C) Bill Gates", "D) Tim Berners-Lee"],
        "answer": "B"
    },
    {
        "question": "Which is the national sport of India?",
        "options": ["A) Cricket", "B) Hockey", "C) Football", "D) Kabaddi"],
        "answer": "B"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Orca"],
        "answer": "B"
    }
]

# Lifelines (usable once per game)
lifelines = {
    "50-50": True,
    "audience": True,
    "skip": True
}

def lifeline_5050(correct):
    options = ['A', 'B', 'C', 'D']
    options.remove(correct)
    removed = random.sample(options, 2)
    return removed

def audience_poll(correct):
    poll = {'A': random.randint(1, 20), 'B': random.randint(1, 20),
            'C': random.randint(1, 20), 'D': random.randint(1, 20)}
    poll[correct] += random.randint(30, 40)
    return poll

def play_game():
    print("\n🎉 Welcome to *Cash Me If You Can*! Let’s begin...\n")

    for index, q in enumerate(questions):
        print(f"\nQuestion {index+1} for {money_tree[index]}")
        print(q["question"])
        for opt in q["options"]:
            print(opt)

        while True:
            print("\nEnter answer (A/B/C/D) or use lifeline:")

            # Show available lifelines
            print("Available Lifelines: ", end="")
            available = []
            if lifelines["50-50"]:
                available.append("50-50 (type: 50)")
            if lifelines["audience"]:
                available.append("Audience Poll (type: AUD)")
            if lifelines["skip"]:
                available.append("Skip (type: SKIP)")
            if not available:
                available.append("None")

            print(", ".join(available))
            print("Type 'QUIT' to exit game.")

            choice = input("Your choice: ").upper()

            # Quit the game
            if choice == "QUIT":
                print("\nYou quit! You won:", money_tree[index-1] if index > 0 else "₹0")
                return

            # 50-50 Lifeline
            if choice == "50":
                if lifelines["50-50"]:
                    removed = lifeline_5050(q["answer"])
                    print("Removed options:", removed)
                    lifelines["50-50"] = False
                else:
                    print("❌ 50-50 already used!")
                continue

            # Audience Poll
            elif choice == "AUD":
                if lifelines["audience"]:
                    poll = audience_poll(q["answer"])
                    print("\n📊 Audience Poll:")
                    for k, v in poll.items():
                        print(f"{k}: {v}%")
                    lifelines["audience"] = False
                else:
                    print("❌ Audience Poll already used!")
                continue

            # Skip Lifeline
            elif choice == "SKIP":
                if lifelines["skip"]:
                    print("Skipped! Moving to next question...")
                    lifelines["skip"] = False
                    break
                else:
                    print("❌ Skip already used!")
                continue

            # Normal Answer
            elif choice in ["A", "B", "C", "D"]:
                if choice == q["answer"]:
                    print("✅ Correct!")
                    if index == 14:
                        print("\n🎉 YOU WON 1 CRORE! 🎉")
                    break
                else:
                    print("❌ Wrong answer!")
                    print("Correct answer was:", q["answer"])
                    print("You won:", money_tree[index-1] if index > 0 else "₹0")
                    return

            else:
                print("Invalid choice! Try again.")
                continue

    print("\n🎉 CONGRATULATIONS! You completed all 15 questions!")
    print("🏆 Total Winnings: 1 CRORE!")

play_game()