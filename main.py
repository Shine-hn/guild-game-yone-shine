"""A tiny text adventure. Grow this world with your team!"""

ROOMS = {
    "hall": {
        "description": "You are in a quiet hall. A door leads north.",
        "exits": {"north": "garden"},
    },
    "garden": {
        "description": "You are in a garden full of strange flowers. The hall is to the south.",
        "exits": {"south": "hall"},
    },
}

ERRORS = {
    "no_exit": "You cannot go {direction} from here. Look at the room description for the exits.",
    "unknown_command": "error. you can't use this command. Shoud you use {command}. ",
    "unknown_item": "error. bad item name. Are you crasy? Try type {item}.",
    "no_money": "NO money! this item is {price}. Try check!",
    "empty_command": "Hey! Try you type!",
    "already_have": "Wow! You have already this {item}. Try check! ",
    "bag_full": "You bag is {limit}. Try check. "
}


def main():
    current = "hall"
    print("Welcome! Type 'go <direction>' to move, or 'quit' to stop.")
    while True:
        print()
        print(ROOMS[current]["description"])
        command = input("> ").strip().lower()
        if command == "quit":
            print("Goodbye!")
            break
        if command.startswith("go "):
            direction = command[3:]
            next_room = ROOMS[current]["exits"].get(direction)
            if next_room:
                current = next_room
            else:
                print("You cannot go that way.")
        else:
            print("I don't understand that.")


if __name__ == "__main__":
    main()
