#!/bin/bash

# CAN device (i.e 'ttyACM1')
DEVICE=ttyACM2

# Load kernel modules
sudo modprobe can
sudo modprobe can-raw
sudo modprobe slcan

# Attach to device
#sudo slcan_attach -f -s6 -o /dev/$DEVICE
#sudo slcand -o -s6 -t hw -S 3000000 /dev/$DEVICE
#sudo slcand -o -s5 /dev/$DEVICE

# Bind the USBCAN device
sleep 1
sudo slcand -o -c -f -s6 /dev/$DEVICE slcan0
sleep 2
sudo ip link set up slcan0

#sudo ip link set can0 up type can bitrate 500000

# Start the slcand for this interface
#sudo slcand $DEVICE slcan0

# Bring the interface up
#sudo ifconfig slcan0 up
#sudo ip link set up slcan0

