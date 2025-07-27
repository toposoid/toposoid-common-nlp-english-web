'''
  Copyright (C) 2025  Linked Ideal LLC.[https://linked-ideal.com/]
 
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Affero General Public License as
  published by the Free Software Foundation, version 3.
 
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Affero General Public License for more details.
 
  You should have received a copy of the GNU Affero General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from nltk.corpus import wordnet as wn

#This module provides utilities for the English version of WordNet

class WordNetUtils(): 

    #Extract synonyms of parameter words using WordNet
    def getSynonyms(self, word):
        synonymsNoun = set()
        synonymsVerb = set()        
        for syn in wn.synsets(word, pos=wn.NOUN):
            for l in syn.lemmas():
                if "_" not in l.name() and "-" not in l.name():
                    synonymsNoun.add(l.name())
        for syn in wn.synsets(word, pos=wn.VERB):
            for l in syn.lemmas():
                if "_" not in l.name() and "-" not in l.name():
                    synonymsVerb.add(l.name())
        return (synonymsNoun, synonymsVerb)