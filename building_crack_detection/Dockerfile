FROM python:3.11.8

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx ffmpeg libsm6 libxext6

# Install PyTorch with CUDA support
# RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy your application code
COPY . .

# Copy the model file into the container
COPY C:\Users\Antho\OneDrive\Desktop\Industrial AI Final Project - Docker\building_crack_detection\model\building_crack_detection.pt /app/model/

# Expose any necessary ports
EXPOSE 5001

# Command to run your application
CMD ["python", "app.py"]
