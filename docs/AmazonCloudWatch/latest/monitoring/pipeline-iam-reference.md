

# CloudWatch pipelines IAM policies and permissions
<a name="pipeline-iam-reference"></a>

This section provides IAM requirements for CloudWatch pipelines. Permissions vary based on your data source and integration method.

The following table helps you identify which IAM sections apply to your use case.


| Use case | Integration method | Source type in pipeline configuration | IAM sections you need | 
| --- | --- | --- | --- | 
| [Third-party integrations (API Pull)](data-sources.md#data-sources-third-party) | Pipeline pulls from vendor API using stored credentials | microsoft\_office365, okta\_sso, palo\_alto\_ngfw, and so on. | [API caller permissions](#api-caller-permissions) \+ [Third-party sources (API Pull)](#third-party-api-pull) \+ [Resource policies](#resource-policies) | 
| [Third-party integrations (S3 delivery)](data-sources.md#data-sources-third-party) | Vendor delivers files to your S3 bucket | s3 | [API caller permissions](#api-caller-permissions) \+ [Third-party sources (S3 delivery)](#third-party-s3-delivery) \+ [Resource policies](#resource-policies) | 
| [Custom data from S3](data-sources.md#data-sources-custom) | Your applications write to S3, pipeline reads from bucket | s3 | [API caller permissions](#api-caller-permissions) \+ [Custom data from S3](#custom-data-s3) \+ [Resource policies](#resource-policies) | 
| [Custom and Syslog data from CloudWatch Logs](data-sources.md#data-sources-custom) | Your applications or the CloudWatch Logs Syslog service deliver logs to a log group | cloudwatch\_logs | [API caller permissions](#api-caller-permissions) \+ [Custom and Syslog data from CloudWatch Logs](#custom-data-cloudwatch-logs) | 
| [Vended AWS service logs](data-sources.md#data-sources-aws-services) | AWS services deliver logs to CloudWatch Logs (VPC Flow Logs, Route 53) | cloudwatch\_logs | [API caller permissions](#api-caller-permissions) \+ [Vended AWS service logs](#vended-service-logs) | 
| [CloudWatch Metrics (OTel)](data-sources.md#data-sources-metrics-otel) | AWS services emit metrics through OTLP | cloudwatch\_metrics | [Pipeline rule permissions for CloudWatch Metrics sources](#pipeline-rule-permissions-metrics) | 

**Note**  
S3-based and third-party API sources require a resource policy for their direct CloudWatch Logs destination. For CloudWatch Logs sources, the `@original` destination does not require a resource policy. Named conditional and templatized destinations use the pipeline source role. For more information, see [Permissions for routed destinations](#routed-destination-permissions).

## API caller permissions
<a name="api-caller-permissions"></a>

The IAM principal that calls `CreateTelemetryPipeline` needs `iam:PassRole` permission for any roles referenced in the pipeline configuration.

**Example PassRole policy template**  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "PassRoleForPipelineSource",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{111122223333}}:role/{{your-source-role}}",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": [
                        "{{service-principal}}"
                    ],
                    "iam:AssociatedResourceARN": [
                        "arn:aws:observabilityadmin:{{us-east-1}}:{{111122223333}}:telemetry-pipeline/*"
                    ]
                }
            }
        }
    ]
}
```

Replace {{service-principal}} with the value from the following table based on your use case.


| Use case | Service principal value | 
| --- | --- | 
| Third-party (API Pull) | telemetry-pipelines.observabilityadmin.amazonaws.com | 
| Third-party (S3 delivery) | telemetry-pipelines.observabilityadmin.amazonaws.com | 
| Custom data from S3 | telemetry-pipelines.observabilityadmin.amazonaws.com | 
| Custom data from CloudWatch Logs | logs.amazonaws.com | 
| Vended AWS service logs | logs.amazonaws.com | 

**Note**  
The `Condition` block is recommended but optional. Without it, the role can be passed to any service.  
For third-party pipelines that use a lookup processor or conditional routing, also allow `logs.amazonaws.com` in `iam:PassedToService`.

### Pipeline rule permissions (CloudWatch Logs sources only)
<a name="pipeline-rule-permissions"></a>

When using `cloudwatch_logs` as a source, the API caller also needs permissions for pipeline rule operations. The `logs:PutPipelineRule` permission is required for `CreateTelemetryPipeline` and `UpdateTelemetryPipeline` operations. The `logs:DeletePipelineRule` permission is required for `DeleteTelemetryPipeline` operations.

**Example IAM policy for CloudWatch Logs pipeline rules**  

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

### Pipeline rule permissions for CloudWatch Metrics sources
<a name="pipeline-rule-permissions-metrics"></a>

When you use `cloudwatch_metrics` as a source, you need permissions for pipeline rule operations. To create or update a pipeline, grant the `cloudwatch:PutPipelineRule` permission. To delete a pipeline, grant the `cloudwatch:DeletePipelineRule` permission. Metrics pipelines do not require `iam:PassRole` or CloudWatch Logs resource policies. You can scope these actions down to the `dataset/default` resource.

**Example IAM policy for CloudWatch metrics pipeline rules**  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "PipelineRuleForCloudWatchMetrics",
            "Effect": "Allow",
            "Action": [
                "cloudwatch:PutPipelineRule",
                "cloudwatch:DeletePipelineRule"
            ],
            "Resource": "arn:aws:cloudwatch:{{us-east-1}}:{{111122223333}}:dataset/default"
        }
    ]
}
```

**Reducing scope with condition keys**

## Source role policies
<a name="source-role-policies"></a><a name="source-specific-iam-policies"></a><a name="trust-relationships"></a>

Each pipeline requires a dedicated IAM role that the service assumes to read your data. The following subsections provide the complete policies (permission and trust) for each use case.

### Third-party sources (API Pull)
<a name="third-party-api-pull"></a>

This section applies to Microsoft Office 365, Microsoft Entra ID, Okta SSO, Palo Alto NGFW, and other vendor API integrations that store credentials in AWS Secrets Manager.

**Permission policy**

The following policy allows the role to retrieve your stored API credentials.

**Example IAM policy for Secrets Manager sources**  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "secretsmanageraccess",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Resource": "arn:aws:secretsmanager:{{us-east-1}}:{{111122223333}}:secret:{{your-secret-name}}*"
        },
        {
            "Sid": "kmsaccess",
            "Effect": "Allow",
            "Action": "kms:Decrypt",
            "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{your-key-id}}"
        }
    ]
}
```

**Note**  
The `kms:Decrypt` statement is only required if your secret in Secrets Manager is encrypted with a customer-managed KMS key.

**Trust policy**

**Example Trust policy for API Pull sources**  

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

#### Complete IAM setup for API Pull pipelines
<a name="api-pull-complete-setup"></a>

The following example shows all the IAM policies needed to create a third-party API Pull pipeline end to end.

**Caller identity policy** — attach to the principal calling `CreateTelemetryPipeline`:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "CreateApiPullPipeline",
            "Effect": "Allow",
            "Action": "observabilityadmin:CreateTelemetryPipeline",
            "Resource": "*"
        },
        {
            "Sid": "PassRoleForApiPullPipeline",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{111122223333}}:role/{{your-source-role}}",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": [
                        "telemetry-pipelines.observabilityadmin.amazonaws.com"
                    ],
                    "iam:AssociatedResourceARN": [
                        "arn:aws:observabilityadmin:{{us-east-1}}:{{111122223333}}:telemetry-pipeline/*"
                    ]
                }
            }
        }
    ]
}
```

