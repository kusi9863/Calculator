FROM python:3.11-slim

WORKER /app

COPY pyproject.toml .
RUN pip install --no-cache-dir .

COPY src/ ./src/

EXPOSE 5000

CMD ["python", "src/api.py"]
