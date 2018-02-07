#!/usr/bin/env python

import logging

# Sets up logging
LOGGER = logging.getLogger('IR Tool Kit')
LOGGER.setLevel(logging.INFO)

# Setup file to log to
LOG2FILE = logging.FileHandler('log/incidentR.log')
LOG2FILE.setLevel(logging.INFO)

# Setup log formatter
FORMATTER = logging.Formatter('time="%(asctime)s" level="%(levelname)s" message="%(message)s"')

# Apply formatters to log file
LOG2FILE.setFormatter(FORMATTER)

# Add to logger
LOGGER.addHandler(LOG2FILE)
