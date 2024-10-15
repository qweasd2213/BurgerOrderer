FROM python:3.9-slim

RUN apt-get update && apt-get install -y postgresql postgresql-contrib

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

ENV POSTGRES_USER=your_username
ENV POSTGRES_PASSWORD=your_password
ENV POSTGRES_DB=your_database_name

EXPOSE 6000
EXPOSE 5432

CMD service postgresql start && \
    sudo -u postgres psql -c "CREATE USER ${POSTGRES_USER} WITH PASSWORD '${POSTGRES_PASSWORD}';" && \
    sudo -u postgres createdb -O ${POSTGRES_USER} ${POSTGRES_DB} && \
    flask run --host=0.0.0.0 --port=6000

ENTRYPOINT ["python3", "app.py"]
