# IAM Role Setup

The CloudFormation stack in Setup Instructions automates the IAM role setup for you. If you want to manually execute it, please follow the instructions below:

## IAM Role Setup for MCP Server

To access the SMUS Managed MCP server, an IAM role is required with the following inline policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowUseSagemakerUnifiedStudioMcpServer",
            "Effect": "Allow",
            "Action": [
                "sagemaker-unified-studio-mcp:InvokeMcp",
                "sagemaker-unified-studio-mcp:CallReadOnlyTool",
                "sagemaker-unified-studio-mcp:CallPrivilegedTool"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

In the next steps, we will create a profile for this role. Whichever account assumes this role to obtain the credentials should be added to the assume role policy.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAccountToAssumeRole",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::<accountId>:root" },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

## Additional Permissions by Deployment Mode (EMR-EC2/EMR-S/Glue)

### EMR-EC2 Applications

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EMREC2ReadAccess",
            "Effect": "Allow",
            "Action": [
                "elasticmapreduce:DescribeCluster",
                "elasticmapreduce:DescribeStep",
                "elasticmapreduce:ListSteps",
                "elasticmapreduce:ListClusters",
                "elasticmapreduce:DescribeJobFlows"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "EMRS3LogAccess",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": "*"
        },
        {
            "Sid": "EMRPersistentApp",
            "Effect": "Allow",
            "Action": [
                "elasticmapreduce:CreatePersistentAppUI",
                "elasticmapreduce:DescribePersistentAppUI",
                "elasticmapreduce:GetPersistentAppUIPresignedURL"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```

### Glue Jobs

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GlueReadAccess",
            "Effect": "Allow",
            "Action": [
                "glue:GetJob",
                "glue:GetJobRun",
                "glue:GetJobRuns",
                "glue:GetJobs",
                "glue:BatchGetJobs"
            ],
            "Resource": [
                "arn:aws:glue:*:<account id>:job/*"
            ]
        },
        {
            "Sid": "GlueCloudWatchLogsAccess",
            "Effect": "Allow",
            "Action": [
                "logs:GetLogEvents",
                "logs:FilterLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:*:<account id>:log-group:/aws/glue/*"
            ]
        },
        {
            "Sid": "GlueSparkWebUI",
            "Effect": "Allow",
            "Action": [
                "glue:RequestLogParsing",
                "glue:GetLogParsingStatus",
                "glue:GetEnvironment",
                "glue:GetStage",
                "glue:GetStages",
                "glue:GetStageFiles",
                "glue:BatchGetStageFiles",
                "glue:GetStageAttempt",
                "glue:GetStageAttemptTaskList",
                "glue:GetStageAttemptTaskSummary",
                "glue:GetExecutors",
                "glue:GetExecutorsThreads",
                "glue:GetStorage",
                "glue:GetStorageUnit",
                "glue:GetQueries",
                "glue:GetQuery",
                "glue:GetDashboardUrl"
            ],
            "Resource": [
                "arn:aws:glue:*:<account id>:job/*"
            ]
        },
        {
            "Sid": "GluePassRoleAccess",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "iam:PassedToService": "glue.amazonaws.com"
                }
            }
        }
    ]
}
```

### EMR Serverless Applications

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EMRServerlessReadAccess",
            "Effect": "Allow",
            "Action": [
                "emr-serverless:GetJobRun",
                "emr-serverless:GetApplication",
                "emr-serverless:ListApplications",
                "emr-serverless:ListJobRuns",
                "emr-serverless:ListJobRunAttempts",
                "emr-serverless:GetDashboardForJobRun",
                "emr-serverless:ListTagsForResource"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "EMRServerlessCloudWatchLogsAccess",
            "Effect": "Allow",
            "Action": [
                "logs:GetLogEvents",
                "logs:FilterLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:*:<account id>:log-group:/aws/emr-serverless/*"
            ]
        },
        {
            "Sid": "EMRServerlessS3LogsAccess",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": "*"
        }
    ]
}
```

### KMS Permissions - CloudWatch Logs

If the CloudWatch Logs are encrypted with a CMK, add the following policy so the service can read the EMR-Serverless application logs.

```
{
    "Effect": "Allow",
    "Action": [
        "kms:Decrypt",
        "kms:DescribeKey"
    ],
    "Resource": "arn:aws:kms:<region>:<account-id>:key/<cw-logs-cmk-id>"
}
```
