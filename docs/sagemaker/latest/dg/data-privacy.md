# Data Privacy in Amazon SageMaker AI

Amazon SageMaker AI collects aggregate information about the use of AWS-owned and open source
libraries used during training. SageMaker AI uses this aggregate metadata to improve services and
customer experience.

The following sections provide explanations for the type of metadata that SageMaker AI collects
and how to opt out of metadata collection.

## Types of information collected

**Usage Information**

Metadata from AWS-owned and open source libraries that are used with
SageMaker training, such as those used for distributed training, compilation, and
quantization.

**Errors**

Errors from unexpected behavior including failures, crashes, cascades, and
failures that result from interacting with the SageMaker training
platform.

## How to opt out of metadata collection

You can opt out of sharing aggregated metadata with SageMaker training when creating a
training job using the `CreateTrainingJob` API. If you are using the console
to create training jobs, metadata collection is disabled by default.

###### Important

You must choose to opt out of metadata collection for each training job that you
submit. You must also choose to opt out in an API call as shown in the following
examples. You cannot choose to opt out inside a training script.

The following section shows how you can opt out of metadata collection using the
AWS CLI, AWS SDK for Python (Boto3), or the SageMaker Python SDK.

### Opt out of metadata collection using the

AWS Command Line Interface (AWS CLI)

To opt out of metadata collection using the AWS CLI, set the environment variable
`OPT_OUT_TRACKING` to `1` in the
`create-training-job` API as shown in the following code
example.

```
aws sagemaker create-training-job \
--training-job-name `your_job_name` \
--algorithm-specification AlgorithmName=`your_algorithm_name`\
--output-data-config S3OutputPath=`s3://bucket-name/key-name-prefix` \
--resource-config InstanceType=`ml.c5.xlarge`, InstanceCount=`1` \
--stopping-condition MaxRuntimeInSeconds=`100` \
--environment OPT_OUT_TRACKING=1
```

### Opt out of metadata collection using

the AWS SDK for Python (Boto3)

To opt out of metadata collection using the SDK for Python (Boto3), set the environment
variable `OPT_OUT_TRACKING` to `1` in the
`create_training_job` API as shown in the following code
example.

```
boto3.client('sagemaker').create_training_job(
    TrainingJobName='`your_training_job`',
    AlgorithmSpecification={
        'AlgorithmName': '`your_algorithm_name`',
        'TrainingInputMode': 'File',
    },
    RoleArn='`your_arn`',
    OutputDataConfig={
        'S3OutputPath': 's3:`//bucket-name/key-name-prefix`',
    },
    ResourceConfig={
        'InstanceType': '`ml.m4.xlarge`',
        'InstanceCount': `1`,
        'VolumeSizeInGB': `123`,
    },
    StoppingCondition={
        'MaxRuntimeInSeconds': `123`,
    },
    Environment={
        'OPT_OUT_TRACKING': '1'
    },
)
```

### Opt out of metadata collection using the

SageMaker Python SDK

To opt out of metadata collection using the SageMaker Python SDK, set the environment
variable `OPT_OUT_TRACKING` to `1` inside a SageMaker AI estimator as
shown in the following code example.

```
sagemaker.estimator(
    image_uri='`path_to_container`',
    role='`rolearn`',
    instance_count=`1`,
    instance_type='`ml.c5.xlarge`',
    environment={
        'OPT_OUT_TRACKING': '1'
    },
)
```

### Opt out of metadata collection

account-wide

If you want to opt-out of metadata collection for several accounts, you can set an
environment variable to opt-out of tracking account-wide. You must use the SageMaker AI
Python SDK to opt out of metadata collection at an account level.

The following code example shows how opt out of tracking account-wide.

```
SchemaVersion: '1.0'
SageMaker:
  TrainingJob:
    Environment:
      'OPT_OUT_TRACKING': '1'
```

For more information about how to opt out of tracking account-wide, see [Configuring
and using defaults with the SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/overview.html#id22 "https://sagemaker.readthedocs.io/en/stable/overview.html#id22").

## Additional information

**If your downstream service depends on SageMaker AI
training**

If you operate a service that relies on SageMaker training, it is highly recommended that
you inform your customer about aggregate metadata collection in the SageMaker Training
platform and present them with the choice to opt out. Alternatively, you can opt out of
metadata collection on behalf of your customer.

**If you are a client or a customer of a service that uses SageMaker AI
training**

If you are a client or customer of a service that uses SageMaker training, use your
preferred method in the previous section to opt out of metadata collection.
