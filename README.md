# scala-common-nlp-english-web
This is a WEB API that works as a microservice within the Toposoid project.
Toposoid is a knowledge base construction platform.(see [Toposoid Root Project](https://github.com/toposoid/toposoid.git))
This Microservice provides an NLP function that handles English and outputs the result in JSON.

[![Test And Build](https://github.com/toposoid/scala-common-nlp-english-web/actions/workflows/action.yml/badge.svg)](https://github.com/toposoid/scala-common-nlp-english-web/actions/workflows/action.yml)

<img width="1074" src="https://github.com/toposoid/toposoid-common-nlp-english-web/assets/82787843/4493f392-f189-4ce8-9603-a849a666f412">
<img width="1068" src="https://github.com/toposoid/toposoid-common-nlp-english-web/assets/82787843/c11af045-d16c-47a3-be62-02ffd35dc51f">


## Requirements
* Docker version 20.10.x, or later
* docker-compose version 1.22.x

### Memory requirements For Standalone
* Required: at least 4GB of RAM
* Required: at least 8.29GB of HDD(Docker Image Size)

## Setup For Standalone
```bssh
docker-compose up -d
```
The first startup takes a long time until docker pull finishes.

## Usage
```bash
#getSynonyms
curl -X POST -H "Content-Type: application/json" -H 'X_TOPOSOID_TRANSVERSAL_STATE: {"userId":"test-user", "username":"guest", "roleId":0, "csrfToken":""}' -d '{
    "word": "execute"
}' http://localhost:9008/getSynonyms
#getFeatureVector
curl -X POST -H "Content-Type: application/json" -H 'X_TOPOSOID_TRANSVERSAL_STATE: {"userId":"test-user", "username":"guest", "roleId":0, "csrfToken":""}' -d '{
    "sentence": "This is a test."
}' http://localhost:9008/getFeatureVector
```
* ref. http://localhost:9008/docs

# Note
* This microservice uses 9008 as the default port.
* The Bert model used in this repository is below.　
https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2
* You can change the SentenceBERT model by changing the environment variable TOPOSOID_SENTENCEBERT_MODEL_EN.

## License
This program is offered under a commercial and under the AGPL license.
For commercial licensing, contact us at https://toposoid.com/contact.  For AGPL licensing, see below.

AGPL licensing:
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

## Author
* Makoto Kubodera([Linked Ideal LLC.](https://linked-ideal.com/))

Thank you!
