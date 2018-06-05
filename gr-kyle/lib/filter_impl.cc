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
#include "filter_impl.h"

namespace gr {
  namespace kyle {

    static uint32_t hashf(uint32_t x) {
      x = ((x >> 16) ^ x) * 0x45d9f3b;
      x = ((x >> 16) ^ x) * 0x45d9f3b;
      x = (x >> 16) ^ x;
      return x;
    }

    filter::sptr
    filter::make(int msglen, int hashlen)
    {
      return gnuradio::get_initial_sptr
        (new filter_impl(msglen, hashlen));
    }

    /*
     * The private constructor
     */
    filter_impl::filter_impl(int msglen, int hashlen)
      : gr::block("filter",
              gr::io_signature::make(1, 1, sizeof(char)),
              gr::io_signature::make(1, 1, sizeof(char)))
    {
      prev = 0L;
      set_output_multiple(4);
    }

    /*
     * Our virtual destructor.
     */
    filter_impl::~filter_impl()
    {
    }

    void
    filter_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
      ninput_items_required[0] = noutput_items*8;
    }

    int
    filter_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const uint64_t *in = (const uint64_t *) input_items[0];
      uint32_t *out = (uint32_t *) output_items[0];

      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.

      int count = 0;
      
      // could be editted to start at the end and terminate from the first message in the buffer
      for (int j = 0; j < ninput_items[0]/8; j++) { 
        const uint64_t content = in[j];

        uint64_t select_first_32 = ((1L << 32) -1 ) << 32;
        uint64_t select_last_32  = ((1L << 32) -1 );

        for (int i = 0; i < 64; i+=2) {
          uint64_t select_all_but_first_i = (1L << (64-i)) - 1;
          uint64_t select_first_i = ((1L << i) - 1) << (64-i);
          uint64_t newlong = ((prev & select_all_but_first_i) << i) | ((content & select_first_i) >> (64-i));
          uint32_t hsh = (newlong & select_first_32) >> 32;
          uint32_t msg = (newlong & select_last_32 );

          if ((hashf(msg)) == hsh && hsh != 0) {
            // by god, we've done it!
            out[count] = msg;
            count++;
            break;
          }
        }

        prev = content;
      }

      consume_each(ninput_items[0]-(ninput_items[0]%8));

      // Tell runtime system how many output items we produced.
      return count*4;
    }

  } /* namespace kyle */
} /* namespace gr */

