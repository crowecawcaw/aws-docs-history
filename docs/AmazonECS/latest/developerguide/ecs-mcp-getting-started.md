# Getting Started with the Amazon ECS MCP Server

This guide walks you through the steps to set up and use the Amazon ECS MCP Server with your AI code assistants. You'll learn how to configure your environment, connect to the server, and start managing your Amazon ECS clusters through natural language interactions.

###### Note

The Amazon ECS MCP server is in preview release and is subject to change.

## Prerequisites

Before you begin, ensure you have:

- [Created an AWS account with access to Amazon ECS](https://aws.amazon.com/resources/create-account/ "https://aws.amazon.com/resources/create-account/")
- [Installed and configured the AWS CLI with credentials](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md")
- [Installed Python 3.10+](https://www.python.org/ "https://www.python.org/")
- [Installed uv](https://docs.astral.sh/uv/getting-started/installation/ "https://docs.astral.sh/uv/getting-started/installation/")

## Setup

### Verify prerequisites

Check that your Python version is 3.10 or higher

```
python3 --version
```

Check uv installation

```
uv --version
```

Verify AWS CLI configuration

```
aws configure list
```

### Set up IAM permissions

You will need [IAM](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") permissions to make read-only requests to AWS services and interact with the MCP server. You can either leverage [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md"), or a single custom policy for more granular control.

**Option 1: Combined managed and custom policy**

1. Attach the AWS managed policy **ReadOnlyAccess** for read-only access to all AWS services
2. Create and attach an additional custom policy for MCP permissions (see MCP permissions JSON below)

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "MCPServerAccess",
      "Effect": "Allow",
      "Action": [
        "ecs-mcp:InvokeReadOnlyTools",
        "ecs-mcp:UseMcp"
      ],
      "Resource": "*"
    }
  ]
}
```

**Option 2: Single custom policy (most granular control)**

Alternatively, you can create and attach a single custom JSON policy that includes both AWS service permissions and MCP permissions:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "MCPServerAccess",
      "Effect": "Allow",
      "Action": [
        "ecs-mcp:InvokeReadOnlyTools",
        "ecs-mcp:UseMcp"
      ],
      "Resource": "*"
    },
    {
      "Sid": "ECSReadOnlyAccess",
      "Effect": "Allow",
      "Action": [
        "ecs:ListAccountSettings",
        "ecs:ListClusters",
        "ecs:ListContainerInstances",
        "ecs:ListTaskDefinitions",
        "ecs:ListServices",
        "ecs:ListServiceDeployments",
        "ecs:ListTasks",
        "ecs:DescribeClusters",
        "ecs:DescribeCapacityProviders",
        "ecs:DescribeContainerInstances",
        "ecs:DescribeTaskDefinition",
        "ecs:DescribeServices",
        "ecs:DescribeServiceDeployments",
        "ecs:DescribeServiceRevisions",
        "ecs:DescribeTaskSets",
        "ecs:DescribeTasks"
      ],
      "Resource": "*"
    },
    {
      "Sid": "CloudWatchLogsReadOnlyAccess",
      "Effect": "Allow",
      "Action": [
        "logs:DescribeLogGroups",
        "logs:DescribeLogStreams",
        "logs:GetLogEvents",
        "logs:FilterLogEvents"
      ],
      "Resource": "*"
    },
    {
      "Sid": "ELBReadOnlyAccess",
      "Effect": "Allow",
      "Action": [
        "elasticloadbalancing:DescribeLoadBalancers",
        "elasticloadbalancing:DescribeTargetGroups",
        "elasticloadbalancing:DescribeListeners"
      ],
      "Resource": "*"
    },
    {
      "Sid": "EC2ReadOnlyAccess",
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeVpcs",
        "ec2:DescribeSubnets",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeRouteTables",
        "ec2:DescribeNetworkInterfaces"
      ],
      "Resource": "*"
    },
    {
      "Sid": "ECRReadOnlyAccess",
      "Effect": "Allow",
      "Action": [
        "ecr:DescribeRepositories",
        "ecr:DescribeImages"
      ],
      "Resource": "*"
    }
  ]
}
```

### Choose and configure an AI assistant

Install MCP-compatible AI assistants or any MCP-compatible tool. For instance, you can use [Kiro](https://kiro.dev/ "https://kiro.dev/"), [Cline](https://cline.bot/ "https://cline.bot/"), [Cursor](https://cursor.com/ "https://cursor.com/"), or [Claude Code](https://www.claude.com/product/claude-code "https://www.claude.com/product/claude-code"). Then set up your AI code assistant to use Amazon ECS MCP server through MCP Proxy for AWS, which is required for secure, authenticated access to the Amazon ECS MCP Server. The proxy acts as a client-side bridge, handling AWS SigV4 authentication using your local AWS credentials. The below example uses Kiro CLI. Follow this [link](https://kiro.dev/docs/cli/mcp/ "https://kiro.dev/docs/cli/mcp/") to learn more about setting up MCP in Kiro.

#### Locate MCP configuration file

- **macOS/Linux:**

```
~/.kiro/settings/mcp.json
```

- **Windows:**

```
%USERPROFILE%\.kiro\settings\mcp.json
```

Create the configuration file if it doesn't exist.

#### Add MCP server configuration

Be sure to replace the region (`{region}`) placeholder with your desired region (e.g., `us-west-2`). Refer to the [Linux containers on AWS Fargate](AWS_Fargate-Regions.md#linux-regions "AWS_Fargate-Regions.md#linux-regions") for a complete list of regions. Also be sure to replace the `{profile}` placeholder with your [AWS CLI profile name](../../../cli/latest/userguide/getting-started-quickstart.md "../../../cli/latest/userguide/getting-started-quickstart.md"), e.g. `default`.

**For Mac/Linux:**

```
{
  "mcpServers": {
    "ecs-mcp": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://ecs-mcp.{region}.api.aws/mcp",
        "--service",
        "ecs-mcp",
        "--profile",
        "{profile}",
        "--region",
        "{region}"
      ]
    }
  }
}
```

**For Windows:**

```
{
  "mcpServers": {
    "ecs-mcp": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "--from",
        "mcp-proxy-for-aws@latest",
        "mcp-proxy-for-aws.exe",
        "https://ecs-mcp.{region}.api.aws/mcp",
        "--service",
        "ecs-mcp",
        "--profile",
        "{profile}",
        "--region",
        "{region}"
      ]
    }
  }
}
```

#### Verify configuration

Restart Kiro CLI, `kiro-cli`, verify that the MCP server is loaded, `/mcp`, and check available tools `/tools`.

#### Verify your setup

**Test connection**

Ask your AI assistant a simple question to verify the connection:

```
List all ECS clusters in my AWS account
```

You should see a list of your Amazon ECS clusters.

#### Converse with your AI assistant that uses the Amazon ECS MCP server

**Example 1: Monitor deployments**

```
Check deployment status for my web-service in production-cluster
Show me the ALB URL for my deployed service
Get service events for the last hour
```

**Example 2: Investigate container health**

```
Show me all tasks that failed in the last 2 hours
Why are my containers failing health checks?
Display container logs for my api-service
```

**Example 3: Troubleshoot failures**

```
Analyze task failures in my production cluster
Check for image pull errors in the last 30 minutes
Why is my task definition stuck in DELETE_IN_PROGRESS state?
```

**Example 4: Inspect configurations**

```
Show me the network configuration for my web-service
What security groups are attached to my service?
List all VPC and subnet details for my ECS service
```

## Common configurations and best practices

### Multiple AWS profiles

If you work with multiple AWS accounts, create separate MCP server configurations.

**For Mac/Linux:**

```
{
  "mcpServers": {
    "ecs-mcp-prod": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://ecs-mcp.{region}.api.aws/mcp",
        "--service",
        "ecs-mcp",
        "--profile",
        "production",
        "--region",
        "us-west-2"
      ]
    },
    "ecs-mcp-dev": {
      "disabled": false,
      "type": "stdio",
      "command": "uvx",
      "args": [
        "mcp-proxy-for-aws@latest",
        "https://ecs-mcp.{region}.api.aws/mcp",
        "--service",
        "ecs-mcp",
        "--profile",
        "development",
        "--region",
        "us-east-1"
      ]
    }
  }
}
```

### Security best practices

Do not pass secrets or sensitive information via allowed input mechanisms:

- Do not include secrets or credentials in any configuration files
- Do not pass sensitive information directly in prompts to the model
- Do not include secrets in task definitions or service configurations
- Avoid logging sensitive information in application logs
- Use or Parameter Store to store sensitive information

## Tool configurations

For a complete list of tools and configurations, see [Amazon ECS MCP Server Tool Configurations](ecs-mcp-tool-configurations.md "ecs-mcp-tool-configurations.md").
