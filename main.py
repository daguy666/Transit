#!/usr/bin/env python


# menu file for IR program

from pprint import pprint

from utils.logger import LOGGER
from extras.colors import Make_Color
from utils.helper import Gather_System_Info
from utils.info_scan import Informational_Scan
from plist_dir.plist_user import Return_User_Plists
from utils.system_scan import System_Information_Scan
from plist_dir.plist_all_users import Return_All_User_Plists
from plist_dir.plist_root_level import Return_Root_Level_Plists

# log that were running the program
LOGGER.info('Running menu.py')

transit = """
======================================================================

         ___________________________. .___________________________.
     .--/____|______________________| |___|||||___|_|____|_|___ --|
     |    |-|                    | |=| |          |_|    |-|      |
     |  __|-|____________________|_|=|_|__________|_|____|-|__.   |
     |_/<_>=<_>\_________/<_>=<_>\_|=|_|<_>=<_>|_____|<_>=<_>|____|
=====================================================================
"""


# TODO Get a better work flow for this.
# TODO Maybe use something like ...
"""
data = Make_Color('')
data.inbound = "something to color"
print data.color_me_red()
"""

blue = Make_Color(transit)
red = Make_Color('\t\tWelcome to Transit\n')

try:

    lines = "==" * 35

    print lines
    print red.color_me_red()  # ascii4rt this up later
    print "\t\tIncident Response Toolkit."
    print "\tPick one of the following menu items to begin: "
    print lines
    print blue.color_me_blue()


    menu_item_one = "Run a full informational scan: " # do everything (whatever that is)
    # Maybe make plists a tree'd option
    menu_item_two = "Gather preference lists for all users: "
    menu_item_three = "Gather preference lists for one user: "  # ask for user later
    menu_item_four = "Gather all Root level preference lists: (May require root)"
    menu_item_five = "Tar up log directories: "  # provide the logging directories run path exists to confirm
    menu_item_six = "Gather system information: "  # os version, os name, patch level, users, wifi, ..etc

    # validate all input. duh.
    # come up with some more items.

    user_input = raw_input( """
    1. %s
    2. %s
    3. %s
    4. %s
    5. %s
    6. %s
    \n
    >> """ % (menu_item_one,
              menu_item_two,
              menu_item_three,
              menu_item_four,
              menu_item_five,
              menu_item_six))

    not_yet = "[+] Feature not available yet."

    ### == ### Instantiate our classes ### == ###
    IS   = Informational_Scan()
    GSI  = Gather_System_Info()
    #PLR  = Return_User_Plists(username)  # Needs username
    PLAU = Return_All_User_Plists()
    RRLP = Return_Root_Level_Plists()
    SIS = System_Information_Scan()
    #############################################


    if user_input.isdigit():
        if user_input == "1":
            LOGGER.info('Option 1 chosen full info scan')
            # Informational_Scan()
            IS.main()

        elif user_input == "2":
            LOGGER.info('Option 2 chosen - Experimental Mode')
            PLAU.main()

        elif user_input == "3":
            # Returns user level launchA
            username = raw_input('Please enter a username to search: ').lower()
            if username.isalnum():
                LOGGER.info('Option 3 chosen gather plist for user %s ' % username)
                # GSI()
                # Checks that the user account has a home directory listed
                if username in GSI.return_home_dirs():
                    print "username"
                    PLR = Return_User_Plists(username)
                    # TODO adjust the code to take the username in the main PLR.Return_User_Plists()
                    # PPrints for readability
                    PLR.main()
                else:
                    print "[!] Username not found on system"
                    LOGGER.error('Choice 3 but username: %s not found on system' % username)
            else:
                print "[!] Error problem with username: %s " % username
                LOGGER.error('Choice 3 - Problem with username: %s' % username)


        elif user_input == "4":
            # Returns the root level plists for launchA / launchD
            #Return_Root_Level_Plists()
            RRLP.main()

        elif user_input == "5":
            # Returns the tar of the log directories
            #Gather_System_Info()
            print "[+] Taring up the root logging directory ..."
            GSI.tar_log_directory()
            print "[+] Completed. \n"
        
        elif user_input == "6":
        # There is no option 6 as of yet.
            LOGGER.info('Option 6 chose, but no content yet.')
            SIS.main()

        elif user_input == "7":
            # For prototyping only
            #LOGGER.info('Running a prototype scan')
            #users = GSI.return_list_of_users()
            #for i in users:
            #    print GSI.return_crons(i)
            from proto.temp import proto_test
            proto_test()


    else:
        print "\n[!] Invalid input: %s" % user_input


except KeyboardInterrupt:
        print "\n[-] Program exited.\n"


#TODO call out the classes better here. At the moment its sloppy and per a code block.