**Source role permission policy** — attach to the role the pipeline assumes:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "SecretsManagerAccess",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Resource": "arn:aws:secretsmanager:{{us-east-1}}:{{111122223333}}:secret:{{your-secret-name}}*"
        }
    ]
}
```

**Source role trust policy**:

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

**Note**  
After creating the pipeline, you must also create a resource policy within 5 minutes. See [Resource policies](#resource-policies).

**Note**  
For production use, scope down `iam:PassRole` by using the condition keys shown in [API caller permissions](#api-caller-permissions). If your secret uses a customer-managed KMS key, add `kms:Decrypt` to the source role permission policy.

### Third-party sources (S3 delivery)
<a name="third-party-s3-delivery"></a>

This section applies to any third-party vendor that delivers log files to your S3 bucket (for example, CrowdStrike Falcon, Wiz, or Cisco Umbrella).

**Permission policy**

The following policy allows the role to read objects from S3 and consume SQS notifications.

**Example IAM policy for S3 sources**  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "s3access",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::{{your-bucket-name}}/*"
        },
        {
            "Sid": "sqsaccess",
            "Effect": "Allow",
            "Action": [
                "sqs:ReceiveMessage",
                "sqs:DeleteMessage",
                "sqs:ChangeMessageVisibility"
            ],
            "Resource": "arn:aws:sqs:{{us-east-1}}:{{111122223333}}:{{your-queue-name}}"
        },
        {
            "Sid": "kmsaccess",
            "Effect": "Allow",
            "Action": "kms:Decrypt",
            "Resource": "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{your-key-id}}"
        }
    ]
}
```

