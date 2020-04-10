
FROM arm32v7/python:3.7-slim-buster
RUN apt-get update
RUN apt-get install libssl-dev -y
RUN apt-get install libffi-dev
RUN apt-get install build-essential -y 
RUN pip install poetry
RUN pip install --upgrade pip

COPY ./pyproject.toml /app/
WORKDIR /app/
RUN poetry install --no-dev

COPY ./rpiserver /app/rpiserver
RUN poetry install --no-dev
ENTRYPOINT poetry run uvicorn rpiserver.server:led_app --reload --host 0.0.0.0 --port 8080
