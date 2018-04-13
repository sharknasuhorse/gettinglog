import time
import __main__
import openpyxl as px
import csv
import cisco_cmd

def get_hostaddr():
    with open('testhosts.csv', 'r') as hosts_csv:
        hostlist = list(csv.reader(hosts_csv))
        return hostlist

if __name__ == '__main__':
    hostlist = get_hostaddr()
    for x in hostlist:
        for y in x:
            print(x)

    while True :
        try:
            print()
            cisco_cmd.login()
        except:
            print("ログイン出来ませんでした")
            continue
        cisco_cmd.length0()
        cisco_cmd.cmd_showrun( )
        cisco_cmd.close_connection()
        print("next whsssile")
    exit()
