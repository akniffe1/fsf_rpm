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

# set proper file attribute on systemd file
if [ -e /etc/systemd/system/fsf.service ]; then chmod 644 /etc/systemd/system/fsf.service
fi

# symlink the server start and client
if [ ! -e /usr/local/bin/fsfserver ]; then ln -s $FSF_SRCDIR/fsf-server/main.py /usr/local/bin/fsfserver
fi 

if [ ! -e /usr/local/bin/fsfclient ]; then ln -s $FSF_SRCDIR/fsf-client/fsf_client.py /usr/local/bin/fsfclient
fi
