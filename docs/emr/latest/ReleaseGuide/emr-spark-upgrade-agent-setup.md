

# Setup for Upgrade Agent
<a name="emr-spark-upgrade-agent-setup"></a>

**Note**  
The Apache Spark Upgrade Agent uses cross-region inference to process natural language requests and generate responses. For more details please refer to this page on [Cross-region processing for the Apache Spark Upgrade Agent](emr-spark-upgrade-agent-cross-region.md). 

## Prerequisites
<a name="spark-upgrade-agent-prerequisites"></a>

Before we begin our setup process for integration with Kiro CLI, make sure you have the following installed on your workstation:
+  [ Install AWS CLI ](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) 
+  [ Install Python 3.10\+ ](https://www.python.org/downloads/release/python-3100/) 
+  [ Install the `uv` package manager ](https://docs.astral.sh/uv/getting-started/installation/) for [ MCP Proxy for AWS](https://github.com/aws/mcp-proxy-for-aws?tab=readme-ov-file) 
+  [ Install Kiro CLI ](https://kiro.dev/docs/cli/) 
+ AWS local credentials configured (via [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html), environment variables, or IAM roles) - for local operations such uploading upgraded job artifacts for EMR validation job execution.

## Setup Resources
<a name="spark-upgrade-agent-setup-resources"></a>

You can use an CloudFormation template to setup the resource for the MCP server. These templates are samples that you should modify to meet your requirements. The template creates the following resources for the upgrade process:
+ IAM role which has permissions to call MCP Server and required permissions for upgrade process for the underlying EMR platform.
+ Amazon S3 staging bucket used to upload upgrade artifacts and optional KMS key for Amazon S3 encryption.

Choose one of the **Launch Stack** buttons in the following table. This launches the stack on the CloudFormation console in the respective region.


| Region | Launch | 
| --- | --- | 
| US East (N. Virginia) |  [![Launch Stack button with information icon.](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=spark-upgrade-mcp-setup&templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-us-east-1.s3.us-east-1.amazonaws.com/cloudformation/spark-upgrade-mcp-setup.yaml)  | 
| US East (Ohio) |  [![Launch Stack button with information icon.](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?stackName=spark-upgrade-mcp-setup&templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-us-east-2.s3.us-east-2.amazonaws.com/cloudformation/spark-upgrade-mcp-setup.yaml)  | 
| US West (Oregon) |  [![Launch Stack button with information icon.](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=spark-upgrade-mcp-setup&templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-us-west-2.s3.us-west-2.amazonaws.com/cloudformation/spark-upgrade-mcp-setup.yaml)  | 
| Europe (Ireland) |  [![Launch Stack button with information icon.](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?stackName=spark-upgrade-mcp-setup&templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-eu-west-1.s3.eu-west-1.amazonaws.com/cloudformation/spark-upgrade-mcp-setup.yaml)  | 
| Asia Pacific (Tokyo) |  [![Launch Stack button with information icon.](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/new?stackName=spark-upgrade-mcp-setup&templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-ap-northeast-1.s3.ap-northeast-1.amazonaws.com/cloudformation/spark-upgrade-mcp-setup.yaml)  | 
| Asia Pacific (Singapore) |  [![Launch Stack button with information icon.](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-1#/stacks/new?stackName=spark-upgrade-mcp-setup&templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/cloudformation/spark-upgrade-mcp-setup.yaml)  | 
| Asia Pacific (Sydney) |  [![Launch Stack button with information icon.](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/new?stackName=spark-upgrade-mcp-setup&templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-ap-southeast-2.s3.ap-southeast-2.amazonaws.com/cloudformation/spark-upgrade-mcp-setup.yaml)  | 
| Canada (Central) |  [![Launch Stack button with information icon.](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ca-central-1#/stacks/new?stackName=spark-upgrade-mcp-setup&templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-ca-central-1.s3.ca-central-1.amazonaws.com/cloudformation/spark-upgrade-mcp-setup.yaml)  | 
| South America (São Paulo) |  [![Launch Stack button with information icon.](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=sa-east-1#/stacks/new?stackName=spark-upgrade-mcp-setup&templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-sa-east-1.s3.sa-east-1.amazonaws.com/cloudformation/spark-upgrade-mcp-setup.yaml)  | 
| Europe (Frankfurt) |  [![Launch Stack button with information icon.](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/new?stackName=spark-upgrade-mcp-setup&templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-eu-central-1.s3.eu-central-1.amazonaws.com/cloudformation/spark-upgrade-mcp-setup.yaml)  | 
| Europe (Stockholm) |  [![Launch Stack button with information icon.](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-north-1#/stacks/new?stackName=spark-upgrade-mcp-setup&templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-eu-north-1.s3.eu-north-1.amazonaws.com/cloudformation/spark-upgrade-mcp-setup.yaml)  | 
| Europe (London) |  [![Launch Stack button with information icon.](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/new?stackName=spark-upgrade-mcp-setup&templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-eu-west-2.s3.eu-west-2.amazonaws.com/cloudformation/spark-upgrade-mcp-setup.yaml)  | 
| Europe (Paris) |  [![Launch Stack button with information icon.](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-3#/stacks/new?stackName=spark-upgrade-mcp-setup&templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-eu-west-3.s3.eu-west-3.amazonaws.com/cloudformation/spark-upgrade-mcp-setup.yaml)  | 
| Asia Pacific (Seoul) |  [![Launch Stack button with information icon.](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-2#/stacks/new?stackName=spark-upgrade-mcp-setup&templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-ap-northeast-2.s3.ap-northeast-2.amazonaws.com/cloudformation/spark-upgrade-mcp-setup.yaml)  | 
| Asia Pacific (Mumbai) |  [![Launch Stack button with information icon.](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/images/cloudformation-launch-stack-button.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-south-1#/stacks/new?stackName=spark-upgrade-mcp-setup&templateURL=https%3A%2F%2Fsmus-mcp-cfn-template-prod-ap-south-1.s3.ap-south-1.amazonaws.com/cloudformation/spark-upgrade-mcp-setup.yaml)  | 

Proceed to the **Specify stack details** page, enter the **Stack name**. Enter additional information under **Parameters**. Provide the following information and proceed to create the stack.
+ **SparkUpgradeIAMRoleName** - Name of the IAM role to use for Spark upgrade process
+ **EnableEMREC2** - Enable EMR-EC2 upgrade permissions (default: true)
+ **EnableEMRServerless** - Enable EMR-Serverless upgrade permissions (default: true)
+ **StagingBucketPath** - Amazon S3 path for staging artifacts (e.g., s3://my-bucket/spark-upgrade or my-bucket/spark-upgrade). Leave empty to auto-generate a new bucket
+ **UseS3Encryption** - Enable KMS encryption for Amazon S3 staging bucket (default: false, set to true to use KMS encryption instead of default S3 encryption)
+ **S3KmsKeyArn** - (Optional) ARN of existing KMS key for Amazon S3 bucket encryption. Only used if UseS3Encryption is true and you have an existing bucket with a KMS key
+ **CloudWatchKmsKeyArn** - (Optional) ARN of existing KMS key for CloudWatch Logs encryption (EMR Serverless only, leave empty for default encryption)
+ **EMRServerlessS3LogPath** - (Optional) S3 path where EMR-Serverless application logs are stored (e.g., s3://my-bucket/emr-serverless-logs or my-bucket/emr-serverless-logs). When provided, grants the IAM role read access to these logs for analysis. Only used when EnableEMRServerless is true
+ **ExecutionRoleToGrantS3Access** - (Optional) IAM Role Name or ARN of existing EMR-EC2/EMR-Serverless execution role to grant Amazon S3 staging bucket access. Only applies when a new staging bucket is created. Useful for granting EMR job execution roles access to the staging bucket. Supports both simple role names and ARNs with paths.

You may also download and review [the CloudFormation template](https://github.com/aws-samples/aws-emr-utilities/blob/03c20fece616de23ec0ea5389f0113a5bc65fc3a/utilities/apache-spark-agents/spark-upgrade-agent-cloudformation/spark-upgrade-mcp-setup.yaml), specify the options above and launch the template by yourself with CloudFormation CLI commands, see below for an example:

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

See [Using the Upgrade Agent](emr-spark-upgrade-agent-using.md) for the configuration guidance for different MCP clients like Kiro, Cline and GitHub CoPilot.