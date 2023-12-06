FROM python:3.9.10-alpine3.14

WORKDIR /backend

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /backend

WORKDIR /backend/app

ENV FLASK_APP=__init__

CMD ["flask", "run", "--host", "0.0.0.0"]