**Note**  
The `kms:Decrypt` statement is only required if your S3 bucket or SQS queue uses a customer-managed KMS key for encryption.

**Trust policy**

**Example Trust policy for S3 delivery sources**  

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

#### Complete IAM setup for S3 delivery pipelines
<a name="s3-delivery-complete-setup"></a>

The following example shows all the IAM policies needed to create an S3 delivery pipeline end to end.

**Caller identity policy** — attach to the principal calling `CreateTelemetryPipeline`:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "CreateS3Pipeline",
            "Effect": "Allow",
            "Action": "observabilityadmin:CreateTelemetryPipeline",
            "Resource": "*"
        },
        {
            "Sid": "PassRoleForS3Pipeline",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{111122223333}}:role/{{your-source-role}}",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": [
                        "telemetry-pipelines.observabilityadmin.amazonaws.com"
                    ],
                    "iam:AssociatedResourceARN": [
                        "arn:aws:observabilityadmin:{{us-east-1}}:{{111122223333}}:telemetry-pipeline/*"
                    ]
                }
            }
        }
    ]
}
```

**Source role permission policy** — attach to the role the pipeline assumes:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "S3Access",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::{{your-bucket-name}}/*"
        },
        {
            "Sid": "SqsAccess",
            "Effect": "Allow",
            "Action": [
                "sqs:ReceiveMessage",
                "sqs:DeleteMessage",
                "sqs:ChangeMessageVisibility"
            ],
            "Resource": "arn:aws:sqs:{{us-east-1}}:{{111122223333}}:{{your-queue-name}}"
        }
    ]
}
```

**Source role trust policy**:

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

**Note**  
After creating the pipeline, you must also create a resource policy within 5 minutes. See [Resource policies](#resource-policies).

**Note**  
For production use, scope down `iam:PassRole` by using the condition keys shown in [API caller permissions](#api-caller-permissions). If your S3 bucket or SQS queue uses a customer-managed KMS key, add `kms:Decrypt` to the source role permission policy.

### Custom data from S3
<a name="custom-data-s3"></a>

This section applies to your own applications or infrastructure writing log files to an S3 bucket.

The IAM setup is identical to [Third-party sources (S3 delivery)](#third-party-s3-delivery). Use the same permission policy and trust policy. The pipeline reads from your bucket through SQS event notifications regardless of who wrote the data.

### Custom and Syslog data from CloudWatch Logs
<a name="custom-data-cloudwatch-logs"></a>

This section applies to your own applications logging to a CloudWatch Logs log group (for example, Lambda functions, ECS containers, or custom EC2 applications) and to messages delivered through the CloudWatch Logs Syslog service.

**Permission policy**

The following policy allows the role to process logs from your specified log groups.

**Example IAM policy for CloudWatch Logs sources**  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "logsprocessingaccess",
            "Effect": "Allow",
            "Action": [
                "logs:processWithPipeline"
            ],
            "Resource": [
                "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:{{your-log-group-01}}",
                "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:{{your-log-group-02}}"
            ]
        }
    ]
}
```

You can scope down this permission by using the `logs:data_source_name` and `logs:data_source_type` condition keys to restrict which pipeline sources can invoke transformations. The `logs:data_source_name` value corresponds to the `data_source_name` in your pipeline configuration, and `logs:data_source_type` corresponds to the `data_source_type` in your pipeline configuration.

**Example Permission policy for CloudWatch Logs sources (scoped down with condition keys)**  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowProcessWithPipelineScopedDown",
            "Effect": "Allow",
            "Action": "logs:ProcessWithPipeline",
            "Resource": "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:{{your-log-group-name}}",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "{{111122223333}}",
                    "logs:data_source_name": "{{your-source-name}}",
                    "logs:data_source_type": "{{your-source-type}}"
                }
            }
        }
    ]
}
```

