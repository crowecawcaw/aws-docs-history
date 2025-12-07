# What is the AWS MCP Server?

The AWS MCP Server is a managed remote Model Context Protocol (MCP) server that provides AI assistants
and agents with secure, authenticated access to AWS services through natural language interactions. You can use the
AWS MCP Server to perform complex, multi-step AWS tasks by combining real-time access to AWS documentation,
syntactically correct API calls, and pre-built workflows called Agent SOPs that follow AWS best practices.

With the AWS MCP Server, you can ask AI assistants to provision infrastructure, troubleshoot issues, configure services,
and manage AWS resources without needing to know specific API syntax or remember complex procedures. The server handles
authentication through standard AWS Identity and Access Management (IAM) controls and provides comprehensive audit
logging through AWS CloudTrail.

The AWS MCP Server consolidates capabilities from existing MCP servers (AWS Knowledge MCP and AWS API MCP) into a single, unified interface
that reduces configuration complexity while improving AI agent effectiveness across multi-service AWS workflows.

###### Topics

- [What can I do with the AWS MCP Server?](#what-can-i-do-mcp-server "#what-can-i-do-mcp-server")
- [How the AWS MCP Server works](#how-aws-mcp-server-works "#how-aws-mcp-server-works")
- [Pricing](#mcp-server-pricing "#mcp-server-pricing")

## What can I do with the AWS MCP Server?

You can use the AWS MCP Server to do the following:

- **Execute multi-step AWS workflows** – Use Agent SOPs to perform complex
  tasks like setting up production VPCs, deploying serverless applications, or configuring monitoring across
  multiple AWS services with step-by-step guidance that follows AWS Well-Architected principles.
- **Get real-time AWS knowledge** – Search and retrieve up-to-date AWS
  documentation, API references, best practices, and regional availability information to inform your AI
  assistant's responses and decisions.
- **Make authenticated AWS API calls** – Execute most of the 15,000+ AWS APIs
  with SigV4 through your existing IAM roles and policies, with automatic syntax validation and error handling.
- **Troubleshoot AWS issues** – Analyze CloudWatch logs and CloudTrail events, investigate permission
  problems, debug application failures, and diagnose performance issues using guided workflows and access to
  comprehensive AWS knowledge sources.
- **Provision and configure infrastructure** – Create and configure AWS resources
  like VPCs, databases, compute instances, and storage with automated workflows that implement security best
  practices and proper resource tagging.
- **Manage costs** – Set up billing alerts, analyze resource usage, and understand resource
  costs and billing using pre-built procedures that follow AWS best practices.

## How the AWS MCP Server works

The AWS MCP Server operates as a remote service that your MCP-compatible client connects to over HTTPS. When you
ask your AI assistant to perform an AWS task, the server uses three integrated capabilities to complete your request:

- **Agent SOPs provide structured guidance** – The server searches its library of
  pre-built Agent SOPs to find workflows relevant to your task. These scripts contain step-by-step instructions that
  guide the AI through complex procedures while following AWS best practices and security guidelines.
- **Knowledge tools provide current information** – When the AI needs clarification or
  encounters unfamiliar concepts, it can search AWS documentation, retrieve API references, check regional availability,
  and access the latest AWS announcements to make more informed decisions.
- **API tools execute authenticated actions** – The server translates natural language
  requests into properly formatted AWS API calls, handles authentication using your IAM credentials, and executes the
  commands while providing detailed feedback about results and any errors.

For example, when you ask to "Create a full-stack TODO React web application on AWS", the agent finds the relevant
Agent SOP. The SOP guides the agent through the entire process: setting up authentication using Amazon Cognito, provisioning APIs with AWS AppSync,
configuring compute resources, and creating an Amazon DynamoDB database while following AWS security best practices.

Authentication and authorization use your existing AWS IAM roles and policies, so you maintain full control over
what resources and actions are available. All API calls are logged through AWS CloudTrail for audit visibility.

###### Note

We recommend scoping down IAM roles to the minimum permissions that the agent needs to perform its task.

## Pricing

With the AWS MCP Server, you pay only for the AWS resources you use and any applicable data transfer costs. The MCP server itself has no additional charges.
For more information about AWS pricing, see [AWS Pricing](https://aws.amazon.com/pricing/ "https://aws.amazon.com/pricing/"). If you are new to
AWS, you can get started with many services for free. For more information, see [AWS
Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/").
