from classes import *

standard_cards = [
    TACard('Richard, Head of Exodia', 1600, 1600),
    TACard('λaryn, λord of λambdas', 2100, 1300),
    TACard('Addison, from operator import add', 1500, 1500),
    TACard('Connie, Consumer of Carbs', 1500, 1900),
    TutorCard('Mingxiao, QwQ', 1600, 1600),
    TACard('Cyrus, Prince of Persia', 1000, 2000),
    AICard('Nikhil, Laughter Incinerator', 1500, 1700),
    AICard('Daniel, the Cocker Spaniel', 1900, 1500),
    AICard('James, Progenitor of Code', 2200, 1100),
    TACard('Owen the Omnipotent Otter', 1500, 1800),
    AICard('Amol, expert procrastinator', 1700, 1600),
    TutorCard('Jessica, Defender of Noodles', 2100, 1000),
    TutorCard('Rachel, the Vitamin Overlord', 1200, 2200),
    TutorCard('Alex, Unlimited Bug Works HA↗HA↘HA↗HA↘', 1900, 1400),
    AICard('Omar, The Ganderer', 1700, 1400),
    TutorCard('Chris, Maker of Bad Purchase Decisions', 1000, 2000),
    AICard('The Floormat', 1200, 2200),
    AICard('Billy, the Kid', 1200, 1900),
    TACard('Jamie, Scribbler of Eimaj-ination', 1000, 2100),
    TACard('Patricia, Ace Attorney', 1000, 2300),
    TACard('Tim Tu, Tuple of Twos', 1200, 2000),
    TACard('Ben, Wanderer of Northside', 2100, 1100),
    AICard('Hailey, Summoner of Penguins', 2000, 1400),
    TutorCard('Maanav, Wizard of Variables', 1800, 1600),
    TutorCard('Christina, Burner of Croissants', 2200, 1100),
    AICard('Yuto, Imposter of Amogus', 2000, 1300),
    AICard('Wes, Regulator of Vibes', 1300, 2000),
    TACard('Anthony, Grease PiazzaBot', 2200, 1200),
    TACard('Daphne, Left Leg of the Forbidden One', 2000, 1200),
    TACard('Vanshaj, Right Arm of the Forbidden One', 1200, 1300),
    TACard('Yersultan, Yogurt', 1100, 2000),
    AICard('Justin, Squishmallow Squisher', 1200, 1900),
    AICard('Janani, Lover of Pun-anas', 1500, 1800),
    AICard('Shiv, the maker of sandwiches', 2000, 1300),
    TACard('Samee, Left Arm of the Forbidden One', 2000, 1100),
    TACard('Ryan, the Right Leg of the Forbidden One', 1000, 2100),
    AICard('Poggers', 1700, 1600),
    AICard('Karen, Seeker of Managers', 1200, 1800),
    TutorCard('Kevin, the Clueless Developer', 1500, 1700),
    TutorCard('Aneesh, the Conqueror ', 1500, 1200),
    AICard('Shipransh, your best nightmare', 2000, 1100),
    AICard('Ani, the Gilded Hand', 1900, 1500),
    TACard('Arushi, The Bloodless Butcher of Abstraction Barriers', 1800, 1100),
    TACard('Roy, Apothecary of Soup', 1000, 2300),
    TACard('Albert, Dealer of Dumplings', 1700, 1700),
    TutorCard('Lucy, Abstraction Protector', 1000, 2200),
    AICard('Ben, Oatmeal on Two Wheels', 1000, 2300),
    TACard('Catherine, Gacha Acolyte ', 2100, 1200),
    AICard('Ergun, Protector of Nature', 1200, 2000),
    TutorCard('Shivana, Queen of Procrastination and Regret', 1500, 1800),
    InstructorCard('John DeNero, Protector of Abstraction Barriers', 5000, 5000),
    InstructorCard('Pamela Fox, Your Higher-Order Highness', 0, 10000)
]

standard_deck = Deck(standard_cards)
player_deck = standard_deck.copy()
opponent_deck = standard_deck.copy()
