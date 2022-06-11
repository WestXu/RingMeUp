FROM python:3.8-slim-buster

# prevent invisible logs when running
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip3 install .

ENTRYPOINT ["ring"]
