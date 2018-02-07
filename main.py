#!/usr/bin/env python


# menu file for IR program

from pprint import pprint

from utils.logger import LOGGER
from utils.helper import Gather_System_Info
from utils.info_scan import Informational_Scan
from plist_dir.plist_user import Return_User_Plists
from plist_dir.plist_root_level import Return_Root_Level_Plists


LOGGER.info('Running menu.py')

try:

    lines = "==" * 35

    print lines
    print "\t\tWelcome to Transit ...\n"  # ascii4rt this up later
    print "\tPick one of the following menu items to begin: "
    print lines


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

    if user_input.isdigit():
        if user_input == "1":
            LOGGER.info('Option 1 chosen full info scan')
            IS = Informational_Scan()
            IS.main()

        elif user_input == "2":
            LOGGER.info('Option 2 chosen - But is not ready yet')
            print not_yet

        elif user_input == "3":
            # Returns user level launchA
            username = raw_input('Please enter a username to search: ').lower()
            if username.isalnum():
                LOGGER.info('Option 3 chosen gather plist for user %s ' % username)
                gsi = Gather_System_Info()
                # Checks that the user account has a home directory listed
                if username in gsi.return_home_dirs():
                    plr = Return_User_Plists(username)
                    # PPrints for readability
                    pprint(plr.main())
                else:
                    print "[!] Username not found on system"
                    LOGGER.error('Choice 3 but username: %s not found on system' % username)
            else:
                print "[!] Error problem with username: %s " % username
                LOGGER.error('Choice 3 - Problem with username: %s' % username)


        elif user_input == "4":
            # Returns the root level plists for launchA / launchD
            rrlp = Return_Root_Level_Plists()
            rrlp.main()

        elif user_input == "5":
            # Returns the tar of the log directories
            gsi = Gather_System_Info()
            print "[+] Taring up the root logging directory ..."
            gsi.tar_log_directory()
            print "[+] Completed. \n"
        
        elif user_input == "6":
        # There is no option 6 as of yet.
            print "[!] There is no spoon." 
            LOGGER.info('Option 6 chose, but no content yet.')
    else:
        print "\n[!] Invalid input: %s" % user_input


except KeyboardInterrupt:
        print "\n[-] Program exited.\n"


#TODO call out the classes better here. At the moment its sloppy and per a code block.

