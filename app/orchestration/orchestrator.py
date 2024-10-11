from ..bots import FactoryBot
from ..models import Pipeline
from .business_process import BusinessProcess

class Bots: 
    def __init__(self):
        self.adder = FactoryBot.create(FactoryBot.ADDER)
        self.multiplier = FactoryBot.create(FactoryBot.MULTIPLE)   
        self.printer = FactoryBot.create(FactoryBot.PRINTER)
        self.subtract = FactoryBot.create(FactoryBot.SUBTRACT)


class Orchestrator:

    def __init__(self) -> None:
        self.bots = Bots()

    def start(self, lhs: int, rhs: int) -> None:
        pipeline = Pipeline(lhs, rhs, BusinessProcess.STARTED)
        BusinessProcess.run(self, pipeline)
        return pipeline.result