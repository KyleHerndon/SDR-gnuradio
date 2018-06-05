/* -*- c++ -*- */
/* 
 * Copyright 2018 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <iostream>

#include <gnuradio/io_signature.h>
#include "hash_impl.h"

namespace gr {
  namespace kyle {

    static uint32_t hashf(uint32_t x) {
      x = ((x >> 16) ^ x) * 0x45d9f3b;
      x = ((x >> 16) ^ x) * 0x45d9f3b;
      x = (x >> 16) ^ x;
      return x;
    }

    hash::sptr
    hash::make(int msglen, int hashlen)
    {
      return gnuradio::get_initial_sptr
        (new hash_impl(msglen, hashlen));
    }

    /*
     * The private constructor
     */
    hash_impl::hash_impl(int msglen, int hashlen)
      : gr::sync_interpolator("hash",
              gr::io_signature::make(1, 1, sizeof(char)),
              gr::io_signature::make(1, 1, sizeof(char)), 2)
    {
      set_output_multiple(8);
      std::cout << "Hello, I am the hash function!" << std::endl;
    }

    /*
     * Our virtual destructor.
     */
    hash_impl::~hash_impl()
    {
    }

    int
    hash_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const uint32_t *in = (const unsigned int *) input_items[0];
      uint32_t *out = (unsigned int *) output_items[0];

      //std::cout << "I received a request for " << noutput_items << std::endl;
      if (noutput_items%8 !=0) {
        std::cout << "Terrible thing happened" << std::endl;
        exit(1);
      }

      int ninput_items = noutput_items/2;
      // Do <+signal processing+>
      for(size_t i = 0; i < ninput_items/4; i++) {
        //std::cout << "First data point is " << in[0] << std::endl;
        out[2*i] = hashf(in[0]);
        out[2*i+1] = in[0];
      }

      // Tell runtime system how many output items we produced.
      this->consume_each(ninput_items-(ninput_items%4)); // remove remainder 

      return noutput_items;
    }

  } /* namespace kyle */
} /* namespace gr */

