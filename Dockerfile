FROM python:3.9-slim
WORKDIR /app/
COPY poetry.lock .
RUN pip install poetry
RUN poetry install  
COPY  expertpython/ .
ENTRYPOINT ["python", "expertpython/echo.py"]