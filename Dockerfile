FROM python:3.10.7-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN apt-get update && apt-get install -y libx11-6 libxext-dev libxrender-dev libxinerama-dev libxi-dev libxrandr-dev libxss-dev libxtst-dev libxt-dev libxv-dev libxkbfile-dev libxkbcommon-dev libxkbcommon-x11-dev libxcomposite-dev libxcursor-dev libxdamage-dev libxfixes-dev libxft-dev libxi-dev libxinerama-dev libxkbcommon-dev libxrandr-dev libxrender-dev libxss-dev libxt-dev libxv-dev libxvmc-dev libxxf86vm-dev libxkbfile-dev tk-dev && rm -rf /var/lib/apt/lists/*

CMD ["python", "main.py"]

