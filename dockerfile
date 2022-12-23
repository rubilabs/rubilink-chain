FROM python:3.9-buster
COPY .. /requirements
COPY ../app.py /app.py
RUN pip freeze > /requirements.txt
