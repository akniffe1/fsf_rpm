%define defaultbuildroot /
AutoProv: no
%undefine __find_provides
AutoReq: no
%undefine __find_requires
# Do not try autogenerate prereq/conflicts/obsoletes and check files
%undefine __check_files
%undefine __find_prereq
%undefine __find_conflicts
%undefine __find_obsoletes
# Be sure buildpolicy set to do nothing
%define __spec_install_post %{nil}
# Something that need for rpm-4.1
%define _missing_doc_files_terminate_build 0
#dummy
#dummy
#BUILDHOST:    knifehands
#BUILDTIME:    Wed Feb  1 17:41:09 2017
#SOURCERPM:    fsfserver-1-1.src.rpm

#RPMVERSION:   4.13.0

#INSTALLTIME:  Fri Jan 27 13:54:32 2017
#INSTPREFIXES: /
#OS:           linux
#SIZE:           164696
#ARCHIVESIZE:           179548
#ARCH:         x86_64
BuildArch:     x86_64
Name:          fsfserver
Version:       1
Release:       1
License:       unknown 
Group:         default
Summary:       File Scanning Framework Server


URL:           https://github.com/akniffe1/fsf_rpm
Vendor:        MOCYBER
Packager:      <adamkniffen@gmail.com>





Prefix:        /
Provides:      fsfserver = 1-1
Provides:      fsfserver(x86-64) = 1-1
Requires:      /bin/sh  
Requires:      autoconf  
Requires:      automake  
Requires:      cabextract  
Requires:      libffi-devel  
Requires:      libtool  
Requires:      macholibre  
Requires:      net-tools  
Requires:      openssl  
Requires:      openssl-devel  
Requires:      python-concurrentloghandler  
Requires:      python-ctypescrypto  
Requires:      python-czipfile  
Requires:      python-devel  
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
#suggest
#enhance
%description
The File Scanning Framework Server provides a daemonized python socket server and recursive file analysis capability. 
%files
%attr(0755, fsf, fsf) "/run/fsf/"
%attr(0755, fsf, fsf) "/var/lib/fsf/logs"
%attr(0755, fsf, fsf) "/var/lib/fsf/archive"
%attr(0664, root, root) "/etc/systemd/system/fsf.service"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-client/__init__.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-client/conf/__init__.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-client/conf/config.py"
%attr(0755, fsf, fsf) "/opt/fsf/fsf-client/fsf_client.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/__init__.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/conf/__init__.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/conf/config.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/conf/disposition.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/daemon.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/jq/embedded_sfx_rar_w_exe.jq"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/jq/exe_in_zip.jq"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/jq/fresh_vt_scan.jq"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/jq/macro_gt_five_suspicious.jq"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/jq/many_objects.jq"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/jq/more_than_ten_yara.jq"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/jq/no_yara_hits.jq"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/jq/one_module.jq"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/jq/pe_recently_compiled.jq"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/jq/vt_broadbased_detections_found.jq"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/jq/vt_exploit_detections_found.jq"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/jq/vt_match_found.jq"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/jq/vt_match_not_found.jq"
%attr(0775, fsf, fsf) "/opt/fsf/fsf-server/main.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/EXTRACT_CAB.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/EXTRACT_EMBEDDED.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/EXTRACT_GZIP.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/EXTRACT_HEXASCII_PE.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/EXTRACT_RAR.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/EXTRACT_RTF_OBJ.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/EXTRACT_SWF.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/EXTRACT_TAR.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/EXTRACT_UPX.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/EXTRACT_VBA_MACRO.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/EXTRACT_ZIP.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/META_BASIC_INFO.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/META_ELF.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/META_JAVA_CLASS.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/META_MACHO.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/META_OLECF.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/META_OOXML.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/META_PDF.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/META_PE.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/META_PE_SIGNATURE.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/META_VT_INSPECT.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/SCAN_YARA.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/__init__.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/modules/template.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/processor.py"
%attr(0664, fsf, fsf) "/opt/fsf/fsf-server/scanner.py"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/ft_cab.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/ft_elf.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/ft_exe.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/ft_gzip.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/ft_jar.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/ft_java_class.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/ft_macho.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/ft_office_open_xml.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/ft_ole_cf.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/ft_pdf.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/ft_rar.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/ft_rtf.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/ft_swf.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/ft_tar.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/ft_zip.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/misc_compressed_exe.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/misc_hexascii_pe_in_html.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/misc_no_dosmode_header.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/misc_ooxml_core_properties.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/misc_pe_signature.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/misc_upx_packed_binary.yara"
%attr(0664, fsf, fsf) "/var/lib/yara-rules/rules.yara"
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
