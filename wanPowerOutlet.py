import serial
import os
import urllib2
import json
import datetime
import gspread
import time
import logging
from oauth2client.client import SignedJwtAssertionCredentials


# The following line is for serial port
defaultPort = '/dev/ttyUSB0'

arduino = None
worksheet = None


def init(port=None, opts=None):
    global worksheet
    if not port:
        port = defaultPort
    arduino = serial.Serial(port, 9600, timeout=5)
    time.sleep(2)  # wait for arduino
    if opts and 'credentialsKey' in opts and 'spreadsheet' in opts:
        json_key = json.load(open(opts['credentialsKey']))
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
        gc = gspread.authorize(credentials)

        try:
            worksheet = gc.open(opts['spreadsheet']).sheet1
        except:
            raise 'ERROR: Spreadsheet %s not found' % opts['spreadsheet']

    return arduino


def isInitiated():
    return not arduino


def isInternetOn():
    try:
        urllib2.urlopen('http://www.google.com', timeout=1)
        return True
    except urllib2.URLError:
        pass
    return False


def isInternetDown():
    return not isInternetOn()


def wasInternetDown():
    return os.path.isfile('.down')


def unmarkInternetDown(msg=None):
    stat = os.stat('.down')
    log(msg, stat.ST_CTIME)
    os.remove('.down')


def markInternetDown():
    if not os.path.isfile('.down'):
        open('.down', 'w').write('')


def turnPowerOff(ttl=10):
    if not arduino:
        print 'arduino not found'
        sys.exit(1)
    arduino.write('0')
    return json.loads(arduino.readline())


def turnPowerOn(ttl=10):
    if not arduino:
        print 'arduino not found'
        sys.exit(1)
    arduino.write('1')
    return json.loads(arduino.readline())


def log(message=None, date=None):
    global worksheet
    if not message:
        return
    if not date:
        now = datetime.datetime.now().isoformat()
    else:
        now = datetime.datetime.fromtimestamp(date).isoformat()
    if worksheet:
        worksheet.append_row([now, message])
    else:
        print '%s %s' % (now, message)
        logging.info('%s %s' % (now, message))
