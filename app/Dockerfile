# Start from official Python 3.11 slim image (small and fast)
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first — Docker caches this layer
# so it won't reinstall packages unless requirements change
COPY requirements.txt .

# Install the Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app code
COPY . .

# Tell Docker the app runs on port 5000
EXPOSE 5000

# Start the app using gunicorn (production server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]