FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
RUN chmod a+x ./docker_scripts/alembic.sh
ENTRYPOINT ["./docker_scripts/alembic.sh"]
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]