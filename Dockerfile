# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /code

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Default command (is overridden by docker-compose)
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]