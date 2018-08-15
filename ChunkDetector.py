import re
word = "said to"
sentence = "What a great sentence"
chunks = "I love chunks"
chunks_split = chunks.split()
chunk_input = 'chunk_input.txt'
chunks = []

#Check if word appears in split chunk
#if word in chunks_split:
#    print(word, "- in chunks_split")
#else:
#    print(word, "- not in chunks_split")

with open('ChunkList.csv', "r", encoding='ISO-8859-1') as f:
    chunk_csv = f.readlines()
    for line in chunk_csv:
        line = line.split(',')
        chunks.append(line[0].strip())

chunks = [element.lower() for element in chunks]

#Same as line above but more elaborate
# chunk2 = []
# for element in chunks:
#    element = element.lower()
#    chunks2.append(element)
# chunks = chunks2

#open and print txt file, also strip punctuation and lower case.
with open(chunk_input, encoding='utf-8-sig') as f:
    data_old = f.readlines()
    data_old = [line.strip(' ,.;:!?\'\n') for line in data_old]
    data_old = [element.lower() for element in data_old]
    print(data_old)

#open and print txt file, also strip punctuation, lower case and split.
with open(chunk_input, encoding='utf-8-sig') as f:
    data = f.readlines()
    data = [line.strip(' ,.;:!?\'\n') for line in data]
    data = [element.lower() for element in data]
    data = [line.split() for line in data]
    print(data)

for row in chunks:
    # print('yes')
    if (data.find(row)) in chunks:
        print('found')
    else:
        print('no')

#check if word appears in csv
if word in chunks:
    print(word, '- word in csv')

#check to see if the text in txt appears in csv
for element in data_old:
    if element in chunks:
        print(element, '- txt in csv')