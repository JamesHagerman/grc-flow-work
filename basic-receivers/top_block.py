#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Jan 25 11:28:02 2018
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import math
import osmosdr
import sip
import sys
import time


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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
        # Variables
        ##################################################
        self.rf_freq = rf_freq = 434.2e6
        self.audio_rate = audio_rate = 48000
        self.squelch_thresh = squelch_thresh = -30
        self.samp_rate = samp_rate = 1000000
        self.samp_per_sym = samp_per_sym = 1000
        self.offset = offset = 10
        self.low_cut = low_cut = 10e3
        self.fsk_deviation_hz = fsk_deviation_hz = 4500
        self.average_len = average_len = 150
        self.audio_interp = audio_interp = rf_freq/audio_rate

        ##################################################
        # Blocks
        ##################################################
        self._squelch_thresh_range = Range(-90, 1, 1, -30, 200)
        self._squelch_thresh_win = RangeWidget(self._squelch_thresh_range, self.set_squelch_thresh, 'Squelch', "counter_slider", float)
        self.top_layout.addWidget(self._squelch_thresh_win)
        self._samp_per_sym_range = Range(1, 10000, 10, 1000, 200)
        self._samp_per_sym_win = RangeWidget(self._samp_per_sym_range, self.set_samp_per_sym, 'Samples per symbol', "counter_slider", int)
        self.top_layout.addWidget(self._samp_per_sym_win)
        self._offset_range = Range(-20, 20, 1, 10, 200)
        self._offset_win = RangeWidget(self._offset_range, self.set_offset, 'Offset', "counter_slider", int)
        self.top_layout.addWidget(self._offset_win)
        self._low_cut_range = Range(0, samp_rate/2, 1e3, 10e3, 200)
        self._low_cut_win = RangeWidget(self._low_cut_range, self.set_low_cut, 'Low Cut', "counter_slider", float)
        self.top_layout.addWidget(self._low_cut_win)
        self._average_len_range = Range(1, 1000, 1, 150, 200)
        self._average_len_win = RangeWidget(self._average_len_range, self.set_average_len, 'Averaging Length', "counter_slider", int)
        self.top_layout.addWidget(self._average_len_win)
        self.rtlsdr = osmosdr.source( args="numchan=" + str(1) + " " + 'rtl=0' )
        self.rtlsdr.set_sample_rate(samp_rate)
        self.rtlsdr.set_center_freq(rf_freq, 0)
        self.rtlsdr.set_freq_corr(0, 0)
        self.rtlsdr.set_dc_offset_mode(0, 0)
        self.rtlsdr.set_iq_balance_mode(0, 0)
        self.rtlsdr.set_gain_mode(False, 0)
        self.rtlsdr.set_gain(10, 0)
        self.rtlsdr.set_if_gain(20, 0)
        self.rtlsdr.set_bb_gain(20, 0)
        self.rtlsdr.set_antenna('', 0)
        self.rtlsdr.set_bandwidth(0, 0)
          
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
        	50, #size
        	samp_rate, #samp_rate
        	"After Complete Recovery", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(1)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-0.5, 1.5)
        
        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_NEG, 5, 0, 0, "start_tag")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	80*1000, #size
        	samp_rate, #samp_rate
        	"After Average", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(1)
        self.qtgui_time_sink_x_0.set_y_axis(-15, 15)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_NEG, 5, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rf_freq, #fc
        	samp_rate*2, #bw
        	"Before and after filter and Squelch", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1.enable_grid(False)
        self.qtgui_freq_sink_x_0_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1.enable_control_panel(True)
        
        if not True:
          self.qtgui_freq_sink_x_0_1.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_1.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_1_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	10, samp_rate, low_cut, 10e3, firdes.WIN_HAMMING, 6.76))
        self.digital_correlate_access_code_tag_bb_0 = digital.correlate_access_code_tag_bb('10101010101010101010101010101010', 0, 'start_tag')
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(samp_per_sym*(1+0.0), 0.1, 0, 0.01, 0.01)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bf((0,1), 1)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_unpacked_to_packed_xx_0 = blocks.unpacked_to_packed_bb(1, gr.GR_MSB_FIRST)
        self.blocks_tagged_stream_align_0 = blocks.tagged_stream_align(gr.sizeof_char*1, 'start_tag')
        self.blocks_tag_debug_0_0 = blocks.tag_debug(gr.sizeof_char*1, 'start_tag_found', "start_tag"); self.blocks_tag_debug_0_0.set_display(True)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(average_len, 1.0/average_len, 4000)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/jamis/my_root/dev/radio/grc-flow-work/basic-receivers/output-working-2fsk-front-end-bytes.raw', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_vff((offset, ))
        self.analog_simple_squelch_cc_0 = analog.simple_squelch_cc(squelch_thresh, 1)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(samp_rate/(2*math.pi*fsk_deviation_hz/8.0))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.blocks_add_const_vxx_0_0, 0))    
        self.connect((self.analog_simple_squelch_cc_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_moving_average_xx_0, 0))    
        self.connect((self.blocks_moving_average_xx_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))    
        self.connect((self.blocks_moving_average_xx_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_tagged_stream_align_0, 0), (self.blocks_unpacked_to_packed_xx_0, 0))    
        self.connect((self.blocks_unpacked_to_packed_xx_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_correlate_access_code_tag_bb_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))    
        self.connect((self.digital_correlate_access_code_tag_bb_0, 0), (self.blocks_tag_debug_0_0, 0))    
        self.connect((self.digital_correlate_access_code_tag_bb_0, 0), (self.blocks_tagged_stream_align_0, 0))    
        self.connect((self.digital_correlate_access_code_tag_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.analog_quadrature_demod_cf_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0_1, 1))    
        self.connect((self.rtlsdr, 0), (self.analog_simple_squelch_cc_0, 0))    
        self.connect((self.rtlsdr, 0), (self.qtgui_freq_sink_x_0_1, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_rf_freq(self):
        return self.rf_freq

    def set_rf_freq(self, rf_freq):
        self.rf_freq = rf_freq
        self.rtlsdr.set_center_freq(self.rf_freq, 0)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(self.rf_freq, self.samp_rate*2)
        self.set_audio_interp(self.rf_freq/self.audio_rate)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.set_audio_interp(self.rf_freq/self.audio_rate)

    def get_squelch_thresh(self):
        return self.squelch_thresh

    def set_squelch_thresh(self, squelch_thresh):
        self.squelch_thresh = squelch_thresh
        self.analog_simple_squelch_cc_0.set_threshold(self.squelch_thresh)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(self.rf_freq, self.samp_rate*2)
        self.low_pass_filter_0.set_taps(firdes.low_pass(10, self.samp_rate, self.low_cut, 10e3, firdes.WIN_HAMMING, 6.76))
        self.analog_quadrature_demod_cf_0.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz/8.0))

    def get_samp_per_sym(self):
        return self.samp_per_sym

    def set_samp_per_sym(self, samp_per_sym):
        self.samp_per_sym = samp_per_sym
        self.digital_clock_recovery_mm_xx_0.set_omega(self.samp_per_sym*(1+0.0))

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self.blocks_add_const_vxx_0_0.set_k((self.offset, ))

    def get_low_cut(self):
        return self.low_cut

    def set_low_cut(self, low_cut):
        self.low_cut = low_cut
        self.low_pass_filter_0.set_taps(firdes.low_pass(10, self.samp_rate, self.low_cut, 10e3, firdes.WIN_HAMMING, 6.76))

    def get_fsk_deviation_hz(self):
        return self.fsk_deviation_hz

    def set_fsk_deviation_hz(self, fsk_deviation_hz):
        self.fsk_deviation_hz = fsk_deviation_hz
        self.analog_quadrature_demod_cf_0.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz/8.0))

    def get_average_len(self):
        return self.average_len

    def set_average_len(self, average_len):
        self.average_len = average_len
        self.blocks_moving_average_xx_0.set_length_and_scale(self.average_len, 1.0/self.average_len)

    def get_audio_interp(self):
        return self.audio_interp

    def set_audio_interp(self, audio_interp):
        self.audio_interp = audio_interp


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
