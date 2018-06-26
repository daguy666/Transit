#!/usr/bin/env python

import os

from datetime import datetime
from helper import Gather_System_Info
from extras.colors import Make_Color

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
        Starts building the output for the info scan.
        """
        print "\n\n\tInformation Scan"
        print self.lines
        # Obtain the system time
        system_time = datetime.today().strftime('%Y-%m-%d--%H:%M:%S')
        # System up time
        for i in self.gsi.return_system_uptime():
            self._create_output('System Uptime', i)
        print self.lines
        # Return logged in users
        for i in self.gsi.return_logged_in_users():
            self._create_output('Logged in Users:', i)
        print self.lines
        self._create_output('System Time', system_time)
        self._create_output('Processor Info', self.gsi.return_platform_info())
        self._create_output('Hostname', self.gsi.return_hostname())
        print self.lines
        for h_dir in self.gsi.return_home_dirs_with_paths():
            self._create_output('Home Directories', h_dir)
        print self.lines
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
        # Present any screen sessions.
        print self.lines
        for screen in self.gsi.return_any_screen_sessions():
            self._create_output('Screen Session', screen)

    def main(self):
        """
        Lets start this thing up.
        """
        self.build_up_system_info()


if __name__ == '__main__':
    IS = Informational_Scan()
    IS.main()


# TODO Document what a informational scan is, and what it covers.
