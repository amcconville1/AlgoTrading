# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY src/ .

# Expose port 8080
EXPOSE 8080

# Run the application
CMD ["python", "main.py"]
