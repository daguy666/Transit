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
        cpu = self.GSI.return_platform_info()
        hostname = self
        # TODO FINEEESH THIS.
