
import json
import urllib2

class DashingImport:

    def __init__(self, host='localhost', port=3030, auth_token=''):
        self.host = host
        self.port = port
        self.auth_token = auth_token

    def SendEvent(self, widget, send_dict):

        # Convert the send_dict to send_json
        send_dict['auth_token'] = self.auth_token
        send_json = json.dumps(send_dict)

        # Now send the widget information
        urllib2.urlopen("http://%s:%i/widgets/%s" % ( self.host, self.port, widget ), send_json)



