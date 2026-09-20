

# Logs sent to Amazon S3
<a name="AWS-logs-infrastructure-V2-S3"></a>

For an AWS CLI example, see [Create a delivery to Amazon S3](AWS-vended-logs-permissions-V2.md#vended-logs-same-account-example-s3).

## User permissions
<a name="AWS-logs-infrastructure-V2-S3-user-permissions"></a>

To enable sending logs to Amazon S3, you must be signed in with the following permissions.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ReadWriteAccessForLogDeliveryActions",
            "Effect": "Allow",
            "Action": [
                "logs:GetDelivery",
                "logs:GetDeliverySource",
                "logs:PutDeliveryDestination",
                "logs:GetDeliveryDestinationPolicy",
                "logs:DeleteDeliverySource",
                "logs:PutDeliveryDestinationPolicy",
                "logs:CreateDelivery",
                "logs:GetDeliveryDestination",
                "logs:PutDeliverySource",
                "logs:DeleteDeliveryDestination",
                "logs:DeleteDeliveryDestinationPolicy",
                "logs:DeleteDelivery",
                "logs:UpdateDeliveryConfiguration"
            ],
            "Resource": [
            "arn:aws:logs:{{us-east-1}}:{{111122223333}}:delivery:*",
    "arn:aws:logs:{{us-east-1}}:{{111122223333}}:delivery-source:*",
    "arn:aws:logs:{{us-east-1}}:{{111122223333}}:delivery-destination:*"
            ]
        },
        {
            "Sid": "ListAccessForLogDeliveryActions",
            "Effect": "Allow",
            "Action": [
                "logs:DescribeDeliveryDestinations",
                "logs:DescribeDeliverySources",
                "logs:DescribeDeliveries",
                "logs:DescribeConfigurationTemplates"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowUpdatesToResourcePolicyS3",
            "Effect": "Allow",
            "Action": [
                "s3:PutBucketPolicy",
                "s3:GetBucketPolicy"
            ],
            "Resource": "arn:aws:s3:::bucket-name"
        }
    ]
}
```

------

## Amazon S3 bucket resource policy
<a name="AWS-logs-infrastructure-V2-S3-bucket-resource-policy"></a>

The S3 bucket where the logs are being sent must have a resource policy that includes certain permissions. If the bucket currently does not have a resource policy and the user setting up the logging has the `S3:GetBucketPolicy` and `S3:PutBucketPolicy` permissions for the bucket, then AWS automatically creates the following policy for it when you begin sending the logs to Amazon S3.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "AWSLogDeliveryWrite20150319",
    "Statement": [
        {
            "Sid": "AWSLogDeliveryWrite",
            "Effect": "Allow",
            "Principal": {
                "Service": "delivery.logs.amazonaws.com"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/AWSLogs/account-ID/*",
            "Condition": {
                "StringEquals": {
                    "s3:x-amz-acl": "bucket-owner-full-control",
                    "aws:SourceAccount": [
                        "0123456789"
                    ]
                },
                "ArnLike": {
                    "aws:SourceArn": [
                        "arn:aws:logs:us-east-1:{{111122223333}}:delivery-source:*"
                    ]
                }
            }
        }
    ]
}
```

------

In the previous policy, for `aws:SourceAccount`, specify the list of account IDS for which logs are being delivered to this bucket. For `aws:SourceArn`, specify the list of ARNs of the resource that generates the logs, in the form `arn:aws:logs:{{source-region}}:{{source-account-id}}:*`. 

If the bucket has a resource policy but that policy doesn't contain the statement shown in the previous policy, and the user setting up the logging has the `S3:GetBucketPolicy` and `S3:PutBucketPolicy` permissions for the bucket, that statement is appended to the bucket's resource policy.

**Note**  
In some cases, you may see `AccessDenied` errors in AWS CloudTrail if the `s3:ListBucket` permission has not been granted to `delivery.logs.amazonaws.com`. To avoid these errors in your CloudTrail logs, you must grant the `s3:ListBucket` permission to `delivery.logs.amazonaws.com` and you must include the `Condition` parameters shown with the `s3:GetBucketAcl` permission set in the preceding bucket policy. To make this simpler, instead of creating a new `Statement`, you can directly update the `AWSLogDeliveryAclCheck` to be `“Action”: [“s3:GetBucketAcl”, “s3:ListBucket”]`

## Amazon S3 bucket server-side encryption
<a name="AWS-logs-SSE-KMS-S3-V2"></a>

