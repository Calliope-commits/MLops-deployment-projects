# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.11-slim

# Allow immediate display of instructions and log messages in Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code into the container image.
# Set the working directory in the container to /app
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
# Execute pip install for the packages specified in requirements.txt
# it downloads the entire working directory
RUN pip install -r requirements.txt

# Run the web service when the container starts. Here, we use the gunicorn web server,
# with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to match the number of available cores.
# The timeout is set to 0 to disable worker timeouts to allow Cloud Run to manage instance scaling.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
