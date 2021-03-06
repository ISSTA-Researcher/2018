from delorean.environments.datetime_1 import *
from delorean.clients.bii_server_2_old import *

###########################
# Wrapping Functions
###########################
def bii_2(year, month, day, hour, minute, second, tz, flag):
    if flag:
        dt = Datetime(year, month, day, hour, minute, second, tz)
    else:
        dt = Datetime(year, month, day, hour, minute, second)
    utcdt = UtcDatetime(dt, tz)
    # this is how delorean checks if two delorean objects are equal.
    return utcdt._delorean.epoch
