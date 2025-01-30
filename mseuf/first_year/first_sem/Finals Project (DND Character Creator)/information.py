# races and associated info
races = {
    "Human": {
        "description": "Versatile and ambitious, humans excel in many fields.",
        "size": "Medium",
        "ASI": {"Strength": 1, "Dexterity": 1, "Constitution": 1, "Intelligence": 1, "Wisdom": 1, "Charisma": 1},
        "features": ["Versatile (any two ability scores of your choice each increase by 1)"],
        "skills": [],
        "languages": ["Common"]
},
    "Tiefling": {
        "description": "Descendants of devils, known for their infernal heritage.",
        "size": "Medium",
        "ASI": {"Charisma": 2, "Intelligence": 1},
        "features": [
            "Darkvision: Can see in dim light within 60 ft. as if it were bright light, and in darkness as if it were dim light.",
            "Hellish Resistance: Resistance to fire damage.",
            "Infernal Legacy: Can cast *Thaumaturgy* at will. At 3rd level, can cast *Hellish Rebuke*. At 5th level, can cast *Darkness*."
        ],
        "skills": [],
        "languages": ["Common", "Infernal"]
    },
    "Elf": {
        "description": "Graceful and wise, elves live long lives and excel in magic.",
        "size": "Medium",
        "ASI": {"Dexterity": 2},
        "features": [
            "Darkvision: Can see in dim light within 60 ft. as if it were bright light, and in darkness as if it were dim light.",
            "Keen Senses: Proficiency in the Perception skill.)",
            "Fey Ancestry: Advantage on saving throws against being charmed, and magic can't put you to sleep.",
            "Trance: Elves don't need to sleep. Instead, they meditate deeply for 4 hours a day."
        ],
        "skills": ["Perception"],
        "languages": ["Common", "Elvish"]
    },
    "Half-Orc": {
        "description": "Strong and resilient, half-orcs are known for their strength.",
        "size": "Medium",
        "ASI": {"Strength": 2, "Constitution": 1},
        "features": [
            "Darkvision: Can see in dim light within 60 ft. as if it were bright light, and in darkness as if it were dim light.",
            "Menacing: Proficiency in the Intimidation skill.)",
            "Relentless Endurance: When reduced to 0 hit points but not killed outright, can drop to 1 hit point instead. Usable once per long rest.",
            "Savage Attacks: When scoring a critical hit with a melee weapon attack, can roll one additional weapon damage die."
        ],
        "skills": ["Intimidation"],
        "languages": ["Common", "Orc"]
    },
    "Dwarf": {
        "description": "Stout and sturdy, dwarves excel in craftsmanship and combat.",
        "size": "Medium",
        "ASI": {"Constitution": 2, "Wisdom": 1},
        "features": [
            "Darkvision: Can see in dim light within 60 ft. as if it were bright light, and in darkness as if it were dim light.",
            "Dwarven Resilience: Advantage on saving throws against poison, and resistance to poison damage.",
            "Stonecunning: Proficiency with History checks related to stonework."
        ],
        "skills": ["History"],
        "languages": ["Common", "Dwarvish"]
    },
    "Gnome": {
        "description": "Inventive and curious, gnomes love exploring and creating.",
        "size": "Small",
        "ASI": {"Intelligence": 2},
        "features": [
            "Darkvision: Can see in dim light within 60 ft. as if it were bright light, and in darkness as if it were dim light.",
            "Gnome Cunning: Advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."
        ],
        "skills": [],
        "languages": ["Common", "Gnomish"]
    },
    "Halfling": {
        "description": "Small but courageous, halflings are known for their luck.",
        "size": "Small",
        "ASI": {"Dexterity": 2, "Charisma": 1},
        "features": [
            "Lucky: When rolling a 1 on a d20 for an attack roll, ability check, or saving throw, can reroll the die and must use the new roll.",
            "Halfling Nimbleness: (Can move through the space of a creature larger than you.)",
            "Brave: (Advantage on saving throws against being frightened.)"
        ],
        "skills": [],
        "languages": ["Common", "Halfling"]
    }
}

