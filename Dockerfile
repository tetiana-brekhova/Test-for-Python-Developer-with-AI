FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3000
ENV FLASK_APP=main.py
CMD ["flask", "--app", "main", "run", "--host=0.0.0.0", "--port=3000"]