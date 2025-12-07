# CloudWatch pipelines IAM policies and permissions

This section provides detailed IAM requirements for CloudWatch pipelines, including permissions for API
callers, source-specific policies, trust relationships, and resource policies.

## API caller permissions

Any role specified in the pipeline configuration that calls the
`CreateTelemetryPipeline` API (such as S3 source roles, Secrets Manager
access roles, or CloudWatch Logs source roles) must have specific permissions to pass
roles.

**PassRole permissions**

Required for any roles specified in the pipeline configuration (S3 source roles,
Secrets Manager access roles, or CloudWatch Logs source roles).

###### Example IAM policy for S3 sources

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PassRoleForS3Source",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::`your-account-id`:role/`your-s3-source-role`"
        }
    ]
}
```

###### Example IAM policy for Secrets Manager sources

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PassRoleForSecretsManagerSource",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::`your-account-id`:role/`your-secrets-manager-role`"
        }
    ]
}
```

###### Example IAM Policy for CloudWatch Logs Sources

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PassRoleForCloudWatchLogsSource",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::`your-account-id`:role/`your-cloudwatch-logs-role`""
        }
  ]
}
```

**Pipeline rule permissions**

When using `cloudwatch_logs` source for Create/Update operations
(`logs:PutPipelineRule`) and Delete operations
(`logs:DeletePipelineRule`) the role must also have permissions to
perform those operations.

###### Example IAM policy for CloudWatch Logs pipeline rules

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PipelineRuleForCloudWatchLogs",
            "Effect": "Allow",
            "Action": [
                "logs:PutPipelineRule",
                "logs:DeletePipelineRule"
            ],
            "Resource": "*"
        }
    ]
}
```

**Reducing scope with condition keys**

To scope down the permission policy to telemetry pipelines, you can specify Condition
Keys as shown in the following examples:

###### Example IAM policy for S3 sources (basic)

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PassRoleForS3Source",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::`your-account-id`:role/`your-s3-source-role`"
        }
    ]
}
```

###### Example IAM policy for S3 sources (scoped down with condition keys)

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PassRoleForS3Source",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::`your-account-id`:role/`your-s3-source-role`",
            "Condition": {
              "StringEquals": {
                "iam:PassedToService": [
                  "telemetry-pipelines.observabilityadmin.amazonaws.com"
                ],
                "iam:AssociatedResourceARN": [
                  "arn:aws:observabilityadmin:`your-region`:`your-account-id`:telemetry-pipeline/*"
                ]
              }
            }
        }
    ]
}
```

###### Example IAM policy for Secrets Manager sources (basic)

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PassRoleForSecretsManagerSource",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::`your-account-id`:role/`your-secrets-manager-role`"
        }
    ]
}
```

###### Example IAM policy for Secrets Manager sources (scoped down with condition keys)

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
          "Sid": "PassRoleForSecretsManagerSource",
          "Effect": "Allow",
          "Action": "iam:PassRole",
          "Resource": "arn:aws:iam::`your-account-id`:role/`your-secrets-manager-role`",
          "Condition": {
            "StringEquals": {
              "iam:PassedToService": [
                "telemetry-pipelines.observabilityadmin.amazonaws.com"
              ],
              "iam:AssociatedResourceARN": [
                "arn:aws:observabilityadmin:`your-region`:`your-account-id`:telemetry-pipeline/*"
              ]
            }
          }
        }
    ]
}
```

###### Example IAM policy for CloudWatch Logs sources (scoped down with condition keys)

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
          "Sid": "PassRoleForCloudWatchLogsSource",
          "Effect": "Allow",
          "Action": "iam:PassRole",
          "Resource": "arn:aws:iam::`your-account-id`:role/`your-cloudwatch-logs-role`",
          "Condition": {
            "StringEquals": {
              "iam:PassedToService": [
                "logs.amazonaws.com"
              ],
              "iam:AssociatedResourceARN": [
                "arn:aws:observabilityadmin:`your-region`:`your-account-id`:telemetry-pipeline/*"
              ]
            }
          }
        }
    ]
}
```

## Source-specific IAM policies

Different source types require specific IAM permissions to access their respective
data sources.

**CloudWatch Logs sources**

For CloudWatch Logs sources, any IAM role specified in the pipeline configuration must have a trust relationship with `logs.amazonaws.com`.

###### Example IAM role trust policy for CloudWatch Logs sources (basic)

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            ""Effect": "Allow",
            "Principal": {
                "Service": "logs.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

**S3 sources**

For S3 sources, customers must provide an IAM role with permissions to access S3
objects and SQS queues.

###### Example IAM policy for S3 sources

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "s3-access",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::`your-bucket-name`/*"
        },
        {
            "Sid": "sqs-access",
            "Effect": "Allow",
            "Action": [
                "sqs:ReceiveMessage",
                "sqs:DeleteMessage",
                "sqs:ChangeMessageVisibility"
            ],
            "Resource": "arn:aws:sqs:`your-region`:`your-account-id`:`your-queue-name`"
        },
        {
            "Sid": "kms-access",
            "Effect": "Allow",
            "Action": "kms:Decrypt",
            "Resource": "arn:aws:kms:`your-region`:`your-account-id`:key/`your-key-id`",
            "Condition": {
                "Comment": "Only required if S3 buckets and/or SQS queue uses KMS encryption"
            }
        }
    ]
}
```

