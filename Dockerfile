FROM python:3.7

WORKDIR /fastapiblog
COPY . /fastapiblog
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["./docker-entrypoint.sh"]