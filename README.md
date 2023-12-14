# Project Description
This is a project to create a bridge between IPG CarMaker and the brake system. The project serves as a part of hardware-in-loop to send commands to the test rig of the brake system from a simulation running on CarMaker software.

## Prerequisites
To be able to use this program, you need to install CarMaker software in Linux. The installation guide can be found in the downloaded zip folder provided by IPG.
To read/write data on the CAN bus on the test rig, CAN adaption [usb-tin](https://www.fischl.de/usbtin/) is used because of its simple design and ability to operate with Linux.
The baud rate used is 500 kb/s.

## Code usability
To start with the project, set up your CAN Adapter with 500 kb/s. For this, run the `setup_new.sh` script as follows:
```shell
./setup_new.sh
```

Once your CAN adapter is up, test it by sending a request to CAN bus:
```shell
cansend 780#02.10.03.00.00.00.00.00
```
Start other terminal, and listen to the response:
```shell
candump slcan0
```
You shoud receive `788 02 50 03 00 00 00 00 00`.
