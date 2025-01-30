import random # for dice rolling
import json # for saving and loading the characters
import os # to save and load the character sheets in a specific folder and folder checking
from information import races, classes, backgrounds  # Import race, class, and background dictionaries from `information.py`


# main menu code block
def main():
    print("-----------------------------------------------------------------------------------------------------------")
    print("\n✨ Welcome to the D&D 5e Character Creator! Create your own character now! ✨\n")
    while True:
        print("-----------------------------------------------------------------------------------------------------------")
        print("\n🕹️ Main Menu 🕹️")
        print()
        print("1. 📝 Create a New Character")
        print("2. 💿 Load Existing Character")
        print("3. ❌ Exit")
        choice = input("\n> Enter your choice: ").strip()
        
        if choice == "1":
            character_creation()
        elif choice == "2":
            load_character()
        elif choice == "3":
            print("Exiting the program. Goodbye! 👋👋👋")
            break
        else:
            print("❌ Invalid choice. Please try again. ❌")
          
            
# character creation code block a.k.a the heart of the program 😭
def character_creation():
    print("\n-----------------------------------------------------------------------------------------------------------")
    print("✨ Character Creation Menu: ✨")
    print()
    
    # user inputs player name
    player_name = input("> Enter your name: ").strip()
    
    # user inputs character name
    character_name = input("> Enter your character's name: ").strip()
    
    # user input for starting level
    while True:
        try:
            starting_level = int(input("> Enter your starting level (1-3) ").strip())
            if 1 <= starting_level <= 3:
                break
            else:
                print("❌ Invalid input. Please enter a number between 1 and 3. ❌")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number. ❌")
            
    # calls race selection function
    character_race = select_race()
    
    # calls alignment selector function
    character_alignment = select_alignment()
    
    # calls class selector function
    character_class = select_class()
    
    # calls subclass selector depending on level
    if (starting_level >= 3) or (character_class == "⛑️ Cleric" or character_class == "🪄 Wizard" and starting_level >=2): # per 5e rules clerics and wizards get subclass at lvl 2
        character_subclass = select_subclass(character_class, starting_level)
    else:
        character_subclass = "None"

    # calls background selector function
    character_bg = select_bg()
    
    # runs the stats roller and stats assigner
    stats = roll_stats()
    assigned_stats = assign_stats(stats)
    
    # applies racial ASI (ability score improvement) to stats
    final_stats = apply_race_asi(assigned_stats, character_race)
    
    # Get race and background proficiencies
    race_proficiencies = get_race_proficiencies(character_race)
    bg_proficiencies = get_bg_proficiencies(character_bg)
    
    # choosing class skills after stats are assigned
    class_skills = choose_class_skills(character_class, race_proficiencies, bg_proficiencies)

    # combines all skill proficiencies into a set
    total_proficiencies = set(race_proficiencies + bg_proficiencies + class_skills)
    
    # calculates all skill modifiers
    skill_modifiers = calculate_modifiers(final_stats, total_proficiencies, starting_level)

    # gets the needed class features
    class_features = get_class_features(character_class, character_subclass, starting_level)
    
    # gets the needed race features
    race_name = character_race  # Replace with the desired race name
    race_features = display_race_features(race_name, races)

    # Print the character summary
    print("\n-----------------------------------------------------------------------------------------------------------")
    print("Character Created Successfully!")
    print(f"Player Name: {player_name}")
    print(f"Character Name: {character_name}")
    print(f"Starting Level: {starting_level}")
    print(f"Race: {character_race}")
    print(f"Alignment: {character_alignment}")
    print(f"Class: {character_class}")
    print(f"Subclass: {character_subclass}")
    print(f"Background: {character_bg}")
    print(f"Stats: {final_stats}")
    print(f"Skill Proficiencies: {sorted(total_proficiencies)}")
    print("\n-----------------------------------------------------------------------------------------------------------")
    
    print("Skill Modifiers:")
    for skill, modifier in sorted(skill_modifiers.items()):
        print(f"{skill}: {'+' if modifier >= 0 else ''}{modifier}")
    print("\n-----------------------------------------------------------------------------------------------------------")
    
    print("Class Features:")
    for level, features in class_features.items():
        print(f"Level {level}:")
        for feature, description in features.items():
            print(f"  - {feature}: {description}")
    print("\n-----------------------------------------------------------------------------------------------------------")
    
    print("Race Features:")
    print(race_features)
    
    # Create a dictionary with the character data
    character_data = {
        "player_name": player_name,
        "character_name": character_name,
        "starting_level": starting_level,
        "race": character_race,
        "alignment": character_alignment,
        "class": character_class,
        "subclass": character_subclass,
        "background": character_bg,
        "stats": final_stats,
        "class_skills": class_skills,
        "total_proficiencies": sorted(total_proficiencies),
        "skill_modifiers": skill_modifiers,
        "class_features": class_features,
        "race_features": race_features
    }

    # Save the character to a file
    save_choice = input("\n> Do you want to save this character to a file? (y/n): ").strip().lower()
    if save_choice in ("y", "yes"):
        filename = input("> Enter a filename (default filename: character): ").strip()
        if not filename:
            filename = "character.json"
        elif not filename.endswith(".json"):
            filename += ".json"
        save_character(character_data, filename)

    return character_data


