FROM python:3.11-alpine

# Create app directory
WORKDIR /app

# Create non-root user
RUN adduser -D appuser

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

# Change ownership
RUN chown -R appuser /app

USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]