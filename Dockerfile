FROM python:3.12-slim

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod 755 /docker-entrypoint.sh

CMD ["/docker-entrypoint.sh"]
