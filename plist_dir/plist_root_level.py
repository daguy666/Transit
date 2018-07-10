#!/usr/bin/env python

import os

from pprint import pprint

from plist import Get_Plist_Info
from plist_two import Plist_Reader
from extras.colors import Make_Color


#TODO INCLUDE HASH OF PLIST IN OUTPUT

# Returns a the output of the root level
# LaunchAgents and LaunchDaemons

class Return_Root_Level_Plists(object):

    def __init__(self):
        self.path_one = "/Library/LaunchAgents"
        self.path_two = "/Library/LaunchDaemons"
        self.GPI = Get_Plist_Info()

    def show_root_plist(self, path):
        """
        Returns plists for each of the root level
        locations.
        """
        color = Make_Color('ROOT')
        try:
            if os.path.exists(path):
                plr = Plist_Reader(path)
                for i in plr.main():
                    hash = self.GPI.get_md5('%s/%s.plist' % (path, i['Label']))
                    print "==" * 40
                    print "[%s] %s/%s \n[HASH]: %s" % (color.color_me_red(),
                                             path, i['Label'],
                                             hash)
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