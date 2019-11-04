FROM ubuntu:latest

RUN apt-get -yqq update
RUN apt-get -yqq install python-pip python-dev

ADD .ssh/id_rsa /root/.ssh/id_rsa
ADD .ssh/id_rsa.pub /root/.ssh/id_rsa.pub
ADD ./ /ansible
WORKDIR /ansible

RUN pip install -r requirements.txt
