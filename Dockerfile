FROM python:3.9

RUN mkdir /posts

WORKDIR /posts

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /posts/docker/*.sh

CMD ["gunicorn", "main:app", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]

