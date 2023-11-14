from hazm import *
import os
import json

directory_path = 'Documents'
files_name_list = os.listdir(directory_path)
# print(os.listdir(directory_path))

token_counts = {}

# find Text files
text_files = [file for file in files_name_list if file.endswith('.txt')]

# create a word(token) list
for text_file in files_name_list:
    file_path = os.path.join(directory_path, text_file)
    with open(file_path,'r+',encoding="utf8") as file:
        file_contents = file.read()
        tokens_list = word_tokenize(file_contents)

# create a dictionary that stores the counts of each token
for token in tokens_list:
    if token in token_counts:
        token_counts[token] += 1
    else:
        token_counts[token] = 1

with open('dict-output.json', 'w', encoding="utf8") as f:
   json.dump(token_counts,f)
# print(token_counts)