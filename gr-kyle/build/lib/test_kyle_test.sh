#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/kh/gr-kyle/lib
export PATH=/home/kh/gr-kyle/build/lib:$PATH
export LD_LIBRARY_PATH=/home/kh/gr-kyle/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-kyle 
