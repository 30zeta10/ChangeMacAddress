import logging
import random
import subprocess as sp
from optparse import OptionParser


class MacChange():
    
    def __init__(self, mac_addr=None, iface = None):
        self.mac = mac_addr
        self.iface = iface

    #return the current saved interface
    def get_iface(self):
        return self.iface


    #set an interface string
    def set_iface(self, iface):
        self.iface = iface


    #return the current saved mac-address
    def get_mac(self):
        return self.mac


    #set a mac-address
    def set_mac(self, mac):
        self.mac = mac


    #built a random mac-address
    def set_random_mac(self):
        rnd_mac =  ':'.join(("%012x" % random.randint(0, 0xFFFFFFFFFFFF))[i:i+2] for i in range(0, 12, 2))
        set_mac(rnd_mac)


    #shows the ip link interfaces 
    def show_interface(self):
        
        if self.iface:
            command = "ip link show " + interface

        else:
            command = "ip link show"

        sp.call(command.split())


    #change the mac address in ip link
    def change_mac(self):
       
        if self.iface:
            idown = "ip link set dev " + self.iface + " down"
            sp.call(idown.split())
            
            if self.mac:
                ch_mac = "ip link set dev " + self.iface + " address " + self.mac
                sp.call(ch_mac.split())

            else:
                logging.error("No MacAddress choosen")
                exit()

            fn_cmd = "ip link set dev " + self.iface + " up"
            sp.call(fn_cmd.split())

        else:
            logging.error("No Interface choosen")
            exit()


if __name__ == '__main__':


