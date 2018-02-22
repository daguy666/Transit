#!/usr/bin/env python

import os

from datetime import datetime
from helper import Gather_System_Info


class Informational_Scan(object):

    def __init__(self):
        self.temp_list = []
        self.gsi = Gather_System_Info()
        self.lines = "--" * 35

    def build_up_system_info(self):
        """
        Starts building up some system info
        """
        # Print put system time
        system_time = datetime.today().strftime('%Y-%m-%d--%H:%M:%S')
        print self.lines
        print "[+] System Time: %s" % system_time
        # Print some info about the processor
        print "[+] Processor info: %s " % self.gsi.return_platform_info()
        # Print out the computer hostname
        print "[+] Hostname: %s" % self.gsi.return_hostname()
        # Print out home directories
        print "[+] Home Directories Present: "
        for i in self.gsi.return_home_dirs():
            print "\t[-]%s" % i
        print self.lines
        # Print OS Version
        print "[+] OS Version: %s " % self.gsi.return_os_version()
        # Print OS Build
        print "[+] OS Build: %s " % self.gsi.return_os_build()
        # Print OS Name
        print "[+] OS Name: %s" % self.gsi.return_os_version_name().capitalize()
        # Print shutdown and reboot status. 
        print self.lines
        print "[+] Shutdown history: "
        for i in self.gsi.show_last_shutdown():
            print "\t[-] %s" % i
        print self.lines
        print "[+] Reboot history: "
        for i in self.gsi.show_last_reboot():
            print "\t[-] %s " % i
        print self.lines
        # Print out wireless networks
        for wifi in self.gsi.return_wireless_networks():
            print "[+] %s" % wifi.strip()




    def main(self):
        self.build_up_system_info()


if __name__ == '__main__':
    IS = Informational_Scan()
    IS.main()


# TODO Document what a informational scan is, and what it covers.
