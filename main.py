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
    "empty_command": "You didn't type anything. Type 'help' to see what you can type.",
    "no_exit": "You cannot go {direction} from here. Look at the room description for the exits.",
    "unknown_command": "I don't know the command '{command}'. Type 'help' to see what you can type.",
}

COMMANDS = {
    "go <direction>": "move to the next room, like 'go north'",
    "run <direction>": "rush to the next room, like 'run south'",
    "wait": "stay in this room for a moment",
    "help": "show the commands you can type",
    "quit": "stop the game",
}


def show_help():
    print("You can type:")
    for command, text in COMMANDS.items():
        print(f"  {command:<16} {text}")


def main():
    current = "hall"
    print("Welcome! Type 'help' to see what you can type, or 'quit' to stop.")
    while True:
        print()
        print(ROOMS[current]["description"])
        command = input("> ").strip().lower()
        if command == "":
            print(ERRORS["empty_command"])
        elif command == "quit":
            print("Goodbye!")
            break
        elif command == "help":
            show_help()
        elif command == "wait":
            print("You wait for a moment. Nothing happens.")
        elif command.startswith("go ") or command.startswith("run "):
            verb, direction = command.split(" ", 1)
            next_room = ROOMS[current]["exits"].get(direction)
            if next_room:
                if verb == "run":
                    print(f"You run {direction}!")
                current = next_room
            else:
                print(ERRORS["no_exit"].format(direction=direction))
        else:
            print(ERRORS["unknown_command"].format(command=command))


if __name__ == "__main__":
    main()
