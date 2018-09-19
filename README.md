# ChangeMacAddress
Python script for Linux for changing the Mac Address
---------------------------------------------------------------
Parameter

-s  : Show Interface 

-r  : Build a random Mac Address

-i  : Choose a Interface (needed to change the Mac-Address)

-m  : Choose a Mac Address m and change the current one in m

-----------------------------------------------------------------

Example usage:

Change the Mac Address in Interface eth0 with a random Mac Address

./change_mac -i eth0 -r

Change the MacAddress in eth0 into 3c:d9:2c:24:9f:4e
  
./change_mac -i eth0 -m 3c:d9:2c:24:9f:4e

Show the Interface from eth0

./change_mace -s -i eth0

  
