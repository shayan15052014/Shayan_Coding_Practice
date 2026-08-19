pet = "Storm"


def show_menu():
    print("\n===== MY VIRTUAL PET =====")
    print("1. Feed Pet")
    print("2. Play with Pet")
    print("3. Check Status")
    print("4. Exit")


def feed_pet(hunger):
    hunger = hunger + 10

    if hunger > 100:
        hunger = 100

    print(f"You fed {pet}! Yum!")
    return hunger


def play_with_pet(happiness):
    happiness = happiness + 10

    if happiness > 100:
        happiness = 100

    print(f"You played with {pet}! Fun!")
    return happiness


def check_status(hunger, happiness):
    print(f"\n{pet}'s Status:")
    print(f"Hunger: {hunger} / 100")
    print(f"Happiness: {happiness} / 100")


hunger = 50
happiness = 50

print(f"Welcome! Your virtual pet's name is {pet}!")

while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        hunger = feed_pet(hunger)

    elif choice == "2":
        happiness = play_with_pet(happiness)

    elif choice == "3":
        check_status(hunger, happiness)

    elif choice == "4":
        print(f"Bye! Take care of {pet} again soon!")
        break

    else:
        print("Invalid option. Please choose 1, 2, 3, or 4.")

    if happiness == 100:
        print(f"Congrats! {pet} has played to its heart's content. It doesn't want to play anymore.")

    if hunger == 100:
        print(f"Congrats! {pet} has eaten enough. It doesn't want to eat anymore.") 



#_____________________________________That's all for now______________________________________