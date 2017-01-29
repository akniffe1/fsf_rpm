#! /usr/bin/sh 
# Build the FSF RPM
cp -R .fsfserver-1-1 ~/rpmbuild/BUILDROOT
rpmbuild -ba fsf.spec