# race selector function
def select_race():
    print("\n-----------------------------------------------------------------------------------------------------------")
    print("Choose your race from the following options:\n")
    
    # lists all available races to pick from
    for i, race in enumerate(races.keys(), start=1):
        print(f"{i}. {race}: {races[race]['description']}")
        
    while True:
        try:
            race_choice = int(input("\n> Select a number corresponding to your choice: ").strip())
            if 1 <= race_choice <= len(races):
                selected_race = list(races.keys())[race_choice-1] # converts keys to list for indexing
                return selected_race
            else:
                print("❌ Invalid choice. Please select a number from the list. ❌")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number. ❌")


# alignment selector function
def select_alignment():
    alignments = [
        "Lawful Good", "Neutral Good", "Chaotic Good",
        "Lawful Neutral", "True Neutral", "Chaotic Neutral",
        "Lawful Evil", "Neutral Evil", "Chaotic Evil"
    ]
    
    print("\n-----------------------------------------------------------------------------------------------------------")
    print("Choose your alignment from the following options:\n")
    for i, alignment in enumerate(alignments, start=1):
        print(f"{i}. {alignment}")
    
    while True:
        try:
            alignment_choice = int(input("\n> Select a number corresponding to your choice: ").strip())
            if 1 <= alignment_choice <= len(alignments):
                return alignments[alignment_choice - 1]
            else:
                print("❌ Invalid choice. Please select a number from the list. ❌")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number. ❌")
    
    
# class selector function
def select_class():
    print("\n-----------------------------------------------------------------------------------------------------------")
    print("Choose your class from the following options:\n")
    
    # lists available classes
    for i, cls in enumerate(classes.keys(), start=1):
        print(f"{i}. {cls}: {classes[cls]['description']}")
        
    while True:
        try:
            class_choice = int(input("\n> Select a number corresponding to your choice: ").strip())
            if 1 <= class_choice <= len(classes):
                selected_class = list(classes.keys())[class_choice - 1]
                return selected_class
            else:
                print("❌ Invalid choice. Please select a number from the list. ❌")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number. ❌")
         
            
# subclass selector function
def select_subclass(character_class, level):
    if character_class in classes and classes[character_class]["subclasses"]:
        print("\n-----------------------------------------------------------------------------------------------------------")
        print(f"Choose your subclass for {character_class} at Level {level}:\n")
        subclasses = classes[character_class]["subclasses"]
        for i, subclass in enumerate(subclasses, start=1):
            print(f"{i}. {subclass}")
            
        while True:
            try:
                subclass_choice = int(input("\n> Select a number corresponding to your choice: ").strip())
                if 1 <= subclass_choice <= len(subclasses):
                    return subclasses[subclass_choice - 1]
                else:
                    print("❌ Invalid choice. Please select a number from the list. ❌")
            except ValueError:
                print("❌ Invalid input. Please enter a valid number. ❌")
    else:
        print("No subclasses available at your current level.")
        return "N/A"     


def select_bg():
    print("\n-----------------------------------------------------------------------------------------------------------")
    print("Choose your background from the following options:\n")
   
   # lists available backgrounds
    for i, bg in enumerate(backgrounds.keys(), start=1):
        print(f"{i}. {bg}: {backgrounds[bg]['description']}")
       
    while True:
        try:
            bg_choice = int(input("\n> Select a number corresponding to your choice: ").strip())
            if 1 <= bg_choice <= len(backgrounds):
                select_bg = list(backgrounds.keys())[bg_choice - 1]
                return select_bg
            else:
                print("❌ Invalid choice. Please select a number from the list. ❌")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number. ❌")


# stat roller function (rolls 4d6 and drops the lowest roll for each ability score)
def roll_stats():
    stats = []
    
    for _ in range(6):
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.remove(min(rolls))
        stats.append(sum(rolls))
        
    return sorted(stats)


