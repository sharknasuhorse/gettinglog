import telnetlib

def login ( hostname , address, password ):
    c = telnetlib.Telnet(address,timeout=3)
    print("logging")
    c.read_until(b"Password:")
    c.write(b"\n")
    c.read_until(b"Password:")
    c.write(bytes(password,'utf-8') + b"\n")
    prompt = hostname[:-3] + ">"
    c.read_until(prompt.encode('utf-8'))
    c.write(b"enable\n")
    c.read_until(b"Password:")
    c.write(bytes(password,'utf-8') + b"\n")
    print("fin login")
    __main__.c = c

def length0 (hostname):
    c = __main__.c
    prompt = hostname + "#"
    c.read_until(prompt.encode('utf-8'))
    c.write(b"ter len 0\n")    

def close_connection():
    c = __main__.c
    c.write(b"exit\n")

def cmd_showrun(hostname,command,teamnum):
    c = __main__.c
    prompt = hostname + "#"
    c.read_until(prompt.encode('utf-8'))
    command = command + "\n"
    c.write(command.encode('utf-8'))
    result = c.read_until(prompt.encode('utf-8'))
    logname = "./" + str(int(teamnum/6+1)) + "-"  + hostname + ".cfg"
    wb = open(logname ,'wb')
    wb.write(result)
    wb.close()
    c.write(b"\n")

def cmd_showtech(hostname,command):
    c = __main__.c
    prompt = hostname + "#"
    c.read_until(prompt.encode('utf-8'))
    command = command + "\n"
    c.write(command.encode('utf-8'))
    result = c.read_until(prompt.encode('utf-8'))
    logname = "./" + hostname + "-tech-support.log"
    wb = open(logname ,'wb')
    wb.write(result)
    wb.close()
    c.write(b"\n")
