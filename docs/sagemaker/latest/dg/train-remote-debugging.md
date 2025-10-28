# Access a training container through AWS Systems Manager for

remote debugging

You can securely connect to SageMaker training containers through AWS Systems Manager (SSM). This gives
you a shell-level access to debug training jobs that are running within the container. You
can also log commands and responses that are streamed to Amazon CloudWatch. If you use your own
Amazon Virtual Private Cloud (VPC) to train a model, you can use AWS PrivateLink to set up a VPC endpoint for
SSM and connect to containers privately through SSM.

You can connect to [SageMaker AI Framework Containers](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only "https://github.com/aws/deep-learning-containers/blob/master/available_images.md#sagemaker-framework-containers-sm-support-only") or connect to your own training container set up with
the SageMaker Training environment.

## Set up IAM permissions

To enable SSM in your SageMaker training container, you need to set up an IAM role for
the container. For you or users in your AWS account to access the training containers
through SSM, you need to set up IAM users with permissions to use SSM.

### IAM role

For a SageMaker training container to start with the SSM agent, provide an IAM role
with SSM permissions.

To enable remote debugging for your training job, SageMaker AI needs to start the [SSM agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md") in the training container when the training job starts. To
allow the SSM agent to communicate with the SSM service, add the following
policy to the IAM role that you use to run your training job.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssmmessages:CreateControlChannel",
 "ssmmessages:CreateDataChannel",
 "ssmmessages:OpenControlChannel",
 "ssmmessages:OpenDataChannel"
 ],
 "Resource": "*"
 }
 ]
 }`

```

### IAM user

Add the following policy to provide an IAM user with SSM session permissions
to connect to an SSM target. In this case, the SSM target is a SageMaker training
container.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession",
 "ssm:TerminateSession"
 ],
 "Resource": "*"
 }
 ]
}`

```

You can restrict IAM users to connect only to containers for specific training
jobs by adding the `Condition` key, as shown in the following policy
sample.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:StartSession",
 "ssm:TerminateSession"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringLike": {
 "ssm:resourceTag/aws:ssmmessages:target-id": [
 "sagemaker-training-job:*"
 ]
 }
 }
 }
 ]
}`

```

You can also explicitly use the `sagemaker:EnableRemoteDebug` condition
key to restrict remote debugging. The following is an example policy for IAM users
to restrict remote debugging.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyRemoteDebugInTrainingJob",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateTrainingJob",
 "sagemaker:UpdateTrainingJob"
 ],
 "Resource": "*",
 "Condition": {
 "BoolIfExists": {
 "sagemaker:EnableRemoteDebug": false
 }
 }
 }
 ]
}`

```

For more information, see [Condition keys for Amazon SageMaker AI](../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-policy-keys "../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-policy-keys") in the _AWS
Service Authorization Reference_.

## How to enable remote debugging for a

SageMaker training job

In this section, learn how to enable remote debugging when starting or updating a
training job in Amazon SageMaker AI.

SageMaker Python SDK
Using the estimator class in the SageMaker Python SDK, you can turn remote
debugging on or off using the `enable_remote_debug` parameter or
the `enable_remote_debug()` and
`disable_remote_debug()` methods.

**To enable remote debugging when you create a
training job**

To enable remote debugging when you create a new training job, set the
`enable_remote_debug` parameter to `True`. The
default value is `False`, so if you don’t set this parameter at
all, or you explicitly set it to `False`, remote debugging
functionality is disabled.

```
import sagemaker

session = sagemaker.Session()

estimator = sagemaker.estimator.Estimator(
    ...,
    sagemaker_session=session,
    image_uri="`<your_image_uri>`", #must be owned by your organization or Amazon DLCs
    role=`role`,
    instance_type="`ml.m5.xlarge`",
    instance_count=`1`,
    output_path=`output_path`,
    max_run=`1800`,
    enable_remote_debug=`True`
)
```

**To enable remote debugging by updating a training
job**

Using the following estimator class methods, you can enable or disable
remote debugging while a training job is running when the
`SecondaryStatus` of the job is `Downloading` or
`Training`.

```
# Enable RemoteDebug
estimator.enable_remote_debug()

# Disable RemoteDebug
estimator.disable_remote_debug()
```

AWS SDK for Python (Boto3)
**To enable remote debugging when you create a
training job**

To enable remote debugging when you create a new training job, set the
value for the `EnableRemoteDebug` key to `True` in the
`RemoteDebugConfig` parameter.

