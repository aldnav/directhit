#-------------------------------------------------------------------------------
# Name:        directhit
# Purpose:	   Retrieves system data.
#
# Author:      8bitvandal
#
# Created:     13/12/2013
# Copyright:   (c) Bonz-pc 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, sys, datetime

props = {}

def main():
    pass
    print "=== Initializing..."
    crawl()
    fileWrite()

def crawl():
	props['compname'] = os.getenv('COMPUTERNAME')
	props['path'] = "C:\\"
	props['env-vars'] = os.environ
	props['system'] = sys.platform
	props['abspath'] = os.path.split(sys.argv[0])
	props['date'] = datetime.datetime.now()
	# here
	dirList = os.listdir(props['path'])	
	for items in dirList:
		print items
	props['dirs'] = dirList
	
def displayReport():
	print "=== Details ==="
	print "    Comp. Name: ", props['compname']
	print "        System: ", props['system']
	print "   Access Path: ", props['path']	
	print "      Abs Path: ", props['abspath']
	print "    Envi. Vars: ", props['env-vars']

def fileWrite():
	fo = open(props['compname']+".dh", "w")
	for key, values in props.items():
		fo.write(key + ": " + str(values) + "\n\n")
	fo.close()


if __name__ == '__main__':
    main()
    # displayReport()
    print "=== Done."