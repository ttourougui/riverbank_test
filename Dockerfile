FROM python:3.7.5


COPY ./app /app

WORKDIR /app

RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]

CMD [ "app.py" ]

