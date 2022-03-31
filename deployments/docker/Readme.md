# Barter 
### Barter app is the Python Djanjo(Framework) application 

* Since this is an Python Django application there are packages needs to be installed and it's in requirements.txt file. 
* Below you'll find Dockerfile example file could be used in the application
* Please check out the `Dockerfile` example [link](https://docs.docker.com/samples/django/)

## Dockerfile example

```
FROM python:3.6-slim

RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt /code/

RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## Bonus:
### Build Image and *run* on local machine

`git clone https://{link}/barter`

`cd barter`
`docker build -t rahymov/barter .` #build docker image example name
<!-- will build image -->
`docker images` # check the image if exist?
`docker run --rm -it -p 8000:8000 rahymov/barter` 
or 
`docker run --rm -it -d -p 8000:8000 rahymov/barter` # run in the background


* Push your image to hub.docker.com
`docker push rahymov/barter` # to push your image to hub.docker.com
