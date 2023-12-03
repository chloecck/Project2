20012820
Chuqing Ke

Github URL: https://github.com/chloecck/Project2


- an estimate of how many hours you spent on the project: 3 hours


- a description of how you tested your code
    Run "python3 adventure.py test.map"

- any bugs or issues you could not resolve
    None that I'm awared of.
- an example of a difficult issue or bug and how you resolved
    I had a problem understanding the game initially, so I googled some game of adventure example, and quickly understood the concept especially through the demo of wiki.







Extensions: python3 adventure.py loop.map

    1. help function
python3 adventure.py loop.map
> A white room

You are in a simple room with white walls.

Items: blue key

Exits: north northwest

What would you like to do? help
You can run the following command:
  drop ...
  get ...
  go ...
  help
  inventory
  load_map ...
  look
What would you like to do? 


    2. drop function

> A white room

You are in a simple room with white walls.

Items: blue key

Exits: north northwest

What would you like to do? get blue key
You pick up the blue key.
What would you like to do? drop blue key
You dropped the blue key.
What would you like to do? 

    3. a locked doors featured that can be open with specific keys.
> A white room

You are in a simple room with white walls.

Items: blue key

Exits: north northwest

What would you like to do? get blue key
You pick up the blue key.
What would you like to do? go north
Found the key in the bag!, unlocking your door now!
You go north.

> A blue room

This room is simple, too, but with blue walls.

Items: green key

Exits: west south

What would you like to do? get green key
You pick up the green key.
What would you like to do? go west
Found the key in the bag!, unlocking your door now!
You go west.

> A green room

You are in a simple room, with bright green walls.

Items: banana, bandana, bellows, deck of cards, red key

Exits: east southeast

What would you like to do? get red key
You pick up the red key.
What would you like to do? go southeast
You go southeast.

> A white room

You are in a simple room with white walls.

Exits: north northwest

What would you like to do? go northwest
Found the key in the bag!, unlocking your door now!
You go northwest.

> A red room

This room is fancy. It's red!

Items: rose

Exits: north west

What would you like to do? get rose
You pick up the rose.
Yes finally, you reach the goal by getting the rose!
What would you like to do? r