import pexpect
import sys
import time
from pwn import *
#from enert import *

c = pexpect.spawn("telnet 172.17.50.254")

s = remote("172.17.50.254", 23)
#a = s.sendlineafter("Password:", "cisco")
a = s.recvuntil("Password:")
print(a)
exit()

logname = "./log" + "test" + ".log"
wb = open(logname ,'wb')
c.logfile_read = wb



#c.logfile = sys.stdout

expect_list = [u"#",
                u">",
                u"\nlogin: ",
                u"Username: ",
                u"Password: ",
                u"Connection closed by foreign host.",
                u"Login incorrect"]

c.expect("Password:")
c.sendline("cisco")
c.expect("2911_RT-A>")
c.sendline("enable")
c.expect("Password:")
c.sendline("enable")
c.sendline("cisco")
c.expect("2911_RT-A#")
c.sendline("ter len 0")
c.expect("2911_RT-A#")
c.sendline("show run")
c.expect("2911_RT-A#")
time.sleep(3)
print c.before
c.sendline("q")
c.close()
#c.expect("")
#print c.buffer
