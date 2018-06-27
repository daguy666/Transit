#!/usr/bin/env python

import os

from datetime import datetime
from helper import Gather_System_Info


class System_Information_Scan(object):
    
    def __init__(self):
        self.temp_list = []
        self.GSI = Gather_System_Info()
        self.lines = "--" * 35

    def _create_output(self, key, value):
        """
        Internal method to clean up the random print statments.
        """
        print "[+] %s %s" % (key, value)

    def aquire_system_info(self):
        """
        Gather information about the system, siilar to info scan."
        """
        print "\n\n\tSystem Informational Scan" 
        print self.lines
        system_time = datetime.today().strftime('%Y-%m-%d--%H:%M:%S')
        self._create_output('Current System Type:', system_time)
        self._create_output('CPU:', self.GSI.return_platform_info())
        self._create_output('Hostname:', self.GSI.return_hostname())
        print self.lines
        self._create_output('OS Version:', self.GSI.return_os_version())
        self._create_output('OS Build:', self.GSI.return_os_build())
        self._create_output('OS Name:', self.GSI.return_os_version_name().capitalize())
        print self.lines
        for mount in self.GSI.return_diskspace():
            self._create_output('Disk Space:', mount)
        print self.lines
        self._create_output(self.GSI.return_system_memory(), '')
        self._create_output(self.GSI.return_uuid(), '')
        self._create_output(self.GSI.return_macos_serial_number(), '')
        print self.lines
        for i in self.GSI.return_processor_speed():
            self._create_output(i.strip(), '')
        print self.lines
        for i in self.GSI.return_other_very_random_info():
            print i
        print self.lines
        # TODO FINEEESH THIS.
    
    def main(self):
        """
        Start it up!
        """
        self.aquire_system_info()

