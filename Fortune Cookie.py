import random

# List of fortunes
fortunes = [
    "Great opportunities are coming your way.",
    "Today is a perfect day to learn something new.",
    "A surprise will make you smile soon.",
    "Believe in yourself, and success will follow.",
    "Good news is on its way.",
    "Your hard work will pay off.",
    "Adventure is waiting for you.",
    "Happiness begins with a positive mindset.",
    "A new friendship will brighten your day.",
    "Every challenge is a chance to grow."
]

# Lucky colors
colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink"]

# Lucky emojis
emojis = ["🍀", "🌟", "😊", "🎉", "💖", "✨", "😄"]

print("🥠 Welcome to the Fortune Cookie Game!")

while True:
    input("\nPress Enter to open your fortune...")

    print("\n✨ Your Fortune:")
    print(random.choice(fortunes))
    print(f"🍀 Lucky Number: {random.randint(1, 99)}")
    print(f"🎨 Lucky Color: {random.choice(colors)}")
    print(f"😊 Lucky Emoji: {random.choice(emojis)}")

    again = input("\nOpen another fortune? (y/n): ").lower()

    if again != "y":
        print("\n👋 Thanks for playing! Have a wonderful day!")
        break