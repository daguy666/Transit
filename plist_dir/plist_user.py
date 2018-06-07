#!/usr/bin/env python

import os

from pprint import pprint

from utils.logger import LOGGER
from plist_two import Plist_Reader
from extras.colors import Make_Color


#TODO INCLUDE HASH OF PLIST IN OUTPUT


class Return_User_Plists(object):

    def __init__(self, user):
        self.user = user
        self.path = "/Users/%s/Library/LaunchAgents" % self.user
        self.plist_list = []
        self.lines = "==" * 40


    def show_user_plist(self):
        """
        Method to check user plists.
        """
        if os.path.exists(self.path):
            plr  = Plist_Reader(self.path)
            for i in plr.main():
                self.plist_list.append(i)
        else:
            #print "[?] Path: %s not found" % self.path
            LOGGER.error('plist_user show_user_plist path not found: %s' % self.path)

    def main(self):
        """
        Main entry for the Return_User_Plists() class.
        """
        LOGGER.info('Running plist_user for %s' % self.user)
        self.show_user_plist()
        color = Make_Color('LOCAL')
        for i in self.plist_list:
            print self.lines
            print "[%s] %s/%s" % (color.color_me_green(), self.path, i['Label'])
            print self.lines
            pprint(i)


if __name__ == '__main__':
    rup = Return_User_Plists('username to test')
    rup.main()

