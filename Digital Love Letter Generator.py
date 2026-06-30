import random

compliments = [
    "Your smile brightens every day.",
    "You make my life more beautiful.",
    "Every moment with you is special.",
    "You are my favorite person.",
    "You inspire me to be a better person.",
    "Being with you feels like home."
]

closing_lines = [
    "Forever yours ❤️",
    "With all my love 💖",
    "Always thinking of you 🌹",
    "Yours, today and always ❤️"
]

print("=== Digital Love Letter Generator ===\n")

name = input("Recipient's name: ")
sender = input("Your name: ")
memory = input("A favorite memory together: ")
wish = input("A dream for your future together: ")

letter = f"""
Dear {name},

From the day you came into my life, everything has felt brighter.
{random.choice(compliments)}

One of my favorite memories is:
"{memory}"

I look forward to {wish}. Every day with you is a gift, and I am grateful for your kindness, laughter, and love.

No matter what tomorrow brings, I hope we continue creating beautiful memories together.

{random.choice(closing_lines)}
{sender}
"""

print("\n" + "=" * 50)
print(letter)
print("=" * 50)

filename = f"Love_Letter_For_{name.replace(' ', '_')}.txt"

with open(filename, "w", encoding="utf-8") as file:
    file.write(letter)

print(f"\nYour love letter has been saved as '{filename}'.")