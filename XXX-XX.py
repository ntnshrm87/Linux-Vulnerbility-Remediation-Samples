# Vulnerability: File Permissions (passwd, shadow and group) Are Not Properly Set
# Jira Tracking ID: XXX-XX
# Note:
# 1. The user running the script must have administrative(root) privileges.
# 2. The script is written in python2
# 3. A backup file for file permissions is created at the location '/etc/file_name.acl'
# 4. This .py script will set appropriate file permissions. 
# 5. Log file is created as /tmp/XXX-XX_VulnerabilityFix_$DATE.log

# modifying the file permissions for owner, groups, others  
# DISCLAIMER: The rollback for the following script will work for 24 hours only, post that manual rollback is required.
     
import os, datetime, sys, time
odat = (time.strftime("%d-%m-%Y"))
dat = datetime.datetime.now()

file_log = '/tmp/XXX-XX_VulnerabilityFix_' + str(odat) + '.log'
f=open(file_log,'a+')
saveout = sys.stdout
sys.stdout = f
print "***************Log Started for XXX-XX*******************"
os.system("getfacl -p /etc/group > /etc/group.acl")
os.system("getfacl -p /etc/passwd > /etc/passwd.acl")
os.system("getfacl -p /etc/shadow > /etc/shadow.acl")
print "Backup permissions files are created as '/tmp/group.acl','/tmp/passwd.acl','/tmp/shadow.acl' "
os.system("sudo chmod 644 /etc/passwd")
os.system("sudo chmod 600 /etc/shadow")
os.system("sudo chmod 644 /etc/group")

print '\n'+str(dat)+'\n'
print 'Updated access permissions:\n'
p1 = os.popen("ls -l /etc/passwd")
print p1.readline()
p2 = os.popen("ls -l /etc/shadow")
print p2.readline()
p3 = os.popen("ls -l /etc/group")
print p3.readline()
print "***************Log Ended for XXX-XX*******************"
sys.stdout = saveout
f.close()
print "Check the log file at: ", file_log
