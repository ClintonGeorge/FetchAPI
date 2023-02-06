# Use an official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /fetchAPI

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the rest of the source code to the container
COPY . .

# Expose port 8000 for the FastAPI API
EXPOSE 8000

# Run the cmd to start the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
