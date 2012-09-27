#!/bin/bash
#
# Build script to create an installable RPM
VER=1

# Collate the source code together
cp -R ../bin ../include ../lib SOURCES
pushd SOURCES
tar czvf envjasmine-$VER.tar.gz envjasmine-$VER
popd

# Build the RPM
rpmbuild -ba SPECS/envjasmine.spec

# Copy to Vagrant shared folder for easy distribution
# This last line will fail if you're not using Vagrant
cp RPMS/noarch/envjasmine-$VER-1.noarch.rpm /vagrant
