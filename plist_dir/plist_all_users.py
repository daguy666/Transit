#!/usr/bin/env python

# TODO ###################################################################################
# TODO write a script that will use the .utils.helper script to list out all users...
# TODO ....then return the plists for the root location and all users.
# TODO ###################################################################################


import os

from plist_user import Return_User_Plists
from utils.helper import Gather_System_Info
from plist_root_level import Return_Root_Level_Plists




class Return_All_User_Plists(object):

    def __init__(self):
        self.gsi = Gather_System_Info()
        self.root_plist = Return_Root_Level_Plists()
        #self.user_pref = Return_User_Plists()
        self.user_list = []


    def gather_all_users(self):
        """
        This method will gather all the users on
        the system and save them to self.user_list
        """
        data = self.gsi.return_list_of_users()
        if type(data) == list:
            for i in data:
                self.user_list.append(i)
        else:
            print "[!] Error user list in wrong format"

    def _loop_over_users(self):
        """
        Loop over the user list we created in prior method.
        Verify path exists.
        """
        if self.user_list:
            for i in self.user_list:
                self.user_pref = Return_User_Plists(i)
                self.user_pref.main()

    def return_root_plists(self):
        """
        Return all the root plists
        """
        root_lists = self.root_plist.main()
        #if root_lists:
            #todo finish this method

    def main(self):
        """
        Lets do it!
        """
        self.gather_all_users()
        self._loop_over_users()
