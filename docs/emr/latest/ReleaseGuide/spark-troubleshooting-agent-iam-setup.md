

# IAM permissions for the Apache Spark agents

## How the Apache Spark agents use your permissions
<a name="spark-agents-iam-overview"></a>

The Apache Spark agents use the IAM identity that your MCP client is configured with, which is the identity in your AWS CLI profile. Authorization works the same way as when you run AWS CLI or AWS SDK commands yourself. The agents can access only what that identity is allowed to access, and your existing IAM policies control every request. You don't need to grant any MCP-specific permissions.

### What the agents do with your permissions
<a name="spark-agents-iam-what-agents-do"></a>
+ **Read only** – The agents read your job runs, job metadata, logs, and Spark UI (Spark History Server) data. They don't start, modify, or stop your jobs.
+ **No access of their own** – For each request, the Amazon SageMaker Unified Studio (SMUS) MCP server uses short-lived credentials for your identity. The server has no access of its own to your resources, and it doesn't store your credentials.
+ **Auditable** – AWS CloudTrail logs the API calls that the agents make, in the same way that it logs any other call from your identity.

### How requests are authorized
<a name="spark-agents-iam-how-authorized"></a>

The SMUS MCP server authenticates each request with SigV4, adds two IAM condition keys to it, and forwards it to the AWS service, such as AWS Glue or Amazon EMR. That service then authorizes the request against your IAM policies.
+ `aws:ViaAWSMCPService` – Set to `true` for requests made through an AWS managed MCP server.
+ `aws:CalledViaAWSMCP` – Set to the service principal of the MCP server, `sagemaker-unified-studio-mcp.amazonaws.com`.

You don't need to reference these keys in your policies for the agents to work. If your identity can already read your job metadata, logs, and Spark History Server data, the agents work without any policy changes.

