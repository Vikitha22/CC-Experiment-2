FROM ubuntu:24.04

RUN apt-get update && \
    apt-get install -y python3-fastapi python3-uvicorn && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY app.py .

EXPOSE 8000

CMD ["python3", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
