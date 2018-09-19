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
            command = "ip link show " +self.iface 

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

    opt = OptionParser()
    mac = MacChange()

    #Adding options for change_mac to set a manuelly mac with the interface or a random mac with the interface
    opt.add_option('-m', '--mac', help='Choose a Mac Address\n', dest='mac')
    opt.add_option('-i', '--interface', help='Choose a Interface\n', dest='iface')
    opt.add_option('-r', '--random', help='Build random Mac Address\n', dest='rndmac', action='store_true')
    opt.add_option('-s', '--show', help='Show the interface\n', dest='shw', action='store_true')
    
    arg, args = opt.parse_args()
        
    #show all interfaces with -s
    if arg.iface == None and arg.shw:
        mac.show_interface()    
        exit()

    #show only the interfacce  -s -i <interfacename>
    if arg.iface and arg.shw:
        mac.set_iface(arg.iface)
        mac.show_interface()
        exit()

    if arg.iface == None and arg.shw == None:
        logging.error("Interface needed")
        exit()

    if arg.iface and arg.mac:
        mac.set_iface(arg.iface)
        mac.set_mac(arg.mac)
        mac.change_mac()
          
    elif arg.iface and arg.rndmac:
        mac.set_iface(arg.iface)
        mac.set_mac(mac.set_random_mac())
        mac.change_mac()
        
    else:

        logging.error("Failure: Check parameter for interface and mac")
        exit()
