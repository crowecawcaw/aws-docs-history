# Setup for Upgrade Agent

###### Note

The Apache Spark Upgrade Agent uses cross-region inference to process natural language requests and generate responses. For more details please refer to this page on [Cross-region processing for the Apache Spark Upgrade Agent](emr-spark-upgrade-agent-cross-region.md "emr-spark-upgrade-agent-cross-region.md"). The Amazon SageMaker Unified Studio MCP server is in preview and is subject to change.

## Prerequisites

Before we begin our setup process for integration with Kiro CLI, make sure you have the following installed on your workstation:

- [Install AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md")
- [Install Python 3.10+](https://www.python.org/downloads/release/python-3100/ "https://www.python.org/downloads/release/python-3100/")
- [Install the `uv` package manager](https://docs.astral.sh/uv/getting-started/installation/ "https://docs.astral.sh/uv/getting-started/installation/") for
  [MCP Proxy for AWS](https://github.com/aws/mcp-proxy-for-aws?tab=readme-ov-file "https://github.com/aws/mcp-proxy-for-aws?tab=readme-ov-file")
- [Install Kiro CLI](https://kiro.dev/docs/cli/ "https://kiro.dev/docs/cli/")
- AWS local credentials configured (via
  [AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md"), environment variables, or IAM roles) - for local operations such uploading upgraded job artifacts
  for EMR validation job execution.

## Setup Resources

You can use an CloudFormation template to setup the resource for the MCP server. These templates are samples that you should modify to meet your requirements. The template creates the following resources for the upgrade process:

- IAM role which has permissions to call MCP Server and required permissions for upgrade process for the underlying EMR platform.
- Amazon S3 staging bucket used to upload upgrade artifacts and optional KMS key for Amazon S3 encryption.

Choose one of the **Launch Stack** buttons in the following table. This launches the stack on the CloudFormation console in the respective region.

| Region                    | Launch |
| ------------------------- | ------ |
| US East (N. Virginia)     |        |
| US East (Ohio)            |        |
| US West (Oregon)          |        |
| Europe (Ireland)          |        |
| Asia Pacific (Tokyo)      |        |
| Asia Pacific (Singapore)  |        |
| Asia Pacific (Sydney)     |        |
| Canada (Central)          |        |
| South America (São Paulo) |        |
| Europe (Frankfurt)        |        |
| Europe (Stockholm)        |        |
| Europe (London)           |        |
| Europe (Paris)            |        |
| Asia Pacific (Seoul)      |        |
| Asia Pacific (Mumbai)     |        |

Proceed to the **Specify stack details** page, enter the **Stack name**. Enter additional information under **Parameters**. Provide the following information and proceed to create the stack.

- **SparkUpgradeIAMRoleName** - Name of the IAM role to use for Spark upgrade process
- **EnableEMREC2** - Enable EMR-EC2 upgrade permissions (default: true)
- **EnableEMRServerless** - Enable EMR-Serverless upgrade permissions (default: true)
- **StagingBucketPath** - Amazon S3 path for staging artifacts (e.g., s3://my-bucket/spark-upgrade or my-bucket/spark-upgrade). Leave empty to auto-generate a new bucket
- **UseS3Encryption** - Enable KMS encryption for Amazon S3 staging bucket (default: false, set to true to use KMS encryption instead of default S3 encryption)
- **S3KmsKeyArn** - (Optional) ARN of existing KMS key for Amazon S3 bucket encryption. Only used if UseS3Encryption is true and you have an existing bucket with a KMS key
- **CloudWatchKmsKeyArn** - (Optional) ARN of existing KMS key for CloudWatch Logs encryption (EMR Serverless only, leave empty for default encryption)
- **EMRServerlessS3LogPath** - (Optional) S3 path where EMR-Serverless application logs are stored (e.g., s3://my-bucket/emr-serverless-logs or my-bucket/emr-serverless-logs). When provided, grants the IAM role read access to these logs for analysis. Only used when EnableEMRServerless is true
- **ExecutionRoleToGrantS3Access** - (Optional) IAM Role Name or ARN of existing EMR-EC2/EMR-Serverless execution role to grant Amazon S3 staging bucket access. Only applies when a new staging bucket is created. Useful for granting EMR job execution roles access to the staging bucket. Supports both simple role names and ARNs with paths.

You may also download and review [the CloudFormation template](https://github.com/aws-samples/aws-emr-utilities/blob/03c20fece616de23ec0ea5389f0113a5bc65fc3a/utilities/apache-spark-agents/spark-upgrade-agent-cloudformation/spark-upgrade-mcp-setup.yaml "https://github.com/aws-samples/aws-emr-utilities/blob/03c20fece616de23ec0ea5389f0113a5bc65fc3a/utilities/apache-spark-agents/spark-upgrade-agent-cloudformation/spark-upgrade-mcp-setup.yaml"), specify the options above and launch the template by yourself with CloudFormation CLI commands, see below for an example:

```
# deploy the stack with CloudFormation CLI commands
aws cloudformation deploy \
  --template-file spark-upgrade-mcp-setup.yaml \
  --stack-name spark-mcp-setup \
  --region <your mcp server launch region> \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
    ExecutionRoleToGrantS3Access=<your EMR or EMR Serverless job execution role>


# retrieve the 1-line instruction to set the local environment variables, which will be used for the following MCP server configuration
aws cloudformation describe-stacks \
  --stack-name spark-mcp-setup \
  --region <your mcp server launch region> \
  --query "Stacks[0].Outputs[?OutputKey=='ExportCommand'].OutputValue" \
  --output text
```

Open the Outputs tab (or retrieve from the CloudFormation describe-stacks CLI command above) and copy the 1-line instruction `ExportCommand`, then execute it in your local environment. Example 1-line instruction:

```
export SMUS_MCP_REGION=<your mcp server launch region> && export IAM_ROLE=arn:aws:iam::111122223333:role/spark-upgrade-role-xxxxxx && export STAGING_BUCKET_PATH=<your staging bucket path>
```

Then run the following command locally to setup the IAM profile and MCP server configuration

```
# Step 1: Configure AWS CLI Profile
aws configure set profile.spark-upgrade-profile.role_arn ${IAM_ROLE}
aws configure set profile.spark-upgrade-profile.source_profile <AWS CLI Profile to assume the IAM role - ex: default>
aws configure set profile.spark-upgrade-profile.region ${SMUS_MCP_REGION}

# Step 2: if you are using Kiro CLI, use the following command to add the MCP configuration
kiro-cli-chat mcp add \
    --name "spark-upgrade" \
    --command "uvx" \
    --args "[\"mcp-proxy-for-aws@latest\",\"https://sagemaker-unified-studio-mcp.${SMUS_MCP_REGION}.api.aws/spark-upgrade/mcp\", \"--service\", \"sagemaker-unified-studio-mcp\", \"--profile\", \"spark-upgrade-profile\", \"--region\", \"${SMUS_MCP_REGION}\", \"--read-timeout\", \"180\"]" \
    --timeout 180000\
    --scope global
```

This should update `~/.kiro/settings/mcp.json` to include the MCP server configuration as below.

```
{
  "mcpServers": {
    "spark-upgrade": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://sagemaker-unified-studio-mcp.us-east-1.api.aws/spark-upgrade/mcp",
        "--service",
        "sagemaker-unified-studio-mcp",
        "--profile",
        "spark-upgrade-profile",
        "--region",
        "us-east-1",
        "--read-timeout",
        "180"
      ],
      "timeout": 180000,
      "disabled": false
    }
  }
}
```

See [Using the Upgrade Agent](emr-spark-upgrade-agent-using.md "emr-spark-upgrade-agent-using.md") for the configuration guidance for different MCP clients like Kiro, Cline and GitHub CoPilot.
