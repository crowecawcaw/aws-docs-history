

# Using the AWS for SAP Management MCP Server
<a name="mcp-server"></a>

Configure the AWS for SAP Management MCP Server with your AI assistant to manage and monitor SAP applications running on AWS. The `uvx` tool automatically downloads and runs the MCP server when your AI assistant starts. For source code and project details, see the [AWS for SAP Management MCP Server GitHub repository](https://github.com/awslabs/mcp/tree/main/src/aws-for-sap-management-mcp-server).

The MCP server uses the Model Context Protocol (MCP), an open standard for connecting large language models (LLMs) with external tools. For more information about the Model Context Protocol specification, see the [Model Context Protocol documentation](https://modelcontextprotocol.io).

The MCP server runs locally on your machine and connects to your AI assistant through stdio transport. It uses your existing AWS credentials from `~/.aws/config` and requires no additional infrastructure. When you issue a prompt, the AI assistant invokes the MCP server’s tools, which call Systems Manager for SAP and related AWS service APIs on your behalf. The MCP server aggregates data across these services and returns SAP-contextual results within the conversation.

**Note**  
There is no additional charge for using the MCP server. Standard AWS service charges apply for the underlying API calls to services such as Systems Manager for SAP, Amazon CloudWatch, AWS Backup, Amazon EC2, and Amazon EventBridge Scheduler. These are the same charges that apply when you use these services through the AWS Management Console or AWS CLI. For more information about pricing, see [Pricing](what-is-ssm-for-sap.md#pricing-ssm-for-sap).

## Capabilities and safety controls
<a name="mcp-server-capabilities-safety"></a>

The MCP server provides tools in the following categories.

 **Monitoring and reporting (read-only)** 
+ View your SAP application landscape, including registered applications, component topology, and metadata.
+ Retrieve health summaries that correlate SAP application status from Systems Manager for SAP, metrics from Amazon CloudWatch, backup status from AWS Backup, filesystem usage, and configuration compliance into a single response.
+ Generate downloadable Markdown health reports for compliance or team reviews.

 **Configuration compliance (read-only)** 
+ Run SAP on AWS targeted configuration checks for instances, storage, and Pacemaker setups.
+ Drill into individual rule evaluations showing actual compared to expected values, with remediation guidance.

 **Application lifecycle management (confirmation required)** 
+ Start and stop SAP applications through natural language.
+ The MCP server understands component dependencies. When stopping a HANA database, it discovers dependent NetWeaver applications and offers to cascade-stop them in the correct order, along with the underlying Amazon EC2 infrastructure.
+ Register new SAP applications with Systems Manager for SAP.

 **Scheduled operations (confirmation required)** 
+ Create recurring schedules through Amazon EventBridge Scheduler. For example, schedule non-production systems to run only during business hours for cost optimization.
+ The MCP server handles EventBridge Scheduler configuration, IAM role creation, and payload construction.

Read-only operations, such as monitoring and configuration compliance checks, run without confirmation. Operations that change application state, such as start, stop, register, and schedule operations, require your explicit confirmation before the MCP server runs them.

## Prerequisites
<a name="mcp-server-prerequisites"></a>

Before you set up the MCP server, verify that you have the following.
+  ** AWS credentials** – An AWS profile configured in `~/.aws/config` with permissions for the following services: Systems Manager for SAP, Amazon CloudWatch, Amazon EC2, Amazon EventBridge Scheduler, AWS Backup, AWS Systems Manager, and AWS Identity and Access Management (IAM).
+  **Registered SAP applications** – SAP applications registered with Systems Manager for SAP. For more information, see [Getting started with Systems Manager for SAP](https://docs.aws.amazon.com/ssm-sap/latest/userguide/get-started.html).
+  **MCP-compatible AI assistant** – An AI assistant that supports the MCP protocol, such as Amazon Q Developer CLI, Claude Desktop, or Kiro.
+  **Python 3.10 or later** – Python 3.10 or later with `uv` installed. Install `uv` from the [Astral documentation website](https://docs.astral.sh/uv/getting-started/installation) or the [astral-sh/uv repository](https://github.com/astral-sh/uv#installation) on the GitHub website.

## Setting up the MCP server
<a name="mcp-server-setting-up"></a>

No manual download or installation is required. When you add the MCP server to your AI assistant’s configuration, `uvx` automatically downloads and runs the server.

To configure the MCP server, add the following JSON to your AI assistant’s MCP configuration file. Replace `YOUR_AWS_PROFILE` with the name of your AWS profile.

```
{
  "mcpServers": {
    "awslabs.aws-for-sap-management-mcp-server": {
      "autoApprove": [],
      "disabled": false,
      "command": "uvx",
      "args": ["awslabs.aws-for-sap-management-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "<YOUR_AWS_PROFILE>",
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "transportType": "stdio"
    }
  }
}
```

The location of the MCP configuration file varies by AI assistant. Refer to your AI assistant’s documentation for the correct file path.

**Note**  
If your configuration file does not exist, create it with the complete structure shown above. If the file exists but does not have an `mcpServers` section, add one.

You can also use the ** AWS API MCP Server** alongside the ** AWS for SAP Management MCP Server** for general-purpose AWS API access. To use both servers, add the following combined configuration to your MCP configuration file.

```
{
  "mcpServers": {
    "awslabs.aws-for-sap-management-mcp-server": {
      "autoApprove": [],
      "disabled": false,
      "command": "uvx",
      "args": ["awslabs.aws-for-sap-management-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "<YOUR_AWS_PROFILE>",
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "transportType": "stdio"
    },
    "awslabs.aws-api-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.aws-api-mcp-server@latest"],
      "env": {
        "AWS_PROFILE": "<YOUR_AWS_PROFILE>"
      },
      "transportType": "stdio"
    }
  }
}
```

For more information about the AWS API MCP Server, see the [AWS API MCP Server documentation](https://awslabs.github.io/mcp/servers/aws-api-mcp-server/).

## Example prompts
<a name="mcp-server-example-prompts"></a>

The following are examples of prompts you can use with the MCP server through an MCP-compatible AI assistant.
+ "List all my SAP applications"
+ "What is the current health status of my ERPProdHANA application?"
+ "Show me the configuration check results for ERPProdHANA"
+ "Run configuration checks on ERPProdHANA every Friday at 6pm PDT"
+ "Stop ERPProdHANA and its dependent applications"
+ "Stop my SAP application DevHANA every Friday at 6pm PDT and start it back at 6am PDT every Monday"
+ "Generate a health summary report of ERPProdHANA and save it to a file"

## Troubleshooting
<a name="mcp-server-troubleshooting"></a>

The following are common issues and solutions for the MCP server.
+  **MCP server does not appear in your AI assistant** – Verify that your MCP configuration file contains valid JSON. Restart your AI assistant after updating the configuration. Confirm that `uvx` is installed and available in your system PATH.
+  **Authentication errors** – Verify that the `AWS_PROFILE` value in your MCP configuration matches a profile in `~/.aws/config`. Confirm that the profile has the required IAM permissions for the services listed in the prerequisites.
+  **SAP applications are not discovered** – Verify that your SAP applications are registered with Systems Manager for SAP. Confirm that the AWS Region in your profile matches the Region where your SAP applications are registered. For supported Regions, see [Systems Manager for SAP endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ssm-sap.html) in the * AWS General Reference*.