#!/usr/bin/env python

import os

from pprint import pprint
from plist_two import Plist_Reader

#TODO INCLUDE HASH OF PLIST IN OUTPUT

# Returns a the output of the root level
# LaunchAgents and LaunchDaemons

class Return_Root_Level_Plists(object):

    def __init__(self):
        self.path_one = "/Library/LaunchAgents"
        self.path_two = "/Library/LaunchDaemons"

    def show_root_plist(self, path):
        """
        Returns plists for each of the root level
        locations.
        """
        try:
            if os.path.exists(path):
                plr = Plist_Reader(path)
                for i in plr.main():
                    print "==" * 40
                    print "%s/%s" % (path, i['Label'])
                    print "==" * 40
                    print ""
                    pprint(i)
            else:
                print "[?] Path not found or something went wrong."
        except IOError, err:
            if err.errno == 13:
                print "\n[!] Permission denied when accessing %s" % err.filename
                print "[?] Maybe run as root next time."
            else:
                print "[!] Error: %s" % err


    def main(self):
        self.show_root_plist(self.path_one)
        self.show_root_plist(self.path_two)

if __name__ == '__main__':
    rrlp = Return_Root_Level_Plists()
    rrlp.main()