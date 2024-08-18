FROM python:3.12-slim

ARG TOKEN
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD [ "python3", "main.py" ]
