# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Nginx and Supervisord
RUN apt-get update && apt-get install -y supervisor && rm -rf /var/lib/apt/lists/*

# Copy Supervisord configuration file
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose port 1234
EXPOSE 1234

# Copy the environment variables
COPY .env .env

# Create directories for Gunicorn logs
RUN mkdir -p /var/log/gunicorn

# Start Supervisord to manage both Nginx and Gunicorn
CMD ["/usr/bin/supervisord"]
