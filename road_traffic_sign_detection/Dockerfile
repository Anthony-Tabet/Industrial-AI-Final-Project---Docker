FROM python:3.11.8

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx ffmpeg libsm6 libxext6

# Install PyTorch with CUDA support
# RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the model file into the container
COPY ./road_traffic_sign_detection/model/ /app/road_traffic_sign_detection/model/

# Copy your application code
COPY . /app

# Expose any necessary ports
EXPOSE 5003

# Command to run your application
CMD ["python", "app.py"]
