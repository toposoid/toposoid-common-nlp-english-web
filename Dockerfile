FROM python:3.9

WORKDIR /app
ARG TARGET_BRANCH
ENV DEPLOYMENT=local

RUN apt-get update \
&& apt-get -y install git \
&& git clone https://github.com/toposoid/scala-common-nlp-english-web.git \
&& cd scala-common-nlp-english-web \
&& git fetch origin ${TARGET_BRANCH} \
&& git checkout ${TARGET_BRANCH} \
&& pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt \
&& python -m spacy download en_core_web_lg \
&& python installWordNet.py


COPY ./docker-entrypoint.sh /app/
ENTRYPOINT ["/app/docker-entrypoint.sh"]