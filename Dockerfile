FROM python:3.10-slim

# Set env vars
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create non-root user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Set working dir
WORKDIR /app

# Copy files
COPY . /app

# Change ownership (optional but good practice)
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

# Example: install requirements if you have requirements.txt
# RUN pip install -r requirements.txt

# Example: set CMD to run your Flask app
# CMD ["python", "app.py"]
# Use the official Python image as the base
# Install dependencies
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install flask_cors

# Expose the port the app runs on
EXPOSE 5501

# Define the command to run the application
CMD ["python", "app.py"]
