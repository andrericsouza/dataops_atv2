FROM python:3.13-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Install dependencies first (cached if requirements unchanged)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py ./

# Expose port and run as non-root user
EXPOSE 5000
USER nobody
CMD ["python", "app.py"]
