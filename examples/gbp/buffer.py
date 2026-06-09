from pyjevsim import BehaviorModel, Infinite, SysMessage

import datetime

class Buffer(BehaviorModel):
    def __init__(self, name):
       BehaviorModel.__init__(self, name)

       self.init_state("Wait")
       self.insert_state("Wait", Infinite)
       
       # Wait -> ONE, ONE -> TWO, TWO -> THREE, THREE -> FOUR
       # insert states with time advance 1
       # TODO: ONE, TWO, THREE, FOUR에 대한 time advance를 1로 설정한 상태 입력
       self.insert_state("ONE", 1)
       self.insert_state("TWO", 1)
       self.insert_state("THREE", 1)
       self.insert_state("FOUR", 1)

       self.insert_input_port("in")
       self.insert_output_port("out")

    def ext_trans(self, port, msg):
        if self._cur_state == "Wait" and port == "in":
            print(f"{self.get_name()}[WAIT] -> [ONE]:{datetime.datetime.now()}")
            self._cur_state = "ONE" 
        elif self._cur_state == "ONE" and port == "in":
            print(f"{self.get_name()}[ONE] -> [TWO]:{datetime.datetime.now()}")
            self._cur_state = "TWO"
        elif self._cur_state == "TWO" and port == "in":
            print(f"{self.get_name()}[TWO] -> [THREE]:{datetime.datetime.now()}")
            self._cur_state = "THREE"
        elif self._cur_state == "THREE" and port == "in":
            print(f"{self.get_name()}[THREE] -> [FOUR]:{datetime.datetime.now()}")
            self._cur_state = "FOUR"

    def output(self, msg_deliver):
        if self._cur_state == "ONE":
            print(f"{self.get_name()}[ONE] -> [WAIT]:{datetime.datetime.now()}")
            message = SysMessage(self.get_name(), "out")
            msg_deliver.insert_message(message)
        elif self._cur_state == "TWO":
            print(f"{self.get_name()}[TWO] -> [ONE]:{datetime.datetime.now()}")
            message = SysMessage(self.get_name(), "out")
            msg_deliver.insert_message(message)
        elif self._cur_state == "THREE":
            print(f"{self.get_name()}[THREE] -> [TWO]:{datetime.datetime.now()}")
            message = SysMessage(self.get_name(), "out")
            msg_deliver.insert_message(message)
        elif self._cur_state == "FOUR":
            print(f"{self.get_name()}[FOUR] -> [THREE]:{datetime.datetime.now()}")
            message = SysMessage(self.get_name(), "out")
            msg_deliver.insert_message(message)

    def int_trans(self):
        if self._cur_state == "Wait":
            self._cur_state = "Wait"
        elif self._cur_state == "ONE":
            # ONE -> Wait
            self._cur_state = "Wait"
        elif self._cur_state == "TWO":
            # TWO -> ONE
            self._cur_state = "ONE"
        elif self._cur_state == "THREE":
            # THREE -> TWO
            self._cur_state = "TWO"
        elif self._cur_state == "FOUR":
            # FOUR -> THREE
            self._cur_state = "THREE"