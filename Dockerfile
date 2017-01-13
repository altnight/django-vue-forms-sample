FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y python3
RUN apt-get install -y python-virtualenv python-pip

RUN git clone https://github.com/altnight/muscle-percentage-sample.git
RUN cd muscle-percentage-sample

RUN virtualenv venv -p `which python3`
RUN . ./venv/bin/activate
# TODO: github にあげたら試す。あと 8000 で立ち上がってるサーバーを見る方法を探す
#RUN pip install -r requirements.txt
#RUN python manage.py migrate
#RUN python manage.py runserver 0.0.0.0:8000

CMD ['/bin/bash']
