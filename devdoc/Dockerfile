# Use the official Python image for the app
FROM python:3.12.5-bullseye

# Set the working directory inside the container
WORKDIR /devdoc

# Copy the application code to the container
COPY . /devdoc

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for the Python app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Expose the application port
EXPOSE 8000

# Command to run the Python application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
