# Using the API with Hybrid Jobs

You can access and interact with Amazon Braket Hybrid Jobs directly using the
API. However, defaults and convenience methods are not available when
using the API directly.

###### Note

We strongly recommend that you interact with Amazon Braket Hybrid Jobs using the
[Amazon Braket Python
SDK](https://github.com/aws/amazon-braket-sdk-python "https://github.com/aws/amazon-braket-sdk-python"). It offers convenient defaults and protections that help your hybrid jobs run
successfully.

This topic covers the basics of using the API. If you choose to use the
API, keep in mind that this approach can be more complex and be prepared for several
iterations to get your hybrid job to run.

To use the API, your account should have a role with the
`AmazonBraketFullAccess` managed policy.

###### Note

For more information on how to obtain a role with the
`AmazonBraketFullAccess` managed policy, see the [Enable Amazon Braket](braket-enable-overview.md "braket-enable-overview.md") page.

Additionally, you need an **execution role**. This role
will be passed to the service. You can create the role using the **Amazon Braket console**. Use the **Execution
roles** tab on the **Permissions and settings**
page to create a default role for hybrid jobs.

The `CreateJob`
API requires that you specify all the required parameters for the hybrid job. To
use Python, compress your algorithm script files to a tar bundle, such as an input.tar.gz
file, and run the following script. Update the parts of the code within angled brackets
(`<>`) to match your account information and entry point that specify
the path, file, and method where your hybrid job starts.

```
from braket.aws import AwsDevice, AwsSession
import boto3
from datetime import datetime

s3_client = boto3.client("s3")
client = boto3.client("braket")

project_name = "job-test"
job_name = project_name + "-" + datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
bucket = "amazon-braket-<your_bucket>"
s3_prefix = job_name

job_script = "input.tar.gz"
job_object = f"{s3_prefix}/script/{job_script}"
s3_client.upload_file(job_script, bucket, job_object)

input_data = "inputdata.csv"
input_object = f"{s3_prefix}/input/{input_data}"
s3_client.upload_file(input_data, bucket, input_object)

job = client.create_job(
    jobName=job_name,
    roleArn="arn:aws:iam::<your_account>:role/service-role/AmazonBraketJobsExecutionRole",  # https://docs.aws.amazon.com/braket/latest/developerguide/braket-manage-access.html#about-amazonbraketjobsexecution
    algorithmSpecification={
        "scriptModeConfig": {
            "entryPoint": "<your_execution_module>:<your_execution_method>",
            "containerImage": {"uri": "292282985366.dkr.ecr.us-west-1.amazonaws.com/amazon-braket-base-jobs:1.0-cpu-py37-ubuntu18.04"},   # Change to the specific region you are using
            "s3Uri": f"s3://{bucket}/{job_object}",
            "compressionType": "GZIP"
        }
    },
    inputDataConfig=[
        {
            "channelName": "hellothere",
            "compressionType": "NONE",
            "dataSource": {
                "s3DataSource": {
                    "s3Uri": f"s3://{bucket}/{s3_prefix}/input",
                    "s3DataType": "S3_PREFIX"
                }
            }
        }
    ],
    outputDataConfig={
        "s3Path": f"s3://{bucket}/{s3_prefix}/output"
    },
    instanceConfig={
        "instanceType": "ml.m5.large",
        "instanceCount": 1,
        "volumeSizeInGb": 1
    },
    checkpointConfig={
        "s3Uri":  f"s3://{bucket}/{s3_prefix}/checkpoints",
        "localPath": "/opt/omega/checkpoints"
    },
    deviceConfig={
        "priorityAccess": {
            "devices": [
                "arn:aws:braket:us-west-1::device/qpu/rigetti/Ankaa-3"
            ]
        }
    },
    hyperParameters={
        "hyperparameter key you wish to pass": "<hyperparameter value you wish to pass>",
    },
    stoppingCondition={
        "maxRuntimeInSeconds": 1200,
        "maximumTaskLimit": 10
    },
)
```

Once you create your hybrid job, you can access the hybrid job details through the `GetJob`
API or the console. To get the hybrid job details from the Python session in which
you ran the `createJob` code as in the previous example, use the following
Python command.

```
getJob = client.get_job(jobArn=job["jobArn"])
```

To cancel a hybrid job, call the `CancelJob`
API with the Amazon Resource Name of the job
('JobArn').

```
cancelJob = client.cancel_job(jobArn=job["jobArn"])
```

You can specify checkpoints as part of the `createJob`
API using the `checkpointConfig` parameter.

```
    checkpointConfig = {
        "localPath" : "/opt/omega/checkpoints",
        "s3Uri": f"s3://{bucket}/{s3_prefix}/checkpoints"
    },
```

###### Note

The localPath of `checkpointConfig` cannot start with any of the following
reserved paths: `/opt/ml`, `/opt/braket`, `/tmp`, or
`/usr/local/nvidia`.
