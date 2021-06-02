FROM python:3.8

RUN  apt-get update

WORKDIR /venom

COPY . .

RUN pip install -r requirement.txt

ENV FLASK_APP=controllers.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]

