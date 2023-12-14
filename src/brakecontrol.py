from pycarmaker import CarMaker, Quantity
from canbus import CanBusClass
import time
import logging

logging.basicConfig(filename='brakeData.log', format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',  level=logging.INFO)

IP_ADDRESS = "localhost"
PORT = 16660

class CarMakerClass:
    def __init__(self, IP_ADDRESS, PORT, canbusObj):
        self.cm = CarMaker(IP_ADDRESS, PORT)
        self.canbus = canbusObj
        self.cm.connect()
        self.apply_brakes = True

        self.brake_moment_fr = 0
        self.brake_moment_fr = Quantity("DM.Brake", Quantity.FLOAT)
        self.brake_moment_fr.data = -1.0
        self.cm.subscribe(self.brake_moment_fr)
        self.sim_status = Quantity("SimStatus", Quantity.INT, True)
        self.cm.subscribe(self.sim_status)
        self.cm.read()
        self.cm.read()
        time.sleep(0.1)
    
    def read_brake_moment(self):
        while(self.sim_status.data>=0):
            # Read data from carmaker
            self.cm.read()
            print()
            print("Vehicle speed: " + str(self.brake_moment_fr.data) + " km/h")
            if self.brake_moment_fr.data > 0.1 and self.apply_brakes:
                print("True")
                self.canbus.start_session()
                time.sleep(0.1)
                self.canbus.start_zeroing()
                self.apply_brakes = False

            print("Simulation status: " + ("Running" if self.sim_status.data >=
                                        0 else self.cm.status_dic.get(self.sim_status.data)))
            #logging.info('Bremsmoment_FR: {}'.format(brake_moment_fr.data))
            
            time.sleep(1)
            
canbusObj = CanBusClass()
canbusObj.start_session()
time.sleep(0.1)
canbusObj.start_zeroing()
#carmakerObj = CarMakerClass(IP_ADDRESS, PORT, canbusObj)
#carmakerObj.read_brake_moment()