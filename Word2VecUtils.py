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

import spacy
import os
import numpy as np

#This module provides utilities for the English version of WordNet

class Word2VecUtils():
    nlp = None
    def __init__(self) :
        self.nlp = spacy.load(os.environ["TOPOSOID_SPACY_MODEL_EN"])
        #self.nlp = spacy.load('en_core_web_lg')
    
    #This function calculates the similarity between two words given by a parameter in Word2Vec
    def calcSimilarityByWord2Vec(self, word, synonym):
        return self.nlp(word).similarity(self.nlp(synonym))
    
    #This function gets synonyms with high similarity from Word2Vec.
    def getSimilarWords(self, word):
        thresholdW2V = float(os.environ["TOPOSOID_WORD2VEC_SIMILARITY_THRESHHOLD_EN"])        
        similarWords = set()
        words, scores = self.mostSimilar(word)
        for (w, s) in zip(words, scores):
            if s > thresholdW2V and not w == word:
                similarWords.add(w)
        return similarWords

    #This function gets synonyms with high similarity from Word2Vec.
    def mostSimilar(self, word, topn=10):
        ms = self.nlp.vocab.vectors.most_similar(
        self.nlp(word).vector.reshape(1,self.nlp(word).vector.shape[0]), n=topn)
        words = [self.nlp.vocab.strings[w] for w in ms[0][0]]        
        if len(words) == 0: return [], []
        distances = list(ms[2][0])
        return words, distances

