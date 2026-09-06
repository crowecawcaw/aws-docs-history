

# Define Hyperparameter Ranges
<a name="automatic-model-tuning-define-ranges"></a>

This guide shows how to use SageMaker APIs to define hyperparameter ranges. It also provides a list of hyperparameter scaling types that you can use.

Choosing hyperparameters and ranges significantly affects the performance of your tuning job. Hyperparameter tuning finds the best hyperparameter values for your model by searching over a [range](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-HyperParameterRanges) of values that you specify for each tunable hyperparameter. You can also specify up to 100 [static hyperparameters](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-StaticHyperParameters) that do not change over the course of the tuning job. You can use up to 100 hyperparameters in total (static \+ tunable). For guidance on choosing hyperparameters and ranges, see [Best Practices for Hyperparameter Tuning](automatic-model-tuning-considerations.md). You can also use autotune to find optimal tuning job settings. For more information, see the following **Autotune** section.

**Note**  
SageMaker AI Automatic Model Tuning (AMT) may add additional hyperparameters(s) that contribute to the limit of 100 total hyperparameters. Currently, to pass your objective metric to the tuning job for use during training, SageMaker AI adds `_tuning_objective_metric` automatically.

## Static hyperparameters
<a name="automatic-model-tuning-define-ranges-static"></a>

Use static hyperparameters for the following cases:    If you have background knowledge that guides you to select a constant value.   If you don't want to explore a value range for the hyperparameters.   For example, you can use AMT to tune your model using `param1` (a tunable parameter) and `param2` (a static parameter). If you do, then use a search space for `param1` that lies between two values, and pass `param2` as a static hyperparameter, as follows.

```
param1: ["range_min","range_max"]
param2: "static_value"
```

Static hyperparameters have the following structure:

```
"StaticHyperParameters": {
    "objective" : "reg:squarederror",
    "dropout_rate": "0.3"
}
```

You can use the Amazon SageMaker API to specify key value pairs in the [StaticHyperParameters](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-StaticHyperParameters) field of the `HyperParameterTrainingJobDefinition` parameter that you pass to the [CreateHyperParameterTuningJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHyperParameterTuningJob.html) operation.

## Dynamic hyperparameters
<a name="automatic-model-tuning-define-ranges-dynamic"></a>

You can use the SageMaker API to define [hyperparameter ranges](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-HyperParameterRanges). Specify the names of hyperparameters and ranges of values in the `ParameterRanges` field of the `HyperParameterTuningJobConfig` parameter that you pass to the [`CreateHyperParameterTuningJob`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHyperParameterTuningJob.html) operation. 

The `ParameterRanges` field has three subfields: categorical, integer, and continuous. You can define up to 30 total (categorical \+ integer \+ continuous) tunable hyperparameters to search over. 

**Note**  
Each categorical hyperparameter can have at most 30 different values.

Dynamic hyperparameters have the following structure:

```
"ParameterRanges": {
    "CategoricalParameterRanges": [
        {
            "Name": "tree_method",
            "Values": ["auto", "exact", "approx", "hist"]
        }
    ],
    "ContinuousParameterRanges": [
        {
            "Name": "eta",
            "MaxValue" : "0.5",
            "MinValue": "0",
            "ScalingType": "Auto"
        }
    ],
    "IntegerParameterRanges": [
        {
            "Name": "max_depth",
            "MaxValue": "10",
            "MinValue": "1",
            "ScalingType": "Auto"
        }
    ]
}
```

If you create a tuning job with a `Grid` strategy, you can only specify categorical values. You don't need to provide the `MaxNumberofTrainingJobs`. This value is inferred from the total number of configurations that can be produced from your categorical parameters. If specified, the value of `MaxNumberOfTrainingJobs` should be equal to the total number of distinct categorical combinations possible.

## Autotune
<a name="automatic-model-tuning-define-ranges-autotune"></a>

