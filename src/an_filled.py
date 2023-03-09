
import os
import sys


# Hardcoded folder names:
CURR_DIR = os.path.dirname(__file__)
sys.path.append(CURR_DIR)
INFO_FOLDER = CURR_DIR + '/info'
LOG_FOLDER =  CURR_DIR + '/logs'
HOTELS_INFO_FILE = 'hotel_bookings.csv'
LOG_FILE = LOG_FOLDER + '/hotel_logs.txt'