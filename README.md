# wanPowerOutlet

It was inspired by the necessity of turning off my ISP modem for 10 seconds everytime a connection outage happened. So I built that arduino powered outlet to monitor the connection and send a report to a Google Spreadsheet logging the events of on/off connectivity.

You basicly needs:
- Arduino (I use the nano version)
- Power cord
- USB 1.0 cable
- Relay

If you have no spare time, or just like me, are lazy can you a use a photoswitch sensor instead of soldering the relay and connect the ardino to its 'photo sensor' simulating the lights on, lights out, so it triggers the current on the power outlet.

You connect the outlet to a computer USB port, and start a service on that computer to monitor the connection and manage the arduino.

If you wan to log the events to google spreadsheet you should <a href="http://gspread.readthedocs.org/en/latest/oauth2.html">obtain OAuth2 credentials from Google Developers Console</a> first and get the json credentials.
