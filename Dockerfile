FROM python:3.13.3

COPY . /opt

RUN pip --version

RUN pip install -r /opt/requirements.txt

CMD ["python3","/opt/app.py" ]
