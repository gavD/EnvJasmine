Summary: Command line runnable version of EnvJasmine that takes two arguments - source and test
Name: envjasmine
Version: 1
Release: 1
Source0: envjasmine-1.tar.gz
License: MIT
Group: MyJunk
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot

Requires: rhino >= 1.5
Requires: java-1.6.0-openjdk

%description
EnvJasmine allows you to run headless JavaScript tests. This is a bundled version that can be
installed and run against any code on the box. Requires rhino and OpenJDK-7. Recomended install
through Yum

%prep
%setup -q
%build
%install

# Check "man install" for options on the "install" command
# Create directory structure
install -d $RPM_BUILD_ROOT/opt/envjasmine
install -d $RPM_BUILD_ROOT/opt/envjasmine/bin
install -d $RPM_BUILD_ROOT/opt/envjasmine/include
install -d $RPM_BUILD_ROOT/opt/envjasmine/lib
install -d $RPM_BUILD_ROOT/opt/envjasmine/lib/envjs
install -d $RPM_BUILD_ROOT/opt/envjasmine/lib/jasmine
install -d $RPM_BUILD_ROOT/opt/envjasmine/lib/jasmine-ajax
install -d $RPM_BUILD_ROOT/opt/envjasmine/lib/jasmine-jquery
install -d $RPM_BUILD_ROOT/opt/envjasmine/lib/jasmine-jquery-reporter
install -d $RPM_BUILD_ROOT/opt/envjasmine/lib/jasmine-rhino-reporter
install -d $RPM_BUILD_ROOT/opt/envjasmine/lib/rhino
install -d $RPM_BUILD_ROOT/opt/envjasmine/lib/spanDir

# Install relevant files from directory structure
install -m 0755 -D bin/*sh $RPM_BUILD_ROOT/opt/envjasmine/bin
install -D include/*.js $RPM_BUILD_ROOT/opt/envjasmine/include
install -D lib/*.html $RPM_BUILD_ROOT/opt/envjasmine/lib/
install -D lib/*.js $RPM_BUILD_ROOT/opt/envjasmine/lib/
install -D lib/envjs/*.js $RPM_BUILD_ROOT/opt/envjasmine/lib/envjs/
install -D lib/jasmine/* $RPM_BUILD_ROOT/opt/envjasmine/lib/jasmine/
install -D lib/jasmine-ajax/* $RPM_BUILD_ROOT/opt/envjasmine/lib/jasmine-ajax/
install -D lib/jasmine-jquery/* $RPM_BUILD_ROOT/opt/envjasmine/lib/jasmine-jquery/
install -D lib/jasmine-rhino-reporter/* $RPM_BUILD_ROOT/opt/envjasmine/lib/jasmine-rhino-reporter/
install -D lib/rhino/* $RPM_BUILD_ROOT/opt/envjasmine/lib/rhino/
install -D lib/spanDir/* $RPM_BUILD_ROOT/opt/envjasmine/lib/spanDir/

# Install blank configuration file
touch $RPM_BUILD_ROOT/opt/envjasmine/include/conf.js
chmod 666 $RPM_BUILD_ROOT/opt/envjasmine/include/conf.js

%clean
rm -rf $RPM_BUILD_ROOTa

%post
echo " "
echo "EnvJasmine runner installed!"

%files
%dir /opt/envjasmine
/opt/envjasmine

