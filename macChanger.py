#==================+ SCRIPT BY LABARAN + =====================================================================
# ==================+ CONTACT : https://twitter.com/labaran_1  + ===============================================================
#====================+GITHUB : https://github.com/labaran1 + ================================================
# ===================+WebSite: www.labaran.me + ====================================================
#==================== + Blog : www.labaran.me/blog + =============================================

#!/usr/bin/env python3

import sys
import os
import subprocess
import optparse



# initialize object parser
parser = optparse.OptionParser()


# check root priveleges 
if (os.geteuid() != 0 ):
    print('[+++++++] Script must be run as root [+++++++]')
    sys.exit(1)

# get all interface 
interface = []

for i in os.listdir('/sys/class/net'):
    interface.append(i)
    


# print(interface)
# options
parser.add_option('-i','--interface', dest='interface' ,help='interface to change it macc address')
parser.add_option('-m','--mac', dest='mac' ,help='mac address to set interface XX:XX:XX:XX:XX:XX')


# parser.parse_args()
(options, argument) = parser.parse_args()


#get argument pass from the terminal 
setInterface = options.interface
newMac = options.mac


# check if the interface pass is  a valid interface 
found = False
for i in interface:
    if(i == setInterface):
        found= True

def changeMac(interface , macc ):
    if(found == True):
        # print(macc)
        subprocess.call(f'ifconfig  {interface}  down', shell=True)
        subprocess.call(f'ifconfig {interface} hw ether {macc}', shell=True)
        subprocess.call(f'ifconfig {interface} up' , shell=True)
        print(f'new maccAddress is  {macc}')
    else:
        print("Invalid Interface")
   
    
  







changeMac(setInterface , newMac)