To save time and resources searching for hyperparameter ranges, resources or objective metrics, autotune can automatically guess optimal values for some hyperparameter fields. Use autotune to find optimal values for the following fields:
+ **[ParameterRanges](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html#sagemaker-Type-HyperParameterTuningJobConfig-ParameterRanges)** – The names and ranges of hyperparameters that a tuning job can optimize.
+ **[ResourceLimits](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceLimits.html) ** – The maximum resources to be used in a tuning job. These resources can include the maximum number of training jobs, maximum runtime of a tuning job, and the maximum number of training jobs that can be run at the same time.
+ **[TrainingJobEarlyStoppingType](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html#sagemaker-Type-HyperParameterTuningJobConfig-TrainingJobEarlyStoppingType)** – A flag that stops a training job if a job is not significantly improving against an objective metric. Defaults to enabled. For more information, see [Stop Training Jobs Early](automatic-model-tuning-early-stopping.md).
+ **[RetryStrategy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTrainingJobDefinition.html#sagemaker-Type-HyperParameterTrainingJobDefinition-RetryStrategy)** – The number of times to retry a training job. Non-zero values for `RetryStrategy` can increase the likelihood that your job will complete successfully.
+ **[Strategy](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobConfig.html#sagemaker-Type-HyperParameterTuningJobConfig-Strategy)** – Specifies how hyperparameter tuning chooses the combinations of hyperparameter values to use for the training job that it launches.
+ **[ConvergenceDetected](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ConvergenceDetected.html)** – A flag to indicate that Automatic Model Tuning (AMT) has detected model convergence.

To use autotune, do the following:

1. Specify the hyperparameter and an example value in the `AutoParameters` field of the [ParameterRanges](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ParameterRanges.html) API.

1. Enable autotune.

AMT will determine if your hyperparameters and example values are eligible for autotune. Hyperparameters that can be used in autotune are automatically assigned to the appropriate parameter range type. Then, AMT uses `ValueHint` to select an optimal range for you. You can use the `DescribeHyperParameterTrainingJob` API to view these ranges.

The following example shows you how to configure a tuning job that uses autotune. In the configuration example, the hyperparameter `max_depth` has `ValueHint` containing an example value of `4`.

```
config = {
    'Autotune': {'Mode': 'Enabled'},
    'HyperParameterTuningJobName':'my-autotune-job',
    'HyperParameterTuningJobConfig': {
        'HyperParameterTuningJobObjective': {'Type': 'Minimize', 'MetricName': 'validation:rmse'},
        'ResourceLimits': {'MaxNumberOfTrainingJobs': 5, 'MaxParallelTrainingJobs': 1},
        'ParameterRanges': {       
            'AutoParameters': [
                {'Name': 'max_depth', 'ValueHint': '4'}
            ]
        }
    },
    'TrainingJobDefinition': {
    .... }
```

Continuing the previous example, a tuning job is created after the previous configuration is included in a call to the `CreateHyperParameterTuningJob` API. Then, autotune converts the max\_depth hyperparameter in AutoParameters to the hyperparameter `IntegerParameterRanges`. The following response from a `DescribeHyperParameterTrainingJob` API shows that the optimal `IntegerParameterRanges` for `max_depth` are between `2` and `8`.

```
{
    'HyperParameterTuningJobName':'my_job',
    'HyperParameterTuningJobConfig': {
        'ParameterRanges': {
            'IntegerParameterRanges': [
                {'Name': 'max_depth', 'MinValue': '2', 'MaxValue': '8'},
            ],
        }
    },
    'TrainingJobDefinition': {
        ...
    },
    'Autotune': {'Mode': 'Enabled'}
    
}
```

## Hyperparameter scaling types
<a name="scaling-type"></a>

For integer and continuous hyperparameter ranges, you can choose the scale that you want hyperparameter tuning to use. For example, to search the range of values, you can specify a value for the `ScalingType` field of the hyperparameter range. You can choose from the following hyperparameter scaling types:

Auto  
SageMaker AI hyperparameter tuning chooses the best scale for the hyperparameter.

Linear  
Hyperparameter tuning searches the values in the hyperparameter range by using a linear scale. Typically, you choose this if the range of all values from the lowest to the highest is relatively small (within one order of magnitude). Uniformly searching values from the range provides a reasonable exploration of the entire range.

Logarithmic  
Hyperparameter tuning searches the values in the hyperparameter range by using a logarithmic scale.  
Logarithmic scaling works only for ranges that have values greater than 0.  
Choose logarithmic scaling when you're searching a range that spans several orders of magnitude.   
For example, if you're tuning a [Tune a linear learner model](linear-learner.md) model, and you specify a range of values between .0001 and 1.0 for the `learning_rate` hyperparameter, consider the following: Searching uniformly on a logarithmic scale gives you a better sample of the entire range than searching on a linear scale would. This is because searching on a linear scale would, on average, devote 90 percent of your training budget to only the values between .1 and 1.0. As a result, that leaves only 10 percent of your training budget for the values between .0001 and .1.

`ReverseLogarithmic`  
Hyperparameter tuning searches the values in the hyperparameter range by using a reverse logarithmic scale. Reverse logarithmic scaling is supported only for continuous hyperparameter ranges. It is not supported for integer hyperparameter ranges.  
Choose reverse logarithmic scaling when you are searching a range that is highly sensitive to small changes that are very close to 1.  
Reverse logarithmic scaling works only for ranges that are entirely within the range 0<=x<1.0.

For an example notebook that uses hyperparameter scaling, see these [Amazon SageMaker AI hyperparameter examples on GitHub](https://github.com/awslabs/amazon-sagemaker-examples/blob/master/hyperparameter_tuning).