**Note**  
The IAM role for CloudWatch Logs sources requires both the trust policy (to allow `logs.amazonaws.com` to assume the role) and the permission policy (to grant `logs:ProcessWithPipeline`). Without both policies, CloudWatch pipelines cannot transform log events during ingestion.

**Trust policy**

**Example Trust policy for CloudWatch Logs sources**  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "logs.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

**Note**  
No resource policy is needed for CloudWatch Logs source pipelines.

**Note**  
CloudWatch Logs Syslog ingestion requires a separate resource policy to deliver messages to the source log group. For more information, see [Setting up syslog ingestion](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_Syslog_Setup.html).

#### Complete IAM setup for CloudWatch Logs pipelines
<a name="cloudwatch-logs-complete-setup"></a>

The following example shows all the IAM policies needed to create a CloudWatch Logs pipeline end to end.

**Caller identity policy** — attach to the principal calling `CreateTelemetryPipeline`:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "CreateLogsPipeline",
            "Effect": "Allow",
            "Action": [
                "observabilityadmin:CreateTelemetryPipeline",
                "logs:PutPipelineRule",
                "logs:DeletePipelineRule"
            ],
            "Resource": "*"
        },
        {
            "Sid": "PassRoleForLogsPipeline",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{111122223333}}:role/{{your-source-role}}",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": [
                        "logs.amazonaws.com"
                    ],
                    "iam:AssociatedResourceARN": [
                        "arn:aws:observabilityadmin:{{us-east-1}}:{{111122223333}}:telemetry-pipeline/*"
                    ]
                }
            }
        }
    ]
}
```

**Source role permission policy** — attach to the role the pipeline assumes:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "LogsProcessing",
            "Effect": "Allow",
            "Action": [
                "logs:processWithPipeline"
            ],
            "Resource": [
                "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:{{your-log-group}}"
            ]
        }
    ]
}
```

**Source role trust policy**:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "logs.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

