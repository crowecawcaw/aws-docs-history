# Specify a Custom Run Group Name

In addition to setting a custom experiment name, you can also specify a custom name for the run groups created by SageMaker Experiments during pipeline executions.
This name is appended with the pipeline execution ID to ensure uniqueness. You can specify a custom run group name to identify and analyze related pipeline runs within the same experiment. The following section shows how to define a pipeline with a custom run group name while using the default pipeline name for the experiment name.

**Create a pipeline**

```
pipeline_name = f"MyPipeline"
pipeline = Pipeline(
    name=pipeline_name,
    parameters=[...],
    pipeline_experiment_config=PipelineExperimentConfig(
      ExecutionVariables.PIPELINE_NAME,
      Join(on="-", values=["CustomTrialName", ExecutionVariables.PIPELINE_EXECUTION_ID])
    ),
    steps=[step_train]
)
```

**Pipeline definition file**

```
{
  ...,
  "PipelineExperimentConfig": {
    "ExperimentName": {"Get": "Execution.PipelineName"},
    "TrialName": {
      "On": "-",
      "Values": [
         "CustomTrialName",
         {"Get": "Execution.PipelineExecutionId"}
       ]
    }
  },
  "Steps": [...]
}
```
