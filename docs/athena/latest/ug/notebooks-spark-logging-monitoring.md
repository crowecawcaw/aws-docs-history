# Logging and monitoring for Apache Spark sessions

From the release Apache Spark version 3.5 onwards, you can specify managed, Amazon S3, or CloudWatch logging as your logging options.

With managed logging and S3 logging, the following table lists the log locations and UI availability that you can expect if you choose those options.

| Option                             | Event logs                  | Container logs              | Application UI |
| ---------------------------------- | --------------------------- | --------------------------- | -------------- |
| Managed logging (default)          | Stored in managed S3 bucket | Stored in managed S3 bucket | Supported      |
| Both managed logging and S3 bucket | Stored in both places       | Stored in S3 bucket         | Supported      |
| Amazon S3 bucket                   | Stored in S3 bucket         | Stored in S3 bucket         | Not supported1 |

1 We suggest that you keep the Managed logging option selected. Otherwise, you can't use the built-in application UIs.

## Managed logging

By default, Athena Spark workgroups stores application logs securely in service-managed S3 buckets for a maximum of 30 days.

You can optionally provide a KMS key (key id, arn, alias, or alias arn) that the service will use to encrypt the managed logs.

```
aws athena start-session \
  --work-group "WORKGROUP" \
  --monitoring-configuration '{
    "ManagedLoggingConfiguration": {
        "Enabled": true,
        "KmsKey": "KMS_KEY"
    },
  }'
  --engine-configuration ''
```

###### Note

If you turn off managed logging, Athena can't troubleshoot your sessions on your behalf. Example: You will not be access the Spark-UI from Amazon SageMaker AI Studio Notebooks or using the `GetResourceDashboard` API.

To turn off this option from the AWS CLI, use the `ManagedLoggingConfiguration` configuration when you start an interactive session.

```
aws athena start-session \
  --work-group "WORKGROUP" \
  --monitoring-configuration '{
    "ManagedLoggingConfiguration": {
      "Enabled": false
    },
  }'
  --engine-configuration ''
```

### Required permissions for managed logging

If you provided a KMS key, you will need the following permissions in the permissions policy for the execution role.

```
{
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
    ],
    "Resource": "*",
    "Effect": "Allow"
}
```

## Amazon S3 logging

You can configure log delivery to Amazon S3 buckets.

To enable S3 log delivery from the AWS CLI, use the `S3LoggingConfiguration` configuration when you start an interactive session.

```
aws athena start-session \
  --work-group "WORKGROUP" \
  --monitoring-configuration '{
    "S3LoggingConfiguration": {
      "Enabled":true,
      "LogLocation": "s3://bucket/",
    },
  }'
  --engine-configuration ''
```

You can optionally provide a KMS key (key id, arn, alias, or alias arn) that the service will use to encrypt the S3 logs.

```
aws athena start-session \
  --work-group "WORKGROUP" \
  --monitoring-configuration '{
    "S3LoggingConfiguration": {
      "Enabled":true,
      "LogLocation": "s3://bucket/",
      "KmsKey": "KMS_KEY"
    },
  }'
  --engine-configuration ''
```

### Required permissions for log delivery to Amazon S3

Before your sessions can deliver logs to Amazon S3 buckets, include the following permissions in the permissions policy for the execution role.

```
{
    "Action": "s3:*",
    "Resource": "*",
    "Effect": "Allow"
}
```

If you provided a KMS key, you will also need the following permissions in the permissions policy for the execution role.

```
{
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
    ],
    "Resource": "*",
    "Effect": "Allow"
}
```

If kms key and bucket are not from same account then KMS needs to allow S3 service principal.

```
{
  "Effect": "Allow",
  "Principal": { "Service": "s3.amazonaws.com" },
  "Action": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:GenerateDataKey*"
  ],
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "aws:SourceAccount": "ACCOUNT_HAVING_KMS_KEY"
    }
  }
}
```

## CloudWatch logging

You can configure log delivery to CloudWatch log groups.

To enable S3 log delivery from the AWS CLI, use the `CloudWatchLoggingConfiguration` configuration when you start an interactive session.

