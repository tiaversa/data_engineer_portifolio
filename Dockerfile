# To make the requirements stable
FROM python:3.12

COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r /requirements.txt