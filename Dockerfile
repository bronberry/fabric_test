FROM python:3.11.0-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
EXPOSE 8000/tcp
RUN apt-get update -y --no-install-recommends
RUN apt-get install -y --no-install-recommends
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN pip install --upgrade pip
RUN mkdir /fabric_test
COPY requirements.txt /fabric_test/
WORKDIR /fabric_test/
COPY . /fabric_test/
RUN pip install -r requirements.txt
RUN chmod +x entrypoint.*
