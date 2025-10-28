# Pipeline Structure and Execution

###### Topics

- [Pipeline Structure](#build-and-manage-pipeline-structure "#build-and-manage-pipeline-structure")
- [Pipeline Execution using Parallelism
  Configuration](#build-and-manage-pipeline-execution "#build-and-manage-pipeline-execution")

## Pipeline Structure

An Amazon SageMaker Pipelines instance is composed of a `name`, `parameters`, and
`steps`. Pipeline names must be unique within an `(account, region)`
pair. All parameters used in step definitions must be defined in the pipeline. Pipeline
steps listed automatically determine their order of execution by their data dependencies on
one another. The Pipelines service resolves the relationships between steps in the data
dependency DAG to create a series of steps that the execution completes. The following is an
example of a pipeline structure.

###### Warning

When building a pipeline through the visual editor or SageMaker AI Python SDK, do not include
sensitive information in pipeline parameters or any step definition field (such as
environment variables). These fields will be visible in the future when returned in a
`DescribePipeline` request.

```
from sagemaker.workflow.pipeline import Pipeline

  pipeline_name = f"AbalonePipeline"
  pipeline = Pipeline(
      name=pipeline_name,
      parameters=[
          processing_instance_type,
          processing_instance_count,
          training_instance_type,
          model_approval_status,
          input_data,
          batch_data,
      ],
      steps=[step_process, step_train, step_eval, step_cond],
  )
```

## Pipeline Execution using Parallelism

Configuration

By default, a pipeline performs all steps that are available to run in parallel. You can
control this behavior by using the `ParallelismConfiguration` property when
creating or updating a pipeline, as well as when starting or retrying a pipeline execution.

Parallelism configurations are applied per execution. For example, if two executions are
started they can each run a maximum of 50 steps concurrently, for a total of 100
concurrently running steps. Also, `ParallelismConfiguration`(s) specified when
starting, retrying or updating an execution take precedence over parallelism configurations
defined in the pipeline.

###### Example Creating a pipeline execution with `ParallelismConfiguration`

```
pipeline = Pipeline(
        name="`myPipeline`",
        steps=[step_process, step_train]
    )

  pipeline.create(role, parallelism_config={"MaxParallelExecutionSteps": 50})

```