You can protect the data in your Amazon S3 bucket by enabling server-side encryption. You can use Amazon S3-managed keys (SSE-S3) or a AWS KMS key stored in AWS Key Management Service (SSE-KMS). For more information, see [ Protecting data using server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html). 

If you choose SSE-S3, no additional configuration is required. Amazon S3 handles the encryption key.

**Customer managed key required**  
If you choose SSE-KMS, you must use a customer managed key. You can't use an AWS managed key. If you configure encryption with an AWS managed key, CloudWatch Logs delivers the logs in an unreadable format.

For SSE-KMS, specify the Amazon Resource Name (ARN) of the key when you enable bucket encryption. Add the following to the key policy (not to the bucket policy for your S3 bucket), so that the log delivery account can write to your S3 bucket.

```
{
    "Sid": "Allow Logs Delivery to use the key",
    "Effect": "Allow",
    "Principal": {
        "Service": [ "delivery.logs.amazonaws.com" ]
    },
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "aws:SourceAccount": ["{{012345678901}}"]
        },
        "ArnLike": {
            "aws:SourceArn": ["arn:aws:logs:{{us-east-1}}:{{012345678901}}:delivery-source:*"]
        }
        }
}
```

For `aws:SourceAccount`, specify the account IDs whose logs are delivered to this bucket. For `aws:SourceArn`, specify the delivery source ARNs in the following format: `arn:aws:logs:{{source-region}}:{{source-account-id}}:delivery-source:*`.

## Amazon S3 object key format
<a name="AWS-logs-infrastructure-V2-S3-object-key"></a>

For deliveries that use V2 permissions, the Amazon S3 object key is determined by the destination prefix, the log type, the delivery's suffix path, and whether Hive-compatible paths are enabled. The exact service-defined path and supported suffix variables vary by log type.

Destination prefix  
An optional path that you append to the bucket ARN when you call [PutDeliveryDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html). For example, `arn:aws:s3:::{{bucket-name}}/{{MyLogPrefix}}`. Delivered objects begin with this prefix. For log types that otherwise use a default `AWSLogs/{{source-account-id}}/{{service-name}}/` path, the destination prefix replaces that default path.

Suffix path  
An optional path that you configure for an individual delivery in its [S3DeliveryConfiguration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_S3DeliveryConfiguration.html). A suffix can contain static text and variables. To find the variables supported by a log type, call [DescribeConfigurationTemplates](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeConfigurationTemplates.html) and check `allowedSuffixPathFields`. If you don't specify a suffix path, the log type's default suffix path is used when one is available.

Hive-compatible path  
When `enableHiveCompatiblePath` is `true`, variables in the effective path are rendered as `{{key}}={{value}}`. For example, the default account segment `AWSLogs/{{source-account-id}}/` becomes `AWSLogs/aws-account-id={{source-account-id}}/`. Hive-compatible formatting also applies when you omit `suffixPath` and the log type uses its default suffix.

The following examples show the beginning of an Application Load Balancer access-log object key for account `111122223333` in `us-east-1`. Unless noted, the examples assume no destination prefix.


| Configuration | Beginning of the object key | 
| --- | --- | 
| Hive-compatible path disabled, suffix omitted | AWSLogs/111122223333/elasticloadbalancing/us-east-1/2026/09/10/ | 
| Hive-compatible path enabled, suffix omitted | AWSLogs/aws-account-id=111122223333/elasticloadbalancing/region=us-east-1/year=2026/month=09/day=10/ | 
| Hive-compatible path enabled, suffix myFolder/{yyyy}/{MM}/{dd} | AWSLogs/aws-account-id=111122223333/elasticloadbalancing/myFolder/year=2026/month=09/day=10/ | 
| Destination prefix MyLogPrefix, Hive-compatible path disabled, suffix omitted | MyLogPrefix/us-east-1/2026/09/10/ | 

**Note**  
CloudFront documents its standard logging (v2) path behavior and examples in [Send logs to Amazon S3](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/standard-logging.html#send-logs-s3).

**Note**  
Changing the destination prefix, suffix path, or Hive-compatible setting affects new objects only. Existing objects are not moved. The bucket policy must allow `s3:PutObject` for the resulting prefix. When you manage the bucket policy, keep the `aws:SourceAccount` and `aws:SourceArn` conditions shown in the Amazon S3 bucket policy in [Amazon S3 bucket resource policy](#AWS-logs-infrastructure-V2-S3-bucket-resource-policy), and grant access only to the required prefix.