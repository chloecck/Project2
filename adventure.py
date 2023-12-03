import sys
import json
import inspect


class Adventure():
    def __init__(self, map_file):
        self.map = self.load_map(map_file)
        self.bag = set()
        self.curr = 0

    def load_map(self, map_file):
        with open(map_file, 'r') as file:
            return json.load(file)

    def look(self):
        print("> " + self.map[self.curr]["name"] + "\n")
        print(self.map[self.curr]["desc"] + '\n')

        if "items" in self.map[self.curr] and len(self.map[self.curr]["items"]) != 0:
            print("Items: " + ', '.join(self.map[self.curr]["items"]) + '\n')

        # assume all rooms have exits
        print("Exits: " +
              ' '.join(list(self.map[self.curr]["exits"].keys())) + '\n')

    def inventory(self):
        if not self.bag:
            print("You're not carrying anything.")
            return
        print("Inventory:")
        for item in self.bag:
            print("  ", item)

    def get(self, item_name):
        if 'items' in self.map[self.curr] and item_name in self.map[self.curr]['items']:
            self.bag.add(item_name)
            self.bag = set(sorted(self.bag))
            self.map[self.curr]['items'].remove(item_name)
            print("You pick up the " + item_name + '.')
            if "rose" in self.bag and 'locked' in self.map[self.curr]:
                print("Yes finally, you reach the goal by getting the rose!")
        else:
            print("There's no", item_name, "anywhere.")

    def go(self, direction):
        if direction in self.map[self.curr]["exits"]:
            next = self.map[self.curr]["exits"][direction]
            if 'locked' in self.map[next]:
                open = (self.map[next]["locked"] == 0)
                if (self.map[next]["locked"] == 1):
                    for item in self.bag:
                        if item == self.map[next]["key"]:
                            print(
                                "Found the key in the bag!, unlocking your door now!")
                            open = True
                if not open:
                    print("Door is locked! You will be stay in the same room.")
                    return

            self.curr = next
            print("You go", direction + '.\n')
            return True
        else:
            print("There's no way to go " + direction + '.')
            return False

# extension
    def help(self):
        # Get all the functions other than init
        funcs = [f for f in dir(Adventure) if not f.startswith("__")]
        print("You can run the following command:")
        for f in funcs:
            # Return the value of the named attribute of object.
            func = getattr(Adventure, f)
            params = inspect.signature(func).parameters
            if len(params) > 1:
                print(' ', f, '...')
            else:
                print(' ', f)

# extension
    def drop(self, item):
        if item not in self.bag:
            print("You do not have the ", item, "in your inventory.")
        else:
            self.bag.remove(item)
            print("You dropped the " + item + '.')


def main():
    if len(sys.argv) != 2:
        print("Usage: python game.py <map_file>")
        sys.exit(1)

    map_file = sys.argv[1]
    game = Adventure(map_file)
    game.look()
    while True:
        try:
            command = input(
                "What would you like to do? ").strip().lower().split()
        except EOFError:
            print("\nUse 'quit' to exit.")
            continue
        except KeyboardInterrupt:
            print("Traceback (most recent call last):\n  ...\nKeyboardInterrupt")
            sys.exit(0)
    # Additional cleanup or exit logic can be added here
        # Continue with the game logic
        if not command:
            print("Please enter a command.")
            continue
        verb = command[0]
        if verb == 'go':
            if len(command) < 2:
                print("Sorry, you need to 'go' somewhere.")
                continue
            if game.go(' '.join(command[1:])):
                game.look()
            continue
        elif verb == 'look':
            game.look()
        elif verb == 'get':
            if len(command) < 2:
                print("Sorry, you need to 'get' something.")
                continue
            game.get(' '.join(command[1:]))
        elif verb == 'inventory':
            game.inventory()
        elif verb == 'quit':
            print("Goodbye!")
            sys.exit(0)
        elif verb == 'help':
            game.help()
        elif verb == 'drop':
            if len(command) < 2:
                print("Sorry, you need to 'drop' something.")
                continue
            game.drop(' '.join(command[1:]))
        else:
            print("Use 'quit' to exit.")


if __name__ == "__main__":
    import sys
    main()
