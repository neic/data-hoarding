FROM alpine:3.9

RUN apk add youtube-dl py3-requests\
  && rm -rf /var/cache/apk/*


ADD get_subscriptions.py /etc/periodic/everymin/01-get_subscriptions
ADD youtube-dl-cron.sh /etc/periodic/everymin/02-youtube-dl

ADD crontab /etc/crontabs/root

ENV CHANNEL_FILE=/tmp/channel_list.txt
ENV OUTPUTFOLDER=/youtube

CMD ["crond", "-f"]
