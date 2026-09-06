

# IAM Role Setup
<a name="emr-spark-upgrade-agent-iam-role"></a>

## Prerequisites
<a name="emr-spark-upgrade-agent-iam-prerequisites"></a>

Before you begin, ensure you have:
+ An AWS account with IAM administrative access
+ AWS CLI installed and configured. For more information, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
+ An Amazon Amazon S3 bucket for staging upgraded artifacts

Set the following variables for use in subsequent commands (replace `my-staging-bucket` with your bucket name):

```
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
REGION=$(aws configure get region)
STAGING_BUCKET=my-staging-bucket
```

## Step 1: Create the IAM role
<a name="emr-spark-upgrade-agent-iam-step1"></a>

The SMUS MCP server uses your IAM role to authorize operations at the AWS service level. No separate MCP-specific permissions are required.

**To create the IAM role (AWS CLI)**

1. Create a trust policy document:

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

1. Create the role:

   ```
   aws iam create-role \
     --role-name SparkUpgradeMCPRole \
     --assume-role-policy-document file://mcp-trust-policy.json
   ```

## Step 2: Attach permissions for your deployment mode
<a name="emr-spark-upgrade-agent-iam-step2"></a>

Attach the permissions policy that matches your EMR deployment platform.

### Option A: EMR on EC2
<a name="emr-spark-upgrade-agent-iam-emr-ec2"></a>

1. Create the policy document (replace `<STAGING_BUCKET>` with your Amazon S3 bucket name):

   ```
   cat > emr-ec2-upgrade-policy.json << EOF
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
         "Action": ["s3:GetBucket*", "s3:GetObject*", "s3:List*", "s3:Put*"],
         "Resource": [
           "arn:aws:s3:::${STAGING_BUCKET}",
           "arn:aws:s3:::${STAGING_BUCKET}/*"
         ]
       }
     ]
   }
   EOF
   ```

1. Attach the policy:

   ```
   aws iam put-role-policy \
     --role-name SparkUpgradeMCPRole \
     --policy-name EMREC2UpgradeAccess \
     --policy-document file://emr-ec2-upgrade-policy.json
   ```

Alternatively, attach the [AmazonElasticMapReduceFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonElasticMapReduceFullAccess.html) managed policy plus an Amazon S3 policy for your staging bucket.

#### KMS permissions - Staging Bucket
<a name="emr-spark-upgrade-agent-iam-kms-staging"></a>

If the staging bucket is encrypted with a CMK, add the following policy. The service will automatically use the CMK configured on the bucket when uploading data (replace `<KEY_ID>` with your KMS key ID):

```
aws iam put-role-policy \
  --role-name SparkUpgradeMCPRole \
  --policy-name KMSStagingBucketEncrypt \
  --policy-document "{
    \"Version\": \"2012-10-17\",
    \"Statement\": [{
      \"Effect\": \"Allow\",
      \"Action\": [\"kms:GenerateDataKey\", \"kms:Encrypt\"],
      \"Resource\": \"arn:aws:kms:${REGION}:${ACCOUNT_ID}:key/<KEY_ID>\"
    }]
  }"
```

### Option B: EMR Serverless
<a name="emr-spark-upgrade-agent-iam-emr-serverless"></a>

1. Create the policy document (replace `<STAGING_BUCKET>` with your Amazon S3 bucket name):

   ```
   cat > emr-serverless-upgrade-policy.json << EOF
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
         "Action": ["logs:GetLogEvents", "logs:DescribeLogStreams"],
         "Resource": "arn:aws:logs:*:*:log-group:*"
       },
       {
         "Effect": "Allow",
         "Action": ["s3:GetBucket*", "s3:GetObject*", "s3:List*", "s3:Put*"],
         "Resource": [
           "arn:aws:s3:::${STAGING_BUCKET}",
           "arn:aws:s3:::${STAGING_BUCKET}/*"
         ]
       }
     ]
   }
   EOF
   ```

1. Attach the policy:

   ```
   aws iam put-role-policy \
     --role-name SparkUpgradeMCPRole \
     --policy-name EMRServerlessUpgradeAccess \
     --policy-document file://emr-serverless-upgrade-policy.json
   ```

#### KMS permissions - Staging Bucket
<a name="emr-spark-upgrade-agent-iam-kms-staging-serverless"></a>

If the staging bucket is encrypted with a CMK, add the following policy. The service will automatically use the CMK configured on the bucket when uploading data (replace `<KEY_ID>` with your KMS key ID):

```
aws iam put-role-policy \
  --role-name SparkUpgradeMCPRole \
  --policy-name KMSStagingBucketEncrypt \
  --policy-document "{
    \"Version\": \"2012-10-17\",
    \"Statement\": [{
      \"Effect\": \"Allow\",
      \"Action\": [\"kms:GenerateDataKey\", \"kms:Encrypt\"],
      \"Resource\": \"arn:aws:kms:${REGION}:${ACCOUNT_ID}:key/<KEY_ID>\"
    }]
  }"
```

#### KMS permissions - CloudWatch Logs
<a name="emr-spark-upgrade-agent-iam-kms-cloudwatch"></a>

If the CloudWatch Logs are encrypted with a CMK, add the following policy so the service can read the EMR Serverless application logs (replace `<KEY_ID>` with your KMS key ID):

```
aws iam put-role-policy \
  --role-name SparkUpgradeMCPRole \
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
<a name="emr-spark-upgrade-agent-iam-step3"></a>

Configure your MCP client (for example, Claude Desktop or Amazon Q Developer) to use the role ARN you created:

```
echo "arn:aws:iam::${ACCOUNT_ID}:role/SparkUpgradeMCPRole"
```

Refer to your MCP client's documentation for how to configure AWS credentials (typically via an AWS profile that assumes this role).

## Condition keys for MCP server requests
<a name="emr-spark-upgrade-agent-mcp-permissions-change"></a>

Two condition keys are automatically added to all requests made through the SMUS MCP server:
+ `aws:ViaAWSMCPService` – Set to `true` for any request made via an AWS managed MCP server.
+ `aws:CalledViaAWSMCP` – Set to the MCP server service principal (for example, `sagemaker-unified-studio-mcp.amazonaws.com`).

You can use these condition keys to control access to your resources when requests originate from an AWS managed MCP server.

**Example: Allow EMR operations only when accessed via the SMUS MCP server:**

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowEMRReadViaSMUSMCP",
      "Effect": "Allow",
      "Action": [
        "elasticmapreduce:DescribeCluster",
        "elasticmapreduce:ListClusters",
        "elasticmapreduce:ListSteps",
        "emr-serverless:GetJobRun",
        "emr-serverless:GetApplication"
      ],
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

**Example: Deny all operations via any AWS managed MCP server:**

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

**Example: Deny specific operations via a specific AWS managed MCP server:**

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

For more information about condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.