**Note**  
For production use, scope down `iam:PassRole` by using the condition keys shown in [API caller permissions](#api-caller-permissions).

### Vended AWS service logs
<a name="vended-service-logs"></a>

This section applies to AWS service logs delivered to CloudWatch Logs, such as VPC Flow Logs, Route 53 query logs, and other AWS vended log types.

The IAM setup is identical to [Custom and Syslog data from CloudWatch Logs](#custom-data-cloudwatch-logs). Use the same permission policy (`logs:processWithPipeline` scoped to the log group) and the same trust policy (`logs.amazonaws.com`).

Because this uses the `cloudwatch_logs` source type, the caller also needs `logs:PutPipelineRule` and `logs:DeletePipelineRule` permissions. See [Pipeline rule permissions (CloudWatch Logs sources only)](#pipeline-rule-permissions).

## Resource policies
<a name="resource-policies"></a>

CloudWatch Logs resource policies are required for the direct CloudWatch Logs destination of an S3-based or third-party API pipeline. The direct destination is the single sink, or the named default route when conditional routing is configured.

For a CloudWatch Logs source, the `@original` destination does not require a resource policy. Named conditional and templatized destinations use the pipeline source role instead of the CloudWatch pipelines service principal. For more information, see [Permissions for routed destinations](#routed-destination-permissions).

After calling `CreateTelemetryPipeline`, you receive a pipeline ARN. You must then call `[logs:PutResourcePolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutResourcePolicy.html)` to allow the CloudWatch pipelines service principal to write to the direct destination log group. The principal that creates the policy needs `logs:PutResourcePolicy`. To inspect or update an existing policy, the principal also needs `logs:DescribeResourcePolicies`.

Use a resource-scoped policy for the destination log group. Resource-scoped policies do not count toward the quota of 10 account-level resource policies per account per Region. The destination log group must exist before you create its resource-scoped policy.

**Timing constraint**  
You have less than 5 minutes after receiving the pipeline ARN to create this resource policy. If the pipeline becomes active before the policy is in place, data will be dropped.

**Example Resource policy for a direct destination**  

```
{
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
            "Resource": "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:{{your-log-group-name}}:*",
            "Condition": {
                "StringEquals": {
                    "aws:SourceArn": "arn:aws:observabilityadmin:{{us-east-1}}:{{111122223333}}:telemetry-pipeline/{{your-pipeline-id}}"
                }
            }
        }
    ]
}
```

## Permissions for routed destinations
<a name="routed-destination-permissions"></a>

Additional conditional and templatized destinations are authorized by identity-based permissions on the IAM role in the pipeline source configuration, not by an additional CloudWatch Logs resource policy.

The pipeline source role must allow `logs:CreateLogGroup` for log groups that the pipeline creates automatically. It must also allow `logs:CreateLogStream` and `logs:PutLogEvents` for every named routed destination. A resource policy does not grant `logs:CreateLogGroup`.

**Example Permission policy for routed destinations**  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "CreateRoutedLogGroups",
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "*"
        },
        {
            "Sid": "WriteRoutedLogEvents",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:{{your-region}}:{{your-account-id}}:log-group:{{your-routed-log-group-prefix}}*:*"
        }
    ]
}
```

Scope the write statement to the exact destination log groups or the narrowest prefix that contains them. Include `logs:CreateLogGroup` only when the pipeline must create conditional or templatized destination log groups.

The role trust policy must allow each service that assumes the role:
+ For S3 and third-party API sources, allow `telemetry-pipelines.observabilityadmin.amazonaws.com`. When the pipeline uses conditional routing, also allow `logs.amazonaws.com`.
+ For CloudWatch Logs sources, use `logs.amazonaws.com`.

## Managing resource policies
<a name="managing-resource-policies"></a>

Use the AWS CLI to create or update CloudWatch Logs resource policies for CloudWatch pipelines.

**To check for existing policies**

```
aws logs describe-resource-policies \
    --policy-scope RESOURCE \
    --resource-arn arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:{{your-log-group-name}}
```

**To create a new policy**

```
aws logs put-resource-policy \
    --region {{us-east-1}} \
    --resource-arn arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:{{your-log-group-name}} \
    --policy-document file://policy.json
```

**To merge with an existing policy**

Each log group can have one resource-scoped policy. If a policy already exists, add the new statement to the existing `Statement` array, then call `put-resource-policy` with the merged file and the current revision ID.

1. Retrieve the existing policy:

   ```
   aws logs describe-resource-policies \
       --policy-scope RESOURCE \
       --resource-arn arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:{{your-log-group-name}}
   ```

1. Add the new statement to the existing `Statement` array:

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
                   "logs:PutLogEvents"
               ],
               "Resource": "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:{{your-log-group-name}}:*"
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
               "Resource": "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:{{your-log-group-name}}:*",
               "Condition": {
                   "StringEquals": {
                       "aws:SourceArn": "arn:aws:observabilityadmin:{{us-east-1}}:{{111122223333}}:telemetry-pipeline/{{your-pipeline-id}}"
                   }
               }
           }
       ]
   }
   ```

1. Update the policy:

   ```
   aws logs put-resource-policy \
       --region {{us-east-1}} \
       --resource-arn arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:{{your-log-group-name}} \
       --expected-revision-id {{your-revision-id}} \
       --policy-document file://existing-policy.json
   ```

Confirm the policy was created or updated successfully:

```
aws logs describe-resource-policies \
    --policy-scope RESOURCE \
    --resource-arn arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:{{your-log-group-name}}
```

Replace the following values in the policy:
+ The AWS Region (shown as `us-east-1`) – Replace with your own Region
+ The 12-digit AWS account ID (shown as `111122223333`) – Replace with your own account ID
+ {{your-log-group-name}} – Your CloudWatch Logs log group name
+ {{your-pipeline-id}} – Your telemetry pipeline ID (returned by `CreateTelemetryPipeline`)
+ {{your-revision-id}} – The revision ID returned by `describe-resource-policies` for an existing resource-scoped policy

## Pipeline condition keys
<a name="pipeline-condition-keys"></a>

CloudWatch pipelines supports IAM condition keys that let you restrict who can create pipelines based on the source name and type. Use these condition keys to enforce governance policies across your organization.Available condition keys

`observabilityadmin:SourceName`  
Restricts pipeline creation to specific source names. Applies to logs pipelines only.

`observabilityadmin:SourceType`  
Restricts pipeline creation to specific source types.

Use these condition keys in identity policies to control which pipelines a principal can create.

`observabilityadmin:SourceType`  
Restricts pipeline creation to specific source types. Supported values include `cloudwatch_logs`, `s3`, `microsoft_office365`, `okta_sso`, and `palo_alto_ngfw`.

**Example Restrict pipeline creation by source type**  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowPipelineCreationForSpecificSourceType",
            "Effect": "Allow",
            "Action": "observabilityadmin:CreateTelemetryPipeline",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "observabilityadmin:SourceType": "cloudwatch_logs"
                }
            }
        }
    ]
}
```

## Source role trust policy conditions
<a name="source-role-trust-conditions"></a>

Use these condition keys in the trust policy of your source role to restrict which account can assume the role. This prevents confused deputy attacks where the service might act on behalf of a different account.

`aws:SourceAccount`  
Restricts role assumption to requests originating from a specific AWS account.

`aws:SourceArn`  
Restricts role assumption to requests originating from a specific resource ARN (for example, a log group).

**Example Trust policy with SourceAccount condition (CloudWatch Logs sources)**  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "logs.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{111122223333}}"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:*"
                }
            }
        }
    ]
}
```

