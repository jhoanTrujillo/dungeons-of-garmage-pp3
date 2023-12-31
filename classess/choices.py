class Event:
    """
    This is a class to construct event nodes which are contain the
    content of the story, the options presented, and the type of event.

    categoryf only need to be added when the event has consequences.
    It can take the strings: battle, heal, damage, ending.

    The types of events that a class can be are:

    damage: damages the player by 1
    heal: heals the character by 1
    battle: triggers the battle function in the utility.py The requirement
    should be an string with the name of an enemy from
    the enemies dictionary in characters.py.
    reward: Just like the battle category, you should provide an string
    with the name of the item you would like to append to the player items.
    alternative: in addition you should provide an array with two objects,
    and string and another array that follows the same format as other choices.
    """
    def __init__(self):
        self.text = ""
        self.options = []
        self.category = ""
        self.requirement = ""

    def add_values(self, text, options, category="", requirement=""):
        # Always provide text to display the players.
        self.text = text
        # Needs at least an empty array.
        self.options = options
        self.category = category
        self.requirement = requirement

    def add_option(self, option, next_node):
        """
        Allows to add option to any node.
        """
        self.options.append((option, next_node))


# declaring all events ensure easy of access
intro = Event()
# Dungeon Path
treasure_room = Event()
# Mimic ending is part of this path
library = Event()
armory = Event()
skeleton_fight = Event()
pythonmancer = Event()
# Underground path
cave = Event()
hold_breath = Event()
hide_in_shadows = Event()
interact_with_dwellers = Event()
sneak_from_dwellers = Event()
hostile_towards_dwellers = Event()
undertown = Event()
# Temple (last event for both path)
temple = Event()
heretic_slayer = Event()
cosplayer = Event()
trickster = Event()
the_pythonmancer = Event()
# Boss scenes
the_hand = Event()
the_hand_weaken = Event()
# Endings
mimic_ending = Event()
dead_by_battle = Event()
lamb = Event()
priest_of_hold = Event()
vanquisher = Event()
the_coward = Event()
massacre_by_mob = Event()
escape_route = Event()

# Intro add_values.
intro.add_values(
    """
    The unwelcoming smell of dust and mold fills the dark corridor.
    As you make your way through the hallway, you start to
    hear an unfamiliar noise. What would you do?
    """,
    [
        ("Run forward!", treasure_room),
        ("Analyse the sound", cave)
    ]
)

# Underground path
cave.add_values(
    """
    You fell down a dark abyss, eventually landing in a body of water.
    As you emerge, you can hear creatures in the distance, and the darkness
    gives way to a dim light.
    """,
    [
      ("hold your breath", hold_breath),
      ("Hide into the shadows", hide_in_shadows)
    ], "damage"
)

hold_breath.add_values(
    """
    As you hold your breath, you start to heal thanks to the spring.
    Of course, breathing is still an issue, so as you resurface,
    small fluffy cave dwellers look at you in awe.
    """,
    [
        ("*yell* I'm that who reigns in the depths", interact_with_dwellers),
        ("Leave water, and punch a dweller", hostile_towards_dwellers)
    ], "heal"
)

hide_in_shadows.add_values(
    """
    You leave the water and hide in the shadows, in between rocks.
    You notice small fluffy creatures with little torches
    approaching the body of water. They look at each other and shrug
    """,
    [
        ("Sneak around from the creatures", sneak_from_dwellers),
        ("*Show yourself* ...Hello?.", interact_with_dwellers)
    ]
)

interact_with_dwellers.add_values(
    """
    The creatures laugh and start mimicking you.
    Some are fascinated, while others talk amongst themselves.
    Then, what seems to be the leader points towards the path behind them.
    """,
    [
        ("Follow the fluffy dwellers", undertown),
        ("PUNCH A DWELLER!", massacre_by_mob)
    ],
    "alternative",
    [
        "Modern Guide To Pythonmancy",
        ("Summon snakes, and escape!", sneak_from_dwellers)
    ]
)

