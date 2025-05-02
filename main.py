import pet
import time
import random
"""
- This is a simple pet simulator program that allows users to create a pet and interact with it.
- The user can feed the pet, play with it, teach it tricks, and check its status.
- The program uses a class to represent the pet and its attributes, and it provides a simple text-based interface for user interaction.
- The program is designed to be easy to use and understand, making it suitable for beginners in programming.
- The program is written in Python and uses basic programming concepts such as classes, methods, and user input.
- The program is designed to be run in a terminal or command prompt, and it provides clear instructions for the user to follow.
"""

def loading(action, petName=""):
    """Simulate loading time for pet actions."""
    if action == "teach":
        print(f"Teaching {petName} the new trick", end="")
    else:
        print(f"{petName} is {action}ing", end="")
        for i in range(3):
            print(".", end="")
            time.sleep(0.5)
        print("")

def print_header():
    """Print a decorative header"""
    print("\n" + "="*50)
    print("🐾 Virtual Pet Simulator 🐾".center(50))
    print("="*50)

def print_menu():
    """Print the main menu"""
    print("\nWhat would you like to do?")
    print("1. 🍖 Feed your pet")
    print("2. ⚽ Play with your pet")
    print("3. ✍️  Teach your pet a trick")
    print("4. 📃 Check your pet's status")
    print("5. 😴 Allow your pet to sleep")
    print("6. 📃 Display all tricks your pet knows")
    print("7. 🎮 Play a mini-game")
    print("8. ❌ Exit")
    print("="*50)

def play_mini_game(pet):
    """Play a simple mini-game with the pet"""
    if pet.energy < 3:
        print(f"{pet.name} is too tired to play games right now.")
        return
    
    print("\nLet's play a number guessing game!")
    print(f"{pet.name} will think of a number between 1 and 10.")
    time.sleep(2)
    
    number = random.randint(1, 10)
    attempts = 3
    
    while attempts > 0:
        try:
            guess = int(input(f"Guess the number (attempts left: {attempts}): "))
            if guess == number:
                print(f"🎉 Correct! {pet.name} is impressed!")
                pet.happiness = min(pet.happiness + 2, 10)
                pet.experience += 3
                break
            else:
                attempts -= 1
                if attempts > 0:
                    print("Try again!")
        except ValueError:
            print("Please enter a valid number!")
    
    if attempts == 0:
        print(f"Game over! The number was {number}.")
        pet.happiness = max(pet.happiness - 1, 0)
    
    pet.energy = max(pet.energy - 2, 0)
    time.sleep(2)

def create_pet():
    """Guide the user through pet creation"""
    print_header()
    print("Welcome to the Virtual Pet Simulator!")
    print("Let's create your perfect pet companion!")
    
    # Pet type selection
    pet_types = {
        "1": "🐕 Dog",
        "2": "🐈 Cat",
        "3": "🐇 Rabbit",
        "4": "🐦 Bird",
        "5": "🐢 Turtle"
    }
    
    print("\nWhat type of pet would you like?")
    for key, value in pet_types.items():
        print(f"{key}. {value}")
    
    while True:
        try:
            pet_type_choice = input("\nEnter the number of your preferred pet type (1-5): ")
            if pet_type_choice in pet_types:
                pet_type = pet_types[pet_type_choice]
                break
            else:
                print("Please enter a valid number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Pet name selection
    print("\nNow, let's name your pet!")
    print("You can:")
    print("1. Choose your own name")
    print("2. Get a random name suggestion")
    
    while True:
        try:
            name_choice = input("\nHow would you like to name your pet? (1 or 2): ")
            if name_choice == "1":
                name = input("Enter your pet's name: ").strip()
                if not name:
                    print("Please enter a valid name.")
                    continue
                break
            elif name_choice == "2":
                # List of cute pet names
                random_names = [
                    "Luna", "Max", "Bella", "Charlie", "Lucy",
                    "Cooper", "Daisy", "Milo", "Lily", "Rocky",
                    "Zoe", "Bear", "Molly", "Duke", "Stella"
                ]
                name = random.choice(random_names)
                print(f"How about naming your pet {name}?")
                confirm = input("Do you like this name? (yes/no): ").lower()
                if confirm == "yes":
                    break
                else:
                    continue
            else:
                print("Please enter either 1 or 2.")
        except ValueError:
            print("Please enter a valid choice.")
    
    return name, pet_type

# Main program starts here
pet_name, pet_type = create_pet()
userPet = pet.Pet(pet_name)

print_header()
print(f"🎉 Congratulations! You have created a {pet_type} named {userPet.name}!")
print(f"Your pet's favorite food is {userPet.favorite_food}!")
time.sleep(2)
print("Now, let's see what you can do with your pet.")
time.sleep(2)

while True:
    print_header()
    print_menu()
    
    try:
        userChoice = int(input("Please choose an option (1-8): "))
        if userChoice < 1 or userChoice > 8:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 8.")
        time.sleep(2)
        continue

    if userChoice == 1:
        loading("feed", userPet.name)
        userPet.eat()
        userPet.get_status()
    elif userChoice == 2:
        loading("play", userPet.name)
        userPet.play()
        userPet.get_status()
    elif userChoice == 3:
        trick = input("🎃 Please enter the trick you want to teach your pet: ")
        loading("teach", userPet.name)
        if trick == "":
            print("You didn't enter a trick. Please try again.")
            time.sleep(2)
            continue
        elif len(trick) > 20:
            print("Trick name is too long. Please keep it under 20 characters.")
            time.sleep(2)
            continue
        elif len(trick) < 3:
            print("Trick name is too short. Please provide a name with at least 3 characters.")
            time.sleep(2)
            continue
        elif not trick.isalpha():
            print("Trick name should only contain letters.")
            time.sleep(2)
            continue
        userPet.train(trick)
        userPet.get_status()
    elif userChoice == 4:
        userPet.get_status()
    elif userChoice == 5:
        loading("sleep", userPet.name)
        userPet.sleep()
        time.sleep(2)
        userPet.get_status()
    elif userChoice == 6:
        userPet.show_tricks()
        time.sleep(2)
    elif userChoice == 7:
        play_mini_game(userPet)
        userPet.get_status()
    elif userChoice == 8:
        print("Thank you for using the Virtual Pet Simulator!")
        break

# Simulate closing the simulator
print("\nClosing the Pet simulator", end="")
for i in range(3):
    print(".", end="")
    time.sleep(1)
print("\nGoodbye! 👋") 