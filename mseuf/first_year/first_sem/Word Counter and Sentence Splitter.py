# User input for the sentence
sentence = input("Enter a sentence: ")

# Splitting the sentence and adding to the list
words_list = sentence.split()
words_list = [str(x) for x in words_list]

# Sorting the words
sorted_words = sorted(words_list)

# Counting word frequency
lower_words = [x.lower() for x in words_list] #converted list into lowercase to treat upper and lowercase the same
lower_set = set(lower_words) # Gets rid of duplicates
counted_value = []

for word in lower_set:
    counted_value.append(lower_words.count(word))

lower_set = list(lower_set)

# Display intended outputs
print("===============================================")
print(f'List of words: {words_list}\n')
print(f'Sorted list of words: {sorted_words}\n')
print(f'Word Count: {dict(zip(lower_set, counted_value))}\n')
print("===============================================")
