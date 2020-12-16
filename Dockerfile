FROM python:3
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get -y dist-upgrade \
    && apt-get install -y mysql-client cron \
      bind9-host vim-nox strace telnet supervisor
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/

EXPOSE 8000

ENTRYPOINT [ "/app/init" ]
