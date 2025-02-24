from collections import Counter
replacement_chars = [' ', 'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', 'c', 'm', 'p', 'b', 'g', 'v', 'y', 'f', 'k', 'w', 'z', 'x', 'j', 'q']

def replace_frequent_strings(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    
    words = content.split()

    
    word_frequency = Counter(words)

    
    sorted_words = sorted(word_frequency.keys(), key=lambda x: word_frequency[x], reverse=True)


    word_mapping = {}
    for i, word in enumerate(sorted_words):
        if i < len(replacement_chars):
            word_mapping[word] = replacement_chars[i]

    
    modified_content = content
    for word, replacement in word_mapping.items():
        modified_content = modified_content.replace(word, replacement)

    
    print(modified_content.replace('\n' , '') , end = '' )


input_file = 'output.txt'  
output_file = 'flag.txt'  
replace_frequent_strings(input_file, output_file)
