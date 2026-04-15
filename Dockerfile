FROM python:3.12-alpine

RUN apk update && apk upgrade --no-cache

# Create app directory
WORKDIR /app

# Create non-root user
RUN adduser -D appuser

COPY requirements.txt .
RUN pip install --upgrade pip wheel==0.46.2 && \
    pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app/ ./app

# Change ownership
RUN chown -R appuser /app

# Drop to non-root user
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
