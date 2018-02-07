#!/usr/bin/env python

import os
import pprint
import hashlib
import biplist
import plistlib

from extras.virus_total import Send_MD5_to_VirusTotal
from utils.logger import LOGGER

# If you wish to enable virus total lookups change the value of
# self.virus_total to True in the Get_Plist_Info() class.

# get the details of all the plists on the system


class Get_Plist_Info(object):

        def __init__(self):
            # Root launch*
            self.root_agents  = "/Library/LaunchAgents/"
            self.root_daemons = "/Library/LaunchDaemons/"
            # User launchAgents
            self.home_agents  = "/Users/%s/Library/LaunchAgents"
            self.system_startup_items = "/System/Library/StartupItems"
            self.root_startup_items = "/Library/StartupItems"
            self.some_lines = "====" * 20
            # Some lists to save data
            self.exists = []
            self.does_not_exist = []
            self.dir_contents = []
            # Instantiate the virustotal class.
            self.check_md5 = Send_MD5_to_VirusTotal()
            # To call the virustotal class or not.
            self.virus_total = False

        def get_md5(self, file_to_check):
            """
            Returns a md5 value of a file
            """
            if os.path.exists(file_to_check):
                return hashlib.md5(open(file_to_check, 'rb').read()).hexdigest()

        def check_existence(self, directory):
            """
            This will check to ensure that the path does indeed exist.
            """
            if os.path.exists(directory):
                os.chdir(directory)
                LOGGER.info(self.some_lines)
                LOGGER.info("\t%s" % os.getcwd())
                LOGGER.info(self.some_lines)
                LOGGER.info("")
                for i in os.listdir('.'):
                    LOGGER.info(self.some_lines)
                    LOGGER.info("[+] File: %s" % i)
                    if '.plist' in i:
                        LOGGER.info("[+] MD5: %s " % self.get_md5(i))
                        # Checks VirusTotal for the md5
                        if self.virus_total:
                            self.check_md5.main(i)

                        LOGGER.info(self.some_lines)
                        LOGGER.info("")
                        LOGGER.info(pprint.pformat(biplist.readPlist("%s" % i)))
                        LOGGER.info("")

        def list_dir_contents(self, path):
            """
            Lists the content of a directory
            """
            content_list = []
            if os.path.exists(path):
                for i in os.listdir(path):
                    content_list.append(i)
                return content_list

        def get_local_agents(self):
            """
            Lists the contents of all the launchAgents per home directory
            """
            for user in self.list_dir_contents('/Users/'):
                self.check_existence(self.home_agents % user)

        def main(self):
            #self.get_local_agents()
            #self.check_existence(self.root_agents)
            #self.check_existence(self.root_daemons)
            # figure out a better way to actually list the items in the directories. Walk the file structure.
            self.check_existence(self.root_startup_items)
            self.check_existence(self.system_startup_items)


if __name__ == '__main__':
    if os.getuid() != 0:
        LOGGER.info("[!] Run as root")
    else:
        gpi = Get_Plist_Info()
        gpi.main()




