# Age Finder :
import datetime # to get current date and time

print('Datetime Module :')
print(datetime.datetime.today())
now =datetime.datetime.today()
other = datetime.datetime(1993,8,22,2,30) # Enter your Date-of-Birth in this format (YYYY,MM,DD,HH,Min)
print(now-other)                          # Returns in the Age in (Days:Hours:Minutes:Seconds)

# Another Example :
other = datetime.datetime(1962,12,4,12,12)
print(now-other)

# Try this to get age in years
# Age = (now-other)/365.25  # Slight gliches it has in the output is it shows (year as days)
# print(Age)