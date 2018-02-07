#!/usr/bin/env python

# quick and dirty plist reader

import os
import sys
try:
    import biplist
except ImportError:
    print "[?] Is biplist library installed?"

from utils.helper import Gather_System_Info


class Plist_Reader(object):

    def __init__(self, directory):
        # User provided directory
        self.directory = directory
        # Call out helper.Gather_System_Info()
        self.gsi = Gather_System_Info()
        # Save the plist data to this list
        self.plist_list = []

    def read_plist(self, item):
        """
        Read the plist convert to json, save the output to a list
        """
        try:
            self.plist_list.append(biplist.readPlist(item))

        except biplist.InvalidPlistException:
            return "[!] Unable to return plist"

    def return_directory_contents(self):
        """
        Return directory contents
        """
        if os.path.isdir(self.directory):
            os.chdir(self.directory)
            for i in os.listdir('.'):
                self.read_plist(i)

    def main(self):
        """
        Main entry for this class
        """
        self.return_directory_contents()
        if len(self.plist_list) < 1:
            print "[!] No plists to read."
            sys.exit(1)
        return self.plist_list


if __name__ == '__main__':
    user = "username to test"
    path = "/Users/%s/Library/LaunchAgents" % user
    plr = Plist_Reader(path)
    print plr.main()
