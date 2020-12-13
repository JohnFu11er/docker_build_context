FROM centos/python-36-centos7

LABEL maintainer='john.adrift@gmail.com'

USER root

COPY ./car_report.py .

RUN yum update -y
RUN pip install requests

ENTRYPOINT [ "python", "car_report.py" ]
