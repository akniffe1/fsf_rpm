#! /usr/bin/bash

FSF_LOGDIR=/data/fsf
FSF_ARCHIVEDIR=/data/fsf/archive
YARA_RULEDIR=/var/lib/yara-rules
FSF_SRCDIR=/opt/fsf


# $YARA_RULEDIR

#if [ ! -d $YARA_RULEDIR ]; then mkdir -m 744 $YARA_RULEDIR && chown -R fsf $YARA_RULEDIR
#fi 

# set up $FSF_LOGDIR
#if [ ! -d /data ]; then mkdir -m 0644 /data
#fi

#if [ ! -d $FSF_LOGDIR ]; then mkdir -m 644 $FSF_LOGDIR && chown -R fsf $FSF_LOGDIR
#fi

# set up $FSF_ARCHIVEDIR

#if [ ! -d $FSF_ARCHIVEDIR ]; then mkdir -m 644 $FSF_ARCHIVEDIR && chown -R fsf $FSF_ARCHIVEDIR
#fi

# remove $FSF_SRCDIR
rm -rf $FSF_SRCDIR

# symlink the server start and client
#if [ ! -e $FSF_SRCDIR/fsf_server/main.py ]; then ln -s $FSF_SRCDIR/fsf_server/main.py /usr/bin/fsfserver
#fi 
# remove the client and server symlinks in /usr/local/bin/
if [ -e /usr/local/bin/fsfclient ]; then rm /usr/local/bin/fsfclient
fi

if [ -e /usr/local/bin/fsfserver ]; then rm /usr/local/bin/fsfserver
fi

if [ -e /etc/systemd/system/fsf.service ]; then rm /etc/systemd/system/fsf.service && systemctl daemon-reload
fi
