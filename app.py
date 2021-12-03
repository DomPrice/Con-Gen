# RUN CONLANG WORD GENERATOR
# ----------------------------------------------------------------------------------
# Generates a table of randomly generated Actarian words according to Actarian
# spelling standards and phonotactics

# Import
from classes.wordgen import WordGen

word_gen = WordGen({"lang":"ak"})
words = word_gen.generate_words({"num_words": 10, "word_len": 0, "gender": "fem"})

for w in words:
    print str(w)

            #print(v.decode('utf-8'))
