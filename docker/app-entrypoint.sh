#!/bin/sh

until PGPASSWORD=$POSTGRES_PASSWORD psql -h $POSTGRES_DB_HOST -U $POSTGRES_USER -c 'SELECT 1' > /dev/null 2>&1; do
  >&2 echo "Watching for database"
  sleep 1
done

./manage.py migrate
./manage.py create_default_superuser
./manage.py runserver 0.0.0.0:8000
