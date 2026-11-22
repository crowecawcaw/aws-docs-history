

# Pipelines steps

Pipelines are composed of steps. These steps define the actions that the pipeline takes and the relationships between steps using properties. The following page describes the types of steps, their properties, and the relationships between them.

**Topics**
+ [Add a step](build-and-manage-steps-types.md)
+ [Add integration](build-and-manage-steps-integration.md)
+ [Step properties](#build-and-manage-properties)
+ [Step parallelism](#build-and-manage-parallelism)
+ [Data dependency between steps](#build-and-manage-data-dependency)
+ [Custom dependency between steps](#build-and-manage-custom-dependency)
+ [Run conditions for steps](#build-and-manage-run-conditions)
+ [Optional conditional arguments](#build-and-manage-conditional-arguments)
+ [Custom images in a step](#build-and-manage-images)

## Step properties
<a name="build-and-manage-properties"></a>

Use the `properties` attribute to add data dependencies between steps in the pipeline. Pipelines use these data dependencies to construct the DAG from the pipeline definition. These properties can be referenced as placeholder values and are resolved at runtime. 

The `properties` attribute of a Pipelines step matches the object returned by a `Describe` call for the corresponding SageMaker AI job type. For each job type, the `Describe` call returns the following response object:
+ `ProcessingStep` – [DescribeProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeProcessingJob.html)
+ `TrainingStep` – [DescribeTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingJob.html)
+ `TransformStep` – [DescribeTransformJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTransformJob.html)

To check which properties are referrable for each step type during data dependency creation, see *[Data Dependency - Property Reference](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#data-dependency-property-reference)* in the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable).

## Step parallelism
<a name="build-and-manage-parallelism"></a>

When a step does not depend on any other step, it runs immediately upon pipeline execution. However, executing too many pipeline steps in parallel can quickly exhaust available resources. Control the number of concurrent steps for a pipeline execution with `ParallelismConfiguration`.

The following example uses `ParallelismConfiguration` to set the concurrent step limit to five.

```python
pipeline.create(
    parallelism_config=ParallelismConfiguration(5),
)
```

## Data dependency between steps
<a name="build-and-manage-data-dependency"></a>

You define the structure of your DAG by specifying the data relationships between steps. To create data dependencies between steps, pass the properties of one step as the input to another step in the pipeline. The step receiving the input isn't started until after the step providing the input finishes running.

A data dependency uses JsonPath notation in the following format. This format traverses the JSON property file. This means you can append as many {{<property>}} instances as needed to reach the desired nested property in the file. For more information on JsonPath notation, see the [JsonPath repo](https://github.com/json-path/JsonPath).

```python
{{<step_name>}}.properties.{{<property>}}.{{<property>}}
```

The following shows how to specify an Amazon S3 bucket using the `ProcessingOutputConfig` property of a processing step.

```python
step_process.properties.ProcessingOutputConfig.Outputs["train_data"].S3Output.S3Uri
```

To create the data dependency, pass the bucket to a training step as follows.

```python
from sagemaker.workflow.pipeline_context import PipelineSession

sklearn_train = SKLearn(..., sagemaker_session=PipelineSession())

step_train = TrainingStep(
    name="CensusTrain",
    step_args=sklearn_train.fit(inputs=TrainingInput(
        s3_data=step_process.properties.ProcessingOutputConfig.Outputs[
            "train_data"].S3Output.S3Uri
    ))
)
```

To check which properties are referrable for each step type during data dependency creation, see *[Data Dependency - Property Reference](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#data-dependency-property-reference)* in the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable).

## Custom dependency between steps
<a name="build-and-manage-custom-dependency"></a>

When you specify a data dependency, Pipelines provides the data connection between the steps. Alternatively, one step can access the data from a previous step without directly using Pipelines. In this case, you can create a custom dependency that tells Pipelines not to start a step until after another step has finished running. You create a custom dependency by specifying a step's `DependsOn` attribute.

As an example, the following defines a step `C` that starts only after both step `A` and step `B` finish running.

```json
{
  'Steps': [
    {'Name':'A', ...},
    {'Name':'B', ...},
    {'Name':'C', 'DependsOn': ['A', 'B']}
  ]
}
```

Pipelines throws a validation exception if the dependency would create a cyclic dependency.

The following example creates a training step that starts after a processing step finishes running.

```python
processing_step = ProcessingStep(...)
training_step = TrainingStep(...)

training_step.add_depends_on([processing_step])
```

The following example creates a training step that doesn't start until two different processing steps finish running.

```python
processing_step_1 = ProcessingStep(...)
processing_step_2 = ProcessingStep(...)

training_step = TrainingStep(...)

training_step.add_depends_on([processing_step_1, processing_step_2])
```

The following provides an alternate way to create the custom dependency.

```python
training_step.add_depends_on([processing_step_1])
training_step.add_depends_on([processing_step_2])
```

The following example creates a training step that receives input from one processing step and waits for a different processing step to finish running.

```python
processing_step_1 = ProcessingStep(...)
processing_step_2 = ProcessingStep(...)

training_step = TrainingStep(
    ...,
    inputs=TrainingInput(
        s3_data=processing_step_1.properties.ProcessingOutputConfig.Outputs[
            "train_data"
        ].S3Output.S3Uri
    )

training_step.add_depends_on([processing_step_2])
```

The following example shows how to retrieve a string list of the custom dependencies of a step.

```python
custom_dependencies = training_step.depends_on
```

## Run conditions for steps
<a name="build-and-manage-run-conditions"></a>

By default, a step runs only after all of the steps it depends on have completed successfully. Run conditions let a step declare that it runs based on the outcome of an upstream step, not just on success. This supports patterns such as cleanup that always runs, failure notifications, and fallback logic. You declare the condition on the consuming step. A plain step or step name in `depends_on` keeps its existing behavior.

**Set a trigger on a dependency**

To set a run condition, wrap the upstream step in a `StepDependency` in `depends_on`, and pass a `TriggerCondition`. Run conditions are available in the SageMaker Python SDK v3.26.0 or later, and are not supported in local mode. The following example runs a notification step on any outcome of a training step.

```python
from sagemaker.core.lambda_helper import Lambda
from sagemaker.mlops.workflow import LambdaStep, StepDependency, TriggerCondition

step_notify = LambdaStep(
    name="NotifyOnOutcome",
    lambda_func=Lambda(
        function_arn="arn:aws:lambda:us-west-2:{{111122223333}}:function:notify-on-outcome"
    ),
    depends_on=[StepDependency(step_train, TriggerCondition.ANY)],
)
```

`TriggerCondition` supports the following values:
+ `COMPLETED` – The default. The step runs only if the upstream step succeeded.
+ `FAILED` – The step runs when the upstream step failed.
+ `STOPPED` – The step runs when the upstream step stopped.
+ `ANY` – The step runs on any terminal state of the upstream step, which is succeeded, failed, or stopped.

With multiple dependencies, every condition must be satisfied before the downstream step becomes eligible. When an execution is stopping, a step whose run condition is satisfied can still run.

**Pipeline execution status: CompletedWithFailures**

When a step fails but the pipeline runs to completion because a downstream step with a `FAILED` or `ANY` trigger handles the failure, the pipeline execution ends with the status `CompletedWithFailures`. Compare the terminal statuses as follows:
+ `Succeeded` – All steps completed and no step failed.
+ `CompletedWithFailures` – The DAG ran to completion, and at least one step failed but was handled by a downstream step.
+ `Failed` – A step failed and the DAG did not run to completion, so some steps were never evaluated.
+ `Stopped` – The execution was stopped before the DAG ran to completion.

This status appears in `DescribePipelineExecution`, in Amazon EventBridge pipeline execution status change events, and in the `ExecutionCompletedWithFailures` CloudWatch metric.

**Property references on failed or stopped steps**

When you reference a property that does not exist, such as the model artifacts of a training step that failed, the reference resolves to null and passes through. The platform does not intercept the null value:
+ For a job step, such as a training, processing, or endpoint step, a null value in a required field causes the underlying AWS API to return a validation error, and the step fails.
+ For a Lambda step, a null value in the payload is passed to your function code, which is responsible for handling it.

## Optional conditional arguments
<a name="build-and-manage-conditional-arguments"></a>

Optional conditional arguments let you choose a step argument's value, or leave the argument out, at run time based on pipeline parameters. You don't need a separate condition step and a copy of the step for each combination of values.

To set a conditional argument, use `If`, `ElseIf`, and `Omit`, available in the SageMaker Python SDK v3.30.0 or later. Pass an `If` anywhere a step builder accepts a pipeline parameter, including a list element or a map entry such as an environment variable or a hyperparameter. The following example sets an environment variable based on an environment parameter, and includes the `max_depth` hyperparameter only when a Boolean parameter is true.

```python
from sagemaker.core.workflow import ElseIf, If, Omit
from sagemaker.core.workflow.conditions import ConditionEquals
from sagemaker.core.workflow.parameters import ParameterBoolean, ParameterString
from sagemaker.mlops.workflow import TrainingStep
from sagemaker.train import ModelTrainer

env = ParameterString(name="Env", default_value="dev")
tune_depth = ParameterBoolean(name="TuneDepth", default_value=False)

stage = If(
    ConditionEquals(left=env, right="prod"),
    then="release",
    else_if=[ElseIf(ConditionEquals(left=env, right="beta"), then="preview")],
    else_="dev",
)

model_trainer = ModelTrainer(
    ...,
    hyperparameters={
        "num_round": "10",
        "max_depth": If(ConditionEquals(left=tune_depth, right=True), then="5", else_=Omit()),
    },
    environment={"STAGE": stage},
    sagemaker_session=pipeline_session,
)

step_train = TrainingStep(name="TrainModel", step_args=model_trainer.train())
```

At run time, Pipelines uses the `then` value if the condition is true. Otherwise, it uses the `then` value of the first `ElseIf` whose condition is true, or the `else_` value if none match. When the selected value is `Omit()`, the request leaves out the containing member, list element, or map entry, and keeps the parent member. Pipelines sends a literal empty list, empty dictionary, or empty string unchanged and doesn't treat it as absent.

An `If` takes the following arguments:


| Argument | Required | Value | 
| --- | --- | --- | 
| `condition` | Yes | Any condition that a condition step supports, such as `ConditionEquals`, `ConditionGreaterThan`, `ConditionIn`, `ConditionNot`, or `ConditionOr`. | 
| `then` | Yes | A value for the argument, a nested `If`, or `Omit()`. | 
| `else_if` | No | An ordered list of `ElseIf(condition, then)` entries. | 
| `else_` | Yes | Same as `then`. | 

A step that the condition or any branch references becomes a dependency of the step that uses the `If`. The following restrictions apply:
+ `Omit()` is valid only as a complete `then` or `else_` value, and `If` expressions can be nested at most two levels deep. The SDK checks both when it builds the pipeline definition.
+ `Omit()` cannot remove a required member or reduce a list or map below its required minimum length.
+ The following members do not support conditional arguments, grouped by step type:
  + Processing: `ProcessingOutputConfig`, `ProcessingOutputConfig.Outputs`, and `ProcessingOutputConfig.Outputs.OutputName`
  + AutoML: `AutoMLJobConfig` and `AutoMLJobConfig.Mode`
  + EMR: `ClusterConfig`, `ClusterConfig.Instances`, and `ExecutionRoleArn`
  + EMR Serverless: `ExecutionRoleArn`
  + Lineage: `Actions`, `Artifacts`, `Contexts`, and `Associations`
  + Cleanup: `Resources.S3`, `Resources.S3.StepName`, and `Resources.S3.S3Uris`

## Custom images in a step
<a name="build-and-manage-images"></a>

 You can use any of the available SageMaker AI [Deep Learning Container images](https://github.com/aws/deep-learning-containers/blob/master/available_images.md) when you create a step in your pipeline. 

You can also use your own container with pipeline steps. Because you can’t create an image from within Studio Classic, you must create your image using another method before using it with Pipelines.

To use your own container when creating the steps for your pipeline, include the image URI in the estimator definition. For more information on using your own container with SageMaker AI, see [Using Docker Containers with SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers.html).