# Install 

# docker 
docker build -t backend_api

docker-compose up -d .

# run flask no docker linux
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

# windows
set FLASK_APP=app
set FLASK_ENV=Development
set FLASK_DEBUG=True

# run application
flask db init
flask db migrate
flask db upgrade
