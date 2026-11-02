
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
    "empty_command": "You didn't type anything. Type 'go <direction>' to move, or 'quit' to stop.",
    "no_exit": "You cannot go {direction} from here. Look at the room description for the exits.",
    "unknown_command": "I don't know the command '{command}'. Type 'go <direction>' to move.",
}


def main():
    current = "hall"
    print("Welcome! Type 'go <direction>' to move, or 'quit' to stop.")
    while True:
        print()
        print(ROOMS[current]["description"])
        command = input("> ").strip().lower()
        if command == "":
            print(ERRORS["empty_command"])
        elif command == "quit":
            print("Goodbye!")
            break
        elif command.startswith("go "):
            direction = command[3:]
            next_room = ROOMS[current]["exits"].get(direction)
            if next_room:
                current = next_room
            else:
                print(ERRORS["no_exit"].format(direction=direction))
        else:
            print(ERRORS["unknown_command"].format(command=command))


if __name__ == "__main__":
    main()
