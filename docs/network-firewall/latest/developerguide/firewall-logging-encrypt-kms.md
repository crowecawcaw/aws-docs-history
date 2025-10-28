# Logging in AWS Network Firewall with server-side encryption

and customer-provided keys

If your logging destination uses server-side encryption with keys that are stored
in AWS Key Management Service (SSE-KMS) and you use a customer managed key (KMS key), you
must give Network Firewall permission to use your KMS key. To do this, you add a key policy
to the KMS key for your chosen destination to permit Network Firewall logging to write your
log files to the destination.

###### Policy for an Amazon S3 bucket

Add the following key policy to your KMS key to allow Network Firewall to log to your
Amazon S3 bucket.

```
{
    "Sid": "Allow Network Firewall to use the key",
    "Effect": "Allow",
    "Principal": {
        "Service": [
            "delivery.logs.amazonaws.com"
        ]
    },
    "Action": "kms:GenerateDataKey*",
    "Resource": "*"
}
```

###### Note

Network Firewall supports encryption with Amazon S3 buckets for key type Amazon S3 key (SSE-S3) and for AWS Key Management Service (SSE-KMS) AWS KMS keys. Network Firewall doesn't support encryption for AWS Key Management Service keys that are managed by AWS.

###### Policy for a CloudWatch Logs log group

For a CloudWatch Logs log group, the service principal requires access to the logs for the Region.
This is the same as for all encrypted CloudWatch Logs log streams. For more information about log data
encryption in CloudWatch Logs, see [Encrypt Log Data in
CloudWatch Logs Using AWS KMS](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md").

Add the following key policy to your KMS key to allow Network Firewall to log to your
CloudWatch Logs log group.

```
{
    "Effect": "Allow",
    "Principal": {
        "Service": "logs.{region}.amazonaws.com"
    },
    "Action": [
        "kms:Encrypt*",
        "kms:Decrypt*",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:Describe*"
    ],
    "Resource": "*"
}
```

###### Policy for a Firehose delivery stream

For Firehose delivery streams, you allow the service principal to generate keys
so that it can put the logging records.

Add the following key policy to your KMS key
to allow Network Firewall to log to your Firehose delivery stream.

```
{
    "Sid": "Allow Network Firewall logs to use the key",
    "Effect": "Allow",
    "Principal": {
        "Service": [
            "delivery.logs.amazonaws.com"
        ]
    },
    "Action": "kms:GenerateDataKey*",
    "Resource": "*"
}
```
