

# Getting Started with the Amazon ECS MCP Server
<a name="ecs-mcp-getting-started"></a>

This guide walks you through the steps to set up and use the Amazon ECS MCP Server with your AI code assistants. You'll learn how to configure your environment, connect to the server, and start managing your Amazon ECS clusters through natural language interactions.

**Note**  
The Amazon ECS MCP server is in preview release and is subject to change.

## Prerequisites
<a name="ecs-mcp-prerequisites"></a>

Before you begin, ensure you have:
+ [Created an AWS account with access to Amazon ECS](https://aws.amazon.com/resources/create-account/)
+ [Installed and configured the AWS CLI with credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ [Installed Python 3.10\+](https://www.python.org/)
+ [Installed uv](https://docs.astral.sh/uv/getting-started/installation/)

## Setup
<a name="ecs-mcp-setup"></a>

### Verify prerequisites
<a name="ecs-mcp-verify-prerequisites"></a>

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
<a name="ecs-mcp-iam-permissions"></a>

You will need [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) permissions to make read-only requests to AWS services and interact with the MCP server. You can either leverage [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html), or a single custom policy for more granular control.

**Option 1: Combined managed and custom policy**

1. Attach the AWS managed policy **ReadOnlyAccess** for read-only access to all AWS services

1. Create and attach an additional custom policy for MCP permissions (see the following MCP permissions JSON)

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
    },
    {
      "Sid": "IAMReadOnlyAccessForSecurityAnalysis",
      "Effect": "Allow",
      "Action": [
        "iam:GetRole",
        "iam:ListAttachedRolePolicies",
        "iam:GetPolicy",
        "iam:GetPolicyVersion",
        "iam:ListRolePolicies",
        "iam:GetRolePolicy"
      ],
      "Resource": "*"
    }
  ]
}
```

### Choose and configure an AI assistant
<a name="ecs-mcp-configure-assistant"></a>

Install MCP-compatible AI assistants or any MCP-compatible tool. For instance, you can use [Kiro](https://kiro.dev/), [Cline](https://cline.bot/), [Cursor](https://cursor.com/), or [Claude Code](https://www.claude.com/product/claude-code). Then set up your AI code assistant to use Amazon ECS MCP server through MCP Proxy for AWS, which is required for secure, authenticated access to the Amazon ECS MCP Server. The proxy acts as a client-side bridge, handling AWS SigV4 authentication using your local AWS credentials. The below example uses Kiro CLI. Follow this [link](https://kiro.dev/docs/cli/mcp/) to learn more about setting up MCP in Kiro.

#### Locate MCP configuration file
<a name="ecs-mcp-kiro-config-file"></a>
+ **macOS/Linux:**

  ```
  ~/.kiro/settings/mcp.json
  ```
+ **Windows:**

  ```
  %USERPROFILE%\.kiro\settings\mcp.json
  ```

Create the configuration file if it doesn't exist.

#### Add MCP server configuration
<a name="ecs-mcp-kiro-add-config"></a>

Be sure to replace the region (`{region}`) placeholder with your desired region (e.g., `us-west-2`). Refer to the [Linux containers on AWS Fargate](AWS_Fargate-Regions.md#linux-regions) for a complete list of regions. Also be sure to replace the `{profile}` placeholder with your [AWS CLI profile name](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html), e.g. `default`.

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
<a name="ecs-mcp-kiro-verify"></a>

Restart Kiro CLI, `kiro-cli`, verify that the MCP server is loaded, `/mcp`, and check available tools `/tools`.

#### Verify your setup
<a name="ecs-mcp-verify-setup"></a>

**Test connection**

Ask your AI assistant a simple question to verify the connection:

```
List all ECS clusters in my AWS account
```

You should see a list of your Amazon ECS clusters.

#### Converse with your AI assistant that uses the Amazon ECS MCP server
<a name="ecs-mcp-first-tasks"></a>

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

**Example 5: Assess security posture**

```
Are there any security issues with my production cluster?
Analyze IAM roles and policies for my web-service
Check for overly permissive security groups in my ECS cluster
```

## Common configurations and best practices
<a name="ecs-mcp-common-configs"></a>

### Multiple AWS profiles
<a name="ecs-mcp-multiple-profiles"></a>

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
<a name="ecs-mcp-security-best-practices"></a>

Do not pass secrets or sensitive information via allowed input mechanisms:
+ Do not include secrets or credentials in any configuration files
+ Do not pass sensitive information directly in prompts to the model
+ Do not include secrets in task definitions or service configurations
+ Avoid logging sensitive information in application logs
+ Use or Parameter Store to store sensitive information

## Tool configurations
<a name="ecs-mcp-next-steps"></a>

For a complete list of tools and configurations, see [Amazon ECS MCP Server Tool Configurations](ecs-mcp-tool-configurations.md).