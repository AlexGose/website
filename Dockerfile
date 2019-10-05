# containerize pelican
FROM ubuntu:16.04
RUN mkdir /website
ADD requirements.txt /website/
WORKDIR /website
RUN apt-get update && apt-get install -y python-pip
RUN pip install -r requirements.txt
