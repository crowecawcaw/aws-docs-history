

# Using AI agents to install and troubleshoot Network Flow Monitor agents
<a name="CloudWatch-NetworkFlowMonitor-agents-install-ai"></a>

You can use Model Context Protocol (MCP)-compatible AI agents to install, configure, and troubleshoot Network Flow Monitor agents on your workloads. The `aws-network-monitoring` skill from the [Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/what-is-agent-toolkit.html) can help with the following:
+ **Agent installation** – Install Network Flow Monitor agents using AWS Systems Manager Distributor or command-line install. The skill guides the assistant through attaching the `CloudWatchNetworkFlowMonitorAgentPublishPolicy` managed policy to the instance role, running the install document, and activating the agents.
+ **Troubleshooting** – Diagnose common issues, including HTTP 403 errors from missing IAM permissions, missing performance metrics after installation (activation not run), and connectivity failures from private subnets that lack the required virtual private cloud (VPC) endpoints.

**Prerequisites**  
Before you start, make sure you have the following:
+ **An AI agent** – An AI coding agent that supports MCP, such as Kiro CLI. For a list of supported AI coding agents, see [What is the Agent Toolkit for AWS?](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/what-is-agent-toolkit.html) in the *AWS Agent Toolkit User Guide*.
+ **AWS MCP server** – Configure the [AWS MCP server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/mcp-server.html) in your agent so it can make AWS API calls. For more information, see [Setting up the AWS MCP Server](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html) in the *AWS Agent Toolkit User Guide*.
+ **AWS credentials** – An AWS account with IAM credentials set up on your local machine. Credentials are required for tools that execute AWS API calls and run scripts, but not for searching documentation or discovering skills.

**Install the aws-network-monitoring skill**  
A skill is a curated package of instructions and reference materials that helps your AI agent complete Network Flow Monitor tasks. The `aws-network-monitoring` skill contains install procedures, IAM policy attachment, activation steps, and troubleshooting patterns. For more information, see [Skills](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/skills.html) in the *AWS Agent Toolkit User Guide*.

Use the AWS CLI to install the skill for your agent. For more information about the install command, see [Using the AWS CLI](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html) in the *AWS Agent Toolkit User Guide*.

```
aws agent-toolkit add-skill --skill-name aws-network-monitoring
```

After the skill is installed, your agent can load it on demand when you ask about installing, configuring, or troubleshooting Network Flow Monitor agents.

**Example prompts**  
The following prompts show common Network Flow Monitor workflows you can run through an AI agent after installing the skill.

**Install agents on EC2 instances**  
Provide an Amazon EC2 tag key and value, or one or more instance IDs, and the AWS Region. The agent resolves the target instances, runs the Systems Manager install document, attaches the required IAM policy to each instance role, and activates the agents.

```
Install Network Flow Monitor agents on my EC2 instances tagged Environment=Sandbox in us-east-1.
```

```
Install the Network Flow Monitor agent on my EC2 instance i-abc123 in us-east-1.
```

**Verify that agents are publishing performance metrics**  
Ask the agent to check whether a running Network Flow Monitor agent is successfully publishing reports to the Network Flow Monitor ingestion endpoint.

```
Verify that the Network Flow Monitor agent on i-abc123 in us-east-1 is publishing performance metrics.
```

**Troubleshoot agents that are not sending performance metrics**  
The agent checks the IAM policy attachment, activation status, and endpoint reachability.

```
My Network Flow Monitor agent on i-abc123 in us-east-1 is installed but not sending performance metrics. What's wrong?
```