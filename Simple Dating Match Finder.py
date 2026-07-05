# Simple Dating Match Finder

print("❤️ Welcome to the Dating Match Finder ❤️\n")

name1 = input("Enter First Person's Name: ")
age1 = int(input("Enter First Person's Age: "))
hobby1 = input("Enter First Person's Favorite Hobby: ").lower()
food1 = input("Enter First Person's Favorite Food: ").lower()

print("\n-----------------------------\n")

name2 = input("Enter Second Person's Name: ")
age2 = int(input("Enter Second Person's Age: "))
hobby2 = input("Enter Second Person's Favorite Hobby: ").lower()
food2 = input("Enter Second Person's Favorite Food: ").lower()

score = 0

# Age Compatibility
if abs(age1 - age2) <= 3:
    score += 40
elif abs(age1 - age2) <= 5:
    score += 20

# Hobby Match
if hobby1 == hobby2:
    score += 30

# Food Match
if food1 == food2:
    score += 30

print("\n❤️ Match Result ❤️")
print(f"{name1} ❤️ {name2}")
print(f"Compatibility Score: {score}%")

if score >= 80:
    print("Excellent Match! 💕")
elif score >= 50:
    print("Good Match! 😊")
else:
    print("You have different interests. Friendship could still be a great fit! 🤝")