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

from fastapi import FastAPI
from model import NormalizedWord, SynonymList, SingleSentence, FeatureVector
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from WordNetUtils import WordNetUtils
from Word2VecUtils import Word2VecUtils
from SentenceBertUtils import SentenceBertUtils
import os
from logging import config
config.fileConfig('logging.conf')
import logging
LOG = logging.getLogger(__name__)
import traceback


app = FastAPI(
    title="toposoid-common-nlp-english-web",
    version="0.4-SNAPSHOT"
)

wordNetUtils = WordNetUtils()
word2VecUtils = Word2VecUtils()
sentenceBertUtils = SentenceBertUtils()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# This API is for getting synonyms
@app.post("/getSynonyms")
def getSynonyms(normalizedWord:NormalizedWord):
    try:
        synonyms = []
        thresholdNoun = float(os.environ["SYNONYM_NOUN_SIMILARITY_THRESHHOLD_EN"])
        thresholdVerb = float(os.environ["SYNONYM_VERB_SIMILARITY_THRESHHOLD_EN"])
        if not normalizedWord.word.strip() == "":
            nounSynonums, verbSynonyms = wordNetUtils.getSynonyms(normalizedWord.word)
            for synonym in nounSynonums:
                if synonym in synonyms: continue
                if word2VecUtils.calcSimilarityByWord2Vec(normalizedWord.word, synonym) > thresholdNoun:
                    synonyms.append(synonym) 
            for synonym in verbSynonyms:
                if synonym in synonyms: continue
                if word2VecUtils.calcSimilarityByWord2Vec(normalizedWord.word, synonym) > thresholdVerb:
                    synonyms.append(synonym)    
        return JSONResponse(content=jsonable_encoder(SynonymList(synonyms=synonyms)))
    except Exception as e:
        LOG.error(traceback.format_exc())
        return JSONResponse({"status": "ERROR", "message": traceback.format_exc()})

@app.post("/getFeatureVector")
def getFeatureVector(input:SingleSentence):
    try:        
        vector = sentenceBertUtils.getFeatureVector(input.sentence)
        return JSONResponse(content=jsonable_encoder(FeatureVector(vector=list(vector))))
    except Exception as e:
        LOG.error(traceback.format_exc())
        return JSONResponse({"status": "ERROR", "message": traceback.format_exc()})
