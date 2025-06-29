FROM python:3.10-slim

# Set env vars
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create non-root user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Set working dir
WORKDIR /app

# Copy project files
COPY . /app

# Copy requirements first and install deps as ROOT (default)
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    chown -R appuser:appgroup /app

# Switch to non-root user AFTER dependencies are installed
USER appuser

# Expose port
EXPOSE 5501

# Command to run app
CMD ["python", "app.py"]
