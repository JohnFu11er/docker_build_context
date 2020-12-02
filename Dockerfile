FROM centos/python-36-centos7

LABEL maintainer='john.adrift@gmail.com'

COPY ./greetings.py .

ENTRYPOINT [ "python", "greetings.py" ]