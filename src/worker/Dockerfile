FROM python:3.10

WORKDIR /usr/src/app

COPY worker/requirements.txt requirements.txt
COPY common/requirements.txt common-requirements.txt

RUN pip3 install -r requirements.txt
RUN pip3 install -r common-requirements.txt

COPY worker/main.py main.py
ADD common common/

CMD ["python3", "main.py"]