from random import randint
from os import system


# *** Lists ***

dungeonGoals = [ # 17 items
    "Stop the dungeon's monstrous inhabitants from raiding the surface world.", 
    "Foil a villain's evil scheme.", 
    "Destroy a magical threat inside the dungeon.", 
    "Acquire treasure.", 
    "Find a particular item for a specific purpose.", 
    "Retieve a stolen item for a specific purpose", 
    "Rescue a captive", 
    "Discover the fate of a previous adventuring party", 
    "Find an NPC who disappeared in the area.", 
    "Slay a dragon or some other challenging monster.", 
    "Discover the nature and origin of a strange location or phenomenon.", 
    "Pursue fleeing foes taking refuge in the dungeon.",
    "Escape from captivity in the dungeon.", 
    "Clear a ruin so it can be rebuilt and reoccupied.", 
    "Discover why a villain is interested in the dungeon."
    "Win a bet or complete a rite of passage by surviving the dungeon for a certain amount of time.", 
    "Parley with a villain in the dungeon.",
    "Hide from a threat outside the dungeon."
    ]                     

adventureIntro = [ # 11 items
    "While traveling in the wilderness, the characters fall into a sinkhole that opens beneath their feet, dropping them into the adventure location.",
    "While traveling in the wilderness, the characters notice the entrance to the adventure location.",
    "While traveling on a road, the characters are attacked by monsters that flee into the nearby adventure location.",
    "The adventurers find a map on a dead body. In addition to the map setting up the adventure, the adventure's villain wants the map.",
    "A mysterious magic item or a cruel villain teleports the characters to the adventure location.",
    "A stranger approaches the characters in a tavern and urges them toward the adventure location.",
    "A town or village needs volunteers to go to the adventure location.",
    "An NPC the characters care about needs them to go to the adventure location.",
    "An NPC the characters must obey orders them to go to the adventure location.",
    "An NPC the characters respect asks them to go to the adventure location.",
    "One night, the characters all dream about entering the adventure location.",
    "A ghost appears and terrorizes a village. Research reveals that it can be put to rest only by entering the adventure location."
    ]

adventureClimax= [ # 12 items
    "The adventurers confront the main villain and a group of minions in a bloody battle to the finish.",
    "The adventurers chase the villain while dodging obstacles designed to thwart them, leading to a final confrontation in or outside the villain's refuge.",
    "The actions of the adventurers or the villain result in a cataclysmic event that the adventurers must escape.",
    "The adventurers race to the site where the villain is bringing a master plan to its conclusion, arriving just as that plan is about to be completed.",
    "The villain and two or three lieutenants perform separate rites in a large room. The adventurers must disrupt all the rites at the same time.",
    "An ally betrays the adventurers as they're about to achieve their goal. (Use this climax carefully, and don't overuse it.)",
    "A portal opens to another plane of existence. Creatures on the other side spill out, forcing the adventurers to close the portal and deal with the villain at the same time.",
    "Traps , hazards, or animated objects turn against the adventurers while the main villain attacks.",
    "The dungeon begins to collapse while the adventurers face the main villain, who attempts to escape in the chaos.",
    "A threat more powerful than the adventurers appears, destroys the main villain, and then turns its attention on the characters.",
    "The adventurers must choose whether to pursue the fleeing main villain or save an NPC they care about or a group of innocents.",
    "The adventurers must discover the main villain's secret weakness before they can hope to defeat that villain."
    ]    

dungeonLocation = [ # 22 items later will add exotic locations

    "A building in a city",
    "Catacombs or sewers beneath a city",
    "Beneath a farm house",
    "Beneath a graveyard",
    "Beneath a ruin ed castle",
    "Beneath a ruined city",
    "Beneath a temple",
    "In a chasm",
    "In a cliff face",
    "In a desert",
    "In a forest",
    "In a glacier",
    "In a gorge",
    "In a jungle",
    "In a mountain pass",
    "In a swamp",
    "Beneath or on top of a mesa",
    "In sea caves",
    "In several connected mesas",
    "On a mountain peak",
    "On a promontory",
    "On an island",
    "Underwater",
    ]

dungeonCreator = [ # 11 items
    "Beholder",
    "Cult or religious group (roll on the Cults and Religious Groups table to determine specifics)",
    "Dwarves",
    "Elves (including drow)",
    "Giants",
    "Hobgoblins",
    "Humans (roll on the NPC Alignment and NPC Class tables to determine specifics)",
    "Kuo-toa",
    "Lich",
    "Mindflayers",
    "Yuan-ti",
    "No creator (natural caverns)"
    ]

dungeonPurpose = [ # 8 items
    "Death trap",
    "Stronghold",
    "Lair",
    "Temple or shrine",
    "Maze",
    "Tomb",
    "Mine",
    "Treasure vault",
    "Planar gate"
    ]

dungeonHistory = [ # 11 items
    "Abandoned by creators",
    "Abandoned due to plague",
    "Conquered by invaders",
    "Creators destroyed by attacking raiders",
    "Creators destroyed by discovery made within the site",
    "Creators destroyed by internal conflict",
    "Creators destroyed by magical catastrophe",
    "Creators destroyed by natural disaster",
    "Location cursed by the gods and shunned",
    "Original creator still in control",
    "Overrun by planar creatures",
    "Site of a great miracle"
    ]

# *** Main ***

while True:
    system('clear')
        
    print('''
The Adventure Generator

    An Random adventure will be genarated, then will be presented
    if you like the adventure, it will be exported to a .txt file on your pc 
    
    press enter to genarate.\n''')
    
    input()

    # Getting the adventure goal
    goal = dungeonGoals[randint(0,16)]
       
    # Adventure Introduction
    intro = adventureIntro[randint(0,10)]

    # Adventure Climax
    climax = adventureClimax[randint(0,11)] 
    
    # Dungeon Generation
    location = dungeonLocation[randint(0, 21)]
    creator = dungeonCreator[randint(0,10)]
    porpose = dungeonPurpose[randint(0,7)]
    history = dungeonHistory[randint(0,10)]
    
    adventure = adventure = "Intro: {}\n\nGoal: {}\n\nLocation: {}\n\nCreated by: {}\n\nIts porpose: {}\n\nIts history: {}\n\nClimax: {}\n".format(intro, goal, locat    ion, creator, porpose, history, climax) 
    
    print(adventure)
    print("Press enter to continue")
    input()
    
    print("\n\nWould you like to save this adventure or generate another one?\n\n[ 1 ] - Generate another\n\n[ 2 ] - save and exit\n\n[ 3 ] - exit withou    t saving\n\n")
    
    op = int(input("> "))

    if op == 1: 
        continue

    elif op == 2: # make file
        system("touch gen-adventure.txt")
        f = open("gen-adventure.txt", "w")
        f.write(adventure)
        f.close()
        break
    else: 
        break