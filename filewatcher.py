import time

f = open(r'path/to/file')          
while 1:

    line = f.readline()
    if not line:
        time.sleep(5)
        print "Nothing New"
    else:
        print 'CHANGES MADE!'
        
