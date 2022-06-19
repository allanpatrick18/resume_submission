FROM python:3.8

WORKDIR /resume
COPY requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt

COPY . ./

CMD coverage run -m pytest -v /resume/test && coverage report && uvicorn app:app --reload