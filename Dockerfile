# STEP 1
FROM python:3.9-slim

# STEP 2 Add a non-root user
RUN useradd -ms /bin/bash appuser

# STEP 3 Set the working directory inside the container
WORKDIR /myprogram_app

# STEP 4 Copy the current directory contents into the container at /myprogram_app
COPY . /myprogram_app

# STEP 5 Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# STEP 6 Change the ownership of /app to the non-root user
RUN chown -R appuser /myprogram_app

# STEP 7 Switch to the non-root user
USER appuser

# STEP 8 Make the script runs as an executable
RUN chmod +x myprogram.py

# STEP 9 Run the Python script by default when the container starts
ENTRYPOINT ["python", "./myprogram.py"]
