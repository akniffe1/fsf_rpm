%global build_timestamp %(date +"%Y%m%d")
%global commit0 %(git ls-remote --quiet  https://github.com/EmersonElectricCo/fsf.git | awk '/HEAD/ {print $1}')
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global checkout  %{build_timestamp}git%{shortcommit0}

%define _prefix /opt/fsf


Name:     fsf
Summary:  File Scanning Framework is a recursive file scanning solution that provides a service for static file analysis.
Version:  1.1
Release:  1.%{checkout}%{?dist}
License:  Apache License, Version 2.0
Source0:  https://github.com/EmersonElectricCo/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{checkout}.tar.gz
Patch0:   0001-Adds-service-file-for-managing-fsf-server-daemon.patch
Group:    System
Summary:  File Scanning Framework is a recursive file scanning solution that provides a service for static file analysis.
URL:      https://github.com/EmersonElectricCo/%{name}
Prefix:   %{_prefix}

Provides: fsf-server

BuildRequires: git
BuildRequires: bash
BuildRequires: python2-devel
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires:      openssl-devel
Requires:      autoconf 
Requires:      automake
Requires:      libtool
Requires:      python2-devel  
Requires:      cabextract  
Requires:      libffi-devel  
Requires:      libtool  
Requires:      macholibre  
Requires:      net-tools  
Requires:      openssl  
Requires:      python-concurrentloghandler  
Requires:      python-ctypescrypto  
Requires:      python-czipfile  
Requires:      python-hachoir-core  
Requires:      python-hachoir-metadata  
Requires:      python-hachoir-parser  
Requires:      python-hachoir-regex  
Requires:      python-hachoir-subfile  
Requires:      python-javatools  
Requires:      python-oletools  
Requires:      python-pefile  
Requires:      python-pyelftools  
Requires:      python-pylzma  
Requires:      python-pypdf2  
Requires:      python-rarfile  
Requires:      python-requests  
Requires:      python-ssdeep  
Requires:      python-xmltodict  
Requires:      python2-pyasn1  
Requires:      python2-pyasn1-modules  
#Requires:      rpmlib(CompressedFileNames) <= 3.0.4-1
#Requires:      rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires:      ssdeep-devel  
Requires:      unrar  
Requires:      unzip  
Requires:      upx  
Requires:      yara = 3.4.0

%description
The File Scanning Framework Server provides a daemonized python socket server and recursive file analysis capability. 


%prep
%setup -q -n %{name}-%{commit0} 
git init
git config user.email "..."
git config user.name "..."
git add .
git commit -a -q -m "%{version} baseline."

git am %{patches}

%build

%install

# Copy source files
mkdir -p %{buildroot}%{prefix}
cp -R %{_builddir}/%{buildsubdir}/fsf-client %{buildroot}%{_prefix}/
cp -R %{_builddir}/%{buildsubdir}/fsf-server %{buildroot}%{_prefix}/

# Make default log dirs
mkdir -p %{buildroot}/%{_sharedstatedir}/fsf/logs
mkdir -p %{buildroot}/%{_sharedstatedir}/fsf/archive

# Make dirs for yara rules
mkdir -p %{buildroot}/var/lib/
mv %{buildroot}/%{_prefix}/fsf-server/yara %{buildroot}/var/lib/yara-rules

# Copy systemd service file
mkdir -p %{buildroot}/usr/lib/systemd/system
cp %{_builddir}/%{buildsubdir}/contrib/fsf.service %{buildroot}/usr/lib/systemd/system/

%{__python2} -O -m py_compile %{buildroot}/%{_prefix}/fsf-client/conf/*.py
%{__python2} -O -m py_compile %{buildroot}/%{_prefix}/fsf-client/fsf_client.py
%{__python2} -O -m py_compile %{buildroot}/%{_prefix}/fsf-server/*.py
%{__python2} -O -m py_compile %{buildroot}/%{_prefix}/fsf-server/conf/*.py
%{__python2} -O -m py_compile %{buildroot}/%{_prefix}/fsf-server/modules/*.py

%files
%attr(0664, root, root) %{_unitdir}/fsf.service
%defattr(-,fsf,fsf)
%dir %attr(0755, fsf, fsf) %{_sharedstatedir}/fsf/logs
%dir %attr(0755, fsf, fsf) %{_sharedstatedir}/fsf/archive

%config(noreplace) %attr(0664, fsf, fsf) %{_prefix}/fsf-client/conf/*.py
%attr(0755, fsf, fsf) %{_prefix}/fsf-client/conf/*.py[co]
%attr(0755, fsf, fsf) %{_prefix}/fsf-client/fsf_client.py
%attr(0755, fsf, fsf) %{_prefix}/fsf-client/fsf_client.py[co]

%config(noreplace) %attr(0664, fsf, fsf) %{_prefix}/fsf-server/conf/*.py

%attr(0664, fsf, fsf) %{_prefix}/fsf-server/conf/*.py[oc]
%attr(0755, fsf, fsf) %{_prefix}/fsf-server/modules/*.py[oc]
%attr(0755, fsf, fsf) %{_prefix}/fsf-server/modules/*.py
%attr(0755, fsf, fsf) %{_prefix}/fsf-server/*.py[oc]
%attr(0755, fsf, fsf) %{_prefix}/fsf-server/*.py

%attr(0664, fsf, fsf) %{_prefix}/fsf-server/jq/*.jq
%attr(0664, fsf, fsf) /var/lib/yara-rules/*.yara

%pre -p /bin/sh
#! /usr/bin/bash
# 
# Add fsf user
if ! id "fsf" >/dev/null 2>&1; then useradd -M fsf
fi
%post -p /bin/sh
#! /usr/bin/bash
FSF_SRCDIR=/opt/fsf

# symlink the server start and client
if [ ! -e /usr/local/bin/fsfserver ]; then ln -s $FSF_SRCDIR/fsf-server/main.py /usr/local/bin/fsfserver
fi 

if [ ! -e /usr/local/bin/fsfclient ]; then ln -s $FSF_SRCDIR/fsf-client/fsf_client.py /usr/local/bin/fsfclient
fi

%postun -p /bin/sh
#! /usr/bin/bash


# remove the client and server symlinks in /usr/local/bin/
if [ -e /usr/local/bin/fsfclient ]; then rm /usr/local/bin/fsfclient
fi

if [ -e /usr/local/bin/fsfserver ]; then rm /usr/local/bin/fsfserver
fi

# reload the systemd daemon now that we pulled a systemd service file out
systemctl daemon-reload

%changelog
