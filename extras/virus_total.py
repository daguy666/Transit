#!/usr/bin/env python

import sys
import json
import urllib
import urllib2

from utils.logger import LOGGER


class Send_MD5_to_VirusTotal(object):

    def __init__(self):
        self.report_md5 = "https://www.virustotal.com/vtapi/v2/file/report"
        self.api_key = ""  # put this in a config

    def virus_total_md5(self, vt_md5):
        """Sets up a Virus Total MD5 scan
        """
        parameters = {'resource': vt_md5,
                      'apikey': self.api_key}
        # Start packing together the call.
        data = urllib.urlencode(parameters)
        request = urllib2.Request(self.report_md5, data)
        response = urllib2.urlopen(request)
        output = response.read()
        my_json = json.loads(output)

        try:
            if "positives" in my_json:
                LOGGER.info("[>] Found %s times." % my_json['positives'])
                if "scans" in my_json:
                    items = my_json['scans'].items()
                    if my_json['positives'] == 0:
                        LOGGER.info("[>] Found 0 times.")
                        sys.exit(1)

                    for a_key in items:
                        # Interesting keys, detected, result, update, version
                        if a_key[1]['detected']:
                            detected = "[>] Detected: %s =>" % a_key[1]['detected']
                            result = "Result: %s => " % a_key[1]['result']
                            update = "Update: %s => " % a_key[1]['update']
                            version = "Version: %s" % a_key[1]['version']
                            output = " ".join([detected, result, update, version])
                            LOGGER.info(output)
            else:
                LOGGER.info("[>] Nothing found for that MD5.")
        except ValueError:
            LOGGER.info("ok")

    def main(self, vt_md5):
        self.virus_total_md5(vt_md5)