```
import boto3

sm = boto3.Session(region_name=region).client("sagemaker")

# Start a training job
sm.create_training_job(
    ...,
    TrainingJobName=`job_name`,
    AlgorithmSpecification={
        // Specify a training Docker container image URI
        // (Deep Learning Container or your own training container) to TrainingImage.
        "TrainingImage": "`<your_image_uri>`",
        "TrainingInputMode": "`File`"
    },
    RoleArn=`iam_role_arn`,
    OutputDataConfig=`output_path`,
    ResourceConfig={
        "InstanceType": "`ml.m5.xlarge`",
        "InstanceCount": `1`,
        "VolumeSizeInGB": `30`
    },
    StoppingCondition={
        "MaxRuntimeInSeconds": `86400`
    },
    **RemoteDebugConfig={
 "EnableRemoteDebug": `True`
 }**
)
```

**To enable remote debugging by updating a training
job**

Using the `update_traing_job` API, you can enable or disable
remote debugging while a training job is running when the
`SecondaryStatus` of the job is `Downloading` or
`Training`.

```
# Update a training job
sm.update_training_job(
    TrainingJobName=`job_name`,
    RemoteDebugConfig={
        "EnableRemoteDebug": `True`     # True | False
    }
)
```

AWS Command Line Interface (CLI)
**To enable remote debugging when you create a
training job**

Prepare a `CreateTrainingJob` request file in JSON format, as
follows.

```
// train-with-remote-debug.json
{
    "TrainingJobName": `job_name`,
    "RoleArn": `iam_role_arn`,
    "AlgorithmSpecification": {
        // Specify a training Docker container image URI (Deep Learning Container or your own training container) to TrainingImage.
        "TrainingImage": "`<your_image_uri>`",
        "TrainingInputMode": "`File`"
    },
    "OutputDataConfig": {
        "S3OutputPath": `output_path`
    },
    "ResourceConfig": {
        "InstanceType": "`ml.m5.xlarge`",
        "InstanceCount": `1`,
        "VolumeSizeInGB": `30`
    },
    "StoppingCondition": {
        "MaxRuntimeInSeconds": `86400`
    },
    **"RemoteDebugConfig": {
 "EnableRemoteDebug": `True`
 }**
}
```

After saving the JSON file, run the following command in the terminal
where you submit the training job. The following example command assumes
that the JSON file is named `train-with-remote-debug.json`. If
you run it from a Jupyter notebook, add an exclamation point
(`!`) to the beginning of the line.

```
aws sagemaker create-training-job \
    --cli-input-json `file://train-with-remote-debug.json`
```

**To enable remote debugging by updating a training
job**

Prepare an `UpdateTrainingJob` request file in JSON format, as
follows.

```
// update-training-job-with-remote-debug-config.json
{
    "TrainingJobName": `job_name`,
    "RemoteDebugConfig": {
        "EnableRemoteDebug": `True`
    }
}
```

After saving the JSON file, run the following command in the terminal
where you submit the training job. The following example command assumes
that the JSON file is named `train-with-remote-debug.json`. If
you run it from a Jupyter notebook, add an exclamation point
(`!`) to the beginning of the line.

```
aws sagemaker update-training-job \
    --cli-input-json `file://update-training-job-with-remote-debug-config.json`
```

## Access your training

container

You can access a training container when the `SecondaryStatus` of the
corresponding training job is `Training`. The following code examples
demonstrate how to check the status of your training job using the
`DescribeTrainingJob` API, how to check the training job logs in CloudWatch,
and how to log in to the training container.

**To check the status of a training job**

SageMaker Python SDK
To check the `SecondaryStatus` of a training job, run the
following SageMaker Python SDK code.

```
import sagemaker

session = sagemaker.Session()

# Describe the job status
training_job_info = session.describe_training_job(`job_name`)
print(training_job_info)
```

AWS SDK for Python (Boto3)
To check the `SecondaryStatus` of a training job, run the
following SDK for Python (Boto3) code.

```
import boto3

session = boto3.session.Session()
region = session.region_name
sm = boto3.Session(region_name=region).client("sagemaker")

# Describe the job status
sm.describe_training_job(TrainingJobName=`job_name`)
```

AWS Command Line Interface (CLI)
To check the `SecondaryStatus` of a training job, run the
following AWS CLI command for SageMaker AI.

```
aws sagemaker describe-training-job \
    --training-job-name `job_name`
