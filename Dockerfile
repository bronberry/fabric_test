FROM python:3.11.0-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONWARNINGS=ignore
EXPOSE 8000/tcp
EXPOSE 8000
RUN apt-get update -y --no-install-recommends
RUN apt-get install -y --no-install-recommends
RUN pip install --user pipenv
ENV PATH="${PATH}:/root/.local/bin"
RUN mkdir /fabric_test
#COPY Pipfile.lock Pipfile.lock /fabric_api/
COPY requirements.txt /fabric_test/
WORKDIR /fabric_test/
RUN pip install -r requirements.txt
COPY . /fabric_test/
RUN chmod +x entrypoint.*