sneak_from_dwellers.add_values(
    """
    While the dwellers are distracted, you manage to sneak
    into their little village. Some treasure can be found,
    and you add it to your bag. Apart from that,
    you see a stone staircase leading in two directions
    """,
    [
        ("Go right, People are singing there", temple),
        ("Go left", escape_route)
    ]
)

undertown.add_values(
    """
    After some rest in the Dwellers' village, you are ready to go.
    As you stand in front of a stone staircase which splits into two ways,
    leading back to the dungeon, the dwellers hand you a sword.
    It's too big for the little creatures, but perfect for your journey ahead.
    What do you do?
    """,
    [
        ("Thank the Chief and go right", temple),
        ("Go left, the dwellers said it is an exit", escape_route)
    ], "reward", "Excalibur"
)

# Inner dungeon path
treasure_room.add_values(
    """
    You run as fast as you can, listening to the sound of the collapsing
    floor behind you. Finally, you reach the end, a room, with only one
    treasure chest and a door not far behind it.
    """,
    [
        ("Head for the door", library),
        ("Open the chest", mimic_ending)
    ]
)

library.add_values(
    """
    As you open the door, you look at old dusty tomes sitting on shelves
    that reach the roof. Then, the door locks behind you!
    There isn't much around other than books.
    """,
    [
        ("Search for an exit", armory),
        ("Look at the book.", pythonmancer)
    ]
)

armory.add_values(
    """
    After looking around for a bit, you find another room.
    It looks like an old armory. All the equipment is rusted,
    and a well stands in the middle of the room.
    Some skeletons are on the floor,
    and it seems like one of them is ready to fight!
    """,
    [
        ("Fight the skeleton", skeleton_fight),
        ("Jump down the well", cave)
    ]
)

pythonmancer.add_values(
    """
    Between the hundreds of books,
    annexed in the walls of the library. You find a book called:
    'Modern Guide To Pythonmancy', and put it in your bag.
    Then as you look around there is a small black door, and a big old wooden door.
    """, [
        ("Go throught the wooden door", armory),
        ("Go throught the small black door", temple)
    ], "reward", "Modern Guide To Pythonmancy"
)

skeleton_fight.add_values(
    """
    You fought bravely! but after your fight you notice
    more skeletons start rising. You know this fight will take the best
    of you at this pace. What do you do?
    """,
    [
        ("Run away to the halls", temple),
        ("Jump down the well", cave)
    ], "battle", "Skeleton"
)

temple.add_values(
    """
    You rush towards your next location, locking the black door behind you.
    You find yourself in a temple of sorts, and a group of robed shapes
    seem to be conducting a ritual of sort. unnused robes hanged in the wall,
    but other then that the only exist is behind the priest. What do you do?
    """,
    [
        ("Stop this heresy!", heretic_slayer),
        ("Wear the robe and join the cultist", cosplayer)
    ]
)

heretic_slayer.add_values(
    """
    Your calling is clear! To slay the heretics, and free garmage
    """,
    [("Fight the hand", the_hand)],
    "alternative", ["Excalibur", ("Vanquish evil!", vanquisher)]
)

# Wear the robe and join the cultist circle
cosplayer.add_values(
    """
    You wear the robes of a cultist and join their prayer.
    The priest mentions a sacrifice, and ask the congregation to gather around.
    You do and the a symbol in the floor opens a void into the floor
    and a giant hand comes out. The hand seems to be looking for something.
    """,
    [
        ("Push the cultist next to you, towards the hand", trickster),
        ("Give yourself to the hand. The hand loves you", lamb)
    ],
    "alternative",
    [
        "Modern Guide To Pythonmancy",
        ("Cast your pythonmancer spell", the_pythonmancer)
    ]
)

