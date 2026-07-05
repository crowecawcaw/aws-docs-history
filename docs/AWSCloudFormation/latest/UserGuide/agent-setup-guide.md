# Agent setup guide

AI coding agents can accelerate infrastructure development by providing intelligent
assistance for CloudFormation template authoring, pre-deployment validation, deployment
troubleshooting, and CDK code generation. By configuring your agent with the CloudFormation
skill and the AWS IaC MCP Server, you equip it with the expertise required to build and manage
infrastructure as code on AWS.

## Work with your coding agent

For a quick-start reference, you can drop this link directly into your agent's
context:

```
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/samples/aws-cloudformation-agent-setup.md
```

Choose the installation method that matches your development environment.

## Prerequisites

Ensure the following prerequisites are in place:

- [uv](https://docs.astral.sh/uv/ "https://docs.astral.sh/uv/") installed on your system.
- [Node.js](https://nodejs.org/ "https://nodejs.org/") (v18+) installed on your system
  (required for skills installation).
- (Optional) An AWS account with IAM credentials set up on your local machine.
  Credentials are required for tools that execute AWS API calls (template validation,
  deployment troubleshooting), but not for documentation search. If you do not have
  credentials configured, see [Configuring
  the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") for detailed instructions.

## What gets installed

| Component                | What it provides                                                                                                                                                                                                 |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CloudFormation skill** | Template authoring with secure defaults, 3-layer validation pipeline (cfn-lint,<br>cfn-guard, change sets), and root-cause diagnosis of failed stacks using<br>CloudFormation events and CloudTrail correlation. |
| **AWS IaC MCP Server**   | Documentation search (CloudFormation and CDK), template validation, compliance<br>checks, deployment troubleshooting, and CDK best practices -<br>• all running locally on<br>your machine.                      |

## Claude Code

### Install aws-core plugin from Agent Toolkit for AWS

Run the following command to install the plugin:

```
/plugin marketplace add aws/agent-toolkit-for-aws
/plugin install aws-core@agent-toolkit-for-aws
```

This installs agent skills including the AWS CloudFormation skill, agent hooks, and the
AWS MCP Server configuration in one step.

### Install AWS IaC MCP Server

Replace `AWS_PROFILE` with your local AWS profile name.

```
claude mcp add awslabs-aws-iac-mcp \
  -e AWS_PROFILE=default \
  -e AWS_REGION=us-east-1 \
  -e FASTMCP_LOG_LEVEL=ERROR \
  --scope user \
  -- uvx awslabs.aws-iac-mcp-server@latest
```

## Codex

### Install CloudFormation skill

```
npx skills add https://github.com/aws/agent-toolkit-for-aws --skill aws-cloudformation --yes --global
```

### Install AWS IaC MCP Server

Replace `AWS_PROFILE` with your local AWS profile name.

```
codex mcp add awslabs-aws-iac-mcp \
  --env AWS_PROFILE=default \
  --env AWS_REGION=us-east-1 \
  --env FASTMCP_LOG_LEVEL=ERROR \
  -- uvx awslabs.aws-iac-mcp-server@latest
```

## Cursor

### Install CloudFormation skill

```
npx skills add https://github.com/aws/agent-toolkit-for-aws --skill aws-cloudformation --yes --global
```

### Install AWS IaC MCP Server

Add the following to `.cursor/mcp.json` under `"mcpServers"`.
Replace `AWS_PROFILE` with your local AWS profile name.

```
"awslabs.aws-iac-mcp": {
  "command": "uvx",
  "args": ["awslabs.aws-iac-mcp-server@latest"],
  "env": {
    "AWS_PROFILE": "default",
    "AWS_REGION": "us-east-1",
    "FASTMCP_LOG_LEVEL": "ERROR"
  }
}
```

## Kiro

### Install CloudFormation skill in Kiro CLI

```
npx skills add https://github.com/aws/agent-toolkit-for-aws --skill aws-cloudformation --yes --global
```

### Install AWS IaC MCP Server

Add the following to `~/.kiro/settings/mcp.json` under
`"mcpServers"`. Replace `AWS_PROFILE` with your local AWS profile
name.

```
"awslabs.aws-iac-mcp": {
  "command": "uvx",
  "args": ["awslabs.aws-iac-mcp-server@latest"],
  "env": {
    "AWS_PROFILE": "default",
    "AWS_REGION": "us-east-1",
    "FASTMCP_LOG_LEVEL": "ERROR"
  },
  "disabled": false
}
```

### Install Kiro powers (from Kiro IDE)

Install the following Kiro power that provides specialized CloudFormation context and
tools to Kiro agents on-demand:

- **CloudFormation and CDK** -- install via [Kiro powers link](https://kiro.dev/powers/aws-iac "https://kiro.dev/powers/aws-iac").

## GitHub Copilot

### Install CloudFormation skill

```
npx skills add https://github.com/aws/agent-toolkit-for-aws --skill aws-cloudformation --yes --global
```

### Install AWS IaC MCP Server

Add the following to `.vscode/mcp.json` under `"mcpServers"`.
Replace `AWS_PROFILE` with your local AWS profile name.

```
"awslabs.aws-iac-mcp": {
  "command": "uvx",
  "args": ["awslabs.aws-iac-mcp-server@latest"],
  "env": {
    "AWS_PROFILE": "default",
    "AWS_REGION": "us-east-1",
    "FASTMCP_LOG_LEVEL": "ERROR"
  }
}
```

## Windsurf

### Install CloudFormation skill

```
npx skills add https://github.com/aws/agent-toolkit-for-aws --skill aws-cloudformation --yes --global
```

### Install AWS IaC MCP Server

Add the following to `/.codeium/windsurf/mcp_config.json` under
`"mcpServers"`. Replace `AWS_PROFILE` with your local AWS profile
name.

```
"awslabs.aws-iac-mcp": {
  "command": "uvx",
  "args": ["awslabs.aws-iac-mcp-server@latest"],
  "env": {
    "AWS_PROFILE": "default",
    "AWS_REGION": "us-east-1",
    "FASTMCP_LOG_LEVEL": "ERROR"
  }
}
```

## OpenCode

### Install CloudFormation skill

```
npx skills add https://github.com/aws/agent-toolkit-for-aws --skill aws-cloudformation --yes --global
```

### Install AWS IaC MCP Server

Add the following to `/.config/opencode/opencode.jsonc` under
`"mcpServers"`. Replace `AWS_PROFILE` with your local AWS profile
name.

```
"awslabs.aws-iac-mcp": {
  "command": "uvx",
  "args": ["awslabs.aws-iac-mcp-server@latest"],
  "env": {
    "AWS_PROFILE": "default",
    "AWS_REGION": "us-east-1",
    "FASTMCP_LOG_LEVEL": "ERROR"
  }
}
```

## For all other agents compatible with agent skills and MCP Server configuration

For any other agent that supports the open-source agent skills format and MCP Server
configuration, follow these steps:

### Install CloudFormation skill

```
npx skills add https://github.com/aws/agent-toolkit-for-aws --skill aws-cloudformation --yes --global
```

### Install AWS IaC MCP Server

Add the AWS IaC MCP Server to your agent's MCP client configuration file under
`"mcpServers"`. Replace `AWS_PROFILE` with your local AWS profile
name.

```
"awslabs.aws-iac-mcp": {
  "command": "uvx",
  "args": ["awslabs.aws-iac-mcp-server@latest"],
  "env": {
    "AWS_PROFILE": "default",
    "AWS_REGION": "us-east-1",
    "FASTMCP_LOG_LEVEL": "ERROR"
  }
}
```

## What you can do with your agent

Once configured, your agent can help you with:

| Task                      | Example prompt                                                                  |
| ------------------------- | ------------------------------------------------------------------------------- |
| Author a template         | "Create a CloudFormation template for a VPC with public and private<br>subnets" |
| Validate before deploying | "Validate my template at ./template.yaml and check for security issues"         |
| Troubleshoot a failure    | "My stack 'my-app' in us-east-1 failed to deploy. What happened?"               |
| Search documentation      | "What properties does AWS::ECS::Service support?"                               |
| CDK guidance              | "Show me CDK best practices for Lambda functions"                               |
| Compliance checks         | "Check if my template complies with security best practices"                    |

## IAM permissions

The MCP server requires the following AWS permissions for full functionality:

**For template validation and compliance:** No AWS
permissions required (local validation only).

**For deployment troubleshooting:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cloudformation:DescribeStacks",
        "cloudformation:DescribeStackEvents",
        "cloudformation:DescribeStackResources",
        "cloudtrail:LookupEvents"
      ],
      "Resource": "*"
    }
  ]
}
```

## Related resources

- [AWS IaC
  MCP Server on GitHub](https://github.com/awslabs/mcp/tree/main/src/aws-iac-mcp-server "https://github.com/awslabs/mcp/tree/main/src/aws-iac-mcp-server")
- [Agent Toolkit for
  AWS](https://github.com/aws/agent-toolkit-for-aws "https://github.com/aws/agent-toolkit-for-aws")
- [CloudFormation
  User Guide](../UserGuide.md "../UserGuide.md")
- [AWS CDK Developer
  Guide](../../../cdk/v2/guide.md "../../../cdk/v2/guide.md")
- [Introducing
  the AWS IaC MCP Server (blog)](https://aws.amazon.com/blogs/devops/introducing-the-aws-infrastructure-as-code-mcp-server-ai-powered-cdk-and-cloudformation-assistance/ "https://aws.amazon.com/blogs/devops/introducing-the-aws-infrastructure-as-code-mcp-server-ai-powered-cdk-and-cloudformation-assistance/")
