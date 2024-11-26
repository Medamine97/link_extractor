# STEP 1: Use a base image suitable for the target architecture
FROM --platform=linux/amd64 python:3.9-slim-buster as build

# STEP 2: Add a non-root user for better security
RUN apt-get update && apt-get install -y passwd \
    && useradd -ms /bin/bash appuser

# STEP 3: Set the working directory inside the container
WORKDIR /myprogram_app

# STEP 4: Copy the application files into the container
COPY . /myprogram_app

# STEP 5: Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# STEP 6: Set appropriate ownership for the application directory
RUN chown -R appuser /myprogram_app

# STEP 7: Switch to the non-root user
USER appuser

# STEP 8: Make the script executable and ensure it has a proper shebang
RUN chmod +x myprogram.py

# STEP 9: Set the entry point to execute the script with default arguments
ENTRYPOINT ["python3", "/myprogram_app/myprogram.py", "-u", "https://www.google.com", "-o", "json"]
