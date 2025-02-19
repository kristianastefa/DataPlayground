FROM python:buster

RUN mkdir /src

COPY src /src
ADD ./requirements.txt /

RUN pip install -r requirements.txt

WORKDIR /src
CMD ["python3", "feedback_app.py"]