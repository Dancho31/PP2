#1
import datetime

current_date = datetime.datetime.now()
five_days_ago = current_date - datetime.timedelta(days=5)

print("Current Date:", current_date)
print("Five Days Ago:", five_days_ago)

#2
import datetime

today = datetime.datetime.now()

yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Yesterday:", yesterday.date())
print("Today:", today.date())
print("Tomorrow:", tomorrow.date())

#3
import datetime

now = datetime.datetime.now()
without_microseconds = now.replace(microsecond=0)

print("Original:", now)
print("Without Microseconds:", without_microseconds)
 
#4
import datetime

date1 = datetime.datetime(2025, 2, 20, 12, 0, 0)
date2 = datetime.datetime(2025, 2, 25, 15, 30, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print("Difference in seconds:", seconds)

