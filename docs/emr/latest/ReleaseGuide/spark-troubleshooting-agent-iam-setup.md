# IAM Role Setup

## Prerequisites

Before you begin, ensure you have:

- An AWS account with IAM administrative access
- AWS CLI installed and configured. For more information, see
  [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

Set the following variables for use in subsequent commands:

```
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
REGION=$(aws configure get region)
```

## Step 1: Create the IAM role

The SMUS MCP server uses your IAM role to authorize operations at the AWS service
level. No separate MCP-specific permissions are required.

**To create the IAM role (AWS CLI)**

1. Create a trust policy document that allows your account to assume the role:

```
cat > mcp-trust-policy.json << EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAccountToAssumeRole",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::${ACCOUNT_ID}:root" },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
```

2. Create the role:

```
aws iam create-role \
  --role-name SparkTroubleshootingMCPRole \
  --assume-role-policy-document file://mcp-trust-policy.json
```

## Step 2: Attach permissions for your deployment mode

Attach the permissions policy that matches your Spark deployment platform. You can
attach one or more of the following depending on which platforms you use.

### Option A: EMR on EC2

1. Create the policy document:

```
cat > emr-ec2-policy.json << 'EOF'
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
      "Resource": ["*"]
    },
    {
      "Sid": "EMRS3LogAccess",
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListBucket"],
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
      "Resource": ["*"]
    }
  ]
}
EOF
```

2. Create and attach the policy:

```
aws iam put-role-policy \
  --role-name SparkTroubleshootingMCPRole \
  --policy-name EMREC2TroubleshootingAccess \
  --policy-document file://emr-ec2-policy.json
```

Alternatively, you can attach the
[AmazonElasticMapReduceFullAccess](../../../aws-managed-policy/latest/reference/AmazonElasticMapReduceFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonElasticMapReduceFullAccess.md")
AWS managed policy if your role already uses it:

```
aws iam attach-role-policy \
  --role-name SparkTroubleshootingMCPRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonElasticMapReduceFullAccess
```

### Option B: AWS Glue

1. Create the policy document:

```
cat > glue-policy.json << EOF
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
      "Resource": ["arn:aws:glue:*:${ACCOUNT_ID}:job/*"]
    },
    {
      "Sid": "GlueCloudWatchLogsAccess",
      "Effect": "Allow",
      "Action": ["logs:GetLogEvents", "logs:FilterLogEvents"],
      "Resource": ["arn:aws:logs:*:${ACCOUNT_ID}:log-group:/aws-glue/*"]
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
      "Resource": ["arn:aws:glue:*:${ACCOUNT_ID}:job/*"]
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
EOF
```

2. Attach the policy:

```
aws iam put-role-policy \
  --role-name SparkTroubleshootingMCPRole \
  --policy-name GlueTroubleshootingAccess \
  --policy-document file://glue-policy.json
```

### Option C: EMR Serverless

1. Create the policy document:

```
cat > emr-serverless-policy.json << EOF
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
      "Resource": ["*"]
    },
    {
      "Sid": "EMRServerlessCloudWatchLogsAccess",
      "Effect": "Allow",
      "Action": ["logs:GetLogEvents", "logs:FilterLogEvents"],
      "Resource": ["arn:aws:logs:*:${ACCOUNT_ID}:log-group:/aws/emr-serverless/*"]
    },
    {
      "Sid": "EMRServerlessS3LogsAccess",
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListBucket"],
      "Resource": "*"
    }
  ]
}
EOF
```

2. Attach the policy:

```
aws iam put-role-policy \
  --role-name SparkTroubleshootingMCPRole \
  --policy-name EMRServerlessTroubleshootingAccess \
  --policy-document file://emr-serverless-policy.json
```

### Option D: EMR on EKS

1. Create the policy document:

```
cat > emr-eks-policy.json << EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "emr-containers:DescribeVirtualCluster",
                "emr-containers:DescribeJobRun",
                "emr-containers:ListJobRuns",
                "emr-containers:ListVirtualClusters"
            ],
            "Resource": "*",
            "Effect": "Allow",
            "Sid": "EMREKSReadAccess"
        },
        {
            "Action": [
                "logs:GetLogEvents",
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams"
            ],
            "Resource": "*",
            "Effect": "Allow",
            "Sid": "EMRCloudWatchLogAccess"
        },
        {
            "Action": [
                "elasticmapreduce:CreatePersistentAppUI",
                "elasticmapreduce:DescribePersistentAppUI",
                "elasticmapreduce:GetPersistentAppUIPresignedURL"
            ],
            "Resource": "*",
            "Effect": "Allow",
            "Sid": "EMRPersistentApp"
        },
        {
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": "*",
            "Effect": "Allow",
            "Sid": "EMREKSS3LogAccess"
        }
    ]
}
EOF
```

2. Attach the policy:

```
aws iam put-role-policy \
  --role-name SparkTroubleshootingMCPRole \
  --policy-name EMREKSTroubleshootingAccess \
  --policy-document file://emr-eks-policy.json
```

### Optional: KMS permissions for encrypted CloudWatch Logs

If your CloudWatch Logs are encrypted with a customer-managed KMS key, add the
following (replace `<KEY_ID>` with your KMS key ID):

```
aws iam put-role-policy \
  --role-name SparkTroubleshootingMCPRole \
  --policy-name KMSCloudWatchLogsDecrypt \
  --policy-document "{
    \"Version\": \"2012-10-17\",
    \"Statement\": [{
      \"Effect\": \"Allow\",
      \"Action\": [\"kms:Decrypt\", \"kms:DescribeKey\"],
      \"Resource\": \"arn:aws:kms:${REGION}:${ACCOUNT_ID}:key/<KEY_ID>\"
    }]
  }"
```

## Step 3: Configure your MCP client

Configure your MCP client (for example, Claude Desktop or Amazon Q Developer) to use
the role ARN you created:

```
echo "arn:aws:iam::${ACCOUNT_ID}:role/SparkTroubleshootingMCPRole"
```

Refer to your MCP client's documentation for how to configure AWS credentials
(typically via an AWS profile that assumes this role).

## Condition keys for MCP server requests

Two condition keys are automatically added to all requests made through the SMUS MCP
server:

- `aws:ViaAWSMCPService` – Set to `true` for
  any request made via an AWS managed MCP server.
- `aws:CalledViaAWSMCP` – Set to the MCP server service
  principal (for example,
  `sagemaker-unified-studio-mcp.amazonaws.com`).

You can use these condition keys to control access to your resources when requests
originate from an AWS managed MCP server.

**Example: Allow Glue read operations only when accessed via the
SMUS MCP server:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowGlueReadViaSMUSMCP",
      "Effect": "Allow",
      "Action": ["glue:GetJob", "glue:GetJobRun", "glue:GetJobRuns"],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:CalledViaAWSMCP": "sagemaker-unified-studio-mcp.amazonaws.com"
        }
      }
    }
  ]
}
```

**Example: Deny delete operations when accessed via any AWS
managed MCP server:**

```
{
  "Effect": "Deny",
  "Action": ["s3:DeleteObject", "s3:DeleteBucket"],
  "Resource": "*",
  "Condition": {
    "Bool": {
      "aws:ViaAWSMCPService": "true"
    }
  }
}
```

For more information about condition keys, see
[AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md")
in the _IAM User Guide_.
