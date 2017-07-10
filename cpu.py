#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import psutil
import csv
def cpuinfo():
    men=psutil.virtual_memory()
    menab=(men.available)/(1024*1024)
    menta=(men.total)/(1024*1024)
    menus=(men.used)/(1024*1024)
    disk=psutil.disk_usage('/')
    diskta=(disk.total)/(1024*1024*1024)
    diskus=(disk.used)/(1024*1024*1024)
    diskfr=(disk.free)/(1024*1024*1024)
    time = datetime.datetime.now()
    with open('eggs.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow({"当前时间为：%s"%time})
        spamwriter.writerow({"cpu的使用率为%d%s"%(psutil.cpu_percent(interval=1),"%")})
        spamwriter.writerow({"物理内存总量为%sMB" % int(menta)})
        spamwriter.writerow({"使用的物理内存量为%sMB" % int(menus)})
        spamwriter.writerow({"空闲的物理内存为%sMB" % int(menab)})
        spamwriter.writerow({"挂载盘的总量为%sG" % int(diskta)})
        spamwriter.writerow({"挂载盘使用量为%sG" % int(diskus)})
        spamwriter.writerow({"挂载盘剩余量为%sG" % int(diskfr)})
    with open('eggs.csv', 'r') as csvfile:
          spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
          for row in spamreader:
             print(row)
cpuinfo()