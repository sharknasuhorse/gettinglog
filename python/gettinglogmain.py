import pexpect
import sys
import time
import __main__
import openpyxl as px

expect_list = [u"#",
                u">",
                u"\nlogin: ",
                u"Username: ",
                u"Password: ",
                u"Connection closed by foreign host.",
                u"Login incorrect"]

def login ( hostname, address):
    c = pexpect.spawn("telnet " + address)
    c.expect("Password:")
    c.sendline("cisco")
    c.expect( hostname + ">")
    c.sendline("enable")
    c.expect("Password:")
    c.sendline("enable")
    c.sendline("cisco")
    __main__.c = c

def length0 ():
    c = __main__.c
    c.expect("2911_RT-A#")
    c.sendline("ter len 0")

def excute_command(hostname ,command):
    c = __main__.c
    c.expect( hostname + "#")
    c.sendline(command)
    c.expect(hostname +"#")
    time.sleep(3)
    logname = "./" + hostname + ".cfg"
    wb = open(logname ,'wb')
    wb.write(c.before)

def close_settion():
    c = __main__.c
    c.sendline("q")
    c.close()

def get_excel_hostaddr():
    wb = px.load_workbook('testbook.xlsx')
    ws = wb.active
    i = 1
    dct = {}
    while ws['A' + str(i)].value != None :
        dct[ws['A' + str(i)].value] = ws['B' + str(i)].value
        i+=1
    __main__.dct = dct


get_excel_hostaddr()
key_lst = list(dct.keys())
#### rupe
login(key_lst[0],dct[key_lst[0]])
length0()
excute_command( (key_lst[0]),"show run")
close_settion()
#####
exit()

#logname = "./log" + "test" + ".log"
#wb = open(logname ,'wb')
#c.logfile_read = wb





