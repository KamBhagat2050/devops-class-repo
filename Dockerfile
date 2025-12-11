# Use Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Expose port
EXPOSE 5000

# Run the app
CMD ["python3", "app.py"]
