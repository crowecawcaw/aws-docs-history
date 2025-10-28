# Create a pipeline

with `@step`-decorated functions

You can create a pipeline by converting Python functions into pipeline steps
using the `@step` decorator, creating dependencies between those functions
to create a pipeline graph (or directed acyclic graph (DAG)), and passing the leaf
nodes of that graph as a list of steps to the pipeline. The following sections
explain this procedure in detail with examples.

###### Topics

- [Convert a function to a step](#pipelines-step-decorator-run-pipeline-convert "#pipelines-step-decorator-run-pipeline-convert")
- [Create dependencies between the steps](#pipelines-step-decorator-run-pipeline-link "#pipelines-step-decorator-run-pipeline-link")
- [Use ConditionStep with @step-decorated steps](#pipelines-step-decorator-condition "#pipelines-step-decorator-condition")
- [Define a pipeline using the DelayedReturn output of steps](#pipelines-step-define-delayed "#pipelines-step-define-delayed")
- [Create a pipeline](#pipelines-step-decorator-pipeline-create "#pipelines-step-decorator-pipeline-create")

## Convert a function to a step

To create a step using the `@step` decorator, annotate the function with `@step`.
The following example shows a `@step`-decorated function that preprocesses the data.

```
from sagemaker.workflow.function_step import step

@step
def preprocess(raw_data):
    df = pandas.read_csv(raw_data)
    ...
    return procesed_dataframe

step_process_result = preprocess(raw_data)
```

When you invoke a `@step`-decorated function,
SageMaker AI returns a `DelayedReturn` instance instead of running the function.
A `DelayedReturn` instance is a proxy for the actual return of that function. The `DelayedReturn`
instance can be passed to another function as an argument or directly to a pipeline
instance as a step. For information about the `DelayedReturn` class, see
[sagemaker.workflow.function_step.DelayedReturn](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.function_step.DelayedReturn "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.function_step.DelayedReturn").

## Create dependencies between the steps

When you create a dependency between two steps, you create a connection between the steps in your
pipeline graph. The following sections introduce multiple ways you can create a dependency between
your pipeline steps.

### Data dependencies through input arguments

Passing in the
`DelayedReturn` output of one function as an input to another function automatically
creates a data dependency in the pipeline DAG. In the following example, passing
in the `DelayedReturn` output of the `preprocess` function
to the `train` function creates
a dependency between `preprocess` and `train`.

```
from sagemaker.workflow.function_step import step

@step
def preprocess(raw_data):
    df = pandas.read_csv(raw_data)
    ...
    return procesed_dataframe

@step
def train(training_data):
    ...
    return trained_model

step_process_result = preprocess(raw_data)
step_train_result = train(step_process_result)

```

The previous example defines a training function which is
decorated with `@step`. When this function is invoked, it receives
the `DelayedReturn` output of the preprocessing pipeline step as input.
Invoking the training function returns another `DelayedReturn` instance. This instance
holds the information about all the previous steps defined in that function
(i.e, the `preprocess` step in this example) which form the pipeline DAG.

In the previous example, the `preprocess` function returns a single value. For more
complex return types like lists or tuples, refer to [Limitations](pipelines-step-decorator-limit.md "pipelines-step-decorator-limit.md").

### Define custom dependencies

In the previous example, the `train` function
received the `DelayedReturn` output of `preprocess` and created a dependency.
If you want to define the dependency explicitly without passing the previous
step output, use the `add_depends_on` function with the step.
You can use the `get_step()`
function to retrieve the underlying step from its `DelayedReturn` instance,
and then call `add_depends_on`\_on with the dependency as input. To view the
`get_step()` function definition, see [sagemaker.workflow.step_outputs.get_step](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.step_outputs.get_step "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.step_outputs.get_step").
The following example
shows you how to create a dependency between `preprocess` and `train`
using `get_step()` and `add_depends_on()`.

```
from sagemaker.workflow.step_outputs import get_step

@step
def preprocess(raw_data):
    df = pandas.read_csv(raw_data)
    ...
    processed_data = ..
    return s3.upload(processed_data)

@step
def train():
    training_data = s3.download(....)
    ...
    return trained_model

step_process_result = preprocess(raw_data)
step_train_result = train()

get_step(step_train_result).add_depends_on([step_process_result])

```

### Pass data to and from a `@step`-decorated function

to a traditional pipeline step

You can
create a pipeline that includes a `@step`-decorated step and a
traditional pipeline step and passes data between them. For
example, you can use `ProcessingStep` to process the data and pass its result
to the `@step`-decorated training function. In the following example,
a `@step`-decorated training step references the output of a processing step.

```
# Define processing step

from sagemaker.sklearn.processing import SKLearnProcessor
from sagemaker.processing import ProcessingInput, ProcessingOutput
from sagemaker.workflow.steps import ProcessingStep

sklearn_processor = SKLearnProcessor(
    framework_version='1.2-1',
    role='arn:aws:iam::123456789012:role/SagemakerExecutionRole',
    instance_type='ml.m5.large',
    instance_count='1',
)

inputs = [
    ProcessingInput(source=`input_data`, destination="/opt/ml/processing/input"),
]
outputs = [
    ProcessingOutput(output_name="train", source="/opt/ml/processing/train"),
    ProcessingOutput(output_name="validation", source="/opt/ml/processing/validation"),
    ProcessingOutput(output_name="test", source="/opt/ml/processing/test")
]

process_step = ProcessingStep(
    name="MyProcessStep",
    step_args=sklearn_processor.run(inputs=inputs, outputs=outputs,code='preprocessing.py'),
)
```

```
# Define a `@step`-decorated train step which references the
# output of a processing step

@step
def train(train_data_path, test_data_path):
    ...
    return trained_model

step_train_result = train(
   process_step.properties.ProcessingOutputConfig.Outputs["train"].S3Output.S3Uri,
   process_step.properties.ProcessingOutputConfig.Outputs["test"].S3Output.S3Uri,
)
```

## Use `ConditionStep` with `@step`-decorated steps

Pipelines supports a `ConditionStep` class which evaluates the results of preceding steps
to decide what action to take in the pipeline. You can use `ConditionStep` with a
`@step`-decorated step as well. To use the output of any `@step`-decorated
step with `ConditionStep`,
enter the output of that step as an argument to `ConditionStep`. In the following
example, the condition step receives the output of the `@step`-decorated model evaluation step.

```
# Define steps

@step(name="evaluate")
def evaluate_model():
    # code to evaluate the model
    return {
        "rmse":rmse_value
    }

@step(name="register")
def register_model():
    # code to register the model
    ...
```

```
# Define ConditionStep

from sagemaker.workflow.condition_step import ConditionStep
from sagemaker.workflow.conditions import ConditionGreaterThanOrEqualTo
from sagemaker.workflow.fail_step import FailStep

conditionally_register = ConditionStep(
    name="conditional_register",
    conditions=[
        ConditionGreaterThanOrEqualTo(
            # Output of the evaluate step must be json serializable
            left=evaluate_model()["rmse"],  #
            right=5,
        )
    ],
    if_steps=[FailStep(name="Fail", error_message="Model performance is not good enough")],
    else_steps=[register_model()],
)
```

## Define a pipeline using the `DelayedReturn` output of steps

You define a pipeline the same way whether or not you use a `@step` decorator.
When you pass a `DelayedReturn` instance
to your pipeline, you don't need to pass a full list of steps to
build the pipeline. The SDK automatically infers the previous steps based on the dependencies
you define. All the previous steps of the `Step` objects you passed to the pipeline or
`DelayedReturn` objects are included in the pipeline graph. In the following example, the
pipeline receives the `DelayedReturn` object for the `train` function.
SageMaker AI adds the `preprocess` step, as a previous step of `train`, to the pipeline
graph.

```
from sagemaker.workflow.pipeline import Pipeline

pipeline = Pipeline(
    name="`<pipeline-name>`",
    steps=[step_train_result],
    sagemaker_session=`<sagemaker-session>`,
)
```

If there are no data or custom dependencies between the steps and you run multiple
steps in parallel, the pipeline graph has more than one leaf node. Pass all of these
leaf nodes in a list to the `steps` argument in your pipeline definition, as shown in the
following example:

```
@step
def process1():
    ...
    return data

@step
def process2():
   ...
   return data

step_process1_result = process1()
step_process2_result = process2()

pipeline = Pipeline(
    name="`<pipeline-name>`",
    steps=[step_process1_result, step_process2_result],
    sagemaker_session=`sagemaker-session`,
)
```

When the pipeline runs, both steps run in parallel.

You only pass the leaf nodes of the graph to the pipeline because the leaf nodes contain
information about all the previous steps defined through data or custom dependencies. When it
compiles the pipeline, SageMaker AI also infers of all of the subsequent steps that form
the pipeline graph and adds each of them as a separate step to the pipeline.

## Create a pipeline

Create a pipeline by calling `pipeline.create()`, as shown in the following
snippet. For details about `create()`, see [sagemaker.workflow.pipeline.Pipeline.create](https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.pipeline.Pipeline.create "https://sagemaker.readthedocs.io/en/stable/workflows/pipelines/sagemaker.workflow.pipelines.html#sagemaker.workflow.pipeline.Pipeline.create").

```
role = "`pipeline-role`"
pipeline.create(role)
```

When you call `pipeline.create()`, SageMaker AI compiles all of the steps
defined as part of the pipeline instance. SageMaker AI uploads the serialized function, arguments,
and all the other step-related artifacts to Amazon S3.

Data resides in the S3 bucket according to the following structure:

```
s3_root_uri/
    `pipeline_name`/
        sm_rf_user_ws/
            workspace.zip  # archive of the current working directory (workdir)
        `step_name`/
            `timestamp`/
                arguments/                # serialized function arguments
                function/                 # serialized function
                pre_train_dependencies/   # any dependencies and pre_execution scripts provided for the step
        `execution_id`/
            `step_name`/
                results     # returned output from the serialized function including the model
```

`s3_root_uri` is defined in the SageMaker AI config file and applies to the entire pipeline.
If undefined, the default SageMaker AI bucket is used.

###### Note

Every time SageMaker AI compiles a pipeline, SageMaker AI saves the the steps' serialized functions,
arguments and dependencies in a folder timestamped with the current time. This occurs every time you run
`pipeline.create()`, `pipeline.update()`, `pipeline.upsert()` or
`pipeline.definition()`.
