FROM python:3.8-slim-buster
RUN pip3 install Flask
WORKDIR /app
COPY app.py .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80", "--debug"]