Because these keys mark requests that come from the agents, you can write policies that treat those requests differently from requests that you make directly. For example, you can deny an action to the agents while your own access to that action stays the same. For more information, see [Understanding IAM for Managed AWS MCP Servers](https://aws.amazon.com/blogs/security/understanding-iam-for-managed-aws-mcp-servers/).

### Choose an identity for the agents
<a name="spark-agents-iam-choose-identity"></a>

You can give the agents either of the following identities:
+ **A dedicated role** – Create a role that has only the read permissions that the agents need. This option follows the practice of least privilege. For instructions, see [How do I create a dedicated IAM role for the agents?](#qa-dedicated-role).
+ **A role that you already have** – Reuse the role that you use to analyze your jobs, or the job run role for your Spark jobs. If the role has more permissions than the agents need, add a `Deny` statement that uses the condition keys. The deny applies only to requests from the agents, so the jobs that use the role aren't affected. For examples, see [How can I get more fine-grained control over the agents' permissions?](#qa-fine-grained-permissions).

To check that your role has what the agents need, see [Confirm your role's permissions](#spark-agents-iam-step1).

## Confirm your role's permissions
<a name="spark-agents-iam-step1"></a>

Two policies on an IAM role control whether the agents can use it:
+ **Permissions policy** – Controls what the role can do. The agents need read access to your job runs, logs, and Spark History Server data.
+ **Trust policy** – Controls who can assume the role. Your IAM principal must be allowed to assume the role so that your MCP client can use it.

Use the following steps to confirm that your role is ready.

1. Check the permissions policy. Compare the policies attached to the role with the permissions for each Spark platform that you use:
   + [EMR on EC2](#spark-agents-iam-policy-emr-ec2)
   + [AWS Glue](#spark-agents-iam-policy-glue)
   + [EMR Serverless](#spark-agents-iam-policy-emr-serverless)
   + [EMR on EKS](#spark-agents-iam-policy-emr-eks)

   You need permissions only for the platforms that you want the agents to analyze. If the role is missing a permission, the agents can't read that data.

1. If you reuse a job run role, check its trust policy. A job run role usually trusts only its service, such as `glue.amazonaws.com` or `emr-serverless.amazonaws.com`. Keep the existing service statement, and add a statement that allows your IAM principal to assume the role. Allow only the specific principal that runs your MCP client, as in the following example:

   ```
   {
     "Effect": "Allow",
     "Principal": { "AWS": "arn:aws:iam::111122223333:role/your-developer-role" },
     "Action": "sts:AssumeRole"
   }
   ```

If your CloudWatch Logs are encrypted with a customer managed KMS key, the role also needs permission to use that key. For more information, see [How do the agents access encrypted CloudWatch Logs?](#qa-kms-cloudwatch-logs).

To configure your MCP client to use your role, see [Set up the Apache Spark agents](spark-troubleshooting-agent-setup.md).

## Frequently asked questions
<a name="spark-agents-iam-faq"></a>

The following questions cover common objections and ways to tailor the agents' access.

### How can I get more fine-grained control over the agents' permissions?
<a name="qa-fine-grained-permissions"></a>

Your role (for example, a job run role) might have more permissions than you want the agents to use. You can keep using it and deny the extra permissions to the agents with condition keys. You don't need to create a new role, and the jobs that use the role aren't affected, because the deny applies only to requests made through the MCP server.

Two condition keys are automatically added to all requests made through the SMUS MCP server:
+ `aws:ViaAWSMCPService` – Set to `true` for any request made through an AWS managed MCP server.
+ `aws:CalledViaAWSMCP` – Set to the MCP server service principal (for example, `sagemaker-unified-studio-mcp.amazonaws.com`).

You can use these condition keys to control access to your resources when requests originate from an AWS managed MCP server.

To deny the extra permissions to the agents, add a `Deny` statement like the second of the following examples to your role.

**Example: Allow AWS Glue read operations only when accessed through the SMUS MCP server:**

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

**Example: Deny delete operations when accessed through any AWS managed MCP server:**

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

For more information about condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

If you'd rather give the agents a role with only the permissions they need, see [How do I create a dedicated IAM role for the agents?](#qa-dedicated-role).

### How do I create a dedicated IAM role for the agents?
<a name="qa-dedicated-role"></a>

You might want to create a new IAM role dedicated to the agents, so that you don't have to modify any existing roles.

#### Create the role with the AWS CLI
<a name="qa-dedicated-role-cli"></a>

The trust policy uses your account ID. Set `ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)`, or replace `${ACCOUNT_ID}` with your account ID.

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

1. Create the role:

   ```
   aws iam create-role \
     --role-name your-role-name \
     --assume-role-policy-document file://mcp-trust-policy.json
   ```

After you create the role, attach the permissions policies for the platforms you use from [Appendix: Example IAM policies](#spark-agents-iam-appendix).

#### Create the role with AWS CloudFormation
<a name="qa-dedicated-role-cfn"></a>

The following AWS CloudFormation template is a quick way to create the role and its assume-role profile. These templates are only samples; modify them to meet your requirements.

The template creates the following resources:

1. An IAM role that has permissions to call the MCP server and the permissions required for the selected platform.

Choose one of the **Launch Stack** buttons in the following table. This launches the stack on the AWS CloudFormation console in the respective Region.


| Region | Launch | 
| --- | --- | 
| US East (Ohio) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-us-east-2.s3.us-east-2.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  | 
| US East (N. Virginia) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-us-east-1.s3.us-east-1.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  | 
| US West (Oregon) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-us-west-2.s3.us-west-2.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  | 
| Asia Pacific (Tokyo) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-ap-northeast-1.s3.ap-northeast-1.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  | 
| Europe (Ireland) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-eu-west-1.s3.eu-west-1.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  | 
| Asia Pacific (Singapore) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-ap-southeast-1.s3.ap-southeast-1.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  | 
| Asia Pacific (Sydney) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-ap-southeast-2.s3.ap-southeast-2.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  | 
| Canada (Central) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-ca-central-1.s3.ca-central-1.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  | 
| South America (São Paulo) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-sa-east-1.s3.sa-east-1.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  | 
| Europe (Frankfurt) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-eu-central-1.s3.eu-central-1.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  | 
| Europe (Stockholm) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-eu-north-1.s3.eu-north-1.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  | 
| Europe (London) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-eu-west-2.s3.eu-west-2.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  | 
| Europe (Paris) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-eu-west-3.s3.eu-west-3.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  | 
| Asia Pacific (Seoul) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-ap-northeast-2.s3.ap-northeast-2.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  | 
| Asia Pacific (Mumbai) |  [![Launch Stack button with information icon.](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/new?templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-ap-south-1.s3.ap-south-1.amazonaws.com%2Fcloudformation%2Fspark-troubleshooting-mcp-setup.yaml&stackName=spark-troubleshooting-mcp-setup)  | 

Proceed to the **Specify stack details** page and enter the **Stack name**. Enter additional information under **Parameters**. Provide the following information and proceed to create the stack.
+ **TroubleshootingRoleName** – Name of the agent IAM role to create.
+ **EnableEMREC2** – Enable EMR on EC2 permissions (default: true).
+ **EnableEMRServerless** – Enable EMR Serverless permissions (default: true).
+ **EnableEMREKS** – Enable EMR on EKS permissions (default: true).
+ **EnableGlue** – Enable AWS Glue permissions (default: true).
+ **CloudWatchKmsKeyArn** – (Optional) ARN of an existing KMS key for CloudWatch Logs encryption (EMR Serverless only; leave empty for default encryption).

You can also download and review [the CloudFormation template](https://github.com/aws-samples/aws-emr-utilities/blob/03c20fece616de23ec0ea5389f0113a5bc65fc3a/utilities/apache-spark-agents/spark-troubleshooting-agent-cloudformation/spark-troubleshooting-mcp-setup.yaml), specify the preceding options, and launch the template yourself with AWS CloudFormation CLI commands. The following is an example:

```
# deploy the stack with CloudFormation CLI commands
aws cloudformation deploy \
  --template-file spark-troubleshooting-mcp-setup.yaml \
  --stack-name spark-troubleshooting-mcp-setup \
  --region <your Spark MCP server launch region> \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
    TroubleshootingRoleName=spark-troubleshooting-role


# retrieve the 1-line instruction to set the local environment variables, which will be used for the following MCP server configuration
aws cloudformation describe-stacks \
  --stack-name spark-troubleshooting-mcp-setup \
  --region <your Spark MCP server launch region> \
  --query "Stacks[0].Outputs[?OutputKey=='ExportCommand'].OutputValue" \
  --output text
```

Open the **Outputs** tab (or retrieve the value from the preceding AWS CloudFormation `describe-stacks` CLI command) and copy the one-line instruction from the AWS CloudFormation output to set your environment variables, then run it in your local environment. The following is an example one-line instruction:

```
export SMUS_MCP_REGION=<your mcp server launch region> && export IAM_ROLE=arn:aws:iam::111122223333:role/spark-troubleshooting-role-xxxxxx
```

Then configure your MCP client to use a profile that assumes the new role, as described in [Set up the Apache Spark agents](spark-troubleshooting-agent-setup.md).

### How do the agents access encrypted CloudWatch Logs?
<a name="qa-kms-cloudwatch-logs"></a>

If your CloudWatch Logs are encrypted with a customer managed KMS key, the agents need `kms:Decrypt` and `kms:DescribeKey` on that key to read the logs. Add these permissions to the role your MCP client uses. For example, the following command adds them as an inline policy. Replace `your-role-name` with your role's name and `<KEY_ID>` with your KMS key ID. The command uses the `ACCOUNT_ID` and `REGION` variables described in [Appendix: Example IAM policies](#spark-agents-iam-appendix).

```
aws iam put-role-policy \
  --role-name your-role-name \
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

### Do the troubleshooting and optimization agents need different permissions or roles?
<a name="qa-same-role-both-agents"></a>

No. Both agents use the same role and permissions. If you set up one agent, you can use the other without changes on any platform that both agents support.

## Appendix: Example IAM policies
<a name="spark-agents-iam-appendix"></a>

This appendix lists the permissions that the agents use at full capability, by platform. Use it to check what your existing role allows. If you created a dedicated role for the agents, attach the policies for the platforms you use to that role.

The following commands use the `ACCOUNT_ID` and `REGION` variables. Set them before you run the commands:

```
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
REGION=$(aws configure get region)
```

The commands use `your-role-name` as an example; replace the `--role-name` value with your own role name.

### EMR on EC2
<a name="spark-agents-iam-policy-emr-ec2"></a>

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

1. Create and attach the policy:

   ```
   aws iam put-role-policy \
     --role-name your-role-name \
     --policy-name EMREC2TroubleshootingAccess \
     --policy-document file://emr-ec2-policy.json
   ```

Alternatively, you can attach the [AmazonElasticMapReduceFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonElasticMapReduceFullAccess.html) AWS managed policy if your role already uses it:

```
aws iam attach-role-policy \
  --role-name your-role-name \
  --policy-arn arn:aws:iam::aws:policy/AmazonElasticMapReduceFullAccess
```

### AWS Glue
<a name="spark-agents-iam-policy-glue"></a>

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
         "Resource": "arn:aws:iam::${ACCOUNT_ID}:role/{{my-job-execution-role-prefix}}*",
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

   Replace {{my-job-execution-role-prefix}} with the name prefix of your AWS Glue job execution roles.

1. Attach the policy:

   ```
   aws iam put-role-policy \
     --role-name your-role-name \
     --policy-name GlueTroubleshootingAccess \
     --policy-document file://glue-policy.json
   ```

### EMR Serverless
<a name="spark-agents-iam-policy-emr-serverless"></a>

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

1. Attach the policy:

   ```
   aws iam put-role-policy \
     --role-name your-role-name \
     --policy-name EMRServerlessTroubleshootingAccess \
     --policy-document file://emr-serverless-policy.json
   ```

### EMR on EKS
<a name="spark-agents-iam-policy-emr-eks"></a>

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

1. Attach the policy:

   ```
   aws iam put-role-policy \
     --role-name your-role-name \
     --policy-name EMREKSTroubleshootingAccess \
     --policy-document file://emr-eks-policy.json
   ```