FROM python:3.8

RUN mkdir /code
WORKDIR /code

COPY . /code/

RUN pip install pip --upgrade
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["bash", "/entrypoint.sh"]