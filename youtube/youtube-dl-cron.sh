#!/bin/sh
PIDFILE=/youtube-dl.pid

echo "Starting youtube-dl"

if [ -f $PIDFILE ]
then
    PID=$(cat $PIDFILE)
    ps -p $PID > /dev/null 2>&1
    if [ $? -eq 0 ]
    then
        echo "Process already running"
        exit 1
    else
        ## Process not found assume not running
        echo $$ > $PIDFILE
        if [ $? -ne 0 ]
        then
            echo "Could not create PID file"
            exit 1
        fi
    fi
else
    echo $$ > $PIDFILE
    if [ $? -ne 0 ]
    then
        echo "Could not create PID file"
        exit 1
    fi
fi



youtube-dl --download-archive $OUTPUTFOLDER/downloaded.txt -i \
           -o "$OUTPUTFOLDER/%(uploader)s/%(upload_date)s - %(title)s - (%(duration)ss) [%(resolution)s].%(ext)s" \
           -f bestvideo[ext=mp4]+bestaudio --batch-file=$CHANNEL_FILE



rm $PIDFILE