```
aws athena start-session \
  --work-group "WORKGROUP" \
  --monitoring-configuration '{
    "CloudWatchLoggingConfiguration": {
      "Enabled": true,
      "LogGroup": "/aws/athena/sessions/${workgroup}",
      "LogStreamNamePrefix": "session-"
    }
  }'
  --engine-configuration ''
```

All logs will be delivered by default, but you can optionally specify which log types to include.

```
aws athena start-session \
  --work-group "WORKGROUP" \
  --monitoring-configuration '{
    "CloudWatchLoggingConfiguration": {
      "Enabled": true,
      "LogGroup": "/aws/athena/sessions/${workgroup}",
      "LogStreamNamePrefix": "session-",
      "LogTypes": {
          "SPARK_DRIVER": [
              "STDOUT",
              "STDERR"
          ],
          "SPARK_EXECUTOR": [
              "STDOUT",
              "STDERR"
          ]
       }
    }
  }'
  --engine-configuration ''
```

### Required permissions for log delivery to CloudWatch

Before your sessions can deliver logs to CloudWatch log groups, include the following permissions in the permissions policy for the execution role.

```
{
    "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "logs:DescribeLogGroups",
        "logs:DescribeLogStreams"
    ],
    "Resource": "*",
    "Effect": "Allow"
}
```

And following permission to KMS key resource policy.

```
{
  "Effect": "Allow",
  "Principal": {
    "Service": "logs.<region>.amazonaws.com"
  },
  "Action": [
    "kms:Encrypt",
    "kms:Decrypt",
    "kms:ReEncrypt*",
    "kms:GenerateDataKey*",
    "kms:DescribeKey"
  ],
  "Resource": "*"
}
```

## Configuring logging defaults at the Workgroup

You can also specify default logging options at the Workgroup level.

To specify default logging options from the AWS CLI for a workgroup, use the `monitoring-configuration` configuration when creating a new Workgroup:

```
aws athena create-work-group \
  --region "REGION" \
  --name "WORKGROUP_NAME" \
  --monitoring-configuration '{
      "CloudWatchLoggingConfiguration": {
          "Enabled": true,
          "LogGroup": "/aws/athena/sessions/${workgroup}",
          "LogStreamNamePrefix": "session-",
          "LogTypes": {
              "SPARK_DRIVER": [
                  "STDOUT",
                  "STDERR"
              ],
              "SPARK_EXECUTOR": [
                  "STDOUT",
                  "STDERR"
              ]
          }
        },
        "ManagedLoggingConfiguration": {
            "Enabled": true,
            "KmsKey": "KMS_KEY"
        },
        "S3LoggingConfiguration": {
            "Enabled": true,
            "KmsKey": "KMS_KEY"
            "LogLocation": "s3://bucket/",
            "LogTypes": {
                "SPARK_DRIVER": [
                    "STDOUT",
                    "STDERR"
                ],
                "SPARK_EXECUTOR": [
                    "STDOUT",
                    "STDERR"
                ]
            }
        }
    }'
```

To modify defaults logging options from the AWS CLI for a workgroup, use the `monitoring-configuration` configuration when updating a Workgroup. The changes apply to new interactive sessions going forward.

```
aws athena update-work-group \
  --region "REGION" \
  --work-group "WORKGROUP_NAME"
  --monitoring-configuration '{
      "CloudWatchLoggingConfiguration": {
          "Enabled": true,
          "LogGroup": "/aws/athena/sessions/${workgroup}",
          "LogStreamNamePrefix": "session-",
          "LogTypes": {
              "SPARK_DRIVER": [
                  "STDOUT",
                  "STDERR"
              ],
              "SPARK_EXECUTOR": [
                  "STDOUT",
                  "STDERR"
              ]
          }
        },
        "ManagedLoggingConfiguration": {
            "Enabled": true,
            "KmsKey": "KMS_KEY"
        },
        "S3LoggingConfiguration": {
            "Enabled": true,
            "KmsKey": "KMS_KEY"
            "LogLocation": "s3://bucket/",
            "LogTypes": {
                "SPARK_DRIVER": [
                    "STDOUT",
                    "STDERR"
                ],
                "SPARK_EXECUTOR": [
                    "STDOUT",
                    "STDERR"
                ]
            }
        }
    }'
```
