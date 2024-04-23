FROM python:3.11.8

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy your application code
COPY . .

# Expose any necessary ports
EXPOSE 5002

# Command to run your application
CMD ["python", "app.py"]
