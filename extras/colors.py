#!/usr/bin/env python

from termcolor import colored


class Make_Color(object):
    """
    Let's add a splash of color.
    Using the termcolor lib
    """

    def __init__(self, inbound):
        self.inbound = inbound

    def color_me_red(self):
        """
        Change output to RED
        """
        if self.inbound:
            return colored(self.inbound, 'red')

    def color_me_green(self):
        """
        Change output to GREEN
        """
        if self.inbound:
            return colored(self.inbound, 'green')

    def color_me_blue(self):
        """
        Change output to BLUE
        """
        if self.inbound:
            return colored(self.inbound, 'blue')



"""
#####USAGE##############################

from extras.color import Make_Color

color = Make_Color('Text to change color')

color.color_me_red()

#####USAGE##############################
"""