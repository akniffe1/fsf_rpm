fpm -s dir -t rpm -n fsfserver -v 1 --iteration 1 \
-d "python-concurrentloghandler" \
-d "python-czipfile" \
-d "python-hachoir-core" \
-d "python-hachoir-metadata" \
-d "python-hachoir-parser" \
-d "python-hachoir-regex" \
-d "python-hachoir-subfile" \
-d "python-javatools" \
-d "python-oletools" \
-d "python-pefile" \
-d "python-pylzma" \
-d "python-pypdf2" \
-d "python-ssdeep" \
-d "python-requests" \
-d "python2-pyasn1" \
-d "python2-pyasn1-modules" \
-d "python-pyelftools" \
-d "python-rarfile" \
-d "python-xmltodict" \
-d "python-ctypescrypto" \
-d "macholibre" \
-d "autoconf" \
-d "python-devel" \
-d "automake" \
-d "libtool" \
-d "openssl" \
-d "openssl-devel" \
-d "net-tools" \
-d "ssdeep-devel" \
-d "libffi-devel" \
-d "unrar" \
-d "upx" \
-d "unzip" \
-d "cabextract" \
-d "yara == 3.4.0" \
--rpm-use-file-permissions \
--rpm-user fsf \
--rpm-group fsf \
--before-install ./pre-install.sh \
--after-install ./post-install.sh \
./yara/=/var/lib/yara-rules/ ./fsf/=/opt/fsf ./init.d/fsf.service=/etc/systemd/system/fsf.service

