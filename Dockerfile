# Use a newer Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /myapp

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Create non-root user for security
RUN useradd -m myuser
USER myuser

# Expose port 5000 (default for Flask)
EXPOSE 5000

# Run the Flask app with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