**Sources using AWS Secrets Manager**

For sources that reference AWS Secrets Manager (Microsoft Office 365, Microsoft
Entra ID, Palo Alto NGFW), customers must provide an IAM role with Secrets
Manager access.

###### Example IAM policy for Secrets Manager sources

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "secrets-manager-access",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Resource": "arn:aws:secretsmanager:`your-region`:`your-account-id`:secret:`your-secret-name`*"
        },
        {
            "Sid": "kms-access",
            "Effect": "Allow",
            "Action": "kms:Decrypt",
            "Resource": "arn:aws:kms:`your-region`:`your-account-id`:key/`your-key-id`",
            "Condition": {
                "Comment": "Only required if Secrets Manager uses KMS encryption"
            }
        }
    ]
}
```

## Trust relationships

Any IAM role specified in the pipeline configuration must have a trust relationship
with the CloudWatch pipelines service principal.

**Pipeline role trust policy**

All pipeline roles must trust the
`telemetry-pipelines.observabilityadmin.amazonaws.com` service
principal.

###### Example Trust policy for pipeline roles

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "telemetry-pipelines.observabilityadmin.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

## Resource policies

CloudWatch Logs resource policies are required for pipelines that write to log groups, except
for pipelines using the `cloudwatch_logs` source.

**CloudWatch Logs** resource policy

After calling `CreateTelemetryPipeline` API, you will receive a pipeline
ARN. For pipelines where the source is not `cloudwatch_logs`, customers must
call `logs:PutResourcePolicy` to allow the CloudWatch pipelines service principal to write
to the configured log group.

###### Timing constraint

You have a limited time window (less than 5 minutes) to create the resource policy
after receiving the pipeline ARN. If the pipeline becomes active before the policy
is in place, data will be dropped.

###### Example logs:PutResourcePolicy request

```
{
    "policyName": "resourceArn=arn:aws:logs:`your-region`:`your-account-id`:log-group:`your-log-group-name`:*",
    "policyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "telemetry-pipelines.observabilityadmin.amazonaws.com"
                },
                "Action": [
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],

                "Condition": {
                    "StringEquals": {
                        "aws:SourceArn": "arn:aws:observabilityadmin:`your-region`:`your-account-id`:telemetry-pipeline/`your-pipeline-id`"
                    }
                }
            }
        ]
    }
}
```

## Managing resource policies

This guide provides steps for creating or updating a CloudWatch Logs resource policy for
telemetry pipelines using the AWS CLI.

Check for existing policies:

```
aws logs describe-resource-policies --resource-arn arn:aws:logs:`your-region`:`your-account-id`:log-group:`your-log-group-name`:*
```

This returns all existing resource policies attached to the log group. Look for any policy that might already
be associated with your log group.

If no resource policy exists, create a new one:

```
aws logs put-resource-policy \
        --region <YOUR-REGION> \
        --policy-name  "resourceArn": "arn:aws:logs:`your-region`:`your-account-id`:log-group:`your-log-group-name`:*"\
        --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "telemetry-pipelines.observabilityadmin.amazonaws.com"
            },
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:SourceArn": "arn:aws:observabilityadmin:`your-region`:`your-account-id`:telemetry-pipeline/`your-pipeline-id`"
                }
            }
        }
    ]
}'
```

Replace the following placeholders:

- `your-region` - Your AWS region (e.g.,
  us-east-1)
- `your-account-id` - Your 12-digit AWS account
  ID
- `your-log-group-name` - Your CloudWatch Logs log group
  name
- `your-pipeline-id` - Your telemetry pipeline ID

If a resource policy already exists, merge the new statement with it:

1. Retrieve the existing policy:

```
aws logs describe-resource-policies --resource-arn arn:aws:logs:`your-region`:`your-account-id`:log-group:`your-log-group-name`:*
```

2. Open `existing-policy.json` and add the new statement to
   the existing `Statement` array:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "existing-service.amazonaws.com"
            },
            "Action": [
                "logs:SomeAction"
            ]
        },
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "telemetry-pipelines.observabilityadmin.amazonaws.com"
            },
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],

            "Condition": {
                "StringEquals": {
                    "aws:SourceArn": "arn:aws:observabilityadmin:`your-region`:`your-account-id`:telemetry-pipeline/`your-pipeline-id`"
                }
            }
        }
    ]
}
```

3. Update the policy:

```
aws logs put-resource-policy \
        --region `your-region` \
        --policy-name resourceArn=arn:aws:logs:`your-region`:`your-account-id`:log-group:`your-log-group-name`:* \
        --policy-document file://existing-policy.json
```

Confirm the policy was created or updated successfully:

```
aws logs describe-resource-policies --resource-arn arn:aws:logs:`your-region`:`your-account-id`:log-group:`your-log-group-name`:*
```
