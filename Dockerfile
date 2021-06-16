FROM python:3.9.5

WORKDIR /app

COPY src /app

CMD ["python3", "psik.py"]