# When the player uses the pythonmancy spell book on the cultist
the_pythonmancer.add_values(
    """
    Using the power of the book, anacondas and pythons jump at the enemy.
    After the snakes attack, all cultists are stopped,
    and the ritual is interrupted. The Hand is weakened.
    The cultists are unconscious, and the priest runs through a door behind.
    The Hand senses you and is ready to take you on.
    """,
    [
        ("Slay The Hand", the_hand_weaken),
        ("Take what you can and run away!", the_coward)
    ]
)

# Push the cultist next to you.
trickster.add_values(
    """
    \"What did you do? That was steve!
    we can\'t force our chocice on The Hand!\", said the priest,
    as he starts to run, leaving his crown behind.
    [purple]The Hand[/purple] is out of control,
    throwing and hitting cultist around.
    """,
    [
        ("I...Have to (fight The Hand)", the_hand),
        ("I...Have to (Sacrifice yourself)", lamb)
    ]
)

the_hand.add_values(
    """
    You did it! You defeated The Hand with all your might.
    Legends will be told about you in the future. Although, not perfect,
    Garmage will be a better day today. What would you do?
    """,
  [
    ("Declare yourself The Hero of Garmage!", the_hand),
    ("Run with the loot!", escape_route)
  ], "battle", "The hand"
)

the_hand_weaken.add_values(
    """
    The Hand, lays defeated, a crown of thorns in the floor,
    A a sense of duty towards your new calling. You don't know if it is The Hand,
    or if it is the robe, but it feels right. this is what you always wanted.
    Would you accept the offer of The Hand?
    """,
    [("I'M YOUR MASTER NOW", priest_of_hold)],
    "alternative",
    ["Excalibur",
        ("BEGONE EVILDOERS!", vanquisher)]
)

# Endings

dead_by_battle.add_values(
    """
    You fought with all your might, but might alone won't save a lost soul.
    [red3]You fell in combat[/red3] like hundreds of other adventurers.
    """, [], "ending"
)

mimic_ending.add_values(
    """
    You open the chest, thinking on all the richest you will find.
    Then you take a moment and notice a [red]fleshy interior[/ red],
    teeth around the lid, As you try to close the door
    [red]a giant grotesque tongue surrounds you.[/ red]
    You are drag inside the chest.
    """, [], "ending"
)

lamb.add_values(
    """
    You give yourself to the command of [purple]The Hand[/ purple].
    [red3]You can feel the warm of its embrace, as you traverse the void.
    [/ red3] This is the end of your journey, but it feels right.
    """, [], "ending"
)

the_coward.add_values(
    """
    [purple]The Hand[/purple] nor the cultist had time to see you escape.
    From between a crevices of a cave, going out to the surface, a person
    can be seeing reaching the surface. Not richer, nor migthier, but alive.
    [deep_pink3]Congratulations, you get to live another day![/deep_pink3]
    """, [], "ending"
)

priest_of_hold.add_values(
    """
    With your crown of thorns, and [purple]The Hand[/purple] as your throne,
    you are the new [bold purple]Priest of The Church of Hold[/bold purple].
    May Garmage sleep well one last night, because your reign of evil starts here.
    """, [], "ending"
)

vanquisher.add_values(
    """
    With the power of [yellow]Excalibur[/ yellow] The light of the sword,
    incinerates all evil infront of you. from the cultist,
    to The Hand, They all [red]burnt marks to a crisp[/red].
    You are [bold yellow]The Paladin of Light[/bold yellow],
    Bring a new age of peace to Garmage.
    """, [], "ending"
)

massacre_by_mob.add_values(
    """
    The little cave dwellers, aren't too happy about your aggression.
    Their fur stand, and their fangs start to show. The little creatures
    jump at you like feral devils. [red]Not much of you was left behind[/red].
    """, [], "ending"
)

escape_route.add_values(
    """
    You take what you can! and go up the stairs, and run away with it.
    As you run up a stone staircase, you see a light which grows stronger
    with each step. After a blinding second, you see a [green]lush forest[/green].
    you made it! You are back in Garmage and richer man, of course.
    """, [], "ending"
)