# stat assigner function
def assign_stats(stats):
    ability_scores = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    assigned = {}
    
    print("\n-----------------------------------------------------------------------------------------------------------")
    print("\nAssign the rolled stats to your ability scores:")
    print("Rolled stats pool:", stats)
    print("\n-----------------------------------------------------------------------------------------------------------")
    
    for ability in ability_scores:
        while True:
            try:
                print("\n-----------------------------------------------------------------------------------------------------------")
                print(f"\nAvailable stats: {stats}")
                ability_score_choice = int(input(f"> Assign a stat to {ability}: ").strip())
                if ability_score_choice in stats:
                    assigned[ability] = ability_score_choice
                    stats.remove(ability_score_choice)
                    break
                else:
                    print("❌ Invalid choice. Please select a number from the available stats. ❌")
            except ValueError:
                print("❌ Invalid input. Please enter a valid number. ❌")
    
    return assigned
    
    
# applying race asi to stats function
def apply_race_asi(assigned_stats, race):
    final_stats = assigned_stats.copy() #copies assigned stats to avoid modifying the original directly
    
    if race in races:
        racial_asi = races[race]["ASI"]

        for ability, bonus in racial_asi.items():
            if ability in final_stats:
                final_stats[ability] += bonus
                
    return final_stats


# gets race proficiencies
def get_race_proficiencies(race):
    if race in races:
        return races[race].get("skills", [])
    return []

#gets bg proficiencies
def get_bg_proficiencies(background):
    if background in backgrounds:
        return backgrounds[background].get("skills", [])
    return []


# allows the user to choose class skills based on chosen class and avoids duplicates with skills acquired from race and bg
def choose_class_skills(character_class, race_proficiencies, background_proficiencies):
    character_class = character_class.lower()  # makes class selection case-insensitive
    class_keys = {key.lower(): key for key in classes}  # maps lowercase keys to orig keys

    if character_class not in class_keys:
        print(f"❌ Invalid class: {character_class} ❌")
        return []

    original_class = class_keys[character_class]  # gets the original case-sensitive class name
    available_skills = classes[original_class]["skills"]
    num_choices = 4 if original_class.lower() == "🗡️ rogue" else 2
    
    # calculates proficiencies already gained
    already_proficient = set(skill.lower() for skill in race_proficiencies + background_proficiencies)
    remaining_skills = [skill for skill in available_skills if skill.lower() not in already_proficient]

    print("\n-----------------------------------------------------------------------------------------------------------")
    print("\nTime to choose you class skill proficiencies!!!")
    print(f"Available skills for {original_class}: {remaining_skills}")
    print(f"You need to choose {num_choices} skills.\n")

    chosen_skills = []
    
    while len(chosen_skills) < num_choices:
        choice = input(f"> Choose a skill ({len(chosen_skills) + 1}/{num_choices}): ").strip().lower()
        valid_skills = {skill.lower(): skill for skill in remaining_skills}

        if choice in valid_skills and valid_skills[choice] not in chosen_skills:
            chosen_skills.append(valid_skills[choice])
            print(f"\n{valid_skills[choice]} added!\n")
        elif choice in {skill.lower() for skill in chosen_skills}:
            print(f"\n❌ You've already chosen {valid_skills.get(choice, choice)}. ❌\n")
        else:
            print(f"\n❌ Invalid choice. Please choose from {[skill for skill in remaining_skills]}. ❌\n")
    
    print("\n-----------------------------------------------------------------------------------------------------------")
    print(f"Final chosen skills: {chosen_skills}")
    
    return chosen_skills
    
    
# skill modifier calculator function
def calculate_modifiers(assigned_stats, proficiencies, level):
    # determines proficiency bonus based on level
    proficiency_bonus = (level - 1) // 4 + 2  # starts at +2 and increases every 4 levels

