from ...models.pipeline import Pipeline
from .steps import StepStarted, StepAdding, StepDone, StepValidation, StepSubtract, StepMulti, StepValidation
from typing import Any, List

class BusinessProcess:

    STARTED = "Started"
    ADDING = "Adding"
    SUBTRACTOR = "Subtractor"
    MULTIPLE = "Multiple"
    VALIDATE = "Validate"
    DONE = "Done"

    @staticmethod
    def forward(pipeline: Pipeline):
        steps = BusinessProcess.get_steps()
        index = steps.index(pipeline.step)
        pipeline.step = steps[min(index+1, len(steps)-1)]
    

    @staticmethod
    def get_steps() -> List[str]:
        return [
            BusinessProcess.STARTED,
            BusinessProcess.ADDING,
            BusinessProcess.SUBTRACTOR,
            BusinessProcess.MULTIPLE,
            BusinessProcess.VALIDATE,
            BusinessProcess.DONE,
        ]
    
    @staticmethod
    def run(orchestrator, pipeline: Pipeline):
        if pipeline.step == BusinessProcess.STARTED:
            StepStarted.run(orchestrator, pipeline)
            BusinessProcess.forward(pipeline)
        if pipeline.step == BusinessProcess.VALIDATE:
            StepValidation.run(orchestrator, pipeline)

        if pipeline.step == BusinessProcess.ADDING:
            StepAdding.run(orchestrator, pipeline)
            BusinessProcess.forward(pipeline)
        
        if pipeline.step == BusinessProcess.SUBTRACTOR:
            StepSubtract.run(orchestrator, pipeline)
            BusinessProcess.forward(pipeline)
        
        if pipeline.step == BusinessProcess.MULTIPLE:
            StepMulti.run(orchestrator, pipeline)
            BusinessProcess.forward(pipeline)
    
        if pipeline.step == BusinessProcess.DONE:
            StepDone.run(orchestrator, pipeline)