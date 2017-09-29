import pexpect

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
while True:
        if index == 0:  # success to login.
            return c
        elif index == 1:  # need to promoted to enable mode.
            c.sendline("enable")
            index = c.expect(expect_list)
        elif index == 2 or index == 3:  # need to input "root".
            c.sendline("root")
            index = c.expect(expect_list)
        elif index == 4:  # need to input password.
            c.sendline("cisco")
            index = c.expect(expect_list)
        elif index == 5:  # Connection is closed.
            print("Unmatched password, or connection is closed.")
            return -1
        elif index == 6:  # incorrect password.
            print("\nFault: incorrect password.")
            return -1
c.sendline("cisco")
c.sendline("enable")
c.sendline("cisco")
c.sendline("terminal length 0")
c.expect("2911_RT-A")
c.sendline("show run")
print c.before
