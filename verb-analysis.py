from wiktionaryparser import WiktionaryParser

parser = WiktionaryParser()

word = parser.fetch('sehen', 'german')

# print (word)

definitions = word[0]['definitions']
pos = definitions[0]['partOfSpeech']

print(pos)
print (definitions)
