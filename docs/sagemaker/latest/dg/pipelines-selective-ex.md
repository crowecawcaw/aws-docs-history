# Selective execution of pipeline steps

As you use Pipelines to create workflows
and orchestrate your ML training steps, you might need to undertake multiple experimentation phases.
Instead of running the full pipeline each time, you might only want to repeat certain steps.
With Pipelines, you can execute pipeline steps selectively. This helps optimize your ML training. Selective
execution is useful in the following scenarios:

- You want to restart a specific step with updated instance type, hyperparameters,
  or other variables while keeping the parameters from upstream steps.
- Your pipeline fails an intermediate step. Previous steps in the execution, such as
  data preparation or feature extraction, are expensive to rerun. You might need to
  introduce a fix and rerun certain steps manually to complete the pipeline.
  Using selective execution, you can choose to run any subset of steps as long
  as they are connected in the directed acyclic graph (DAG) of your pipeline. The
  following DAG shows an example pipeline workflow:

![A directed acyclic graph (DAG) of an example pipeline.](images/pipeline-full.png)
You can select steps `AbaloneTrain` and `AbaloneEval` in a selective execution,
but you cannot select just `AbaloneTrain` and `AbaloneMSECond` steps
because these steps are not connected in the DAG. For non-selected steps in the workflow,
the selective execution reuses the outputs from a reference pipeline execution rather than rerunning the steps.
Also, non-selected steps that are downstream from the selected steps do not run in a selective execution.

If you choose to run a subset of intermediate steps in your pipeline, your steps may depend on
previous steps. SageMaker AI needs a reference pipeline execution from which to resource these dependencies. For
example, if you choose to run the steps `AbaloneTrain` and `AbaloneEval`, you need the outputs from the
`AbaloneProcess` step. You can either provide a reference execution ARN or
direct SageMaker AI to use the latest pipeline execution, which is the default behavior. If you have a reference
execution, you can also build the runtime parameters from your reference run and supply them to your selective
executive run with overrides. For details, see [Reuse runtime parameter values from a reference execution](#pipelines-selective-ex-reuse "#pipelines-selective-ex-reuse").

In detail, you provide a configuration for your selective execution pipeline run using `SelectiveExecutionConfig`.
If you include an ARN for a reference pipeline execution (with the `source_pipeline_execution_arn` argument), SageMaker AI
uses the previous step dependencies from the pipeline execution you provided. If you do not include an ARN and a latest pipeline
execution exists, SageMaker AI uses it as a reference by default. If you do not include an ARN and
do not want SageMaker AI to use your latest pipeline execution, set `reference_latest_execution` to `False`.
The pipeline execution which SageMaker AI ultimately uses as a reference, whether the latest or user-specified, must be in
`Success` or `Failed` state.

The following table summarizes how SageMaker AI chooses a reference execution.

| The `source_pipeline_execution_arn` argument value | The `reference_latest_execution` argument value | The reference execution used                                  |
| -------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------- |
| A pipeline ARN                                     | `True` or unspecified                           | The specified pipeline ARN                                    |
| A pipeline ARN                                     | `False`                                         | The specified pipeline ARN                                    |
| `null` or unspecified                              | `True` or unspecified                           | The latest pipeline execution                                 |
| `null` or unspecified                              | `False`                                         | None—in this case, select steps without upstream dependencies |

For more information about selective execution configuration requirements, see the
[sagemaker.workflow.selective_execution_config.SelectiveExecutionConfig](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#selective-execution-config "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#selective-execution-config") documentation.

The following discussion includes examples for the cases in which you want to specify a pipeline
reference execution, use the latest pipeline execution as a reference, or run selective execution without a
reference pipeline execution.

## Selective execution with a user-specified pipeline reference

The following example demonstrates a selective execution of the steps `AbaloneTrain`
and `AbaloneEval` using a reference pipeline execution.

```
from sagemaker.workflow.selective_execution_config import SelectiveExecutionConfig

selective_execution_config = SelectiveExecutionConfig(
    source_pipeline_execution_arn="arn:aws:sagemaker:us-west-2:123123123123:pipeline/abalone/execution/123ab12cd3ef",
    selected_steps=["AbaloneTrain", "AbaloneEval"]
)

selective_execution = pipeline.start(
    execution_display_name=f"Sample-Selective-Execution-1",
    parameters={"MaxDepth":6, "NumRound":60},
    selective_execution_config=selective_execution_config,
)
```

## Selective execution with the latest pipeline execution as a reference

The following example demonstrates a selective execution of the steps `AbaloneTrain` and
`AbaloneEval` using the latest pipeline execution as a reference. Since
SageMaker AI uses the latest pipeline execution by default, you can optionally set the `reference_latest_execution`
argument to `True`.

```
# Prepare a new selective execution. Select only the first step in the pipeline without providing source_pipeline_execution_arn.
selective_execution_config = SelectiveExecutionConfig(
    selected_steps=["AbaloneTrain", "AbaloneEval"],
    # optional
    reference_latest_execution=True
)

# Start pipeline execution without source_pipeline_execution_arn
pipeline.start(
    execution_display_name=f"Sample-Selective-Execution-1",
    parameters={"MaxDepth":6, "NumRound":60},
    selective_execution_config=selective_execution_config,
)

```

## Selective execution without a reference pipeline

The following example demonstrates a selective execution of the steps `AbaloneProcess`
and `AbaloneTrain` without providing a reference ARN and turning off the
option to use the latest pipeline run as a reference. SageMaker AI permits this configuration since this subset of steps doesn’t
depend on previous steps.

```
# Prepare a new selective execution. Select only the first step in the pipeline without providing source_pipeline_execution_arn.
selective_execution_config = SelectiveExecutionConfig(
    selected_steps=["AbaloneProcess", "AbaloneTrain"],
    reference_latest_execution=False
)

# Start pipeline execution without source_pipeline_execution_arn
pipeline.start(
    execution_display_name=f"Sample-Selective-Execution-1",
    parameters={"MaxDepth":6, "NumRound":60},
    selective_execution_config=selective_execution_config,
)
```

## Reuse runtime parameter values from a reference execution

You can build the parameters from your reference pipeline execution using `build_parameters_from_execution`,
and supply the result to your selective execution pipeline. You can use the original parameters from the reference
execution, or apply any overrides using the `parameter_value_overrides` argument.

The following example shows you how to build parameters from a reference execution and apply an override for the
`MseThreshold` parameter.

```
# Prepare a new selective execution.
selective_execution_config = SelectiveExecutionConfig(
    source_pipeline_execution_arn="arn:aws:sagemaker:us-west-2:123123123123:pipeline/abalone/execution/123ab12cd3ef",
    selected_steps=["AbaloneTrain", "AbaloneEval", "AbaloneMSECond"],
)
# Define a new parameters list to test.
new_parameters_mse={
    "MseThreshold": 5,
}

# Build parameters from reference execution and override with new parameters to test.
new_parameters = pipeline.build_parameters_from_execution(
    pipeline_execution_arn="arn:aws:sagemaker:us-west-2:123123123123:pipeline/abalone/execution/123ab12cd3ef",
    parameter_value_overrides=new_parameters_mse
)

# Start pipeline execution with new parameters.
execution = pipeline.start(
    selective_execution_config=selective_execution_config,
    parameters=new_parameters
)
```
