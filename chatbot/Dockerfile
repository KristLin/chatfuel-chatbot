FROM python:3.6.4
WORKDIR /service
COPY ./app /service
RUN pip3 install -r requirements.txt
WORKDIR /service/demo
CMD python3 __init__.py
