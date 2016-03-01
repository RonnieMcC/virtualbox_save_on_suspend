#!/usr/bin/python
# -*- coding: utf-8 -*-

#Copyright (c) 2014, Aaron McCall <amccall(_at_)thepacketlounge.org>
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met:
#
#1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#The views and conclusions contained in the software and documentation are those
#of the authors and should not be interpreted as representing official policies,
#either expressed or implied, of the FreeBSD Project.

# Verify running VirtualBox VM's and save state - Used for going into hibernation with systemd.

import subprocess
import re
import sys
import time

def running_vms():
    try:
        verify_vms = subprocess.check_output(["vboxmanage", "list", "runningvms"]).decode("utf-8")
        if verify_vms:
            vm_list = re.findall("\"(.*)\"", verify_vms)
            print("Active VM's: ", vm_list)
            for i in vm_list:
                print("Saving state of: ", i) 
                subprocess.call(["vboxmanage", "controlvm", "%s" % i , "savestate"])
                time.sleep(2)
                # Add some delay and kill VirtualBox Itself (if running) - Stopping VirtualBox is required to flush mem
                subprocess.call(["kill", "VirtualBox"])
                time.sleep(2)
                sys.exit(0)
        else:
                subprocess.call(["kill", "VirtualBox"])
                time.sleep(2)
    except:
        print("save_vm exception")
        sys.exit(0)

running_vms()
