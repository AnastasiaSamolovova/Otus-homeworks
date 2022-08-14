# docker run -p 8000:8000 -it app

FROM python:3.10-alpine

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install pipenv==2022.8.14

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --deploy --ignore-pipfile

COPY web-app .

EXPOSE 8000

CMD uvicorn main:app --host=0.0.0.0 --port=8000