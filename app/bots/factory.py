from app.bots.adder import AdderBot
from app.bots.printer import PrinterBot
from app.bots.subtract import SubtractorBot
from app.bots.multiplier import MultiBot
class FactoryBot:

    ADDER = "ADDER"
    PRINTER = "PRINTER"
    SUBTRACT = "SUBTRACT"
    MULTIPLE = "MULTIPLE"

    @staticmethod        
    def create(bot):
        if bot == FactoryBot.ADDER:
            return AdderBot()
        elif bot == FactoryBot.PRINTER:
            return PrinterBot()
        elif bot == FactoryBot.SUBTRACT:
            return SubtractorBot()
        elif bot == FactoryBot.MULTIPLE:
            return MultiBot()
        else:
            raise Exception("{bot} not found!")