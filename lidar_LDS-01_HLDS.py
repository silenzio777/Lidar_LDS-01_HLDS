"""
Code based on "lds_driver.cpp"
* Copyright (c) 2016, Hitachi-LG Data Storage
* Copyright (c) 2017, ROBOTIS
 ## Authors: SP Kong, JH Yang, Pyo 
 ## maintainer: Pyo

 ## Python intrface authors: silenzio
"""

import serial
import time
import numpy as np


port = "/dev/cu.usbserial-A50285BI";
baud_rate = 230400;

print("\n>port:", port," baud_rate:", baud_rate );


try:
	lidarSerial = serial.Serial( port, baud_rate )
	print(">lidar connect:", lidarSerial.isOpen())

except serial.serialutil.SerialException:
	print("\n>lidar connect error...")
	exit()


def poll():

	start_count = 0
	got_scan = False
	shutting_down_ = False
	raw_bytes = np.zeros( 2520 , dtype='bytes' )

	good_sets = 0
	motor_speed = 0
	rpms = 0
	index = 0

	while True:
		readByte = None
		try:
			#Wait until first data sync of frame: 0xFA, 0xA0
			readByte = lidarSerial.read(1)	

			if(start_count == 0):
				if( readByte == b'\xfa'):
					start_count = 1
					byte0 = readByte
			else:
				if(start_count == 1):
					byte1 = readByte
					if( readByte == b'\xa0' ):
						start_count = 0

						# Now that entire start sequence has been found, read in the rest of the message
						got_scan = True

						b_result = bytearray()
						received = lidarSerial.read(2518)

						b_result.extend( byte0 ); b_result.extend( byte1 ); b_result.extend( received )

						raw_bytes = bytes(b_result)
						#print(">raw_bytes len:",len(raw_bytes) )

						# scan->angle_min = 0.0;
						# scan->angle_max = 2.0*M_PI;
						# scan->angle_increment = (2.0*M_PI/360.0);

						## Detection distance --> 120mm ~ 3,500mm
						# scan->range_min = 0.12;
						# scan->range_max = 3.5;

						# scan->ranges.resize(360);
						# scan->intensities.resize(360);

						#read data in sets of 6
						for i in range(0, len(raw_bytes), 42):

							if(raw_bytes[i] == 250 and raw_bytes[i+1] == ( 160 + i / 42)): #&& CRC check

								good_sets+=1;
								motor_speed += (raw_bytes[i+3] << 8) + raw_bytes[i+2]; # accumulate count for avg. time increment
								rpms=(raw_bytes[i+3]<<8|raw_bytes[i+2])/10;

								for j in range(i+4, i+40, 6):

									index = 6*(i/42) + (j-4-i)/6

									# Four bytes per reading
									byte0 = raw_bytes[j]; 	byte1 = raw_bytes[j+1]
									byte2 = raw_bytes[j+2]; byte3 = raw_bytes[j+3]

									# Remaining bits are the range in mm
									intensity = (byte1 << 8) + byte0;

									# Last two bytes represent the uncertanty or intensity, might also be pixel area of target...
									# uint16_t intensity = (byte3 << 8) + byte2;
									ranges = (byte3 << 8) + byte2;

									# scan->ranges[359-index] = range / 1000.0;
									# scan->intensities[359-index] = intensity;

									print(">r[",359-index,"]=", ranges / 1000.0 );

					# scan->time_increment = motor_speed/good_sets/1e8;

					else:
						start_count = 0

		except Exception as e:
			print("\n>lidar pool() exception was thrown: ", e)
			time.sleep(2)

poll()
exit()


"""
>port: /dev/cu.usbserial-A50285BI  baud_rate: 230400
>lidar connect: True
>r[ 359.0 ]= 0.784
>r[ 358.0 ]= 0.789
>r[ 357.0 ]= 0.801
>r[ 356.0 ]= 0.797
>r[ 355.0 ]= 0.799
>r[ 354.0 ]= 0.805
>r[ 353.0 ]= 0.815
"""
