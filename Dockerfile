FROM python:3.9-buster
COPY ../requirements /requirements
COPY ../app.py /app.py
RUN pip install -r /requirements/requirements.txt