pi desktop deb
===============
File Tree
---------------
![1][1]

python file 
---------------
<b>path:</b> usr/share/PiDesktop/python

- restart.py
>
shutdown shell

- rtc.py
>
1.Edit the file /boot/config.txt,changing 'dtoverlay=i2c-rtc,pcf8563'.
2.Edit the file /lib/udev/hwclock-set,commenting out some code.
3.Disable fake-hwclock.service

- pppBoot.py
>
Change boot parameters.
Edit the file /boot/cmdline.txt,changing 'root=/dev/sda2'.

- diskClone.py
>
1.Check if there is a mSATA disk.
2.call piclone 
3.call pppBoot.py 

shell file
---------------
<b>path:</b> usr/share/PiDesktop/script

- ppp-hdclone
>
call diskClone.py

- sync-hwclock
>
synchronous time

service
---------------
<b>path:</b> lib/systemd/system
Create the startup service.

- embest.service
>
call restart.py

- embest-shutdown.service
>
call sync-hwclock

Deb File
---------------
####Deb control shell
- control
>
Deb file's infomation.

- postinst
>
Run after install deb file completion.
1. Add +x to shell files.
2. Generate link script(/usr/bin) to pppBoot.py and ppp-hdclone.
3. Enable services(embest-shutdown.service and embest.service).

- postrm
> 
run before remove deb file completion.

####Make pidesktop-base.deb file,command line run:
>
dpkg -b pidesktop-base/ pidesktop-base.deb


[1]:file_tree.png