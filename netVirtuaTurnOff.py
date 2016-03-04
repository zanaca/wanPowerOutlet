#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys
import wanPowerOutlet

#  The following line is for serial port
port = '/dev/ttyUSB0'
name = 'Net Virtua Modem'


initOpts = {'credentialsKey': 'credentials.json', 'spreadsheet': 'Net Virtua Modem'}
wanPowerOutlet.init(port, initOpts)

if wanPowerOutlet.isInternetOn():
    if wanPowerOutlet.wasInternetDown():
        wanPowerOutlet.unmarkInternetDown('Offline')
        wanPowerOutlet.log('Online')

else:
    time.sleep(10)  # false positive?
    if not wanPowerOutlet.isInternetOn():
        output = wanPowerOutlet.turnPowerOff()
        print "Turning off power from %s for %s seconds" % (powerPlug, output.duration/1000)
        wanPowerOutlet.markInternetDown()