# classes and associated info
classes = {
    "👺 Barbarian": {
        "description": "A warrior of rage, strength, and fury.",
        "subclasses": ["Berserker", "Zealot"],
        "saving_throws": ["Strength", "Constitution"],
        "skills": ["Animal Handling", "Athletics", "Intimidation", "Perception", "Survival"],
        "hit_die": 12,
        "armor_proficiencies": ["Light Armor", "Medium Armor"],
        "weapon_proficiencies": ["Simple Weapons", "Martial Weapons"],
        "features": {
            "Level 1": {
                "Rage": "As a bonus action, you can enter a rage that grants you bonus damage and resistance to bludgeoning, piercing, and slashing damage.",
                "Unarmored Defense": "While not wearing heavy armor, your AC equals 10 + Dexterity modifier + Constitution modifier."
            },
            "Level 2": {
                "Reckless Attack": "You can choose to attack with advantage on your attack rolls, but attack rolls against you have advantage until your next turn.",
                "Danger Sense": "You have advantage on Dexterity saving throws against effects you can see, such as traps and spells."
            },
            "Level 3": {
                "Berserker Rage": "While raging, you can choose the Berserker subclass and gain Frenzy, allowing you to make a single bonus attack when you rage.",
                "Zealot Rage": "While raging as a Zealot, you can add a divine smite-like feature to deal radiant damage to your enemies."
            }
        }
    },
    "⛑️ Cleric": {
        "description": "A holy warrior drawing power from divine beings.",
        "subclasses": ["Life Domain", "War Domain"],
        "saving_throws": ["Wisdom", "Charisma"],
        "skills": ["History", "Insight", "Medicine", "Persuasion", "Religion"],
        "hit_die": 8,
        "armor_proficiencies": ["Light Armor", "Medium Armor", "Heavy Armor"],
        "weapon_proficiencies": ["Simple Weapons"],
        "features": {
            "Level 1": {
                "Divine Domain": "Choose your divine domain at level 1, which defines your divine magic and abilities.",
                "Spellcasting": "You can prepare and cast spells using Wisdom as your spellcasting ability."
            },
            "Level 2": {
                "Channel Divinity": "You can use your Channel Divinity to perform powerful effects, usable once per short or long rest."
            },
            "Level 3": {
                "Life Domain Feature": "Life domain grants you access to divine healing spells and bonus healing abilities.",
                "War Domain Feature": "You gain the ability to make additional attacks as a bonus action or war-related combat abilities."
            }
        }
    },
    "⚔️ Fighter": {
        "description": "A master of martial combat.",
        "subclasses": ["Champion", "Battle Master"],
        "saving_throws": ["Strength", "Constitution"],
        "skills": ["Acrobatics", "Animal Handling", "Athletics", "Intimidation", "Perception", "Survival"],
        "hit_die": 10,
        "armor_proficiencies": ["Light Armor", "Medium Armor", "Heavy Armor"],
        "weapon_proficiencies": ["Simple Weapons", "Martial Weapons"],
        "features": {
            "Level 1": {
                "Fighting Style": "Choose a fighting style, granting you unique combat benefits.",
                "Second Wind": "You can use a bonus action to regain 1d10 + your fighter level in hit points once per short or long rest."
            },
            "Level 2": {
                "Action Surge": "You can take an additional action on your turn once per short or long rest."
            },
            "Level 3": {
                "Champion Feature": "Gain Improved Critical, increasing your chance to score a critical hit from a roll of 20 to a roll of 19-20.",
                "Battle Master Feature": "You gain access to combat maneuvers that you can use to control the battlefield."
            }
        }
    },
    "🗡️ Rogue": {
        "description": "A cunning and stealthy skill master.",
        "subclasses": ["Thief", "Assassin"],
        "saving_throws": ["Dexterity", "Intelligence"],
        "skills": ["Acrobatics", "Athletics", "Deception", "Insight", "Investigation", "Perception", "Sleight of Hand", "Stealth"],
        "hit_die": 8,
        "armor_proficiencies": ["Light Armor"],
        "weapon_proficiencies": ["Simple Weapons", "Hand Crossbows", "Shortswords", "Longswords", "Rapiers"],
        "features": {
            "Level 1": {
                "Sneak Attack": "You can deal extra damage when you attack with finesse or ranged weapons if you have advantage on the attack or an ally is within 5 feet of your target.",
                "Thieves' Cant": "You can communicate with other rogues using a secret language known only to rogues."
            },
            "Level 2": {
                "Cunning Action": "You can use a bonus action to Dash, Disengage, or Hide on your turn."
            },
            "Level 3": {
                "Thief Feature": "Gain Fast Hands, allowing you to use your bonus action to disarm traps and pick locks more effectively.",
                "Assassin Feature": "Gain Assassinate, giving you advantage on attack rolls against surprised creatures at the start of combat."
            }
        }
    },
    "🪄 Wizard": {
        "description": "A spellcaster mastering arcane magic.",
        "subclasses": ["Evocation", "Necromancy"],
        "saving_throws": ["Intelligence", "Wisdom"],
        "skills": ["Arcana", "History", "Insight", "Investigation", "Medicine", "Perception"],
        "hit_die": 6,
        "armor_proficiencies": ["Light Armor"],
        "weapon_proficiencies": ["Simple Weapons"],
        "features": {
            "Level 1": {
                "Spellcasting": "You can prepare and cast spells using Intelligence as your spellcasting ability.",
                "Arcane Recovery": "Once per day, you can regain a number of expended spell slots equal to half your wizard level."
            },
            "Level 2": {
                "Savant": "The gold and time you must spend to copy a Evocation spell into your spellbook is halved.",
                "Evocation Feature": "Gain Sculpt Spells, allowing you to shape area spells to avoid allies.",
                "Necromancy Feature": "Gain access to Undead Thralls or Necromantic magic effects to manipulate undead."
            },
            "Level 3": {
                "None"
            }
        }
    }
}

