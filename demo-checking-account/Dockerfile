FROM 163.188.39.81:5000/image-python-server:ubuntu-16.04

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip3 install --no-cache-dir -r server/requirements.txt

RUN pip3 install --no-cache-dir -r server/test/additional_requirements.txt

WORKDIR /usr/src/app/server/test

RUN chmod -X test.py

RUN ["nosetests","--with-xunit"]

EXPOSE 5000

WORKDIR /usr/src/app

ENTRYPOINT ["python3"]

CMD ["-m", "server"]