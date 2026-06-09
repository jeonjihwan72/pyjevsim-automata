from pyjevsim import BehaviorModel, Infinite, SysMessage

import datetime

class Generator(BehaviorModel):
    def __init__(self, name):
       BehaviorModel.__init__(self, name)

       self.init_state("Wait")
       self.insert_state("Wait", Infinite)
       self.insert_state("Generate", 1)

       self.insert_input_port("start")
       self.insert_output_port("out")

    def ext_trans(self, port, msg):
        if self._cur_state == "Wait" and port == "start":
            print(f"{self.get_name()}[start_recv]:{datetime.datetime.now()}")
            self._cur_state = "Generate"

    def output(self, msg_deliver):
        if self._cur_state == "Generate":
            print(f"{self.get_name()}[out_send]:{datetime.datetime.now()}")
            message = SysMessage(self.get_name(), "out")
            msg_deliver.insert_message(message)

    def int_trans(self):
        if self._cur_state == "Generate":
            self._cur_state = "Generate"