class StepValidation:
    
    @staticmethod
    def run(orchestrator, pipeline) -> None:
        if not (
            isinstance(pipeline.lhs, int) or not isinstance(pipeline.rhs, int) and
            pipeline.rhs >=0 and pipeline.lhs >=0
        ):
            raise Exception("Step validation")
        output = StepValidation.__format_output(pipeline)
        orchestrator.bots.printer.print_output(output)




    def __format_output(pipeline):
        return f"{pipeline.step} > {pipeline.lhs}  {pipeline.rhs} is not numbers"