# A collection of GNU Radio Companion flows

This repo is a collection of various flow graphs I've been working on.

Some of them flat out don't work.

Some of them do and they're more documented than the others.

Some of them require special blocks for GNU Radio Companion. They will be called out when that's the case.

## SDRs I've been testing with

For RX, I've found that the trusty RTL-SDR from rtl-sdr.com is pretty nice. It's design
has been improved to help make it work better in the HF range.

For TX, I've been using the BladeRF x40 and the LimeSDR USB.

To install all the packages I need to get GNU Radio Companion, GQRX, drivers, and various other
stuff working, I've used these two links and the Ubuntu PPA's mentioned there:

* http://wiki.myriadrf.org/Packaging
* http://gqrx.dk/download/install-ubuntu

The order of the PPAs matter. Start at the top, and work your way down.

Make sure you've cleaned your machine of all traces of gnu radio, gqrx, drivers, and various
other related packages before you install from these PPAs or you'll be in for a bad time.

## Additions or Changes to this repo

If you have opinions or ideas about how any of these graphs could be improved PLEASE let me
know! I'm new at this

And let me know if you end up using any of these!


