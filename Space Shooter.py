# Space Shooter (No imports)

health = 5
score = 0

print("=== SPACE SHOOTER ===")
print("Commands:")
print("s = Shoot")
print("d = Dodge")
print("q = Quit")

while health > 0:
    enemy = input("\nEnemy ahead! (s/d/q): ").lower()

    if enemy == "s":
        print("Boom! Enemy destroyed!")
        score += 10

    elif enemy == "d":
        print("You dodged the enemy.")
        score += 5

    elif enemy == "q":
        print("You escaped the battle.")
        break

    else:
        print("Wrong command! Enemy hit you.")
        health -= 1

    print("Health:", health)
    print("Score:", score)

if health == 0:
    print("\nGAME OVER!")

print("Final Score:", score)