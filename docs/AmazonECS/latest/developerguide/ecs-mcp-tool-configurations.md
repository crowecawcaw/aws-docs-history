# Amazon ECS MCP Server Tool Configurations

This guide shows all the configurations available for the fully managed Amazon ECS MCP Server.

###### Note

The Amazon ECS MCP server is in preview release and is subject to change.

## Environment variables

**AWS\_PROFILE** (optional)

AWS credentials profile name to use; can be overridden by the `--profile` command-line argument.

Example: `export AWS_PROFILE=dev`

**AWS\_REGION** (optional)

AWS region for SigV4 signing; defaults to `us-west-2` if not set.

Example: `export AWS_REGION=us-west-2`

## Arguments

**SigV4 MCP endpoint URL** (required)

The MCP endpoint URL to connect to.

Example: `https://ecs-mcp.us-west-2.api.aws/mcp`

**--service** (optional)

AWS service name for SigV4 signing; auto-detected from the endpoint hostname if not provided.

Example: `--service ecs-mcp`

**--profile** (optional)

AWS credentials profile to use. Defaults to the `AWS_PROFILE` environment variable if not specified.

Example: `--profile dev`

**--region**

AWS region to use. Uses `AWS_REGION` environment variable if not set, defaults to `us-east-1`.

Example: `--region us-west-2`

**--read-only** (optional)

Disable tools which may require write permissions (tools which DO NOT require write permissions are annotated with `readOnlyHint=true`). By default, all tools are enabled.

Example: `--read-only`

