FROM debian:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-tk \
    python3-venv \
    && apt-get clean

WORKDIR /app

RUN python3 -m venv venv
RUN . /app/venv/bin/activate && pip install --upgrade pip && pip install ttkbootstrap

ENV DISPLAY=:0

COPY . /app

CMD ["/bin/bash", "-c", ". /app/venv/bin/activate && python3 speedReader.py"]
