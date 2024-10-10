class StepMulti:
    
    @staticmethod
    def run(orchestrator, pipeline) -> None:
        pipeline.result = orchestrator.bots.multiplier.multi(pipeline.lhs, pipeline.rhs)
        output = StepMulti.__format_output(pipeline)
        orchestrator.bots.printer.print_output(output)

    def __format_output(pipeline):
        return f"{pipeline.step} > {pipeline.lhs} * {pipeline.rhs} = {pipeline.result}"