# Install 

# docker 
docker build -t backend_api

docker-compose up -d .

# run flask no docker linux
```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True
```

# windows
```sh
$ set FLASK_APP=app
$ set FLASK_ENV=Development
$ set FLASK_DEBUG=True
```
# run application
```sh

flask db init
flask db migrate
flask db upgrade
```
127.0.0.1:5000
| /list | return all data |
| /list/:id | return one row |
| /modify/:id | update new row |
| /delete/:id | delete new row |
