#!/usr/bin/python
import os;

class Manager:
    def updateBoot(self):
        filename = '/boot/cmdline.txt';
        fr = open(filename,'rb');
        key = 'root=';
        value = "root=/dev/sda2";
        try:
            lines = fr.readlines();
            newValue = '';
            update = False;
            for line in lines :
                if line :
                    strps = line.split(" ");
                    for v in strps :
                        if v.startswith(key) and v != value:
                            newValue += value + ' ';
                            update = True;
                        else:
                            newValue += v + ' ';
            
            if update :
                fw = open(filename,'wb');
                try:
                    fw.write(newValue.strip());
                finally:
                    fw.close();
            self.reboot();
        finally:
            fr.close();

    def runask(self):
        ask = "Do you want to change the file system from SD card to SSD?\nIf 'YES',please make sure the 'SD Card Copier' execute correctly.(y/N): "
        answer = raw_input(ask);
        if answer == 'Y' or answer == 'y' or answer == 'yes' or answer == 'YES':
            self.updateBoot();

    def reboot(self):
        ask = "To put the new configuration into effect, you need to restart the system.\nDo you want to reboot now? (Y/n): ";
        answer = raw_input(ask);
        if answer == 'N' or answer == 'n' or answer == 'no' or answer == 'NO':
            print "You don't want to restart now.";
        else:
            os.popen("sudo reboot");

if __name__ == "__main__":
    m = Manager();
    m.runask();
