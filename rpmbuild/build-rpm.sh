#!/bin/bash
#
# Build script to create an installable RPM
VER=1
REL=2

# Collate the source code together
cp -R ../bin ../include ../lib SOURCES
pushd SOURCES
mkdir envjasmine-$VER
mv {bin,include,lib} envjasmine-$VER
tar czvf envjasmine-$VER.tar.gz envjasmine-$VER
popd

# Build the RPM
rpmbuild --define "_topdir `pwd`" -ba SPECS/envjasmine.spec

# Copy to Vagrant shared folder for easy distribution
# This last line will fail if you're not using Vagrant
cp RPMS/noarch/envjasmine-$VER-$REL.noarch.rpm /vagrant
