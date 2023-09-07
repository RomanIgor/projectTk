FROM python:3.9-slim
WORKDIR /app
# Install system dependencies
RUN apt-get update && apt-get install -y libx11-6 libxext-dev libxrender-dev libxinerama-dev libxi-dev libxrandr-dev libxcursor-dev libxtst-dev tk-dev && rm -rf /var/lib/apt/lists/*
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "mainWindow.py" ]
