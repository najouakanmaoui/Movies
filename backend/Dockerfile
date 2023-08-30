FROM python:3.9
RUN apt-get update && apt-get install --yes redis-server postgresql-client
WORKDIR /backend
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]
