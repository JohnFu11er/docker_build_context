FROM centos/python-36-centos7

LABEL maintainer='john.adrift@gmail.com'

COPY ./car_report.py .

ENTRYPOINT [ "python", "car_report.py" ]
