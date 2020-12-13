FROM centos/python-36-centos7

LABEL maintainer='john.adrift@gmail.com'

COPY ./car_report.py .

RUN pip install requests

ENTRYPOINT [ "python", "car_report.py" ]
