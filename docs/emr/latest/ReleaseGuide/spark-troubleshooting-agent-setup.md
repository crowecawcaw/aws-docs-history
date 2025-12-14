# Setup for Troubleshooting Agent

###### Note

The Apache Spark Troubleshooting Agent uses cross-region inference to process natural
language requests and generate responses. For more details, please refer to [Cross-Region Processing for
the Apache Spark
Troubleshooting Agent](spark-troubleshooting-cross-region-processing.md "spark-troubleshooting-cross-region-processing.md"). The Amazon
SageMaker Unified Studio MCP server is in preview and is subject to change.

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

You can use an AWS CloudFormation template to setup the resource for the MCP server. These
templates are samples that you should modify to meet your requirements. The template creates
the following resources for the troubleshooting process:

1. IAM role which has permissions to call MCP Server and required permissions for
   troubleshooting process for the selected platform.

Choose one of the **Launch Stack** buttons in the following table. This
launches the stack on the AWS CloudFormation console in the respective region.

| Region                    | Launch |
| ------------------------- | ------ |
| US East (Ohio)            |        |
| US East (N. Virginia)     |        |
| US West (Oregon)          |        |
| Asia Pacific (Tokyo)      |        |
| Europe (Ireland)          |        |
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

Proceed to the **Specify stack details** page, enter the **Stack
name**. Enter additional information under **Parameters**. Provide
the following information and proceed to create the stack.

- **TroubleshootingRoleName** - Name of the IAM role to create for
  troubleshooting operations
- **EnableEMREC2** - Enable EMR-EC2 troubleshooting permissions
  (default: true)
- **EnableEMRServerless** - Enable EMR-Serverless troubleshooting
  permissions (default: true)
- **EnableGlue** - Enable Glue troubleshooting permissions
  (default: true)
- **CloudWatchKmsKeyArn** - (Optional) ARN of existing KMS key for
  CloudWatch Logs encryption (EMR Serverless only, leave empty for default encryption)

You may also download and review [the CloudFormation template](https://github.com/aws-samples/aws-emr-utilities/blob/03c20fece616de23ec0ea5389f0113a5bc65fc3a/utilities/apache-spark-agents/spark-troubleshooting-agent-cloudformation/spark-troubleshooting-mcp-setup.yaml "https://github.com/aws-samples/aws-emr-utilities/blob/03c20fece616de23ec0ea5389f0113a5bc65fc3a/utilities/apache-spark-agents/spark-troubleshooting-agent-cloudformation/spark-troubleshooting-mcp-setup.yaml"), specify the options above and launch the template by yourself with CloudFormation CLI commands, see below for an example:

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

Open the Outputs tab (or retrieve from the CloudFormation describe-stacks CLI command above) and copy the 1-line instruction from the CloudFormation output to set your
environment variables, then execute it in your local environment. Example 1-line instruction:

```
export SMUS_MCP_REGION=<your mcp server launch region> && export IAM_ROLE=arn:aws:iam::111122223333:role/spark-troubleshooting-role-xxxxxx
```

Then run the following command locally to setup the IAM profile and MCP server
configuration:

```
# Step 1: Configure AWS CLI Profile
aws configure set profile.smus-mcp-profile.role_arn ${IAM_ROLE}
aws configure set profile.smus-mcp-profile.source_profile <AWS CLI Profile to assume the IAM role - ex: default>
aws configure set profile.smus-mcp-profile.region ${SMUS_MCP_REGION}

# Step 2: if you are using kiro CLI, use the following command to add the MCP configuration
# Add Spark Troubleshooting MCP Server
kiro-cli-chat mcp add \
    --name "sagemaker-unified-studio-mcp-troubleshooting" \
    --command "uvx" \
    --args "[\"mcp-proxy-for-aws@latest\",\"https://sagemaker-unified-studio-mcp.${SMUS_MCP_REGION}.api.aws/spark-troubleshooting/mcp\", \"--service\", \"sagemaker-unified-studio-mcp\", \"--profile\", \"smus-mcp-profile\", \"--region\", \"${SMUS_MCP_REGION}\", \"--read-timeout\", \"180\"]" \
    --timeout 180000 \
    --scope global

# Add Spark Code Recommendation MCP Server
kiro-cli-chat mcp add \
    --name "sagemaker-unified-studio-mcp-code-rec" \
    --command "uvx" \
    --args "[\"mcp-proxy-for-aws@latest\",\"https://sagemaker-unified-studio-mcp.${SMUS_MCP_REGION}.api.aws/spark-code-recommendation/mcp\", \"--service\", \"sagemaker-unified-studio-mcp\", \"--profile\", \"smus-mcp-profile\", \"--region\", \"${SMUS_MCP_REGION}\", \"--read-timeout\", \"180\"]" \
    --timeout 180000 \
    --scope global
```

This should update `~/.kiro/settings/mcp.json` to include the MCP
server configuration as below.

```
{
  "mcpServers": {
    "sagemaker-unified-studio-mcp-troubleshooting": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://sagemaker-unified-studio-mcp.us-east-1.api.aws/spark-troubleshooting/mcp",
        "--service",
        "sagemaker-unified-studio-mcp",
        "--profile",
        "smus-mcp-profile",
        "--region",
        "us-east-1",
        "--read-timeout",
        "180"
      ],
      "timeout": 180000,
      "disabled": false
    },
    "sagemaker-unified-studio-mcp-code-rec": {
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://sagemaker-unified-studio-mcp.us-east-1.api.aws/spark-code-recommendation/mcp",
        "--service",
        "sagemaker-unified-studio-mcp",
        "--profile",
        "smus-mcp-profile",
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

See [Supported Interfaces](spark-troubleshooting-using-troubleshooting-agent.md#supported-interfaces "spark-troubleshooting-using-troubleshooting-agent.md#supported-interfaces") for the configuration guidance for different MCP clients like
Kiro, Cline and GitHub CoPilot.