## AI-assisted processor configuration permissions
<a name="ai-assisted-permissions"></a>

To use AI-assisted processor configuration in the CloudWatch pipelines console, the IAM principal must have the `logs:GeneratePipeline` permission. This permission authorizes the generation of processor configurations from natural language descriptions.

**Example IAM policy for AI-assisted processor configuration**  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowGeneratePipeline",
            "Effect": "Allow",
            "Action": "logs:GeneratePipeline",
            "Resource": "*"
        }
    ]
}
```

## Configuring lookup processor permissions
<a name="lookup-processor-permissions"></a>

If your pipeline configuration includes a Lookup processor, the source role needs to have the `logs:GetLookupTable` permission on the lookup table ARN. The role must also be assumable by `logs.amazonaws.com`.

Add the following statement to the source role's permissions policy, for all source types.

**Example Permissions policy statement for lookup table access**  

```
{
    "Sid": "LookupTableAccess",
    "Effect": "Allow",
    "Action": "logs:GetLookupTable",
    "Resource": "arn:aws:logs:{{us-east-1}}:{{111122223333}}:lookup-table:{{your-lookup-table-name}}"
}
```

Replace the following values in the policy:
+ The AWS Region (shown as `us-east-1`) – Replace with your own Region
+ The 12-digit AWS account ID (shown as `111122223333`) – Replace with your own account ID
+ {{your-lookup-table-name}} – The name of your lookup table

The source role trust policy requirement differs by source type.

**Custom data from CloudWatch Logs and vended AWS service logs**

For [Custom and Syslog data from CloudWatch Logs](#custom-data-cloudwatch-logs) and [Vended AWS service logs](#vended-service-logs), the role already trusts `logs.amazonaws.com`, so no trust policy change is required. The following trust policy shows the existing configuration.

**Example Trust policy for CloudWatch Logs sources (no change required)**  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "logs.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

**Third-party sources**

For [Third-party sources (API Pull)](#third-party-api-pull) and [Third-party sources (S3 delivery)](#third-party-s3-delivery), add a second statement to the trust policy so that `logs.amazonaws.com` can assume the role in addition to the existing telemetry service principal. The following trust policy shows both statements.

**Example Trust policy for third-party sources (add logs.amazonaws.com)**  

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
        },
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "logs.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{111122223333}}"
                }
            }
        }
    ]
}
```

**Note**  
If your caller identity policy scopes `iam:PassRole` with the `iam:PassedToService` condition, list `logs.amazonaws.com` alongside `telemetry-pipelines.observabilityadmin.amazonaws.com`. An unconditioned `iam:PassRole` grant already covers both. For more information, see [API caller permissions](#api-caller-permissions).