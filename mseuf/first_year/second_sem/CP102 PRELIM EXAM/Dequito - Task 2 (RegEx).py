#KYLA DESSIREI L. DEQUITO

import re

unique_characters = set()
num_list = []
bee_list =[]
honey_list = []

with open("bee_movie_and_bee_facts.txt", 'r', encoding='utf-8') as file:

    print("-_-" * 25 + "\n")
    print("Everytime Honey appears at the start of a line.\n")
    for line in file:
        line = line.rstrip()
        
        #Searches for lines that start with the word Honey
        if re.search(r'^honey', line, re.IGNORECASE):
            print(line)
    
        #Finds all unique characters in the film
        matches = re.findall(r'^[A-Z0-9]{2,}:$', line) 
        unique_characters.update({match[:-1].capitalize() for match in matches}) #Updates to set to avoid dupes, removes colon, capitalizes
        
        #Finds all instances of the word bee regardless or case or if it is in another word (Ex. honeybee, bee-ing, etc.)
        bee = re.findall(r'bee', line, re.IGNORECASE)
        if len(bee) > 0:
            bee_list += bee
        
        #Finds all instances of the word honey regardless or case or if it is in another word (Ex. honeycomb, honey, etc.)
        honey = re.findall(r'honey', line, re.IGNORECASE)
        if len(honey) > 0:
            honey_list += honey
        
        #Finds all digits in the text file
        num = re.findall(r'\d+(?:,\d+)*', line)  
        for n in num:
             num_list.append(int(n.replace(',', ''))) #Removes commas and convert to int

#Displaying outputs      
print("-_-" * 25 + '\n') 
    
print(f"Unique Movie Characters ({len(unique_characters)} Found):\n{sorted(unique_characters)}")

print("-_-" * 25 + '\n') 

print(f'All instances of the word Bee found: {len(bee_list)}')
print(f'All instances of the word Honey-related words found: {len(honey_list)}')
print(f'The sum of bees and honey: {len(bee_list) + len(honey_list)}')
print(f'The average of bees and honey: {(len(bee_list) + len(honey_list))/2:.2f}')

print("-_-" * 25 + '\n')  

print(f'The amount of numbers found: {len(num_list)}')
print(f'The sum of all numbers: {sum(num_list)}')
print(f'The highest number: {max(num_list)}')
print(f'The lowest number: {min(num_list)}')
print(f'The average of the numbers: {sum(num_list)/len(num_list):.2f}')