FROM python:3.8

RUN apt-get update

ENV INSTALL_PATH /bank-app

ENV PYTHONPATH="${INSTALL_PATH}:${PYTHONPATH}"

RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

RUN pip install --upgrade setuptools

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "./entrypoint.sh" ]