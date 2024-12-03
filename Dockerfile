# Use a base image suitable for the target architecture
FROM python:3.9-slim-buster

# Add a non-root user for better security
RUN apt-get update && apt-get install -y passwd \
    && useradd -ms /bin/bash appuser

# Set the working directory inside the container
WORKDIR /myprogram_app

# Copy the application files into the container
COPY . /myprogram_app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Set appropriate ownership for the application directory
RUN chown -R appuser /myprogram_app

# Switch to the non-root user
USER appuser

# Make the script executable and ensure it has a proper shebang
RUN chmod +x myprogram.py

# Set the entry point to execute the script with default arguments
ENTRYPOINT ["python3", "/myprogram_app/myprogram.py"]