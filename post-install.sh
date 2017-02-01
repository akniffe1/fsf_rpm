#! /usr/bin/bash

FSF_LOGDIR=/data/fsf
FSF_ARCHIVEDIR=/data/fsf/archive
YARA_RULEDIR=/var/lib/yara-rules
FSF_SRCDIR=/opt/fsf


# set up $YARA_RULEDIR

if [ ! -d $YARA_RULEDIR ]; then mkdir -m 744 $YARA_RULEDIR && chown -R fsf $YARA_RULEDIR
fi 

# set up $FSF_LOGDIR
if [ ! -d /data ]; then mkdir -m 0644 /data
fi

if [ ! -d $FSF_LOGDIR ]; then mkdir -m 644 $FSF_LOGDIR && chown -R fsf $FSF_LOGDIR
fi

# set up $FSF_ARCHIVEDIR

if [ ! -d $FSF_ARCHIVEDIR ]; then mkdir -m 644 $FSF_ARCHIVEDIR && chown -R fsf $FSF_ARCHIVEDIR
fi

# set permissions on the $FSF_SRCDIR
chown -R fsf $FSF_SRCDIR

# symlink the server start and client
#if [ ! -e $FSF_SRCDIR/fsf_server/main.py ]; then ln -s $FSF_SRCDIR/fsf_server/main.py /usr/bin/fsfserver
#fi 

if [ ! -e /usr/bin/fsfclient ]; then ln -s $FSF_SRCDIR/fsf-client/fsf_client.py /usr/bin/fsfclient
fi
