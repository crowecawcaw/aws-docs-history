# Customizing the log location for step log files

Beginning in Amazon EMR version 7.11, you can now customize the S3 logging behavior for steps on a per-step basis. For a single step, you
can choose a unique S3 bucket where the step's logs are uploaded. You can also choose a unique KMS key which is used to encrypt
the step's logs at rest, on S3. These options take precedence over any cluster-wide logging settings that are configured when launching
the cluster.

## Prerequisites

- Your cluster should have cluster logging enabled. For more information,
  see [Configure Amazon EMR cluster logging and debugging](emr-plan-debugging.md "emr-plan-debugging.md").
- EC2 instance profile:
  - Your cluster's EC2 instance profile should be allowed to access the S3 bucket which will be used in the
    step's logging configuration.
  - Your cluster's EC2 instance profile should be allowed to access the KMS key which will be used in the step's logging
    configuration. Furthermore, your cluster's EC2 instance profile should allow `kms:Decrypt` and `kms:GenerateDataKey` actions.

## Step log configuration

When you submit a step to EMR, you can configure the step's logging behavior via [StepMonitoringConfiguration](../../../cli/latest/reference/emr/add-steps.md "../../../cli/latest/reference/emr/add-steps.md").
The StepMonitoringConfiguration contains the S3MonitoringConfiguration object where you can specify an S3 logging bucket and/or a KMS key for the step.

The following example shows you how you can customize a step's S3 bucket and KMS key from a python script:

```
import boto3

emr_client = boto3.client("emr", region_name="us-east-1")

# Define your step:
example_step = [
    {
        "Name": "Example Step for StepMonitoringConfiguration",
        "ActionOnFailure": "CONTINUE",
        "HadoopJarStep": {
            "Jar": "command-runner.jar",
            "Args": ["bash", "-c", "echo 1"]
        },
        "StepMonitoringConfiguration": {
            "S3MonitoringConfiguration": {
                "LogUri": "s3://your-s3-bucket/", # Replace this with your S3 bucket
                "EncryptionKeyArn": "arn:aws:kms:your-kms-key-arn" # Replace this with your KMS key ARN
            }
        }
    }
]

response = emr_client.add_job_flow_steps(
    JobFlowId="j-xxxxxxxxxxxxx",  # Replace this with your EMR cluster ID
    Steps=example_step
)
```

## Considerations

- If your cluster does not enable cluster logging, step logs will not be uploaded to S3 even if you
  provide a `StepMonitoringConfiguration`.
- If your step runs a Spark application, the application's container logs will also be uploaded to the location specified
  in the `StepMonitoringConfiguration`.
- You are allowed to specify a `LogUri` without specifiying an `EncryptionKeyArn` or vice versa. EMR will default
  to the cluster-wide setting for any field which is omitted in the `StepMonitoringConfiguration`.
