

import time, calendar

print(time.time())

print(calendar.timegm(time.strptime('2000-01-01 12:34:00', '%Y-%m-%d %H:%M:%S')))