# bgs and associated info
backgrounds = {
    "🛐 Acolyte": {
        "description": "You have spent your life in the service of a temple or religious institution.",
        "skills": ["Insight", "Religion"],
        "tools": ["Prayer wheel", "Herbalism kit"],
        "feature": "Shelter of the Faithful - You can find a place to stay or aid from a temple or religious follower."
    },
    "🥷 Criminal": {
        "description": "You are skilled in stealth and deception and have ties to the underworld.",
        "skills": ["Stealth", "Deception"],
        "tools": ["Disguise kit", "Thieves' tools"],
        "feature": "Criminal Contact - You have a reliable contact in the criminal underworld who can provide information or assistance."
    },
    "🫥 Hermit": {
        "description": "You have spent years in isolation, meditating and searching for truths.",
        "skills": ["Medicine", "Religion"],
        "tools": ["Herbalism kit"],
        "feature": "Discovery - You have found some unique and esoteric truth or hidden knowledge during your isolation."
    },
    "👻 Haunted One": {
        "description": "You have faced supernatural horrors and survived, though it has left its mark on you.",
        "skills": ["Arcana", "Intimidation"],
        "tools": ["None"],
        "feature": "Dark Secret - You carry a terrible secret that could affect you or others if revealed."
    },
    "👑 Noble": {
        "description": "You were born into wealth and privilege.",
        "skills": ["History", "Persuasion"],
        "tools": ["One type of musical instrument", "Calligrapher's supplies"],
        "feature": "Position of Privilege - You are welcome in high society, and people assume you have a degree of authority."
    },
    "🪖 Soldier": {
        "description": "You have a military background, with discipline and combat training.",
        "skills": ["Athletics", "Intimidation"],
        "tools": ["Land Vehicles", "One type of musical instrument"],
        "feature": "Military Rank - You have a rank from your military service, giving you status and recognition among other soldiers."
    }
}


