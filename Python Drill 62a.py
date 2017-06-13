import time;
from datetime import datetime, timedelta
from pytz import timezone
import pytz
utc = pytz.utc
utc.zone
'UTC'
eastern = timezone('US/Eastern')
fmt = '%H:%M:%S'
utc_dt = datetime(2017,06,11,tzinfo=utc)
loc_dt = utc_dt.astimezone(eastern)
loc_dt.strftime(fmt)

europe = timezone('Europe/London')
fmt = '%H:%M:%S'
utc_dt = datetime(2017,06,11,tzinfo=utc)
loc_dt = utc_dt.astimezone(europe)
loc_dt.strftime(fmt)


##Local time in Portland,OR
def checkOpen(branch):
   if ("09:00:00") < branch.strftime("%H:%M:%S")and branch.strftime("%H:%M:%S") < ("21:00:00"):
      print ("Open")
   else:
      print ("Closed")


localTime = datetime.now()
print "West Coast Local Time"
print localTime
checkOpen(localTime)

##Local time in New York,NY
easternTime = datetime.now(timezone('US/Eastern'))
print "\nEast Coast Time"
print easternTime
checkOpen(easternTime)


##Local time in London, England
europeTime = datetime.now(timezone('Europe/London'))
print "\nLondon Time"
print europeTime
checkOpen(europeTime)

