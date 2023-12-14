import can
import logging
import time

# Initializing the corresponding CAN ids
request_id = 0x780
response_id = 0x788
sid = 0x2f
pid = 0xbc

#logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
bus = can.Bus("slcan0", bustype="socketcan")    

class CanBusClass:
        def __init__(self):
                pass
        
        def send_request(self, message):
            bus.send(message)
               
        def start_session(self):
            """
                This method changes the current session to "programming mode". Only then can we send diagnostic codes
                to control the vehicle components.
            """
            session_message = can.Message(arbitration_id=request_id,
                                                data=[0x02, 0x10, 0x03,0,0,0,0,0],
                                                is_extended_id=False)
            bus.send(session_message)

        def tester_present(self):
            session_message = can.Message(arbitration_id=request_id,
                                                data=[0x02, 0x3E, 0,0,0,0,0,0],
                                                is_extended_id=False)
            bus.send(session_message)
        
        def read_brake_fluid_sensor_level(self):
            message = can.Message(arbitration_id=request_id,
                                                data=[0x04, 0x31, 0x03,0x02,0x14,0,0,0],
                                                is_extended_id=False)
            self.send_request(message=message)
        
        def start_pv_bleeding(self):
            message = can.Message(arbitration_id=request_id,
                                                data=[0x04, 0x31, 0x01,0x02,0x12,0,0,0],
                                                is_extended_id=False)
            self.send_request(message=message)

            while True:
                time.sleep(1)
                message = can.Message(arbitration_id=request_id,
                                                data=[0x04, 0x31, 0x03,0x02,0x12,0,0,0],
                                                is_extended_id=False)
                self.send_request(message=message)
        
        def start_zeroing(self):
            message = can.Message(arbitration_id=request_id,
                                                data=[0x05, 0x31, 0x01,0x02,0x03,0x02,0,0],
                                                is_extended_id=False)
            self.send_request(message=message)
                
            time.sleep(1)
            self.tester_present()