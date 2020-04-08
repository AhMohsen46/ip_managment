# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /ip_managment

# Set the working directory to /ip_managment
WORKDIR /ip_managment

# Copy the current directory contents into the container at /ip_managment
ADD . /ip_managment/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
