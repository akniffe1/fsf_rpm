.PHONY:	rpm clean source

build_timestamp:=$(shell date +"%Y%m%d")
shortcommit0:=$(shell \
	git ls-remote --quiet  https://github.com/EmersonElectricCo/fsf.git \
	 | awk '/HEAD/ {print substr($$1,1,7)}')

NAME:=fsf
VERSION:=1.1
RELEASE?=1.$(build_timestamp)git$(shortcommit0)
ARCH:= x86_64
DIST:=$(shell rpm --eval '%{dist}')

SOURCE0 = SOURCES/$(NAME)-$(VERSION)-$(build_timestamp)$(shortcommit0).tar.gz
#SPEC_DEFINES:=	--define 'release_version $(VERSION)' \
		--define 'scala_version $(SCALA_VERSION)' \
		--define 'build_num $(RELEASE)' 

PWD = $(shell pwd)

rpm:   RPMS/$(NAME)-$(VERSION)-$(RELEASE)$(DIST).$(ARCH).rpm
srpm:  SRPMS/$(NAME)-$(VERSION)-$(RELEASE)$(DIST).src.rpm

SOURCES/$(SOURCE0): SPECS/$(NAME).spec
	spectool -g -C SOURCES $<

sources: SOURCES/$(SOURCE0)
	
SRPMS/%.src.rpm: SOURCES/$(SOURCE0) SPECS/$(NAME).spec
	rpmbuild -bs --nodeps \
		--define "_sourcedir $(PWD)/SOURCES" \
		--define "_srcrpmdir $(PWD)/SRPMS" \
		SPECS/$(NAME).spec

RPMS/%.x86_64.rpm: SRPMS/%.src.rpm 
	mock clean
	mock --installdeps $<
	mock --no-clean --no-cleanup-after --resultdir=$(PWD)/RPMS $(SPEC_DEFINES) $<


$(SOURCE): KEYS $(SOURCE).asc
	@wget -q $(URL)
	gpg --verify $(SOURCE).asc $(SOURCE)

$(SOURCE).asc:
	@wget -q https://dist.apache.org/repos/dist/release/kafka/$(KAFKA_VERSION)/$(SOURCE).asc

KEYS:
	@wget -q https://dist.apache.org/repos/dist/release/kafka/KEYS
	gpg --import KEYS

