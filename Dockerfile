# Dockerfile untuk Railway (Alternatif jika Nixpacks bermasalah)
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Upgrade pip and install build dependencies first
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir cython==3.0.10 numpy==1.26.4

# Install dependencies except pystan (pystan needs special handling)
RUN pip install --no-cache-dir \
    Flask==3.0.0 \
    pandas==2.2.2 \
    sqlalchemy==2.0.23 \
    flask-sqlalchemy==3.1.1 \
    joblib==1.3.2 \
    scikit-learn==1.4.2 \
    gunicorn==21.2.0 \
    cmdstanpy==1.1.0 \
    packaging

# Install pystan separately (needs Cython and NumPy already installed)
RUN pip install --no-cache-dir --no-build-isolation pystan==2.19.1.1

# Install prophet (depends on pystan)
RUN pip install --no-cache-dir prophet==1.1.5

# Copy application files
COPY . .

# Expose port
EXPOSE $PORT

# Run gunicorn
CMD gunicorn app:app --bind 0.0.0.0:$PORT

