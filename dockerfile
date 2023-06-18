# Use an official Python runtime as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# Install RabbitMQ and management plugin
RUN apt-get update && apt-get install -y rabbitmq-server
RUN rabbitmq-plugins enable rabbitmq_management

# Set the working directory in the container
WORKDIR /app

# Copy the project code to the container
COPY . /app

# Copy requirements.txt and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Django runs on (8000) and RabbitMQ's port (5672)
EXPOSE 8000 5672

# Set up the database
RUN python manage.py migrate

# Start RabbitMQ, Celery worker, and beat processes
CMD service rabbitmq-server start && \
    celery -A trading_platform worker --beat --loglevel=info & \
    python manage.py runserver 0.0.0.0:8000
