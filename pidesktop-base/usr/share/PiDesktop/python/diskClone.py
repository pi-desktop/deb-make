#!/usr/bin/python
import os;
#from pppBoot import Manager;

def runCommand(command):
    print command;
    r = os.popen(command);
    info = r.readlines();
    for line in info:
        print line;

def newPartition(sd):
    command = 'echo -e "o\nn\np\n1\n\n\nw\n" | sudo fdisk ' + sd;
    os.popen(command);

def chekSD():
    command = 'ls -la /dev/sd*';
    r = os.popen(command);
    info = r.readlines();
    if len(info) > 0:
        sd = '';
        num = 0;
        for line in info :
            if line.startswith("ls:") :
                print 'Please insert mSATA disk.';
                return;
            if line.strip()[-1].isdigit():
                num += 1;
            else:
                sd = line.strip('\r\n');
#        if num == 0:
#            newPartition(sd);
        diskClone();
    else:
        print 'Please insert mSATA disk.';
 
def diskClone():
    message = "Calling the 'SD Card copier' to clone the filesystem from SD Card to SSD...";
    print message;
    command = 'piclone';
    runCommand(command);
#    m = Manager();
#    m.runask();

if __name__ == "__main__":
    chekSD();
