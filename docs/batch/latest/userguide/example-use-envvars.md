# Environment variables

The following example job definition uses environment variables to specify a file type and Amazon S3 URL. This
particular example is from the [Creating a Simple "Fetch &
Run" AWS Batch Job](https://aws.amazon.com/blogs/compute/creating-a-simple-fetch-and-run-aws-batch-job/ "https://aws.amazon.com/blogs/compute/creating-a-simple-fetch-and-run-aws-batch-job/") compute blog post. The [`fetch_and_run.sh`](https://github.com/awslabs/aws-batch-helpers/blob/master/fetch-and-run/fetch_and_run.sh "https://github.com/awslabs/aws-batch-helpers/blob/master/fetch-and-run/fetch_and_run.sh") script that's described in the blog post uses these environment
variables to download the `myjob.sh` script from S3 and declare its file type.

Even though the command and environment variables are hardcoded into the job definition in this example, you can
specify command and environment variable overrides to make the job definition more versatile.

```
{
    "jobDefinitionName": "fetch_and_run",
    "type": "container",
    "containerProperties": {
        "image": "`123456789012`.dkr.ecr.us-east-1.amazonaws.com/fetch_and_run",
        "resourceRequirements": [
            {
                "type": "MEMORY",
                "value": "2000"
            },
            {
                "type": "VCPU",
                "value": "2"
            }
        ],
        "command": [
            "myjob.sh",
            "60"
        ],
        "jobRoleArn": "arn:aws:iam::`123456789012`:role/AWSBatchS3ReadOnly",
        "environment": [
            {
                "name": "BATCH_FILE_S3_URL",
                "value": "s3://amzn-s3-demo-source-bucket/myjob.sh"
            },
            {
                "name": "BATCH_FILE_TYPE",
                "value": "script"
            }
        ],
        "user": "nobody"
    }
}
```
