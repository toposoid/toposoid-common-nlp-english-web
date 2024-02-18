'''
  Copyright 2021 Linked Ideal LLC.[https://linked-ideal.com/]
 
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
 
      http://www.apache.org/licenses/LICENSE-2.0
 
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
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

