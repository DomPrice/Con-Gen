# RUN ACTARIAN WORD GENERATOR
# ----------------------------------------------------------------------------------
# Generates a table of randomly generated Actarian words according to Actarian
# spelling standards and phonotactics

# Import
from classes.congen import ConGen
from classes.exporter import Exporter

print("WordGen Conlang Word Generator")
print("Pick language (Two Letter Code): ")
lang = raw_input()
print("How many words?: ")
num_words = int(raw_input())
print("Specify Word Approximate Length: ")
word_len = int(raw_input())
print("Specify a Gender: ")
gender = raw_input()

print(lang + " " + str(num_words) + " " + str(word_len) + " " +gender )

word_gen = ConGen({"lang":lang})
words = congen.generate_words({"num_words": num_words, "word_len": word_len, "gender": gender})

print "\nEXPORT AS STRINGS:"
print "------------------\n"

for w in words:
    print str(w)

print "\nEXPORT AS JSON:"
print "------------------\n"

exporter = Exporter()
print exporter.export_json(words)
