# Step 2: Configure IAM permissions on your instance role

Fluent Bit runs on the Amazon EC2 instance and uses the instance role
to authenticate with Amazon S3. By default, this role does not include Amazon S3 permissions,
so you must create and attach a policy that grants Fluent Bit
permission to write logs to the `ecs-logs/` prefix, read configuration
from the `fluent-bit/` prefix, and list the bucket.

###### Note

You can also test your policies by using the [IAM Policy Simulator](https://policysim.aws.amazon.com/home/index.jsp?# "https://policysim.aws.amazon.com/home/index.jsp?#"). For
more information about the policy simulator, see [Working with the IAM Policy
Simulator](../../../IAM/latest/UserGuide/policies_testing-policies.md "../../../IAM/latest/UserGuide/policies_testing-policies.md") in the _IAM User Guide_.

Create an IAM policy with the following JSON:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:AbortMultipartUpload",
                "s3:ListMultipartUploadParts"
            ],
            "Resource": "arn:aws:s3:::`host-level-logs-bucket`/ecs-logs/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::`host-level-logs-bucket`/fluent-bit/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads"
            ],
            "Resource": "arn:aws:s3:::`host-level-logs-bucket`"
        }
    ]
}
```

AWS Console

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose
   **Policies**.
3. Choose **Create policy**.
4. Choose the **JSON** tab and paste the
   preceding policy JSON. Replace
   `host-level-logs-bucket` with your bucket
   name.
5. Choose **Next**.
6. For **Policy name**, enter
   `BatchHostLogsS3Access`.
7. Choose **Create policy**.

Then attach the policy to the instance role:

1. In the navigation pane, choose
   **Roles**.
2. Search for and choose
   `ecsInstanceRole`.
3. Choose **Add permissions**, then
   **Attach policies**.
4. Search for `BatchHostLogsS3Access`, select it,
   and choose **Add permissions**.

AWS CLI
Save the preceding policy JSON to a file named
`batch-host-logs-policy.json`, then run the following
commands:

```
aws iam create-policy \
    --policy-name BatchHostLogsS3Access \
    --policy-document file://batch-host-logs-policy.json
```

Note the policy ARN in the output, then attach the policy to your
instance role:

```
aws iam attach-role-policy \
    --role-name ecsInstanceRole \
    --policy-arn arn:aws:iam::`111122223333`:policy/BatchHostLogsS3Access
```
