import time
import random

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting with moderate hunger
        self.energy = 5  # Starting with moderate energy
        self.happiness = 5  # Starting with moderate happiness
        self.tricks = []  # List to store learned tricks
        self.mood = "happy"  # New attribute: mood
        self.favorite_food = random.choice(["fish", "meat", "vegetables", "treats"])  # New attribute: favorite food
        self.age = 0  # New attribute: age
        self.experience = 0  # New attribute: experience points

    def eat(self):
        """Reduces hunger by 3 points and increases happiness by 1"""
        if self.hunger >= 3:
            self.hunger -= 3
        else:
            self.hunger = 0
        
        # Bonus happiness if eating favorite food
        food = input(f"What would you like to feed {self.name}? (fish/meat/vegetables/treats): ").lower()
        if food == self.favorite_food:
            self.happiness = min(self.happiness + 3, 10)
            print(f"🎉 {self.name} loves {food}! Extra happiness boost!")
        else:
            self.happiness = min(self.happiness + 1, 10)
        
        self.experience += 1
        time.sleep(2)
        print(f"{self.name} has eaten {food}🎉.")
        time.sleep(1)

    def sleep(self):
        """Increases energy by 5 points"""
        self.energy = min(self.energy + 5, 10)
        self.age += 0.1  # Pet ages a bit when sleeping
        self.experience += 0.5
        time.sleep(1)
        print(f"{self.name} has slept💤💤.")
        self._check_mood()

    def play(self):
        """Decreases energy by 2, increases happiness by 2, and increases hunger by 1"""
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)
            self.experience += 2
            print(f"You played with {self.name}!")
            self._check_mood()
        else:
            print(f"{self.name} is too tired to play😔.")

    def train(self, trick):
        """Teaches the pet a new trick"""
        if trick in self.tricks:
            print(f"{self.name} already knows '{trick}'.")
        else:
            # Training success depends on pet's energy and happiness
            success_chance = (self.energy + self.happiness) / 20
            if random.random() < success_chance:
                self.tricks.append(trick)
                self.experience += 5
                print(f"\nSuccessfully taught {self.name} the trick '{trick}🎉'!")
                time.sleep(4)
            else:
                print(f"\n{self.name} couldn't learn the trick this time. Try again when they're more rested and happy!")
                time.sleep(4)

    def show_tricks(self):
        """Displays all learned tricks"""
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet😔.")
        else:
            print(f"\n{self.name}'s tricks (Experience Level: {int(self.experience)}):")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. 🎃 {trick}")

    def _check_mood(self):
        """Updates pet's mood based on current stats"""
        if self.happiness >= 8 and self.energy >= 8:
            self.mood = "ecstatic"
        elif self.happiness >= 6 and self.energy >= 6:
            self.mood = "happy"
        elif self.happiness >= 4 and self.energy >= 4:
            self.mood = "content"
        elif self.happiness >= 2 and self.energy >= 2:
            self.mood = "grumpy"
        else:
            self.mood = "miserable"

    def get_status(self):
        """Prints the current state of the pet"""
        self._check_mood()
        print(f"\n{self.name}'s current status:")
        print(f"🍚 Hunger: {self.hunger}/10")
        print(f"⚡ Energy: {self.energy}/10")
        print(f"🐱 Happiness: {self.happiness}/10")
        print(f"😊 Mood: {self.mood}")
        print(f"🎓 Experience: {int(self.experience)}")
        print(f"🎂 Age: {self.age:.1f} years")
        print(f"❤️ Favorite Food: {self.favorite_food}")
        print(f"🎃 Tricks: {', '.join(self.tricks) if self.tricks else f'{self.name} doesn\'t know any tricks yet.'}")
        time.sleep(5)