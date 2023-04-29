# ubertooth-bt-tracker
### Track Bluetooth devices and their proximity to a GPS location. 

This script is written in Python 3 and is used to track Bluetooth devices and their proximity to a GPS location. The script uses the gps3 and subprocess libraries to access GPS location and Bluetooth scanning tools, respectively.

## Prerequisites:

- Python 3
- gps3 library
- ubertooth-scan tool
- ubertooth one
- gpsd
- gps dongle

## Usage:

- Connect the GPS device to the system.
- Connect Ubertooth One to the system.
- Enable bluetooth and gpsd services. 
- Run the script using the command: 

sudo python3 ubertooth-bt-tracker.py

				       kNXK0OOOkkOOO0KXNk                  
				   dNX0OOkkkkkkkkkkkkkkkkOO0XNd          
				;N0OkkkkkkkkkkdokkkkkkkkkkkkkkO0N:       
			      ,XOkkkkkkkkkkkkkx  okkkkkkkkkkkkkkkOX;     
			     OOkkkkkkkkkkkkkkkx    ckkkkkkkkkkkkkkkO0    
			    XOkkkkkkkkkkkkkkkkx      :kkkkkkkkkkkkkkOX   
			   0kkkkkkkkkkkkkkkkkkx        ;kkkkkkkkkkkkkkK  
			  dOkkkkkkkkkkkkkkkkkkx          ,kkkkkkkkkkkkkd 
			 .Okkkkkkkkkkkkkkkkkkkx    .o       kkkkkkkkkkkO
			 xkkkkkkkkkd  ;kkkkkkkx    .OKd      .kkkkkkkkkkx
			 Okkkkkkko      ,kkkkkx    .kkOKx      .kkkkkkkkO
			;kkkkkkkkOXo       kkkx    .kkkk       NOkkkkkkkk
			okkkkkkkkkkOKx      .kx    .kx       N0kkkkkkkkkk
			xkkkkkkkkkkkkOKk                  .N0kkkkkkkkkkkk
			kkkkkkkkkkkkkkkOKO              .N0kkkkkkkkkkkkkk
			     u b e r t o o t h         o n e             
			kkkkkkkkkkkkkkkkkkkOKx      .XOkkkkkkkkkkkkkkkkkk
			kkkkkkkkkkkkkkkkkkkc           kkkkkkkkkkkkkkkkkk
			kkkkkkkkkkkkkkkkk:               kkkkkkkkkkkkkkkk
			dkkkkkkkkkkkkkk;           .       xkkkkkkkkkkkkk
			lkkkkkkkkkkkk,      lXx    .0N.      dkkkkkkkkkkk
			,kkkkkkkkkk       dKOkx    .kk0N.      dkkkkkkkkk
			 kkkkkkkkk      xKOkkkx    .kkkk;      cOkkkkkkkk
			 lkkkkkkkk0N  kKOkkkkkx    .kk       lXOkkkkkkkkl
			 .kkkkkkkkkk0KOkkkkkkkx    ..      dKOkkkkkkkkkk.
			  :kkkkkkkkkkkkkkkkkkkx          xKOkkkkkkkkkkkc 
			      b l u e t o o t h           t r a c k e r  
			    xkkkkkkkkkkkkkkkkkx      0KOkkkkkkkkkkkkkd   
			     lkkkkkkkkkkkkkkkkx    KKOkkkkkkkkkkkkkkl    
			      .kkkkkkkkkkkkkkkx  N0Okkkkkkkkkkkkkkk.     
				 kkkkkkkkkkkkkxN0kkkkkkkkkkkkkkkk.       
				   .kkkkkkkkkkOkkkkkkkkkkkkkkk.          
					  dkkkkkkkkkkkkkkd  

-The script will start scanning for Bluetooth devices nearby.
- If a Bluetooth device with signal strength below a threshold (65 in this case) is detected, the GPS location will be obtained and logged into a file along with Bluetooth device details and a note entered by the user.
- To stop the script, press CTRL + C.

## Note:

- The script requires sudo privileges to run the ubertooth-scan tool.
- The logged data is stored in a text file named in the format mylogfile_<timestamp>.txt where timestamp is the current time in the format yymmdd_hhmmss.
- The script will prompt the user to enter a note each time a Bluetooth device is detected, before logging the data.
- If the script is terminated before logging the data, the script will automatically reset the ubertooth device using ubertooth-util -r.
