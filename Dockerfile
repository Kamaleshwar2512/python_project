
# Use lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Prevent Python from generating bytecode
ENV PYTHONDONTWRITEBYTECODE=1

# Display Python logs immediately
ENV PYTHONUNBUFFERED=1

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run the application
CMD ["python", "main.py"]
