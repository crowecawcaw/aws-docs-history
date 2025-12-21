# IAM Role Setup

The CloudFormation stack in Setup Instructions automates the IAM role setup for you. If you want to manually execute it, please follow the instructions below:

## IAM Role Setup for MCP server

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

## Additional Permissions by Deployment Mode (EMR-EC2/EMR-S)

### EMR-EC2 Applications

Replace Amazon S3 staging bucket in the policy with the Amazon S3 bucket where you want the upgraded artifacts to be stored

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "elasticmapreduce:DescribeCluster",
        "elasticmapreduce:DescribeStep",
        "elasticmapreduce:ListSteps",
        "elasticmapreduce:ListClusters",
        "elasticmapreduce:DescribeJobFlows",
        "elasticmapreduce:AddJobFlowSteps",
        "elasticmapreduce:CreatePersistentAppUI",
        "elasticmapreduce:DescribePersistentAppUI",
        "elasticmapreduce:GetPersistentAppUIPresignedURL"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetBucket*",
        "s3:GetObject*",
        "s3:List*",
        "s3:Put*"
      ],
      "Resource": [
        "arn:aws:s3:::<s3-staging-bucket>",
        "arn:aws:s3:::<s3-staging-bucket>/*"
      ]
    }
  ]
}
```

#### KMS permissions - Staging Bucket

If the staging bucket is encrypted with a CMK, add the following policy. The service will automatically use the CMK configured on the bucket when uploading data.

```
{
  "Effect": "Allow",
  "Action": [
    "kms:GenerateDataKey",
    "kms:Encrypt"
  ],
  "Resource": "arn:aws:kms:<region>:<account-id>:key/<cmk-key-id>"
}
```

### EMR Serverless Applications

Replace Amazon S3 staging bucket in the policy with the Amazon S3 bucket where you want the upgraded artifacts to be stored

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "emr-serverless:StartJobRun",
        "emr-serverless:GetJobRun",
        "emr-serverless:GetApplication",
        "emr-serverless:ListApplications",
        "emr-serverless:GetDashboardForJobRun"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "iam:PassedToService": "emr-serverless.amazonaws.com"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "logs:GetLogEvents",
        "logs:DescribeLogStreams"
      ],
      "Resource": "arn:aws:logs:*:*:log-group:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetBucket*",
        "s3:GetObject*",
        "s3:List*",
        "s3:Put*"
      ],
      "Resource": [
        "arn:aws:s3:::<s3-staging-bucket>",
        "arn:aws:s3:::<s3-staging-bucket>/*"
      ]
    }
  ]
}
```

#### KMS permissions - Staging Bucket

If the staging bucket is encrypted with a CMK, add the following policy. The service will automatically use the CMK configured on the bucket when uploading data

```
{
  "Effect": "Allow",
  "Action": [
    "kms:GenerateDataKey",
    "kms:Encrypt"
  ],
  "Resource": "arn:aws:kms:<region>:<account-id>:key/<cmk-key-id>"
}
```

#### KMS permissions - CloudWatch Logs

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
