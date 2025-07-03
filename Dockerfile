FROM toposoid/python-nlp-english:0.6

ARG TARGET_BRANCH
ARG SENTENCE_TRANSFORMER_MODEL

WORKDIR /app
ENV DEPLOYMENT=local

RUN apt-get update \
&& apt-get -y install git \
&& git clone https://github.com/toposoid/toposoid-common-nlp-english-web.git \
&& cd toposoid-common-nlp-english-web \
&& git fetch origin ${TARGET_BRANCH} \
&& git checkout ${TARGET_BRANCH} \
&& sed -i s/__##GIT_BRANCH##__/${TARGET_BRANCH}/g requirements.txt \
&& pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt \
&& mkdir -p models \
&& mkdir -p models/sentence-transformers_${SENTENCE_TRANSFORMER_MODEL} \
&& mv -f /tmp/${SENTENCE_TRANSFORMER_MODEL}/* ./models/sentence-transformers_${SENTENCE_TRANSFORMER_MODEL}/ \
&& rm -Rf /tmp/*

COPY ./docker-entrypoint.sh /app/
ENTRYPOINT ["/app/docker-entrypoint.sh"]