# maps skills to their corresponding ability scores
    skill_to_ability = {
        "Acrobatics": "Dexterity",
        "Animal Handling": "Wisdom",
        "Arcana": "Intelligence",
        "Athletics": "Strength",
        "Deception": "Charisma",
        "History": "Intelligence",
        "Insight": "Wisdom",
        "Intimidation": "Charisma",
        "Investigation": "Intelligence",
        "Medicine": "Wisdom",
        "Nature": "Intelligence",
        "Perception": "Wisdom",
        "Performance": "Charisma",
        "Persuasion": "Charisma",
        "Religion": "Intelligence",
        "Sleight of Hand": "Dexterity",
        "Stealth": "Dexterity",
        "Survival": "Wisdom",
    }

    # calculates ability modifiers
    ability_modifiers = {key: (score - 10) // 2 for key, score in assigned_stats.items()}

    # calculates skill modifiers
    skill_modifiers = {}
    
    for skill, ability in skill_to_ability.items():
        modifier = ability_modifiers[ability]
        if skill in proficiencies:
            modifier += proficiency_bonus
        skill_modifiers[skill] = modifier

    return skill_modifiers

# get class features function
def get_class_features(character_class, character_subclass, starting_level):
    features = {}
    class_data = classes.get(character_class, {})
    
    for level, feature_set in class_data.get("features", {}).items():
        level_int = int(level.split()[1])  # extract numeric level
        if level_int <= starting_level:
            features[level] = {
                feature: desc
                for feature, desc in feature_set.items()
                if character_subclass in feature or "Feature" not in feature
            }
    
    return features

# get race features function
def display_race_features(race_name, races):
    if race_name not in races:
        return f"Race '{race_name}' not found in the list of available races."
    
    race = races[race_name]
    description = race.get("description", "No description available.")
    size = race.get("size", "Unknown size")
    asi = race.get("ASI", {})
    features = race.get("features", [])
    skills = race.get("skills", [])
    languages = race.get("languages", [])
    
    asi_string = ", ".join([f"{stat} +{bonus}" for stat, bonus in asi.items()])
    features_string = "\n  ".join(features) if features else "None"
    skills_string = ", ".join(skills) if skills else "None"
    languages_string = ", ".join(languages) if languages else "None"
    
    return f"""
Race: {race_name}
Description: {description}
Size: {size}
Ability Score Increase (ASI): {asi_string}
Features:
  {features_string}
Skills: {skills_string}
Languages: {languages_string}
"""


# saving character sheets function
def save_character(character_data, filename="character.json"):
    try:
        # default folder path within the same directory
        folder_path = os.path.join(os.path.dirname(__file__), "character_sheets")
        
        # ensures the folder exists
        os.makedirs(folder_path, exist_ok=True)

        # constructs the full file path
        filepath = os.path.join(folder_path, filename)
        
        # saves the JSON file
        with open(filepath, "w") as json_file:
            json.dump(character_data, json_file, indent=4)
        print(f"\n✅ Character saved successfully to {filepath}! ✅")
    except Exception as e:
        print(f"\n❌ An error occurred while saving the character: {e} ❌")


# loading characters from character_sheets folder
def load_character():
    folder_path = os.path.join(os.getcwd(), "character_sheets")
    
    if not os.path.exists(folder_path):
        print("❌ The 'character_sheets' folder does not exist. Please create a character first. ❌")
        return

    # lists all JSON files in the folder
    character_files = [f for f in os.listdir(folder_path) if f.endswith(".json")]
    
    if not character_files:
        print("❌ No character files found in the 'character_sheets' folder. ❌")
        return
    
    print("\n📂 Available Characters:")
    for i, file in enumerate(character_files, start=1):
        print(f"{i}. {file}")
    
    while True:
        try:
            choice = int(input("\n> Enter the number corresponding to the character you want to load: ").strip())
            if 1 <= choice <= len(character_files):
                selected_file = character_files[choice - 1]
                file_path = os.path.join(folder_path, selected_file)
                
                # loads the character from the selected file
                with open(file_path, "r") as f:
                    character_data = json.load(f)
                
                print("\n✨ Character Loaded Successfully! ✨")
                print_character_summary(character_data)
                return character_data
            else:
                print("❌ Invalid choice. Please select a number from the list. ❌")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number. ❌")

# prints out a character summary for the user
def print_character_summary(character_data):
    """Print a summary of the loaded or created character."""
    print("\n-----------------------------------------------------------------------------------------------------------")
    print(f"Player Name: {character_data.get('player_name', 'N/A')}")
    print(f"Character Name: {character_data.get('character_name', 'N/A')}")
    print(f"Starting Level: {character_data.get('starting_level', 'N/A')}")
    print(f"Race: {character_data.get('race', 'N/A')}")
    print(f"Alignment: {character_data.get('alignment', 'N/A')}")
    print(f"Class: {character_data.get('class', 'N/A')}")
    print(f"Subclass: {character_data.get('subclass', 'N/A')}")
    print(f"Background: {character_data.get('background', 'N/A')}")
    print(f"Stats: {character_data.get('stats', 'N/A')}")
    print(f"Total Skill Proficiencies: {character_data.get('total_proficiencies', 'N/A')}")
    print("\nSkill Modifiers:")
    for skill, modifier in sorted(character_data.get("skill_modifiers", {}).items()):
        print(f"{skill}: {'+' if modifier >= 0 else ''}{modifier}")
    
    print("\nClass Features:")
    for level, features in character_data.get("class_features", {}).items():
        print(f"Level {level}:")
        for feature, description in features.items():
            print(f"  - {feature}: {description}")
    
    print("\nRace Features:")
    race_features = character_data.get("race_features", "No race features found.")
    print(race_features)
    print("\n-----------------------------------------------------------------------------------------------------------")


# starts the program by calling the main function
if __name__ == "__main__":
    main()
