import pexpect
import sys
import time

c = pexpect.spawn("telnet 172.17.50.254")

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
time.sleep(2)
print c.before
c.sendline("q")
c.close()