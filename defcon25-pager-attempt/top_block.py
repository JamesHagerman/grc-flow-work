#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Jul 28 20:06:05 2017
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

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250000
        self.low_cutoff = low_cutoff = 1700
        self.high_cutoff = high_cutoff = 2300
        self.freq = freq = 432.25e6
        self.decimation = decimation = 4
        self.bps = bps = 45.45
        self.audio_rate = audio_rate = 48000
        self.audio_interp = audio_interp = 4

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.samp_rate,
        	callback=self.set_samp_rate,
        	label='Sample Rate',
        	converter=forms.float_converter(),
        )
        self.Add(self._samp_rate_text_box)
        _low_cutoff_sizer = wx.BoxSizer(wx.VERTICAL)
        self._low_cutoff_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_low_cutoff_sizer,
        	value=self.low_cutoff,
        	callback=self.set_low_cutoff,
        	label='Low Cutoff',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._low_cutoff_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_low_cutoff_sizer,
        	value=self.low_cutoff,
        	callback=self.set_low_cutoff,
        	minimum=10,
        	maximum=20e3,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_low_cutoff_sizer)
        _high_cutoff_sizer = wx.BoxSizer(wx.VERTICAL)
        self._high_cutoff_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_high_cutoff_sizer,
        	value=self.high_cutoff,
        	callback=self.set_high_cutoff,
        	label='High Cutoff',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._high_cutoff_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_high_cutoff_sizer,
        	value=self.high_cutoff,
        	callback=self.set_high_cutoff,
        	minimum=10,
        	maximum=20e3,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_high_cutoff_sizer)
        _freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	label='Frequency',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_sizer,
        	value=self.freq,
        	callback=self.set_freq,
        	minimum=300e6,
        	maximum=3.8e9,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_freq_sizer)
        self.wxgui_scopesink2_0_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Scope Before Thresh',
        	sample_rate=audio_rate,
        	v_scale=1,
        	v_offset=0,
        	t_scale=1,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_FREE,
        	y_axis_label='Counts',
        )
        self.GridAdd(self.wxgui_scopesink2_0_0.win, 1, 2, 1, 1)
        self.wxgui_fftsink2_0_0_0 = fftsink2.fft_sink_f(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=20,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=48000,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='Audio after filter',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0_0_0.win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=192000,
                decimation=250000,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(1, 0)
        self.osmosdr_source_0.set_iq_balance_mode(1, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(20, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.gr_sub_xx_0 = blocks.sub_ff(1)
        self.gr_moving_average_xx_0 = blocks.moving_average_ff(2*samp_rate/decimation, 1.0/(2*samp_rate/decimation), samp_rate/decimation)
        self.dc_blocker_xx_0 = filter.dc_blocker_cc(32, True)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/jamis/Desktop/radio-audio-rtty-170-45.wav', True)
        self.band_pass_filter_0 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, audio_rate, low_cutoff, high_cutoff, bps, firdes.WIN_BLACKMAN, 6.76))
        self.audio_sink_0 = audio.sink(8000, 'default', False)
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=audio_rate,
        	quad_rate=audio_rate*audio_interp,
        	tau=75e-6,
        	max_dev=5e3,
          )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_rx_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.gr_moving_average_xx_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.gr_sub_xx_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.wxgui_fftsink2_0_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.audio_sink_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.analog_nbfm_rx_0, 0))
        self.connect((self.gr_moving_average_xx_0, 0), (self.gr_sub_xx_0, 1))
        self.connect((self.gr_sub_xx_0, 0), (self.wxgui_scopesink2_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.dc_blocker_xx_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self._samp_rate_text_box.set_value(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.gr_moving_average_xx_0.set_length_and_scale(2*self.samp_rate/self.decimation, 1.0/(2*self.samp_rate/self.decimation))

    def get_low_cutoff(self):
        return self.low_cutoff

    def set_low_cutoff(self, low_cutoff):
        self.low_cutoff = low_cutoff
        self._low_cutoff_slider.set_value(self.low_cutoff)
        self._low_cutoff_text_box.set_value(self.low_cutoff)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.audio_rate, self.low_cutoff, self.high_cutoff, self.bps, firdes.WIN_BLACKMAN, 6.76))

    def get_high_cutoff(self):
        return self.high_cutoff

    def set_high_cutoff(self, high_cutoff):
        self.high_cutoff = high_cutoff
        self._high_cutoff_slider.set_value(self.high_cutoff)
        self._high_cutoff_text_box.set_value(self.high_cutoff)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.audio_rate, self.low_cutoff, self.high_cutoff, self.bps, firdes.WIN_BLACKMAN, 6.76))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self._freq_slider.set_value(self.freq)
        self._freq_text_box.set_value(self.freq)
        self.osmosdr_source_0.set_center_freq(self.freq, 0)

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation
        self.gr_moving_average_xx_0.set_length_and_scale(2*self.samp_rate/self.decimation, 1.0/(2*self.samp_rate/self.decimation))

    def get_bps(self):
        return self.bps

    def set_bps(self, bps):
        self.bps = bps
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.audio_rate, self.low_cutoff, self.high_cutoff, self.bps, firdes.WIN_BLACKMAN, 6.76))

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.wxgui_scopesink2_0_0.set_sample_rate(self.audio_rate)
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.audio_rate, self.low_cutoff, self.high_cutoff, self.bps, firdes.WIN_BLACKMAN, 6.76))

    def get_audio_interp(self):
        return self.audio_interp

    def set_audio_interp(self, audio_interp):
        self.audio_interp = audio_interp


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
