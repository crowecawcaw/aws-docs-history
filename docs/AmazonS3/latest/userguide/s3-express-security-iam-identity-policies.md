

# IAM identity-based policies for directory buckets
<a name="s3-express-security-iam-identity-policies"></a>

Before you can create directory buckets, you must grant the necessary permissions to your AWS Identity and Access Management (IAM) role or users. This example policy allows access to the `CreateSession` API operation (for use with Zonal endpoint [object level] API operations) and all of the Regional endpoint (bucket-level) API operations. This policy allows the `CreateSession` API operation for use with all directory buckets, but the Regional endpoint API operations are allowed only for use with the specified directory bucket. To use this example policy, replace the `{{user input placeholders}}` with your own information.

**Note**  
As a best practice, grant only the permissions required to perform a task (least-privilege). Remove any actions from this policy that are not needed for your use case. For a complete list of S3 Express One Zone actions, see [Actions, resources, and condition keys for S3 Express One Zone](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3express.html) in the *Service Authorization Reference*.

**Example — Identity-based policy for directory bucket access**  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowRegionalEndpointAPIs",
            "Effect": "Allow",
            "Action": [
                "s3express:CreateBucket",
                "s3express:DeleteBucket",
                "s3express:DeleteBucketPolicy",
                "s3express:GetBucketPolicy",
                "s3express:PutBucketPolicy",
                "s3express:GetEncryptionConfiguration",
                "s3express:PutEncryptionConfiguration",
                "s3express:GetLifecycleConfiguration",
                "s3express:PutLifecycleConfiguration",
                "s3express:GetInventoryConfiguration",
                "s3express:PutInventoryConfiguration",
                "s3express:GetMetricsConfiguration",
                "s3express:PutMetricsConfiguration"
            ],
            "Resource": "arn:aws:s3express:{{region}}:{{account-id}}:bucket/{{bucket-base-name--zone-id--x-s3}}"
        },
        {
            "Sid": "AllowListAndCreateSession",
            "Effect": "Allow",
            "Action": [
                "s3express:ListAllMyDirectoryBuckets",
                "s3express:CreateSession"
            ],
            "Resource": "*"
        }
    ]
}
```

This policy has two statements:
+ The first statement grants permissions for Regional endpoint (bucket-level) API operations on a specific directory bucket. You can remove actions that you don't need for your use case.
+ The second statement grants permissions for `ListAllMyDirectoryBuckets` and `CreateSession`. These actions don't support resource-level permissions, so the `Resource` is `"*"`. The `CreateSession` permission enables all Zonal endpoint (object-level) API operations, such as `PutObject`, `GetObject`, and `DeleteObject`.