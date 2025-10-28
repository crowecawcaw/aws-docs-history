# Disable Experiments Integration

**Create a pipeline**

You can disable your pipeline's integration with SageMaker Experiments by setting the `pipeline_experiment_config` parameter to `None` when you define your pipeline.
This way, SageMaker AI will not automatically create an experiment, run groups, or individual runs for tracking metrics and artifacts associated with your pipeline executions.
The following example sets the pipeline config parameter to `None`.

```
pipeline_name = f"MyPipeline"
pipeline = Pipeline(
    name=pipeline_name,
    parameters=[...],
    pipeline_experiment_config=None,
    steps=[step_train]
)
```

**Pipeline definition file**

This is the same as the preceding default example, without the `PipelineExperimentConfig`.
