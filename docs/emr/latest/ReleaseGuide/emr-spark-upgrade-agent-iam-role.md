# IAM Role Setup

The CloudFormation stack in Setup Instructions automates the IAM role setup for you. If you want to manually execute it, please follow the instructions below:

## IAM Role Setup for MCP server

###### Upcoming change effective May 29, 2026

The `sagemaker-unified-studio-mcp` permissions shown below will no
longer be required after May 29, 2026. Authorization will instead occur at the AWS
service level using your existing IAM policies. If you use these permissions to deny
access, see [Upcoming permissions change (May 29, 2026)](#emr-spark-upgrade-agent-mcp-permissions-change "#emr-spark-upgrade-agent-mcp-permissions-change") to
update your policies before that date.

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

## Upcoming permissions change (May 29, 2026)

Starting May 29, 2026, the AWS SMUS MCP server will no longer require separate IAM
permissions to authorize MCP server operations. Instead, authorization will occur at the
AWS service level using your existing IAM roles and policies.

Two condition keys will automatically be added to all requests made through the SMUS
MCP server:

- `aws:ViaAWSMCPService` – Set to `true` for
  any request made via an AWS managed MCP server.
- `aws:CalledViaAWSMCP` – Set to the MCP server service
  principal (for example,
  `sagemaker-unified-studio-mcp.amazonaws.com`).

If you currently use the `sagemaker-unified-studio-mcp` permissions to
deny access to the SMUS MCP server, or if you do not want to allow any AWS managed MCP
server initiated actions on your account, you must update your policies before May 29, 2026. Use the new condition keys instead.

**Deny all operations via any AWS managed MCP
server:**

```
{
  "Effect": "Deny",
  "Action": "*",
  "Resource": "*",
  "Condition": {
    "Bool": {
      "aws:ViaAWSMCPService": "true"
    }
  }
}
```

**Deny specific operations via a specific AWS managed MCP
server:**

```
{
  "Effect": "Deny",
  "Action": ["glue:GetJobRun", "glue:StartJobRun"],
  "Resource": "*",
  "Condition": {
    "StringEquals": {
      "aws:CalledViaAWSMCP": "sagemaker-unified-studio-mcp.amazonaws.com"
    }
  }
}
```

For more information about condition keys, see
[AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md")
in the _IAM User Guide_.
