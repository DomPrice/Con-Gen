# -*- coding: utf-8 -*-

# Import dependencies
import random

# %% Python 3 only %%
#import sys
#sys.stdout.reconfigure(encoding='utf-8')

# CONLANG WORD GEN
# ---------------------------------------------------------------------------------
# Uses the imported Conlang character tables to return a list of randomly generated
# words that would fit into the syllabic standards of that Conlang

class WordGen:

    # PRESETS
    vowel_table     = []
    consonant_table = []
    initial_table   = []
    coda_table      = []
    char_lib        = "" # This will store the character library at runtime

    # INIT
    # -----------------------------------------------------------------------------
    def __init__(self,opts):
        """Constructor for WordGen"""

        # Check opts valid
        if(opts != None and opts.has_key("lang") and opts["lang"] != None):
            lang = opts["lang"] # Get lang

            # Import language character library class
            lang_module_name = lang.upper()
            lang_mod = __import__("lang."+lang.upper(), fromlist = [lang_module_name])
            self.char_lib = getattr(lang_mod,lang_module_name) # Convert to usable class

            # Generate lists
            self.vowel_table     = self.gen_weighted_table(self.char_lib.vowel_table())
            self.consonant_table = self.gen_weighted_table(self.char_lib.consonant_table())
            self.initial_table   = self.gen_weighted_table(self.char_lib.initial_table())

            # Generate coda lists, check if genered
            if self.char_lib.GENDERED:

                # If coda lists are gendered, split them and generate a weighed table for each
                gendered_tables = self.char_lib.coda_table()
                self.coda_table = {} # Convert to dict
                for gender in gendered_tables:
                    self.coda_table[gender] =self.gen_weighted_table(gendered_tables[gender])

    # END __init__
    # -----------------------------------------------------------------------------

    # GENERATE WEIGHTED TABLE
    # -----------------------------------------------------------------------------
    def gen_weighted_table(self,input_table):
        """Takes dict of character clusters (input_table) and generates a weighted table"""

        # Output list
        out_table = []

        # Check opts valid
        if(type(input_table) is dict):
            # Iterate through the vowels and generate a redundant table based on
            # the specified weights in the dict

            for cc in input_table:
                this_cc = [] # Create list for this character cluster
                wt = int(input_table[cc]+1) # Get weight of this cc and add 1
                for i in range(wt):
                    this_cc.append(cc) # Push character cluster into the temp list 'wt' times
                    out_table += this_cc # Merge into weighted table

            # Return weighted and shuffled character table
            random.shuffle(out_table)

        return out_table

    # END gen_weighted_table()
    # -----------------------------------------------------------------------------

    # GENERATE WORDS
    # -----------------------------------------------------------------------------
    def generate_words(self,opts):
        """Generates a list of words from the provided character libraries"""

        # Output list
        out_words = []

        # Check opts valid
        if(
            opts.has_key("num_words")
            and opts.has_key("word_len")
            and type(opts["num_words"]) is int
            and type(opts["word_len"]) is int
        ):
            num_words = opts["num_words"]
            word_len  = opts["word_len"]

            # Generate words
            for w in range(int(num_words)):

                # New word
                word_stem = random.choice(self.initial_table)

                # If lang is syllabic heck if first char is a consonant, if not,
                # append a vowel cluster
                if self.char_lib.SYLLABIC:
                    if(word_stem[0] not in set(["a","e","i","o","u"])):
                        word_stem += random.choice(self.vowel_table)

                # Subtract two from word length (for initial and coda)
                if(word_len > 4): word_len -= 2

                # Iterate and build word
                for w in range(int(word_len)/2): # We want to halve this since we're doubling up below
                    # Append to word
                    word_stem += random.choice(self.consonant_table)
                    word_stem += random.choice(self.vowel_table)

                # Append a coda, if user specifies gender, then use it
                if(self.char_lib.GENDERED):
                    if(
                        opts.has_key("gender")
                        and opts["gender"] != ""
                        and opts["gender"] in set(self.char_lib.GENDERS)
                    ):
                        if opts["gender"] == "fem" and self.char_lib.SYLLABIC:
                            word_stem += random.choice(self.consonant_table)
                            word_stem += random.choice(self.coda_table[opts["gender"]])
                        else:
                            word_stem += random.choice(self.coda_table[opts["gender"]])
                    else:
                        codas = [] # All Codas
                        for gender in self.coda_table:
                            codas += self.coda_table[gender]
                        word_stem += random.choice(codas)
                else:
                    word_stem += random.choice(self.coda_table)

                out_words.append(word_stem) # Append to words list

        return out_words

    # END generate_words()
    # -----------------------------------------------------------------------------
