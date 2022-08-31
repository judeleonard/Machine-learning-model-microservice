FROM python:3.8

WORKDIR /app

RUN apt-get -y update  && apt-get install -y \
  python3-dev \
  apt-utils \
  python-dev \
  build-essential \
&& rm -rf /var/lib/apt/lists/* \
apt-get update

RUN pip install --upgrade setuptools

COPY requirements.txt .
RUN pip install -r requirements.txt
VOLUME ./model

COPY . .

CMD gunicorn -w 3 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT