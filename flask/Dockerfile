# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

# Install the dependencies
RUN apt-get update

RUN apt-get install -y \ 
    freetds-dev \
    freetds-bin \ 
    unixodbc-dev \
    tdsodbc

RUN dpkg-reconfigure tdsodbc 

run pip install --upgrade pip

RUN pip install -r requirements.txt


# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
