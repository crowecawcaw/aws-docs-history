# Use SageMaker AI managed warm pools

You can use SageMaker AI managed warm pools through the SageMaker Python SDK, the Amazon SageMaker AI console,
or through the low-level APIs. Administrators can optionally use the
`sagemaker:KeepAlivePeriod` condition key to further restrict the
`KeepAlivePeriodInSeconds` limits for certain users or groups.

###### Topics

- [Using the SageMaker AI Python
  SDK](#train-warm-pools-how-to-use-python-sdk "#train-warm-pools-how-to-use-python-sdk")
- [Using the Amazon SageMaker AI
  console](#train-warm-pools-how-to-use-sagemaker-console "#train-warm-pools-how-to-use-sagemaker-console")
- [Using the low-level
  SageMaker APIs](#train-warm-pools-how-to-use-low-level-apis "#train-warm-pools-how-to-use-low-level-apis")
- [IAM condition
  key](#train-warm-pools-how-to-use-iam-condition-key "#train-warm-pools-how-to-use-iam-condition-key")

## Using the SageMaker AI Python

SDK

Create, update, or terminate warm pools using the SageMaker Python SDK.

###### Note

This feature is available in the SageMaker AI [Python SDK
v2.110.0](https://pypi.org/project/sagemaker/2.110.0/ "https://pypi.org/project/sagemaker/2.110.0/") and later.

###### Topics

- [Create a warm
  pool](#train-warm-pools-how-to-use-python-sdk-create "#train-warm-pools-how-to-use-python-sdk-create")
- [Update a warm
  pool](#train-warm-pools-how-to-use-python-sdk-update "#train-warm-pools-how-to-use-python-sdk-update")
- [Terminate a
  warm pool](#train-warm-pools-how-to-use-python-sdk-terminate "#train-warm-pools-how-to-use-python-sdk-terminate")

### Create a warm

pool

To create a warm pool, use the SageMaker Python SDK to create an estimator with a
`keep_alive_period_in_seconds` value greater than 0 and call
`fit()`. When the training job completes, a warm pool is
retained. For more information on training scripts and estimators, see [Train a Model with the SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/overview.html#train-a-model-with-the-sagemaker-python-sdk "https://sagemaker.readthedocs.io/en/stable/overview.html#train-a-model-with-the-sagemaker-python-sdk"). If your script does not
create a warm pool, see [Warm pool creation](train-warm-pools.md#train-warm-pools-creation "train-warm-pools.md#train-warm-pools-creation") for possible
explanations.

```
import sagemaker
from sagemaker import get_execution_role
from sagemaker.tensorflow import TensorFlow

# Creates a SageMaker AI session and gets execution role
session = sagemaker.Session()
role = get_execution_role()

# Creates an example estimator
estimator = TensorFlow(
    ...
    entry_point=`'my-training-script.py'`,
    source_dir=`'code'`,
    role=`role`,
    model_dir=`'model_dir'`,
    framework_version=`'2.2'`,
    py_version=`'py37'`,
    job_name=`'my-training-job-1'`,
    instance_type=`'ml.g4dn.xlarge'`,
    instance_count=`1`,
    volume_size=`250`,
    hyperparameters={
        "batch-size": `512`,
        "epochs": `1`,
        "learning-rate": `1e-3`,
        "beta_1": `0.9`,
        "beta_2": `0.999`,
    },
    keep_alive_period_in_seconds=`1800`,
)

# Starts a SageMaker training job and waits until completion
estimator.fit(`'s3://my_bucket/my_training_data/'`)
```

Next, create a second matching training job. In this example, we create
`my-training-job-2`, which has all of the necessary attributes to
match with `my-training-job-1`, but has a different hyperparameter
for experimentation. The second training job reuses the warm pool and starts up
faster than the first training job. The following code example uses a Tensorflow
estimator. The warm pool feature can be used with any training algorithm that
runs on Amazon SageMaker AI. For more information on which attributes need to match, see
[Matching training jobs](train-warm-pools.md#train-warm-pools-matching-criteria "train-warm-pools.md#train-warm-pools-matching-criteria").

```
# Creates an example estimator
estimator = TensorFlow(
    ...
    entry_point=`'my-training-script.py'`,
    source_dir=`'code'`,
    role=`role`,
    model_dir=`'model_dir'`,
    framework_version=`'py37'`,
    py_version=`'pyxy'`,
    job_name=`'my-training-job-2'`,
    instance_type=`'ml.g4dn.xlarge'`,
    instance_count=`1`,
    volume_size=`250`,
    hyperparameters={
        "batch-size": `512`,
        "epochs": `2`,
        "learning-rate": `1e-3`,
        "beta_1": `0.9`,
        "beta_2": `0.999`,
    },
    keep_alive_period_in_seconds=`1800`,
)

# Starts a SageMaker training job and waits until completion
estimator.fit(`'s3://my_bucket/my_training_data/'`)
```

Check the warm pool status of both training jobs to confirm that the warm pool
is `Reused` for `my-training-job-1` and `InUse`
for `my-training-job-2`.

###### Note

Training job names have date/time suffixes. The example training job names
`my-training-job-1` and `my-training-job-2` should
be replaced with actual training job names. You can use the
`estimator.latest_training_job.job_name` command to fetch the
actual training job name.

```
session.describe_training_job(`'my-training-job-1'`)
session.describe_training_job(`'my-training-job-2'`)
```

The result of `describe_training_job` provides all details about a
given training job. Find the `WarmPoolStatus` attribute to check
information about a training job’s warm pool. Your output should look similar to
the following example:

```
# Warm pool status for training-job-1
...
'WarmPoolStatus': {'Status': 'Reused',
  'ResourceRetainedBillableTimeInSeconds': 1000,
  'ReusedByName': my-training-job-2}
...

# Warm pool status for training-job-2
...
'WarmPoolStatus': {'Status': 'InUse'}
...
```

### Update a warm

pool

When the training job is complete and the warm pool status is
`Available`, then you can update the
`KeepAlivePeriodInSeconds` value.

```
session.update_training_job(job_name, resource_config={"KeepAlivePeriodInSeconds":`3600`})
```

### Terminate a

warm pool

To manually terminate a warm pool, set the `KeepAlivePeriodInSeconds` value to 0.

```
session.update_training_job(job_name, resource_config={"KeepAlivePeriodInSeconds":0})
```

The warm pool automatically terminates when it exceeds the designated
`KeepAlivePeriodInSeconds` value or if there is a patch update
for the cluster.

## Using the Amazon SageMaker AI

console

Through the console, you can create a warm pool, release a warm pool, or check the
warm pool status and billable time of specific training jobs. You can also see which
matching training job reused a warm pool.

1. Open the [Amazon SageMaker AI console](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/") and
   choose **Training jobs** from the navigation pane. If
   applicable, the warm pool status of each training job is visible in the
   **Warm pool status** column and the time left for an
   active warm pool is visible in the **Time left**
   column.
2. To create a training job that uses a warm pool from the console, choose
   **Create training job**. Then, be sure to specify a
   value for the **Keep alive period** field when configuring
   your training job resources. This value must be an integer between 1 and
   3600, which represents duration of time in seconds.
3. To release a warm pool from the console, select a specific training job
   and choose **Release cluster** from the **Actions** dropdown menu.
4. To see more information about a warm pool, choose a training job name. In
   the job details page, scroll down to the **Warm pool
   status** section to find the warm pool status, the time left if
   the warm pool status is `Available`, the warm pool billable
   seconds, and the name of the training job that reused the warm pool if the
   warm pool status is `Reused`.

## Using the low-level

SageMaker APIs

Use SageMaker AI managed warm pools with either the SageMaker API or the AWS CLI.

### SageMaker AI

API

Set up SageMaker AI managed warm pools using the SageMaker API with the following
commands:

- [CreateTrainingJob](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md")
- [UpdateTrainingJob](../APIReference/API_UpdateTrainingJob.md "../APIReference/API_UpdateTrainingJob.md")
- [ListTrainingJobs](../APIReference/API_ListTrainingJobs.md "../APIReference/API_ListTrainingJobs.md")
- [DescribeTrainingJob](../APIReference/API_DescribeTrainingJob.md "../APIReference/API_DescribeTrainingJob.md")

### AWS

CLI

Set up SageMaker AI managed warm pools using the AWS CLI with the following
commands:

- [create-training-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-training-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-training-job.html")
- [update-training-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-training-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-training-job.html")
- [list-training-jobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-training-jobs.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-training-jobs.html")
- [describe-training-job](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-training-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/describe-training-job.html")

## IAM condition

key

Administrators can optionally use the `sagemaker:KeepAlivePeriod`
condition key to further restrict the `KeepAlivePeriodInSeconds` limits
for certain users or groups. SageMaker AI managed warm pools are limited to a
`KeepAlivePeriodInSeconds` value of 3600 seconds (60 minutes), but
administrators can lower this limit if needed.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnforceKeepAlivePeriodLimit",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateTrainingJob"
 ],
 "Resource": "*",
 "Condition": {
 "NumericLessThanIfExists": {
 "sagemaker:KeepAlivePeriod": "`1800`"
 }
 }
 }
 ]
}`

```

For more information, see [Condition keys for Amazon SageMaker AI](../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-policy-keys "../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-policy-keys") in the _Service
Authorization Reference_.
