#! /usr/bin/bash

FSF_LOGDIR=/var/lib/fsf
FSF_ARCHIVEDIR=/var/lib/fsf/archive
YARA_RULEDIR=/var/lib/yara-rules
FSF_SRCDIR=/opt/fsf


# set up $YARA_RULEDIR

if [ ! -d $YARA_RULEDIR ]; then mkdir -m 755 $YARA_RULEDIR && chown -R fsf:fsf $YARA_RULEDIR
fi

# Ensure the default logdir exists
if [ ! -d $FSF_LOGDIR ]; then mkdir -p -m 755 $FSF_LOGDIR && chown -R fsf:fsf $FSF_LOGDIR
fi

# set up $FSF_ARCHIVEDIR

if [ ! -d $FSF_ARCHIVEDIR ]; then mkdir -p -m 755 $FSF_ARCHIVEDIR && chown -R fsf:fsf $FSF_ARCHIVEDIR
fi

# set permissions on the $FSF_SRCDIR
chown -R fsf:fsf $FSF_SRCDIR

# set proper file attribute on systemd file
if [ -e /usr/lib/systemd/system/fsf.service ]; then chmod 644 /usr/lib/systemd/system/fsf.service
fi

# symlink the server start and client
if [ ! -e /usr/local/bin/fsfserver ]; then ln -s $FSF_SRCDIR/fsf-server/main.py /usr/local/bin/fsfserver
fi

if [ ! -e /usr/local/bin/fsfclient ]; then ln -s $FSF_SRCDIR/fsf-client/fsf_client.py /usr/local/bin/fsfclient
fi
