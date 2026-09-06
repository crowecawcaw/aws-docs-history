

# Configure access to an Amazon S3 bucket for data export
<a name="security-iam-s3-export-permissions"></a>

When you use the `exportConfig` parameter in the `CreateWorkflowDefinition` API operation, Nova Act exports Agent Trajectory Data to an Amazon S3 bucket that you specify. To allow this, you must attach an identity-based policy to the calling identity that grants the required Amazon S3 permissions.

**Note**  
The S3 bucket must be in the same account as the caller. Cross-account S3 buckets are not supported.

The policy includes the following statement defining permissions:
+ Permissions to write Agent Trajectory Data to the bucket (`s3:PutObject`).

Add, modify, and remove the statements, resources, and conditions in the following policy and replace `${values}` as necessary:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::${bucket}/${prefix}/*"
        }
    ]
}
```

After modifying the policy to your use case, attach it to the IAM identity that calls the Nova Act API. To learn how to attach permissions to an IAM identity, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html).

For information about enabling encryption on your export S3 bucket, see [Encryption at rest](data-encryption.md#encryption-rest).