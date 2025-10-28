# Create and register a job definition

Now that your Docker image is in an image registry, you can specify it in an AWS Batch job definition. Then, you
can use it later to run an array job. This example only uses the AWS CLI. However, you can also use the AWS Management Console. For
more information, see [Create a single-node job definition](create-job-definition.md "create-job-definition.md") .

###### To create a job definition

1. Create a file named `print-color-job-def.json` in your workspace directory and paste the
   following into it. Replace the image repository URI with your own image's URI.

```
{
  "jobDefinitionName": "print-color",
  "type": "container",
  "containerProperties": {
    "image": "`aws_account_id`.dkr.ecr.`region`.amazonaws.com/print-color",
    "resourceRequirements": [
        {
            "type": "MEMORY",
            "value": "250"
        },
        {
            "type": "VCPU",
            "value": "1"
        }
    ]
  }
}
```

2. Register the job definition with AWS Batch.

```
`$` `aws batch register-job-definition --cli-input-json file://print-color-job-def.json`
```
