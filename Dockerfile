FROM python:3.9
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y libmagic-dev

WORKDIR /ecotextile

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY script.sh /script.sh
RUN chmod +x /script.sh

COPY . .