```

**To find the host name of a training container**

To connect to the training container through SSM, use this format for the target ID:
`sagemaker-training-job:<training-job-name>_algo-<n>`, where
`algo-<n>` is the name of the container host. If your job is running
on a single instance, the host is always `algo-1`. If you run a distributed
training job on multiple instances, SageMaker AI creates an equal number of hosts and log
streams. For example, if you use 4 instances, SageMaker AI creates `algo-1`,
`algo-2`, `algo-3`, and `algo-4`. You must
determine which log stream you want to debug, and its host number. To access log streams
that are associated with a training job, do the following.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the left navigation pane, choose **Training**,
   then choose **Training jobs**.
3. From the **Training jobs** list, choose the
   training job that you want to debug. The training job details page opens.
4. In the **Monitor** section, choose **View logs**. The related training job log stream list
   opens in the CloudWatch console.
5. Log stream names appear in
   `<training-job-name>/algo-<n>-<time-stamp>` format, with
   `algo-<n>` representing the host name.

To learn more about how SageMaker AI manages configuration information for multi-instance
distributed training, see [Distributed Training Configuration](your-algorithms-training-algo-running-container.md#your-algorithms-training-algo-running-container-dist-training "your-algorithms-training-algo-running-container.md#your-algorithms-training-algo-running-container-dist-training").

**To access the training container**

Use the following command in terminal to start the SSM session (`aws ssm start-session`) and connect to the training container.

```
aws ssm start-session --target sagemaker-training-job:`<training-job-name>`_`algo-<n>`
```

For example, if the training job name is `training-job-test-remote-debug`
and the host name is `algo-1`, the target ID becomes
`sagemaker-training-job:training-job-test-remote-debug_algo-1`. If the
output of this command is similar to `Starting session with SessionId:xxxxx`,
the connection is successful.

### SSM access with AWS PrivateLink

If your training containers run within a Amazon Virtual Private Cloud that is not
connected to the public internet, you can use AWS PrivateLink to enable SSM.
AWS PrivateLink restricts all network traffic between your endpoint instances, SSM, and
Amazon EC2 to the Amazon network. For more information on how to setup SSM access
with AWS PrivateLink, see [Set up an Amazon VPC endpoint for Session Manager](../../../systems-manager/latest/userguide/session-manager-getting-started-privatelink.md "../../../systems-manager/latest/userguide/session-manager-getting-started-privatelink.md").

## Log SSM session commands and

results

After following the instructions at [Create a Session Manager preferences document (command line)](../../../systems-manager/latest/userguide/getting-started-create-preferences-cli.md "../../../systems-manager/latest/userguide/getting-started-create-preferences-cli.md"), you can
create SSM documents that define your preferences for SSM sessions. You can use
SSM documents to configure session options, including data encryption, session
duration, and logging. For example, you can specify whether to store session log data in
an Amazon Simple Storage Service (Amazon S3) bucket or in an Amazon CloudWatch Logs group. You can create
documents that define general preferences for all sessions for an
AWS account and AWS Region, or documents that define preferences for individual
sessions.

## Troubleshooting issues

by checking error logs from SSM

Amazon SageMaker AI uploads errors from the SSM agent to your CloudWatch Logs in the
`/aws/sagemaker/TrainingJobs` log group. SSM agent log streams are
named in this format: `<job-name>/algo-<n>-<timestamp>/ssm`. For
example, if you create a two-node training job named
`training-job-test-remote-debug`, the training job log
`training-job-test-remote-debug/algo-<n>-<timestamp>` and multiple
SSM agent error logs
`training-job-test-remote-debug/algo-<n>-<timestamp>/ssm` are
uploaded to your CloudWatch Logs. In this example, you can review the `*/ssm` log
streams to troubleshoot SSM issues.

```
training-job-test-remote-debug/algo-1-1680535238
training-job-test-remote-debug/algo-2-1680535238
training-job-test-remote-debug/algo-1-1680535238/ssm
training-job-test-remote-debug/algo-2-1680535238/ssm
```

## Considerations

Consider the following when using SageMaker AI remote debugging.

- Remote debugging isn't supported for [SageMaker AI algorithm
  containers](algorithms-choose.md "algorithms-choose.md") or containers from SageMaker AI on AWS Marketplace.
- You can't start an SSM session for containers that have network isolation
  enabled because the isolation prevents outbound network calls.
