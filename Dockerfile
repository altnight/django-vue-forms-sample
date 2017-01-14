FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y python3
RUN apt-get install -y python-virtualenv python-pip

RUN git clone https://github.com/altnight/django-vue-forms-sample.git
RUN cd django-vue-forms-sample && virtualenv venv -p `which python3`
RUN cd django-vue-forms-sample && . ./venv/bin/activate && pip install -r requirements.txt
RUN cd django-vue-forms-sample && . ./venv/bin/activate && python manage.py migrate

COPY ./bootstrap.sh /
ENTRYPOINT ["/bootstrap.sh"]
