import hashlib

def text_hash():
    text = input("Enter text: ")
    print("\nSHA-256 Hash:")
    print(hashlib.sha256(text.encode()).hexdigest())

def file_hash():
    filename = input("Enter file name: ")

    try:
        sha256 = hashlib.sha256()

        with open(filename, "rb") as file:
            while chunk := file.read(4096):
                sha256.update(chunk)

        print("\nSHA-256 Hash:")
        print(sha256.hexdigest())

    except FileNotFoundError:
        print("File not found.")

while True:
    print("\n===== HASH GENERATOR =====")
    print("1. Generate Text Hash")
    print("2. Generate File Hash")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        text_hash()

    elif choice == "2":
        file_hash()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")