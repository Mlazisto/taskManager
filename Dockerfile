FROM pypy:latest

# Setting the working directory inside the container
WORKDIR /app

# Copying the files to the working directory
COPY . /app/

# Running the Python script when the container starts
CMD python task_manager.py
