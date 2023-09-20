# Use the official Python image from the DockerHub
FROM python:3.10.7-slim

# Set the working directory in docker
WORKDIR /app

# Set environment variables
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
RUN chmod +x start.sh
CMD ["bash", "start.sh"]