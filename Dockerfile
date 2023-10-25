# Use the official Python image as a parent image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y libpoppler-cpp-dev poppler-utils

# Install Python dependencies
RUN pip install pipenv
RUN pipenv install --system


# CMD to run your Python script
CMD ["python", "main.py"]
