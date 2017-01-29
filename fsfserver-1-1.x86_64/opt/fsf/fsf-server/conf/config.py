#!/usr/bin/env python
#
# Basic configuration attributes for scanner. Used as default
# unless the user overrides them. 
#

SCANNER_CONFIG = { 'LOG_PATH' : '/var/lib/fsf/logs',
                   'YARA_PATH' : '/var/lib/yara-rules/rules.yara',
                   'EXPORT_PATH' : '/var/lib/fsf/archive',
                   'TIMEOUT' : 60,
                   'MAX_DEPTH' : 10 }

SERVER_CONFIG = { 'IP_ADDRESS' : "localhost",
                  'PORT' : 5800 }
