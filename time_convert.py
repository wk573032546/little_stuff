import time
import datetime
from pytz import timezone

def nt_to_unix(nt_timestamp):
    d1 = datetime.datetime(1970,1,1,0,0,0)
    d2 = datetime.datetime(1601,1,1,0,0,0)
    nt_second = (d1 - d2).total_seconds()
    res = nt_timestamp/10000000 - nt_second
    return res
    
def unix_to_nt(unix_timestamp):
    d1 = datetime.datetime(1970,1,1,0,0,0)
    d2 = datetime.datetime(1601,1,1,0,0,0)
    nt_second = (d1 - d2).total_seconds()
    res = (unix_timestamp + nt_second) * 10000000
    return res
    
def datetime_to_nt(Y,M,D,h,m,s,tz = 'UTC'):
    d1 = datetime.datetime(Y,M,D,h,m,s, tzinfo = timezone(tz))
    d2 = datetime.datetime(1601,1,1,0,0,0,tzinfo = datetime.timezone.utc)
    res = int((d1 - d2).total_seconds()*10000000)
    return res
    
print(nt_to_unix(132094823008986464))
print(datetime_to_nt(2019,8,5,9,42,0,tz='EST'))