''' a python 2.7 program that when given a directory tree compares all files under it for modified date
and then outputs newer files than given date to a text file'''

import os, time
NewerFiles = []
#in python call timecheck by doing:
#import NewerThan
#NewerThan.TimeCheck()
def TimeCheck():
    """goes through directory tree, compares modified date for all files newer than user input"""
    Year = int(input('Enter the 4 digit year of the date you want to use: '))
    Month = int(input('Enter the 2 digit month of the date you want to use:'))
    Day = int(input('Enter the 2 digit day of the date you want to use:'))
    Hour = int(input('Enter the 2 digit, 24 hour format hour that you want to use:'))
    Minute = int(input('Enter the 2 digit minute you want to use:'))
    Seconds = 0
    RootDir = raw_input('fully qualified path to search recursively using / instead of \.')
    #CutDate uses Year, Month, Day, 24 Hour, Min, Sec, 3,1,0 format
    #CutDate is the date you want to find anything newer than
    CutDate = (Year,Month,Day,Hour,Minute,Seconds,3,1,0)
    CutTime = time.mktime(CutDate)
    print CutDate
    print CutTime
    try:
       for path, dirs, files in os.walk(unicode(RootDir)):
           #print RootDir
           #This section goes through the given directory, and all subdirectories/files below
           #as part of a loop and checks dates
           for filename in files:
               #print filename
               #Steps through each fine and compares dates to give
               FullName = unicode(os.path.join(path, filename))
               print FullName
                   #does the actual compare
                   ModTime=os.path.getmtime(FullName)
                   print ModTime
                   if CutTime < ModTime:
                       #print ('Works')
                       output = open('ChangedAfter.txt','a')
                       output.write(str(FullName))
                       output.write("\n")
                       output.close
    except IOError, e:
        print e
    if __name__ == "__main__":
        import sys
