FROM python:3.12.7-slim-bullseye

RUN mkdir /usr/src/waterleak
COPY . /usr/src/waterleak
WORKDIR /usr/src/waterleak

RUN pip3 install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]
