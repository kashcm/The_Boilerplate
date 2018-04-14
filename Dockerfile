FROM python:3.6.4-alpine
RUN apk --update add --no-cache bash \
    wget py-pip build-base linux-headers python-dev python supervisor mysql-client tini
WORKDIR /var/www/myproject
ENV PYTHONPATH $PYTHONPATH:/var/www/myproject
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY . .
ENTRYPOINT [ "/sbin/tini",  "-vg" ,"--" ]
CMD [ "/var/www/myproject/entrypoint.sh" ]
