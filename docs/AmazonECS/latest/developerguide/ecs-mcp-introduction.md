

# Amazon ECS MCP server
<a name="ecs-mcp-introduction"></a>

The Amazon ECS MCP server is a fully managed service enabling AI-powered experiences for development and operations. [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) provides a standardized interface that enriches AI agents and applications with real-time, contextual knowledge of your Amazon ECS workloads, enabling more accurate, context-aware responses and AI-powered workflows to inspect, troubleshoot, and optimize your Amazon ECS workloads.

**Note**  
The Amazon ECS MCP server is in preview release and is subject to change.

## Overview
<a name="ecs-mcp-overview"></a>

The Amazon ECS MCP server can be easily integrated with any MCP compatible AI coding assistants, like [Kiro](https://kiro.dev/), or third-party tools like [Claude Code](https://code.claude.com/docs/en/mcp), [Cursor](https://cursor.com/), and [Cline](https://cline.bot/), to enhance your development workflow.

During deployment, it provides real-time visibility into service deployments and task health status. For development and operations, the server simplifies Amazon ECS management by providing high-level workflows for monitoring container health, analyzing service events, and investigating deployment issues. For debugging and troubleshooting, the server accelerates issue resolution through comprehensive diagnostic tools that analyze task failures, container logs, and network configurations. These capabilities are accessible through natural language interactions, enabling you to perform complex container operations more intuitively and efficiently.

The Amazon ECS MCP server provides several tools that you can use to:
+ **Monitor deployments and services**

  Check deployment status, track service events, and monitor container health in real-time.
+ **Troubleshoot container issues**

  Analyze task failures, investigate image pull errors, and examine container logs with customizable time windows.
+ **Inspect network configurations**

  Review VPC, subnet, and security group configurations for your Amazon ECS services.
+ **Resolve resource dependencies**

  Identify blockers preventing task definition deletion and understand resource relationships.
+ **Assess security posture**

  Collect cluster security configuration data for AI-powered analysis against AWS best practices with prioritized remediation steps.
+ **Access up-to-date documentation**

  Look up current AWS documentation for accurate, timely guidance on Amazon ECS features and configurations.

The fully managed Amazon ECS MCP server is hosted in the AWS cloud, eliminating the need for local installation and maintenance. It provides enterprise-grade capabilities like automatic updates and patching, centralized security through IAM integration, comprehensive audit logging via CloudTrail, and the proven scalability, reliability, and support of AWS.

## Getting started
<a name="ecs-mcp-get-started"></a>

To get started, see [Getting Started with the Amazon ECS MCP Server](ecs-mcp-getting-started.md).