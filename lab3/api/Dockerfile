FROM python:3.9

WORKDIR /app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 libgl1-mesa-glx python3-opencv -y

COPY ./api/requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt

COPY ./api/app.py .
COPY ./api/src ./src
COPY ./api/models ./models
COPY ./api/assets ./assets
COPY ./api/output  ./output

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]