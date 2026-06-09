
from pyjevsim import BehaviorModel, Infinite, SysMessage

import datetime

class Processor(BehaviorModel):
    def __init__(self, name):
       BehaviorModel.__init__(self, name)

       self.init_state("Wait")
       self.insert_state("Wait", Infinite)

       self.insert_input_port("in")

    def ext_trans(self, port, msg):
        if self._cur_state == "Wait" and port == "in":
            print(f"{self.get_name()}[in_recv]:{datetime.datetime.now()}")
            self._cur_state = "Wait"

    def output(self, msg_deliver):
        pass

    def int_trans(self):
        if self._cur_state == "Wait":
            self._cur_state = "Wait"