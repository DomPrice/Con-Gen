# -*- coding: utf-8 -*-

# ACTARIAN LANAGUAGE LIBRARY FOR WORDGEN
# ---------------------------------------------------------------------------------
# Contains the character cluster and pattern information for the Actarian Language

class AK:

    # LANGUAGE SETTINGS
    LANG_CODE = "ak"
    SYLLABIC  = True # Set True if the lanaguage follows a syllabic pattern
    GENDERED  = True # Set If True
    GENDERS   = ["mas","fem","neu"]

    # VOWELS
    # --------------------------------------------------------------------------------
    @staticmethod
    def vowel_table():
        return dict({
            "a":  60,
            "e":  57,
            "i":  56,
            "o":  57,
            "u":  54,
            "aâ": 7,
            "eê": 7,
            "uû": 4,
            "oô": 6,
            "iî": 6,
            "ae": 9,
            "ai": 30,
            "ao": 8,
            "au": 30,
            "ea": 6,
            "ei": 3,
            "eo": 2,
            "eu": 2,
            "ia": 2,
            "ie": 1,
            "io": 1,
            "iu": 1,
            "oa": 2,
            "oe": 2,
            "oi": 24,
            "ou": 1,
            "ua": 1,
            "ue": 1,
            "ui": 1,
            "uo": 1
          })

    # CONSONANTS
    # --------------------------------------------------------------------------------
    @staticmethod
    def consonant_table():
        return dict({
            "b":   8,
            "ch":  5,
            "d":   8,
            "f":   3,
            "g":   5,
            "h":   4,
            "j":   4,
            "jx":  7,
            "k":   19,
            "l":   15,
            "m":   8,
            "n":   8,
            "nr":  5,
            "p":   3,
            "r":   6,
            "s":   8,
            "sh":  7,
            "str": 5,
            "t":   19,
            "tr":  14,
            "th":  5,
            "v":   7,
            "y":   8,
            "z":   5,
            "ng":  4,
            "lr":  5,
            "sk":  9,
            "shk": 14,
            "chk": 6,
            "kr":  8,
            "mr":  6,
            "kǩ":  2,
            "nň":  2,
            "mm̌":  2 ,
            "tk":  14,
            "kt":  14
        })

    # INITIALS
    # --------------------------------------------------------------------------------
    @staticmethod
    def initial_table():
        return dict({
            "b":  6,
            "ch": 3,
            "d":  6,
            "f":  3,
            "g":  3,
            "h":  3,
            "j":  3,
            "k":  16,
            "l":  16,
            "m":  3,
            "n":  3,
            "p":  3,
            "r":  9,
            "s":  8,
            "t":  8,
            "v":  16,
            "y":  16,
            "z":  3,
            "jx": 16,
            "sh": 16,
            "a":  3,
            "e":  3,
            "i":  3,
            "o":  3,
            "u":  3
         })

    # INITIALS
    # --------------------------------------------------------------------------------
    @staticmethod
    def coda_table():
        return dict({
            "fem": dict({
                "a":  20,
                "e":  12,
                "i":  10,
                "o":  2,
                "u":  2,
                "ai": 10,
                "oi": 5,
            }),
            "mas": dict({
                "k":   10,
                "r":   5,
                "t":   10,
                "nk":  2,
                "ngk": 1
            }),
            "neu": dict({
        		"m": 2,
        		"n": 6,
        		"v": 9,
        		"l": 9
            })
         })
