# Setting Object Lock retention using Batch Operations

You can use Amazon S3 Batch Operations with S3 Object Lock to manage retention for many
Amazon S3 objects at once. You specify the list of target objects in your manifest and submit
it to Batch Operations for completion. For more information, see [S3 Object Lock retention](batch-ops-retention-date.md "batch-ops-retention-date.md") and [S3 Object Lock legal hold](batch-ops-legal-hold.md "batch-ops-legal-hold.md").

The following examples show how to create an AWS Identity and Access Management (IAM) role with
S3 Batch Operations permissions and update the role permissions to include the
`s3:PutObjectRetention` permissions so that you can run S3 Object Lock
retention on the objects in your manifest bucket. You must also have a
`CSV` manifest that identifies the objects for your
S3 Batch Operations job. For more information, see [Specifying a manifest](batch-ops-create-job.md#specify-batchjob-manifest "batch-ops-create-job.md#specify-batchjob-manifest").

To use the following examples, replace the `user input
 placeholders` with your own information.

The following AWS CLI example shows how to use Batch Operations to apply
S3 Object Lock retention across multiple objects.

```
export AWS_PROFILE='`aws-user`'

read -d '' `retention_permissions` <<EOF
{
    "Version": "2012-10-17"		 	 	 ,		 	 	 TCX5-2025-waiver;,
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObjectRetention"
            ],
            "Resource": [
                "arn:aws:s3:::{{`amzn-s3-demo-manifest-bucket`}}/*"
            ]
        }
    ]
}
EOF

aws iam put-role-policy --role-name `batch_operations-objectlock` --policy-name `retention-permissions` --policy-document "${`retention_permissions`}"
```

For examples of how to use Batch Operations to apply S3 Object Lock retention across multiple objects with the AWS SDK for Java, see [Use CreateJob with an AWS SDK or CLI](../API/s3-control_example_s3-control_CreateJob_section.md "../API/s3-control_example_s3-control_CreateJob_section.md") in the _Amazon S3 API Reference_.
