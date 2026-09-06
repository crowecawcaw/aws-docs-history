

# Setting Object Lock retention using Batch Operations
<a name="batch-ops-object-lock-retention"></a>

You can use Amazon S3 Batch Operations with S3 Object Lock to manage retention for many Amazon S3 objects at once. You specify the list of target objects in your manifest and submit it to Batch Operations for completion. For more information, see [S3 Object Lock retention](batch-ops-retention-date.md) and [S3 Object Lock legal hold](batch-ops-legal-hold.md). 

The following examples show how to create an AWS Identity and Access Management (IAM) role with S3 Batch Operations permissions and update the role permissions to include the `s3:PutObjectRetention` permissions so that you can run S3 Object Lock retention on the objects in your manifest bucket. You must also have a `CSV` manifest that identifies the objects for your S3 Batch Operations job. For more information, see [Specifying a manifest](batch-ops-create-job.md#specify-batchjob-manifest).

To use the following examples, replace the {{`user input placeholders`}} with your own information. 

## Using the AWS CLI
<a name="batch-ops-cli-object-lock-retention-example"></a>

The following AWS CLI example shows how to use Batch Operations to apply S3 Object Lock retention across multiple objects.

```
export AWS_PROFILE='{{aws-user}}'

read -d '' {{retention_permissions}} <<EOF
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObjectRetention"
            ],
            "Resource": [
                "arn:aws:s3:::{{{{amzn-s3-demo-manifest-bucket}}}}/*"
            ]
        }
    ]
}
EOF

aws iam put-role-policy --role-name {{batch_operations-objectlock}} --policy-name {{retention-permissions}} --policy-document "${{{retention_permissions}}}"
```

## Using the AWS SDK for Java
<a name="batch-ops-examples-java-object-lock-retention"></a>

For examples of how to use Batch Operations to apply S3 Object Lock retention across multiple objects with the AWS SDK for Java, see [Use CreateJob with an AWS SDK or CLI](https://docs.aws.amazon.com/AmazonS3/latest/API/s3-control_example_s3-control_CreateJob_section.html) in the *Amazon S3 API Reference*.