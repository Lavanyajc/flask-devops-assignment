FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements1.txt

COPY app1.py .

EXPOSE 5000
CMD ["python", "app1.py"]

