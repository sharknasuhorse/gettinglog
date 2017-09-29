import pexpect
import sys
import time
import os.path
import xlrd

expect_list = [u"#",
                u">",
                u"\nlogin: ",
                u"Username: ",
                u"Password: ",
                u"Connection closed by foreign host.",
                u"Login incorrect"]

ipaddr = 172.17.50.254
hostname = 
logname


def login():
    c = pexpect.spawn("telnet 172.17.50.254")

logname = "./log" + "test" + ".log"
wb = open(logname ,'wb')
c.logfile_read = wb

def excute_command ():
def open_excel():
def save_log():





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
