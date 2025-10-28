# Use Amazon Bedrock AgentCore built-in tools to interact with your applications

Amazon Bedrock AgentCore provides several built-in tools to enhance your development and testing
experience. These tools are designed to help you interact with your application in various ways,
providing capabilities for code execution and web browsing within the Amazon Bedrock AgentCore
environment.

Built-in tools are a key component of Amazon Bedrock AgentCore, allowing you to enhance agents by
adding hosted capabilities such as browser use and code execution. You can execute your code in
a secure environment. This is critical in Agentic AI applications where the agents may execute
arbitrary code that can lead to data compromise or security risks.

These tools are fully managed by Amazon Bedrock AgentCore, eliminating the need to set up and
maintain your own tool infrastructure.

## Built-in Tools Overview

Amazon Bedrock AgentCore offers the following built-in tools:

Code Interpreter

A secure environment for executing code and analyzing data. The
Amazon Bedrock AgentCore Code Interpreter supports multiple programming languages including Python,
TypeScript, and JavaScript, allowing you to process data and perform calculations within
the AgentCore environment.

Browser Tool

A secure, isolated browser environment that allows you to interact with and test web
applications while minimizing potential risks to your system, access online resources,
and perform web-based tasks.

These built-in tools are part of AgentCore's build phase, alongside other components
such as Memory, Gateways, and Identity. They provide secure, managed capabilities that can be
integrated into your agents without requiring additional infrastructure setup.

### Security and Access Control

Built-in tools in Amazon Bedrock AgentCore are designed with security in mind. They provide:

- Isolated execution environments to help prevent cross-contamination
- Configurable session timeouts to limit resource usage
- Integration with IAM for access control
- Network security controls to help restrict external access

### Key components

The built-in tools are designed with a secure, scalable architecture that integrates
with the broader AgentCore services. Each tool operates within its own isolated
environment to support security and resource management.

Tool Resources

The base configuration for a tool, including network settings, permissions, and
feature configuration. Tool resources are created once and can be used for multiple
sessions.

Sessions

Temporary runtime environments created from tool resources. Sessions have a
defined lifecycle and timeout period, and they maintain state during their
lifetime.

APIs

Each tool provides APIs for creating and managing tool resources, starting and
stopping sessions, and interacting with the tool's functionality.

### Integrating built-in tools with Agents

Built-in tools can be integrated with your agents to enhance their capabilities. The
integration process involves:

1. Creating a tool resource (Code Interpreter or Browser Tool) or using a system
   resource
2. Creating a session to interact with the tool
3. Using the tool's API to perform operations
4. Terminating the session when finished
