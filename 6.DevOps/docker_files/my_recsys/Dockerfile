FROM python:buster

RUN mkdir /src
RUN mkdir /models
COPY src /src
COPY models /models
ADD ./requirements.txt /

RUN pip install -r requirements.txt

WORKDIR /src
CMD ["python3", "recommender_app.py"]