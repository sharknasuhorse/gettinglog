import sys
import time
import __main__
import openpyxl as px
import csv

def get_hostaddr():
    with open('testhosts.csv', 'r') as hosts_csv:
        hostlist = list(csv.reader(hosts_csv))
        return hostlist



if __name__ == '__main__':
    hostlist = get_hostaddr()

    while True :
        try:
            print(key_lst[j][:-3])
            login( key_lst[j], dct[key_lst[j]],passlist[j % 6] )
        except:
            print(dct[key_lst[j]])
            continue
        print("len0")
        length0(key_lst[j][:-3])
        exe_showrun_cmd( (key_lst[j][:-3]),"show run",j)
        close_connection()
        j += 1
        print("next while")
    exit()

