#!/bin/bash
# Usage example:
#  jasmine-test.sh /path/to/project/src /path/to/project/spec/*.spec.js
#   => Fully specified
#   => This would execute all tests in /path/to/project/spec/*.spec.js with
#      sources (files to test) in /path/to/project/src
#
#  jasmine-test.sh /path/to/project/spec/*.spec.js
#   => Fully specified
#   => This would execute all tests in /path/to/project/spec/*.spec.js with
#      sources (files to test) in `pwd`/src
#
#  jasmine-test.sh
#   => Default
#   => This would execute all tests in `pwd`/spec/*.spec.js with sources (files to
#      test) in `pwd`/src
#
srcdir="`pwd`/src" # default source dir
tests="`pwd`/spec/*.spec.js" # default tests to run
DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" # Absolute dir of this file


# If user has specified 
if [ $# = 2 ]; then
  srcdir=$1
  tests=$2
elif [ $# = 1 ]; then
  tests=$1
fi

echo JS src is $srcdir
echo Spec files glob is $tests
echo "EnvJasmine.jsDir = '$srcdir/';" > $DIR/../conf.js
$DIR/run_all_tests.sh $tests
