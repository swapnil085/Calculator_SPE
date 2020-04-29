FROM python:3.6.9
WORKDIR /
ADD calculator.py /
CMD [ "python", "./calculator.py" ]
