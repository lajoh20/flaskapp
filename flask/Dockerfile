# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app

# step 6 clone repo
RUN git clone https://gitlab+deploy-token-841743:dxTKrk9XttSffHLTz9Ws@gitlab.com/azuracu/basic-flask-with-nginx-template.git ./ 

# Copy the current directory contents into the container at /app 
ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
