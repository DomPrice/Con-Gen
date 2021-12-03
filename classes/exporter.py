# -*- coding: utf-8 -*-

# Import dependencies
import json

# CONLANG WORD GENERATOR - EXPORTER
# ---------------------------------------------------------------------------------
# Returns the generated words in a variaty of data formats for use in API calls

class Exporter:

    # INIT
    # -----------------------------------------------------------------------------
    def __init__(self):
        """Constructor for Exporter"""

    # END __init__
    # -----------------------------------------------------------------------------

    # GENERATE WEIGHTED TABLE
    # -----------------------------------------------------------------------------
    def export_json(self,words):
        """Returns the word list data in JSON format"""
        return json.dumps(words)

    # END export_json
    # -----------------------------------------------------------------------------
