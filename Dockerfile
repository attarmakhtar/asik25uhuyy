# Dockerfile untuk Railway (Alternatif jika Nixpacks bermasalah)
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (needed for building Python packages with C extensions)
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    cmake \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Upgrade pip and install build dependencies first
RUN pip install --upgrade pip setuptools wheel

# Install NumPy first (needed by many packages)
RUN pip install --no-cache-dir numpy==1.26.4

# Install all dependencies from requirements.txt
# Prophet 1.1.5 uses cmdstanpy, not pystan, so no special handling needed
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port
EXPOSE $PORT

# Run gunicorn
CMD gunicorn app:app --bind 0.0.0.0:$PORT

