# python docker with flask installed
FROM python:3.10

WORKDIR /app
COPY app.py /app

RUN pip install flask opentelemetry-distro 
RUN opentelemetry-bootstrap -a install

ENTRYPOINT [ "flask", "run", "-h", "0.0.0.0", "-p", "80"]