from pyjevsim import BehaviorModel, Infinite
import datetime

class Manuever(BehaviorModel):
    def __init__(self, name, platform):
        BehaviorModel.__init__(self, name)
        
        self.platform = platform
        
        self.init_state("Wait")     # Initial state 설정
        # insert_state(state_name, duration) , 상태별 최대 대기시간 설정
        self.insert_state("Wait", Infinite)
        self.insert_state("Generate", 1)

        self.insert_input_port("start")

    def ext_trans(self,port, msg):
        if port == "start":
            print(f"{self.get_name()}[start_recv]: {datetime.datetime.now()}")
            self._cur_state = "Generate"

    def output(self, msg_deliver):
        self.platform.mo.calc_next_pos_with_heading(1)
        
    def int_trans(self):
        if self._cur_state == "Generate":
            self._cur_state = "Generate"