FROM python:3.11-slim
COPY . .
CMD ["python", "main.py"]
