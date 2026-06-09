import project_config

from pyjevsim import SysExecutor, ExecutionType
from generator import Generator
from processor import Processor

# TODO: implement Buffer and insert it between Generator and Processor
from buffer import Buffer

se = SysExecutor(1, ex_mode=ExecutionType.R_TIME)

se.insert_input_port("start")

gen = Generator("Generator")
se.register_entity(gen)
se.coupling_relation(se, "start", gen, "start")

proc = Processor("Processor")
se.register_entity(proc)
# se.coupling_relation(gen, "out", proc, "in")

# TODO: complete coupling relation between Buffer and Generator, Processor
buff = Buffer("Buffer")
se.register_entity(buff)
se.coupling_relation(gen, "out", buff, "in")
se.coupling_relation(buff, "out", proc, "in")

se.insert_external_event("start", None)

for _ in range(30):
    se.simulate(1)

se.terminate_simulation()