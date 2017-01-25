#! /usr/bin/bash

# keeps the fabulous https://github.com/yara-rules/yara.git repo up to date and synchronized with a master index file 
# while ignoring / excluding certain sets of rules that add little / no value. 

BASERULEDIR=/var/lib/yara-rules
INDEXFILE=$BASERULEDIR/rules.yara
REPORULEDIR=$BASERULEDIR/rules/
RULESTODEPLOY=('malware_index.yar' 'CVE_Rules_index.yar' 'Crypto_index.yar' 'Antidebug_AntiVM_index.yar' 'Exploit-Kits_index.yar' 'Malicious_Documents_index.yar' 'Webshells_index.yar')

# first check for the ruledir, if its not there clone and update permissions
if ! [ -d $REPORULEDIR ]; then
  cd /var/lib/yara-rules && git clone https://github.com/yara-rules/rules.git
  chown -R fsf:fsf $REPORULEDIR
  chmod -R 744 $REPORULEDIR
fi

# next update the rules if there be updates to be had
cd $REPORULEDIR

if [[ $(git status --branch --porcelain | grep 'behind') = *behind* ]]; then
  git pull -f
fi

# next make sure the appropriate yara-rules/rules/*_index.yar are in the $INDEXFILE
if ! [[ $(grep 'yara-rules/rules' $INDEXFILE) = *yara-rules/rules* ]]; then
# Add the header
  sed -i -e "\$a\/\/yara-rules/rules" $INDEXFILE
# add the rules we care about
  for RULE in ${RULESTODEPLOY[@]}; do
    if ! [[ $(grep $RULE $INDEXFILE) = *$RULE* ]]; then 
      sed -i -e "\$ainclude\ \"$REPORULEDIR\/$RULE\"" $INDEXFILE
    fi
  done
fi
