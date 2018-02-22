#!/usr/bin/env python

import os

from datetime import datetime
from helper import Gather_System_Info


class System_Information_Scan(object):
    
    def __init__(self):
        self.temp_list = []
        self.GSI = Gather_System_Info()
        self.lines = "--" * 35

    def aquire_system_info(self):
        """
        Gather information about the system, similar to info_scan.
        """
        # system time at start of scan
        system_time = datetime.today().strftime('%Y-%m-%d--%H:%M:%S')
        print self.lines
        print "Current System Time: %s" % system_time
        print self.lines
        print "[+] CPU: %s" % self.GSI.return_platform_info()
        print "[+] Hostname: %s" % self.GSI.return_hostname()
        print "[+] OS Version: %s " % self.GSI.return_os_version()
        print "[+] OS Build: %s" % self.GSI.return_os_build()
        print "[+] OS Name: %s" % self.GSI.return_os_version_name().capitalize()
        print self.lines
        print "[+] Disk space: "
        for mount in self.GSI.return_diskspace():
            print "\t[+] %s" % mount

        # TODO FINEEESH THIS.
    
    def main(self):
        """
        Start it up!
        """
        self.aquire_system_info()

