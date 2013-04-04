
#!/usr/bin/python

import sys, getopt

# -------------------------------------
# Testing the ARGs passed into script
# -------------------------------------

argv = sys.argv[1:]
inputfile = ''
outputfile = ''
try:
   opts, args = getopt.getopt(argv,"hp:c:",["path=","cname="])
except getopt.GetoptError:
   print 'ERROR: use -h for proper usage'
   sys.exit(2)
for opt, arg in opts:
   if opt == '-h':
      print '<Usage>: challenge3.py -p <path> -c <container name>'
      sys.exit()
   elif opt in ("-p", "--path"):
      path = arg
   elif opt in ("-c", "--cname"):
      cname = arg

if len(argv) in range(3):
   print 'ERRO: use -h for proper usage'
   sys.exit(2)
else:
   print 'path >', path
   print 'container name >', cname
