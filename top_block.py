#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu May 31 13:35:02 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import pipes
import sip
import sys
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self, uri='ip:192.168.2.1'):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.uri = uri

        ##################################################
        # Variables
        ##################################################
        self.sampsym = sampsym = 16
        self.samp_rate = samp_rate = 1000000
        self.period_samples = period_samples = 0x8000
        self.constellations = constellations = 4

        ##################################################
        # Blocks
        ##################################################
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(920e6, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(10, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)

        self.qtgui_sink_x_0_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_0_win)

        self.qtgui_sink_x_0_0.enable_rf_freq(False)



        self.pipes_pipereader_x_0 = pipes.pipereader_x('/temp.txt')
        self.digital_qam_mod_0 = digital.qam.qam_mod(
          constellation_points=constellations,
          mod_code="gray",
          differential=True,
          samples_per_symbol=sampsym,
          excess_bw=0.35,
          verbose=False,
          log=False,
          )
        self.digital_qam_demod_0 = digital.qam.qam_demod(
          constellation_points=constellations,
          differential=True,
          samples_per_symbol=sampsym,
          excess_bw=0.35,
          freq_bw=6.28/100.0,
          timing_bw=6.28/100.0,
          phase_bw=6.28/100.0,
          mod_code="gray",
          verbose=False,
          log=False,
          )
        self.blocks_unpacked_to_packed_xx_0_0 = blocks.unpacked_to_packed_bb(4, gr.GR_MSB_FIRST)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, '/home/dchaffee/gnuradio/latency/TSTestReceive', False)
        self.blocks_file_sink_0_0.set_unbuffered(True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_unpacked_to_packed_xx_0_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.digital_qam_demod_0, 0), (self.blocks_unpacked_to_packed_xx_0_0, 0))
        self.connect((self.digital_qam_mod_0, 0), (self.qtgui_sink_x_0_0, 0))
        self.connect((self.pipes_pipereader_x_0, 0), (self.digital_qam_mod_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.digital_qam_demod_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_uri(self):
        return self.uri

    def set_uri(self, uri):
        self.uri = uri

    def get_sampsym(self):
        return self.sampsym

    def set_sampsym(self, sampsym):
        self.sampsym = sampsym

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.samp_rate)

    def get_period_samples(self):
        return self.period_samples

    def set_period_samples(self, period_samples):
        self.period_samples = period_samples

    def get_constellations(self):
        return self.constellations

    def set_constellations(self, constellations):
        self.constellations = constellations


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--uri", dest="uri", type="string", default='ip:192.168.2.1',
        help="Set URI [default=%default]")
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(uri=options.uri)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
