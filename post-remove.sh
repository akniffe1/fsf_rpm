#! /usr/bin/bash

FSF_LOGDIR=/var/lib/fsf
FSF_ARCHIVEDIR=/var/lib/fsf/archive
YARA_RULEDIR=/var/lib/yara-rules
FSF_SRCDIR=/opt/fsf
FSF_RUNDIR=/run/fsf

# remove $FSF_SRCDIR
rm -rf $FSF_SRCDIR

# remove RUNDIR
rm -rf $FSF_RUNDIR

# remove the client and server symlinks in /usr/local/bin/
if [ -e /usr/local/bin/fsfclient ]; then rm /usr/local/bin/fsfclient
fi

if [ -e /usr/local/bin/fsfserver ]; then rm /usr/local/bin/fsfserver
fi

if [ -e /etc/systemd/system/fsf.service ]; then rm /etc/systemd/system/fsf.service && systemctl daemon-reload
fi
