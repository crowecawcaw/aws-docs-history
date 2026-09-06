

# Define Training Metrics
<a name="define-train-metrics"></a>

SageMaker AI automatically parses training job logs and sends training metrics to CloudWatch. By default, SageMaker AI sends system resource utilization metrics listed in [SageMaker AI Jobs and Endpoint Metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html#cloudwatch-metrics-jobs). If you want SageMaker AI to parse logs and send custom metrics from a training job of your own algorithm to CloudWatch, you need to specify metrics definitions by passing the name of metrics and regular expressions when you configure a SageMaker AI training job request.

You can specify the metrics that you want to track using the SageMaker AI console, the [SageMaker AI Python SDK](https://github.com/aws/sagemaker-python-sdk), or the low-level SageMaker AI API.

If you are using your own algorithm, do the following:
+ Make sure that the algorithm writes the metrics that you want to capture to logs.
+ Define a regular expression that accurately searches the logs to capture the values of the metrics that you want to send to CloudWatch.

For example, suppose your algorithm emits the following metrics for training error and validation error:

```
Train_error=0.138318;  Valid_error=0.324557;
```

If you want to monitor both of those metrics in CloudWatch, the dictionary for the metric definitions should look like the following example:

```
[
    {
        "Name": "train:error",
        "Regex": "Train_error=(.*?);"
    },
    {
        "Name": "validation:error",
        "Regex": "Valid_error=(.*?);"
    }    
]
```

In the regex for the `train:error` metric defined in the preceding example, the first part of the regex finds the exact text "Train\_error=", and the expression `(.*?);` captures any characters until the first semicolon character appears. In this expression, the parenthesis tell the regex to capture what is inside them, `.` means any character, `*` means zero or more, and `?` means capture only until the first instance of the `;` character.

## Define Metrics Using the SageMaker AI Python SDK
<a name="define-train-metrics-sdk"></a>

Define the metrics that you want to send to CloudWatch by specifying a list of metric definitions in the `AlgorithmSpecification` when you create a `TrainingJob` using `sagemaker-core`. For example, if you want to monitor both the `train:error` and `validation:error` metrics in CloudWatch, your `TrainingJob.create()` call would look like the following example:

```
from sagemaker.core.resources import TrainingJob
from sagemaker.core.shapes import (
    AlgorithmSpecification,
    MetricDefinition,
    ResourceConfig,
    OutputDataConfig,
    StoppingCondition,
)

TrainingJob.create(
    training_job_name="{{my-training-job}}",
    role_arn="{{arn:aws:iam::123456789012:role/SageMakerRole}}",
    algorithm_specification=AlgorithmSpecification(
        training_image="{{your-own-image-uri}}",
        training_input_mode="File",
        metric_definitions=[
            MetricDefinition(name="train:error", regex="Train_error=(.*?);"),
            MetricDefinition(name="validation:error", regex="Valid_error=(.*?);"),
        ],
    ),
    resource_config=ResourceConfig(
        instance_type="{{ml.c4.xlarge}}",
        instance_count={{1}},
        volume_size_in_gb={{30}},
    ),
    output_data_config=OutputDataConfig(s3_output_path="{{s3://bucket/output}}"),
    stopping_condition=StoppingCondition(max_runtime_in_seconds={{3600}}),
)
```

For more information about training by using [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable) ModelTrainers, see[ Sagemaker Python SDK](https://github.com/aws/sagemaker-python-sdk#sagemaker-python-sdk-overview) on GitHub. 

## Define Metrics Using the SageMaker AI Console
<a name="define-train-metrics-console"></a>

If you choose the **Your own algorithm container in ECR** option as your algorithm source in the SageMaker AI console when you create a training job, add the metric definitions in the **Metrics** section. The following screenshot shows how it should look after you add the example metric names and the corresponding regular expressions.

![Example Algorithm options form in the console.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/training-metrics-using-smconsole.png)


## Define Metrics Using the Low-level SageMaker AI API
<a name="define-train-metrics-api"></a>

Define the metrics that you want to send to CloudWatch by specifying a list of metric names and regular expressions in the `MetricDefinitions` field of the [`AlgorithmSpecification`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html) input parameter that you pass to the [`CreateTrainingJob`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) operation. For example, if you want to monitor both the `train:error` and `validation:error` metrics in CloudWatch, your `AlgorithmSpecification` would look like the following example:

```
"AlgorithmSpecification": {
    "TrainingImage": {{your-own-image-uri}},
    "TrainingInputMode": "File",
    "MetricDefinitions" : [
        {
            "Name": "train:error",
            "Regex": "Train_error=(.*?);"
        },
        {
            "Name": "validation:error",
            "Regex": "Valid_error=(.*?);"
        }
    ]
}
```

For more information about defining and running a training job by using the low-level SageMaker AI API, see [`CreateTrainingJob`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html).