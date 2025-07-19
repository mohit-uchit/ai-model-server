FROM python:3.10-slim

# System dependencies
RUN apt-get update && apt-get install -y ffmpeg git && \
    pip install --upgrade pip

# Set working dir
WORKDIR /app

# Install Python deps
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app code
COPY main.py .

# Run the service
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
