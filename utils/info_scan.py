#!/usr/bin/env python

import os

from datetime import datetime
from helper import Gather_System_Info


class Informational_Scan(object):

    def __init__(self):
        self.temp_list = []
        self.gsi = Gather_System_Info()
        self.lines = "--" * 35

    def _create_output(self, key, value):
        """
        Internal method to clean up the random print statments.
        """
        print "[+] %s: %s" % (key, value)

    def build_up_system_info(self):
        """
        Starts buidling the output for the info scan.
        """
        print "\n\n\tInformation Scan"
        print self.lines
        # Obtain the system time
        system_time = datetime.today().strftime('%Y-%m-%d--%H:%M:%S')
        self._create_output('System Time', system_time)
        self._create_output('Processor Info', self.gsi.return_platform_info())
        self._create_output('Hostname', self.gsi.return_hostname())
        for h_dir in self.gsi.return_home_dirs():
            self._create_output('Home Directories', h_dir)
        self._create_output('OS Version', self.gsi.return_os_version())
        self._create_output('OS Build', self.gsi.return_os_build())
        self._create_output('OS Name', self.gsi.return_os_version_name().capitalize())
        print self.lines
        for shutdown in self.gsi.show_last_shutdown():
            self._create_output('Shutdown History', shutdown)
        print self.lines
        for restart in self.gsi.show_last_reboot():
            self._create_output('Reboot History', restart)
        print self.lines
        for wifi in self.gsi.return_wireless_networks():
            self._create_output('Wireless', wifi)
        print self.lines
        for open_file in self.gsi.return_open_with_internet():
            self._create_output('Open Files with Internet', open_file)
        print self.lines
        # For loop over the gsi.return_list_of_users()
        # and then use that to run gsi.return_crons()
        for user in self.gsi.return_list_of_users():
            self.gsi.return_cron_tab(user)
       
       #================================================   
       #TODO finish the cron output
       #TODO check on the return open with internet
       #================================================

    def ___build_up_system_info(self):
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
        print self.lines
        for open_files_i in self.gsi.return_open_with_internet():
            print "[+] %s" % open_files_i
        print self.lines
        for open_files in self.gsi.return_open_files():
            print "[+] %s" % open_files

        print self.lines
        for i in self.gsi.return_list_of_users():
            if len(self.gsi.return_crons(i)) > 1:
                print self.gsi.return_crons(i)


    def main(self):
        self.build_up_system_info()


if __name__ == '__main__':
    IS = Informational_Scan()
    IS.main()


# TODO Document what a informational scan is, and what it covers.
