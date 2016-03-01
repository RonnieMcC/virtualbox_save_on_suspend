# virtualbox_save_on_suspend

The script is pretty self explanatory - execute ''vboxmanage list runningvms'' to list running VM's, execute ''vboxmanage controlvm (vmname) savestate'' to, you guessed it, save the state of those running VM's. I also found I needed to kill VirtualBox as a whole to flush the memory.

I use Arch with Systemd, execute this however you can before you system suspends/sleeps/hibernates,etc.

So far it works flawlessly for my setup, let me know if you have any problems though.

Note: I do not attempt to auto restore the VM's state after resume - In most cases I do not require this and performing the VM restore manually is quick and simple.

