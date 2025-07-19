FROM python:3.10-slim

# System dependencies
RUN apt-get update && apt-get install -y ffmpeg git && \
    apt-get clean

# Create working directory
WORKDIR /app

# Install virtualenv and create venv310
RUN pip install virtualenv && \
    python3.10 -m venv venv310

# Activate and install deps into venv310
COPY requirements.txt .
RUN . venv310/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Copy application code
COPY main.py .

# Use shell form to activate venv before running
CMD ["/bin/bash", "-c", ". venv310/bin/activate && uvicorn main:app --host 0.0.0.0 --port 8002"]
