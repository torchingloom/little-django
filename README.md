# Django project example
* Install docker (https://www.docker.com)
* Read docs about docker-compose (https://docs.docker.com/compose)
* Run `docker-compose --file docker/docker-compose.yml up --build` in console
* Open `http://localhost:8000/admin` in browser (username/password `admin/123`)
* Run django manage commands `docker-compose --file docker/docker-compose.yml run web ./manage.py …`