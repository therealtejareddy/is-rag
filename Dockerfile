# Base image
FROM ubuntu:22.04

# Environment setup
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    curl \
    sudo \
    python3 \
    python3-pip

# Install Python packages
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy Streamlit app
COPY . .

# Expose ports
EXPOSE 8501

# Run both services
CMD streamlit run main.py --server.port=8501 --server.address=0.0.0.0
