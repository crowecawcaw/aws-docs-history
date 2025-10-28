# Pipelines steps

Pipelines are composed of steps. These steps define the actions that the pipeline takes and the
relationships between steps using properties. The following page describes the types of steps,
their properties, and the relationships between them.

###### Topics

- [Add a step](build-and-manage-steps-types.md "build-and-manage-steps-types.md")
- [Step properties](#build-and-manage-properties "#build-and-manage-properties")
- [Step parallelism](#build-and-manage-parallelism "#build-and-manage-parallelism")
- [Data dependency between steps](#build-and-manage-data-dependency "#build-and-manage-data-dependency")
- [Custom dependency between steps](#build-and-manage-custom-dependency "#build-and-manage-custom-dependency")
- [Custom images in a step](#build-and-manage-images "#build-and-manage-images")

## Step properties

Use the `properties` attribute to add data dependencies between steps in the
pipeline. Pipelines use these data dependencies to construct the DAG from the pipeline definition.
These properties can be referenced as placeholder values and are resolved at runtime.

The `properties` attribute of a Pipelines step matches the object returned by a
`Describe` call for the corresponding SageMaker AI job type. For each job type, the
`Describe` call returns the following response object:

- `ProcessingStep` – [DescribeProcessingJob](../APIReference/API_DescribeProcessingJob.md "../APIReference/API_DescribeProcessingJob.md")
- `TrainingStep` – [DescribeTrainingJob](../APIReference/API_DescribeTrainingJob.md "../APIReference/API_DescribeTrainingJob.md")
- `TransformStep` – [DescribeTransformJob](../APIReference/API_DescribeTransformJob.md "../APIReference/API_DescribeTransformJob.md")

To check which properties are referrable for each step type during data dependency
creation, see _[Data Dependency - Property Reference](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#data-dependency-property-reference "https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#data-dependency-property-reference")_ in the
[Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable").

## Step parallelism

When a step does not depend on any other step, it runs immediately upon pipeline
execution. However, executing too many pipeline steps in parallel can quickly exhaust
available resources. Control the number of concurrent steps for a pipeline execution with
`ParallelismConfiguration`.

The following example uses `ParallelismConfiguration` to set the concurrent
step limit to five.

```
pipeline.create(
    parallelism_config=ParallelismConfiguration(5),
)
```

## Data dependency between steps

You define the structure of your DAG by specifying the data relationships between steps.
To create data dependencies between steps, pass the properties of one step as the input to
another step in the pipeline. The step receiving the input isn't started until after the step
providing the input finishes running.

A data dependency uses JsonPath notation in the following format. This format traverses
the JSON property file. This means you can append as many
`<property>` instances as needed to reach the desired nested
property in the file. For more information on JsonPath notation, see the [JsonPath repo](https://github.com/json-path/JsonPath "https://github.com/json-path/JsonPath").

```
`<step_name>`.properties.`<property>`.`<property>`
```

The following shows how to specify an Amazon S3 bucket using the
`ProcessingOutputConfig` property of a processing step.

```
step_process.properties.ProcessingOutputConfig.Outputs["train_data"].S3Output.S3Uri
```

To create the data dependency, pass the bucket to a training step as follows.

```
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

To check which properties are referrable for each step type during data dependency
creation, see _[Data Dependency - Property Reference](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#data-dependency-property-reference "https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#data-dependency-property-reference")_ in the
[Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable "https://sagemaker.readthedocs.io/en/stable").

## Custom dependency between steps

When you specify a data dependency, Pipelines provides the data connection between the steps.
Alternatively, one step can access the data from a previous step without directly using Pipelines.
In this case, you can create a custom dependency that tells Pipelines not to start a step until
after another step has finished running. You create a custom dependency by specifying a step's
`DependsOn` attribute.

As an example, the following defines a step `C` that starts only after both
step `A` and step `B` finish running.

```
{
  'Steps': [
    {'Name':'A', ...},
    {'Name':'B', ...},
    {'Name':'C', 'DependsOn': ['A', 'B']}
  ]
}
```

Pipelines throws a validation exception if the dependency would create a cyclic
dependency.

The following example creates a training step that starts after a processing step finishes
running.

```
processing_step = ProcessingStep(...)
training_step = TrainingStep(...)

training_step.add_depends_on([processing_step])
```

The following example creates a training step that doesn't start until two different
processing steps finish running.

```
processing_step_1 = ProcessingStep(...)
processing_step_2 = ProcessingStep(...)

training_step = TrainingStep(...)

training_step.add_depends_on([processing_step_1, processing_step_2])
```

The following provides an alternate way to create the custom dependency.

```
training_step.add_depends_on([processing_step_1])
training_step.add_depends_on([processing_step_2])
```

The following example creates a training step that receives input from one processing step
and waits for a different processing step to finish running.

```
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

The following example shows how to retrieve a string list of the custom dependencies of a
step.

```
custom_dependencies = training_step.depends_on
```

## Custom images in a step

You can use any of the available SageMaker AI [Deep
Learning Container images](https://github.com/aws/deep-learning-containers/blob/master/available_images.md "https://github.com/aws/deep-learning-containers/blob/master/available_images.md") when you create a step in your pipeline.

You can also use your own container with pipeline steps. Because you can’t create an image
from within Studio Classic, you must create your image using another method before using it with
Pipelines.

To use your own container when creating the steps for your pipeline, include the image URI
in the estimator definition. For more information on using your own container with SageMaker AI,
see [Using Docker Containers with SageMaker AI](docker-containers.md "docker-containers.md").
