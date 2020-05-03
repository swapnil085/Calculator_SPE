FROM python:3.6.9
WORKDIR /
ADD . /
CMD [ "python", "./calculator.py" ]
