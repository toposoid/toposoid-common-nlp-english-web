#!/bin/bash

cd /app/scala-common-nlp-english-web
uvicorn api:app --reload --host 0.0.0.0 --port 9008
