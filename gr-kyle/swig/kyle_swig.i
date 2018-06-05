/* -*- c++ -*- */

#define KYLE_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "kyle_swig_doc.i"

%{
#include "kyle/filter.h"
#include "kyle/hash.h"
%}


%include "kyle/filter.h"
GR_SWIG_BLOCK_MAGIC2(kyle, filter);
%include "kyle/hash.h"
GR_SWIG_BLOCK_MAGIC2(kyle, hash);
