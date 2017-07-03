FROM python:3.6

COPY requirements.txt .

RUN python -m pip install -U pip setuptools wheel \
    && pip install -r requirements.txt \
    && mkdir /app

COPY . /app

WORKDIR /app

CMD [ "python" ]