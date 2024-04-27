FROM python:3.11.8

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx ffmpeg libsm6 libxext6

# Install PyTorch with CUDA support
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy your application code
COPY . /app

# Expose any necessary ports
EXPOSE 5003

# Command to run your application
CMD ["python", "app.py"]
