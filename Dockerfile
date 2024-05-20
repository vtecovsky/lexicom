FROM python:3.11

ADD requirements.txt app/requirements.txt
RUN pip install -r app/requirements.txt
COPY . /app
WORKDIR app
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
