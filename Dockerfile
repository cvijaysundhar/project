FROM python:3.13.3

COPY . /opt

WORKDIR /opt

EXPOSE 8080

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]

