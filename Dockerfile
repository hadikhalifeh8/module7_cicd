FROM python:3.12

WORKDIR /app

# RUN python -m venv testenv

COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code in the container
COPY . .

# Expose the port of the jupyter NoteBook (if applicable)
EXPOSE 8888

# COMMAND TO RUN FASTAPI Application using uvicorn .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]






























# FROM python:3.12

# WORKDIR /app

# # Install system dependencies required by some Python libs
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libssl-dev \
#     libffi-dev \
#     python3-dev \
#     && rm -rf /var/lib/apt/lists/*

# COPY requirements.txt .

# # Remove Windows-only packages before installing
# RUN grep -v -E "pywin32|pywinpty" requirements.txt > clean_requirements.txt

# # Install Python dependencies
# RUN pip install --no-cache-dir --prefer-binary -r clean_requirements.txt

# COPY . .

# EXPOSE 8000

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


