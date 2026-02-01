# Troubleshooting Deployment SOPS

## Cannot connect to AWS MCP Server

Follow the AWS MCP Server troubleshooting and configuration instructions in the [AWS MCP Server Getting Started guide](getting-started-aws-mcp-server.md "getting-started-aws-mcp-server.md").

## Application type not supported

Verify that all prerequisites are met. If your application meets the prerequisites but is still reported as unsupported, prompt your coding agent to attempt the deployment anyway, as the coding agent may still be able to deploy your application with minor adjustments.

## Permission errors during deployment

These SOPs require IAM permissions to create and manage AWS resources such as Amazon S3 buckets, Amazon CloudFront distributions, and AWS CloudFormation stacks. If you encounter permission errors, verify that your configured AWS credentials have the necessary permissions. We recommend creating scoped-down IAM policies that grant only the permissions required for your specific deployment.
