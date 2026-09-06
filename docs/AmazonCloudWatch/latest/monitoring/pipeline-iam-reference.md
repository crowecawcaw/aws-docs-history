

# CloudWatch pipelines IAM policies and permissions
<a name="pipeline-iam-reference"></a>

This section provides IAM requirements for CloudWatch pipelines. Permissions vary based on your data source and integration method.

The following table helps you identify which IAM sections apply to your use case.


| Use case | Integration method | Source type in pipeline configuration | IAM sections you need | 
| --- | --- | --- | --- | 
| [Third-party integrations (API Pull)](data-sources.md#data-sources-third-party) | Pipeline pulls from vendor API using stored credentials | microsoft\_office365, okta\_sso, palo\_alto\_ngfw, and so on. | [API caller permissions](#api-caller-permissions) \+ [Third-party sources (API Pull)](#third-party-api-pull) \+ [Resource policies](#resource-policies) | 
| [Third-party integrations (S3 delivery)](data-sources.md#data-sources-third-party) | Vendor delivers files to your S3 bucket | s3 | [API caller permissions](#api-caller-permissions) \+ [Third-party sources (S3 delivery)](#third-party-s3-delivery) \+ [Resource policies](#resource-policies) | 
| [Custom data from S3](data-sources.md#data-sources-custom) | Your applications write to S3, pipeline reads from bucket | s3 | [API caller permissions](#api-caller-permissions) \+ [Custom data from S3](#custom-data-s3) \+ [Resource policies](#resource-policies) | 
| [Custom data from CloudWatch Logs](data-sources.md#data-sources-custom) | Your applications log to a CloudWatch Logs log group | cloudwatch\_logs | [API caller permissions](#api-caller-permissions) \+ [Custom data from CloudWatch Logs](#custom-data-cloudwatch-logs) | 
| [Vended AWS service logs](data-sources.md#data-sources-aws-services) | AWS services deliver logs to CloudWatch Logs (VPC Flow Logs, Route 53) | cloudwatch\_logs | [API caller permissions](#api-caller-permissions) \+ [Vended AWS service logs](#vended-service-logs) | 
| [CloudWatch Metrics (OTel)](data-sources.md#data-sources-metrics-otel) | AWS services emit metrics through OTLP | cloudwatch\_metrics | [Pipeline rule permissions for CloudWatch Metrics sources](#pipeline-rule-permissions-metrics) | 

**Note**  
S3-based sources (`s3`) require a resource policy after pipeline creation. CloudWatch Logs sources (`cloudwatch_logs`) do not.

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
            "Resource": "arn:aws:iam::{{your-account-id}}:role/{{your-source-role}}",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": [
                        "{{service-principal}}"
                    ],
                    "iam:AssociatedResourceARN": [
                        "arn:aws:observabilityadmin:{{your-region}}:{{your-account-id}}:telemetry-pipeline/*"
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
            "Resource": "arn:aws:cloudwatch:{{your-region}}:{{your-account-id}}:dataset/default"
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
            "Sid": "secrets-manager-access",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue"
            ],
            "Resource": "arn:aws:secretsmanager:{{your-region}}:{{your-account-id}}:secret:{{your-secret-name}}*"
        },
        {
            "Sid": "kms-access",
            "Effect": "Allow",
            "Action": "kms:Decrypt",
            "Resource": "arn:aws:kms:{{your-region}}:{{your-account-id}}:key/{{your-key-id}}"
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
            "Action": [
                "observabilityadmin:CreateTelemetryPipeline",
                "iam:PassRole"
            ],
            "Resource": "*"
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
            "Resource": "arn:aws:secretsmanager:{{your-region}}:{{your-account-id}}:secret:{{your-secret-name}}*"
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
            "Sid": "s3-access",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::{{your-bucket-name}}/*"
        },
        {
            "Sid": "sqs-access",
            "Effect": "Allow",
            "Action": [
                "sqs:ReceiveMessage",
                "sqs:DeleteMessage",
                "sqs:ChangeMessageVisibility"
            ],
            "Resource": "arn:aws:sqs:{{your-region}}:{{your-account-id}}:{{your-queue-name}}"
        },
        {
            "Sid": "kms-access",
            "Effect": "Allow",
            "Action": "kms:Decrypt",
            "Resource": "arn:aws:kms:{{your-region}}:{{your-account-id}}:key/{{your-key-id}}"
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
            "Action": [
                "observabilityadmin:CreateTelemetryPipeline",
                "iam:PassRole"
            ],
            "Resource": "*"
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
            "Resource": "arn:aws:sqs:{{your-region}}:{{your-account-id}}:{{your-queue-name}}"
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

### Custom data from CloudWatch Logs
<a name="custom-data-cloudwatch-logs"></a>

This section applies to your own applications logging to a CloudWatch Logs log group (for example, Lambda functions, ECS containers, or custom EC2 applications).

**Permission policy**

The following policy allows the role to process logs from your specified log groups.

**Example IAM policy for CloudWatch Logs sources**  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "logs-processing-access",
            "Effect": "Allow",
            "Action": [
                "logs:processWithPipeline"
            ],
            "Resource": [
                "arn:aws:logs:{{your-region}}:{{your-account-id}}:log-group:{{your-log-group-01}}",
                "arn:aws:logs:{{your-region}}:{{your-account-id}}:log-group:{{your-log-group-02}}"
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
            "Resource": "arn:aws:logs:{{your-region}}:{{your-account-id}}:log-group:{{your-log-group-name}}",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "{{your-account-id}}",
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
                "logs:DeletePipelineRule",
                "iam:PassRole"
            ],
            "Resource": "*"
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
                "arn:aws:logs:{{your-region}}:{{your-account-id}}:log-group:{{your-log-group}}"
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

The IAM setup is identical to [Custom data from CloudWatch Logs](#custom-data-cloudwatch-logs). Use the same permission policy (`logs:processWithPipeline` scoped to the log group) and the same trust policy (`logs.amazonaws.com`).

Because this uses the `cloudwatch_logs` source type, the caller also needs `logs:PutPipelineRule` and `logs:DeletePipelineRule` permissions. See [Pipeline rule permissions (CloudWatch Logs sources only)](#pipeline-rule-permissions).

## Resource policies
<a name="resource-policies"></a>

CloudWatch Logs resource policies are required for S3-based sources and Secrets Manager-based sources (third-party integrations). Resource policies are **not** required for CloudWatch Logs sources (custom data or vended logs).

After calling `CreateTelemetryPipeline`, you receive a pipeline ARN. You must then call `[logs:PutResourcePolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutResourcePolicy.html)` to allow the CloudWatch pipelines service principal to write to the configured log group.

**Timing constraint**  
You have less than 5 minutes after receiving the pipeline ARN to create this resource policy. If the pipeline becomes active before the policy is in place, data will be dropped.

**Example logs:PutResourcePolicy request**  

```
{
    "policyName": "resourceArn=arn:aws:logs:{{your-region}}:{{your-account-id}}:log-group:{{your-log-group-name}}:*",
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
                        "aws:SourceArn": "arn:aws:observabilityadmin:{{your-region}}:{{your-account-id}}:telemetry-pipeline/{{your-pipeline-id}}"
                    }
                }
            }
        ]
    }
}
```

## Managing resource policies
<a name="managing-resource-policies"></a>

Use the AWS CLI to create or update CloudWatch Logs resource policies for CloudWatch pipelines.

**To check for existing policies**

```
aws logs describe-resource-policies \
    --resource-arn arn:aws:logs:{{your-region}}:{{your-account-id}}:log-group:{{your-log-group-name}}:*
```

**To create a new policy**

```
aws logs put-resource-policy \
    --region {{your-region}} \
    --policy-name "resourceArn=arn:aws:logs:{{your-region}}:{{your-account-id}}:log-group:{{your-log-group-name}}:*" \
    --policy-document file://policy.json
```

**To merge with an existing policy**

If a resource policy already exists, add the new statement to the existing `Statement` array in the policy document, then call `put-resource-policy` again with the merged file.

1. Retrieve the existing policy:

   ```
   aws logs describe-resource-policies \
       --resource-arn arn:aws:logs:{{your-region}}:{{your-account-id}}:log-group:{{your-log-group-name}}:*
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
                       "aws:SourceArn": "arn:aws:observabilityadmin:{{your-region}}:{{your-account-id}}:telemetry-pipeline/{{your-pipeline-id}}"
                   }
               }
           }
       ]
   }
   ```

1. Update the policy:

   ```
   aws logs put-resource-policy \
       --region {{your-region}} \
       --policy-name "resourceArn=arn:aws:logs:{{your-region}}:{{your-account-id}}:log-group:{{your-log-group-name}}:*" \
       --policy-document file://existing-policy.json
   ```

Confirm the policy was created or updated successfully:

```
aws logs describe-resource-policies \
    --resource-arn arn:aws:logs:{{your-region}}:{{your-account-id}}:log-group:{{your-log-group-name}}:*
```

Replace the following placeholders:
+ {{your-region}} – Your AWS Region (for example, us-east-1)
+ {{your-account-id}} – Your 12-digit AWS account ID
+ {{your-log-group-name}} – Your CloudWatch Logs log group name
+ {{your-pipeline-id}} – Your telemetry pipeline ID (returned by `CreateTelemetryPipeline`)

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
                    "aws:SourceAccount": "{{your-account-id}}"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:logs:{{your-region}}:{{your-account-id}}:log-group:*"
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