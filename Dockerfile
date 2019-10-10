FROM python:3.7

RUN mkdrir /webapps
WORKDIR /webapps

COPY requirement.txt /webapps/
RUN pip install -r /webapps/requirements.txt

ADD . /webapps/

EXPOSE 8000
