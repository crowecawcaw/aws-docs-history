# Specify a Custom Experiment Name

While the default behavior is to use the pipeline name as the experiment name in SageMaker Experiments, you can override this and specify a custom experiment name instead. This can be useful if you want to group multiple pipeline executions under the same experiment for easier analysis and comparison.
The run group name will still default to the pipeline execution ID unless you explicitly set a custom name for that as well. The following section demonstrates how to create a pipeline with a custom experiment name while leaving the run group name as the default execution ID.

**Create a pipeline**

```
pipeline_name = f"MyPipeline"
pipeline = Pipeline(
    name=pipeline_name,
    parameters=[...],
    pipeline_experiment_config=PipelineExperimentConfig(
      "CustomExperimentName",
      ExecutionVariables.PIPELINE_EXECUTION_ID
    ),
    steps=[step_train]
)
```

**Pipeline definition file**

```
{
  ...,
  "PipelineExperimentConfig": {
    "ExperimentName": "CustomExperimentName",
    "TrialName": {"Get": "Execution.PipelineExecutionId"}
  },
  "Steps": [...]
}
```
