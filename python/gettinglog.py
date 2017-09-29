import pexpect
import time
c = pexpect.spawn("telnet 172.17.50.254")
logname = "./log" + "test" + ".log"
wb = open(logname ,'wb')
c.logfile_read = wb

expect_list = [u"#",
                u">",
                u"\nlogin: ",
                u"Username: ",
                u"Password: ",
                u"Connection closed by foreign host.",
                u"Login incorrect"]

index = c.expect(expect_list)
c.sendline("cisco")
print index
c.sendline("enable")
c.sendline("cisco")
c.sendline("terminal length 0")
c.sendline("show run")
time.sleep(3)
c.sendline("show ip int brief")
print c.expect("2911_RT-A")
print c.buffer
