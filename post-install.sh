#! /usr/bin/bash

FSF_LOGDIR=/data/fsf
FSF_ARCHIVEDIR=/data/fsf/archive
YARA_RULEDIR=/var/lib/yara-rules
FSF_SRCDIR=/opt/fsf

# set up Yara rules directory
if ! id "fsf" >/dev/null 2>&1; then useradd fsf
fi 

# set up $YARA_RULEDIR

if [ ! -d $YARA_RULEDIR ]; then sudo -u fsf && kdir -m 744 $YARA_RULEDIR
fi 

# set up $FSF_LOGDIR

if [ ! -d $FSF_LOGDIR ]; then sudo -u fsf && mkdir -m 0755 $FSF_LOGDIR
fi

# set up $FSF_ARCHIVEDIR

if [ ! -d $FSF_ARCHIVEDIR ]; then sudo -u fsf && mkdir -m 0755 $FSF_ARCHIVEDIR
fi

# finally change ownership of the $FSF_SCRDIR
chown -R fsf:fsf $FSF_SRCDIR

chown -R fsf:fsf $YARA_RULEDIR

# symlink the server start and client
if [ ! -e $FSF_SRCDIR/fsf_server/main.py ]; then ln -s $FSF_SRCDIR/fsf_server/main.py /usr/bin/fsfserver
fi 

if [ ! -e $FSF_SRCDIR/fsf_client/fsf_client.py ]; then ln -s $FSF_SRCDIR/fsf_client/fsf_client.py /usr/bin/fsfclient
fi
