# RUN CONLANG WORD GENERATOR
# ----------------------------------------------------------------------------------
# Generates a table of randomly generated Actarian words according to Actarian
# spelling standards and phonotactics

# Import
from classes.wordgen import ConGen

congen = ConGen({"lang":"ak"})
words = congen.generate_words({"num_words": 10, "word_len": 0, "gender": "fem"})

for w in words:
    print str(w)
