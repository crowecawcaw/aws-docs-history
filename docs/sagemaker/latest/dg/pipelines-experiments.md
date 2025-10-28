# Amazon SageMaker Experiments Integration

Amazon SageMaker Pipelines is closely integrated with Amazon SageMaker Experiments. By default, when Pipelines creates
and executes a pipeline, the following SageMaker Experiments entities are created if they don't
exist:

- An experiment for the pipeline
- A run group for every execution of the pipeline
- A run that's added to the run group for each SageMaker AI job created in a pipeline execution
  step
  You can compare metrics such as model training accuracy across multiple pipeline executions
  just as you can compare such metrics across multiple run groups of a SageMaker AI model training
  experiment.

The following sample shows the relevant parameters of the
[Pipeline](https://github.com/aws/sagemaker-python-sdk/blob/v2.41.0/src/sagemaker/workflow/pipeline.py "https://github.com/aws/sagemaker-python-sdk/blob/v2.41.0/src/sagemaker/workflow/pipeline.py")
class in the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable").

```
Pipeline(
    name="MyPipeline",
    parameters=[...],
    pipeline_experiment_config=PipelineExperimentConfig(
      ExecutionVariables.PIPELINE_NAME,
      ExecutionVariables.PIPELINE_EXECUTION_ID
    ),
    steps=[...]
)
```

If you don't want an experiment and run group created for the pipeline, set
`pipeline_experiment_config` to `None`.

###### Note

Experiments integration was introduced in the Amazon SageMaker Python SDK v2.41.0.

The following naming rules apply based on what you specify for the `ExperimentName`
and `TrialName` parameters of `pipeline_experiment_config`:

- If you don't specify `ExperimentName`, the pipeline `name` is
  used for the experiment name.

If you do specify `ExperimentName`, it's used for the experiment name. If an
experiment with that name exists, the pipeline-created run groups are added to the existing
experiment. If an experiment with that name doesn't exist, a new experiment is
created.

- If you don't specify `TrialName`, the pipeline execution ID is used for the
  run group name.

If you do specify `TrialName`, it's used for the run group name. If a run
group with that name exists, the pipeline-created runs are added to the existing run group.
If a run group with that name doesn't exist, a new run group is created.

###### Note

The experiment entities aren't deleted when the pipeline that created the entities is
deleted. You can use the SageMaker Experiments API to delete the entities.

For information about how to view the SageMaker AI Experiment entities associated with a pipeline, see
[Access experiment data from a pipeline](pipelines-studio-experiments.md "pipelines-studio-experiments.md").
For more information on SageMaker Experiments, see
[Amazon SageMaker Experiments in Studio Classic](experiments.md "experiments.md").

The following sections show examples of the previous rules and how they are represented
in the pipeline definition file. For more information on pipeline definition files, see
[Pipelines overview](pipelines-overview.md "pipelines-overview.md").

###### Topics

- [Default Behavior](pipelines-experiments-default.md "pipelines-experiments-default.md")
- [Disable Experiments Integration](pipelines-experiments-none.md "pipelines-experiments-none.md")
- [Specify a Custom Experiment Name](pipelines-experiments-custom-experiment.md "pipelines-experiments-custom-experiment.md")
- [Specify a Custom Run Group Name](pipelines-experiments-custom-trial.md "pipelines-experiments-custom-trial.md")
