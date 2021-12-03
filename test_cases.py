# RUN CONLANG WORD GENERATOR
# ----------------------------------------------------------------------------------
# Generates a table of randomly generated Actarian words according to Actarian
# spelling standards and phonotactics

# Import
from classes.congen import ConGen
from classes.exporter import Exporter

congen = ConGen({"lang":"ak"})
words = congen.generate_words({"num_words": 10, "word_len": 0, "gender": "fem"})

print "\nEXPORT AS STRINGS:"
print "------------------\n"

for w in words:
    print str(w)

print "\nEXPORT AS JSON:"
print "------------------\n"

exporter = Exporter()
print exporter.export_json(words)
