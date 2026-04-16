FROM python:3.10

WORKDIR /app

COPY . .

RUN echo "Running Python setup"

CMD ["python", "app.py"]