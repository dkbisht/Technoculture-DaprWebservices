FROM python:3.10

WORKDIR /app

COPY ./app /app

RUN pip install -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]