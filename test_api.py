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
from fastapi.testclient import TestClient
from api import app
from model import NormalizedWord, SynonymList
import pytest

#This is a unit test module
client = TestClient(app)
def test_EmptyWord():    
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": ""})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())
    assert synonymList.synonyms == []

def test_SimpleVerb():    
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": "execute"})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())
    assert synonymList.synonyms.sort() == ['accomplish', 'perform'].sort()

def test_SimpleNoun():    
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": "agreement"})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())
    assert synonymList.synonyms.sort() == ['accord', 'arrangement'].sort()

def test_VocabularyNotFoundInWordNet():    
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": "research"})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())
    assert synonymList.synonyms.sort() == ['RESEARCH', 'Studies', 'STUDIES', 'Research', 'studies'].sort()

def test_VocabularyNotFoundInWord2Vec():    
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": "aslkfjg"})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())
    assert synonymList.synonyms == []
