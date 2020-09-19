FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update -y
RUN apt-get install ffmpeg -y
RUN apt-get clean -y

COPY . .

CMD [ "python", "./halbvier.py" ]