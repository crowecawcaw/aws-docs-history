# Default Behavior

**Create a pipeline**

The default behavior when creating a SageMaker AI Pipeline is to automatically integrate it with SageMaker Experiments. If you don't specify any custom configuration,
SageMaker AI creates an experiment with the same name as the pipeline, a run group for each execution of the pipeline using the pipeline execution ID as the name, and individual runs within each run group for every SageMaker AI job launched as part of the pipeline steps.
You can seamlessly track and compare metrics across different pipeline executions, similar to how you would analyze a model training experiment. The following section demonstrates this default behavior when defining a pipeline without explicitly configuring the experiment integration.

The `pipeline_experiment_config` is omitted. `ExperimentName`
defaults to the pipeline `name`. `TrialName` defaults to the execution ID.

```
pipeline_name = f"MyPipeline"
pipeline = Pipeline(
    name=pipeline_name,
    parameters=[...],
    steps=[step_train]
)
```

**Pipeline definition file**

```
{
  "Version": "2020-12-01",
  "Parameters": [
    {
      "Name": "InputDataSource"
    },
    {
      "Name": "InstanceCount",
      "Type": "Integer",
      "DefaultValue": 1
    }
  ],
  "PipelineExperimentConfig": {
    "ExperimentName": {"Get": "Execution.PipelineName"},
    "TrialName": {"Get": "Execution.PipelineExecutionId"}
  },
  "Steps": [...]
}
```
