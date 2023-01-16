FROM mysql

COPY db/init_db.sql /tmp

CMD [ "mysqld", "--init-file=/tmp/init_db.sql" ]