For more configuration options, see [Configuration parameters](https://github.com/aws/mcp-proxy-for-aws?tab=readme-ov-file#configuration-parameters "https://github.com/aws/mcp-proxy-for-aws?tab=readme-ov-file#configuration-parameters").

## Tools

The Amazon ECS MCP server exposes the following [MCP tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools "https://modelcontextprotocol.io/specification/2025-06-18/server/tools").

### Read only tools

**get\_deployment\_status**

The tool checks your Amazon ECS deployment status for a particular Amazon ECS cluster and service.

- Required IAM actions:

  - `ecs:DescribeServices`
  - `elasticloadbalancing:DescribeTargetGroups`
  - `elasticloadbalancing:DescribeLoadBalancers`

- Required parameters:

  - `cluster_name` (string): Amazon ECS cluster name
  - `service_name` (string): Amazon ECS service name

- Response: The tool returns deployment status and details associated with the deployment.

**fetch\_service\_events**

This tool retrieves Amazon ECS service events for diagnostics with customizable time windows.

- Required IAM actions:

  - `ecs:DescribeServices`

- Required parameters:

  - `cluster_name` (string): Amazon ECS cluster name
  - `service_name` (string): Amazon ECS service name

- Optional parameters:

  - `time_window` (integer): You can mention a time window in seconds (default is 1 hour or 3600 seconds)
  - `start_time` (string): Custom start time in ISO format
  - `end_time` (string): Custom end time in ISO format

- Response: The tool returns list of events for the service with summary.

**fetch\_task\_failures**

This tool helps you retrieve and analyze Amazon ECS task failures with summaries. Using this tool, you can identify any patterns in task failures.

- Required IAM actions:

  - `ecs:ListTasks`
  - `ecs:DescribeTasks`

- Required parameters:

  - `cluster_name` (string): Amazon ECS cluster name where your task resides

- Optional parameters:

  - `service_name` (string): You can filter by specific service
  - `time_window` (integer): You can mention a time window in seconds (default is 1 hour or 3600 seconds)
  - `start_time` (string): Custom start time in ISO format
  - `end_time` (string): Custom end time in ISO format

- Response: The tool returns TaskFailureResult with failed tasks and summary

**fetch\_task\_logs**

This tool retrieves CloudWatch logs for Amazon ECS tasks with flexible time range options. You use this tool to troubleshoot runtime issues.

- Required IAM actions:

  - `ecs:DescribeServices`
  - `ecs:DescribeTaskDefinition`
  - `logs:FilterLogEvents`

- Required parameters:

  - `cluster_name` (string): Amazon ECS cluster name
  - `service_name` (string): Amazon ECS service name

- Optional parameters:

  - `time_window` (integer): You can mention a time window in seconds (default is 1 hour or 3600 seconds)
  - `start_time` (string): Custom start time in ISO format
  - `end_time` (string): Custom end time in ISO format
  - `log_group_name` (string): Specify CloudWatch log group

- Response: The tool returns TaskLogsResult with log entries

**get\_task\_definition\_deletion\_blockers**

This tool identifies dependencies that can prevent task definition deletion. The tool is appropriate when you are running cleanup operations and understand what is preventing Amazon ECS resource deletion.

- Required IAM actions:

  - `ecs:ListClusters`
  - `ecs:ListServices`
  - `ecs:DescribeServices`
  - `ecs:ListTasks`
  - `ecs:DescribeTasks`

- Required parameters:

  - `task_definition_arn` (string): Task definition Amazon Resource Name (ARN) to analyze

- Response: The tool returns the blockers and deletion status

**detect\_image\_pull\_failures**

This tool helps you to detect and categorize container image pull failures.

- Required IAM actions:

  - `ecs:ListTasks`
  - `ecs:DescribeTasks`

- Required parameters:

  - `cluster_name` (string): Amazon ECS cluster name

- Optional parameters:

  - `service_name` (string): You can filter by specific service
  - `time_window` (integer): You can mention a time window in seconds (default is 1 hour or 3600 seconds)
  - `start_time` (string): Custom start time in ISO format
  - `end_time` (string): Custom end time in ISO format

- Response: The tool returns the failures and summary

**fetch\_network\_configuration**

This tool retrieves Amazon ECS service network configuration details. You can use this tool to understand the Amazon VPC, subnet, security group configuration of your Amazon ECS setup.

- Required IAM actions:

  - `ecs:DescribeServices`
  - `ec2:DescribeSecurityGroups`
  - `ec2:DescribeSubnets`

- Required parameters:

  - `cluster_name` (string): Amazon ECS cluster name
  - `service_name` (string): Amazon ECS service name

- Response: The tool returns a list of NetworkConfigurationResult with network details

**get\_security\_recommendations**

This tool collects Amazon ECS cluster security configuration data for AI-powered security analysis. It gathers IAM roles and policies, network settings (security groups, subnets, public IP), task definition container settings, and cluster-level configuration. Your AI assistant compares this data against AWS security best practices and generates a prioritized findings report with remediation steps.

- Required IAM actions:

  - `ecs:DescribeClusters`
  - `ecs:ListServices`
  - `ecs:DescribeServices`
  - `ecs:DescribeTaskDefinition`
  - `ec2:DescribeSecurityGroups`
  - `ec2:DescribeSubnets`
  - `iam:GetRole`
  - `iam:ListAttachedRolePolicies`
  - `iam:GetPolicy`
  - `iam:GetPolicyVersion`
  - `iam:ListRolePolicies`
  - `iam:GetRolePolicy`

- Required parameters:

  - `cluster_name` (string): Amazon ECS cluster name to analyze

- Optional parameters:

  - `service_name` (string): Scope analysis to a single service. If omitted, all services in the cluster are analyzed.
  - `max_services` (integer): Maximum number of services to analyze (default 25, capped at 50)

- Response: The tool returns cluster configuration, service configurations, task definition settings, network security details, IAM role and policy data, and any collection warnings. Your AI assistant uses this data to generate a prioritized security findings report with remediation guidance.

### Knowledge tools

These tools provide access to up-to-date AWS documentation. They are powered by the AWS Knowledge MCP Server and do not require any IAM permissions from the caller — the Amazon ECS MCP service connects to the knowledge endpoint on your behalf.

**aws\_knowledge\_aws\_\_\_search\_documentation**

This tool searches AWS documentation for relevant pages matching a query.

- Required IAM actions: None
- Required parameters:

  - `search_phrase` (string): Search query for AWS documentation

- Optional parameters:

  - `topics` (array): Up to 3 topic areas to search across (default `["general"]`)
  - `limit` (integer): Maximum number of results per topic (default 5)

- Response: The tool returns matching documentation pages with titles, URLs, and context snippets.

**aws\_knowledge\_aws\_\_\_read\_documentation**

This tool reads the content of AWS documentation pages and returns them in markdown format.

- Required IAM actions: None
- Required parameters:

  - `requests` (array): Array of request objects. Each object contains:

    - `url` (string, required): URL of the documentation page to read
    - `max_length` (integer, optional): Maximum characters to return (default 10000)
    - `start_index` (integer, optional): Character position to start reading from (default 0)

- Response: The tool returns the documentation page content in markdown format. Long pages are returned in chunks with navigation support.
