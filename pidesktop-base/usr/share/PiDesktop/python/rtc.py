#!/usr/bin/python
import os;

def runCommand(command):
    print command;
    r = os.popen(command);
    info = r.readlines();
    for line in info:
        print line;

def updateConfig():
    filename = '/boot/config.txt';
    key = 'dtoverlay';
    value = 'i2c-rtc,pcf8563'
    fr = open(filename,'rb');
    try:
        lines = fr.readlines();
        update = 0;
        newValue = '';
        for line in lines :
            if line and line.count(key) > 0:
                if not line.strip().startswith('#'):
                    sps = line.split('=',2);
                    if len(sps) == 2 and sps[1] == value:
                        update = 1;
                    elif update == 0:
                        newValue += key +'='+value+'\r\n';
                        update = 2;
            else:
                newValue += line;
        if not update == 1:
            if update == 0:
                newValue += '\r\n' + key+'='+ value;
            fw = open(filename,'wb');
            try:
                fw.write(newValue);
            finally:
                fw.close();
    finally:
        fr.close();

def removeFakeHwclock():
    command = 'sudo systemctl status fake-hwclock.service';
    r = os.popen(command);
    info = r.readlines();
    for line in info:
        if line and line.strip().startswith('Loaded:'):
            strps = line.split('fake-hwclock.service; ',2);
            if len(strps) == 2 and strps[1].strip().startswith('enabled'):
                command = 'sudo systemctl disable fake-hwclock.service';
                runCommand(command);

def updateHwcloclSet() :
    filename = '/lib/udev/hwclock-set';
    fr = open(filename,'rb');
    key = '-e /run/systemd/system';
    update = False;
    doUpdate = False;
    try:
        lines = fr.readlines();
        newValue = '';
        for line in lines :
            if line and line.strip().startswith('if') and line.count(key):
                update = True;
                doUpdate = True;
            if update :
                newValue += '#';
            if line and line.strip() == 'fi':
                update = False;
            newValue += line;
        if doUpdate :
            fw = open(filename,'wb');
            try:
                fw.write(newValue);
            finally:
                fw.close();
    finally:
        fr.close();

if __name__ == "__main__":
    updateConfig();
    updateHwcloclSet();
    removeFakeHwclock();
