# Amazon Bedrock AgentCore in AWS GovCloud (US)

Amazon Bedrock AgentCore is an agentic platform for building, deploying, and operating effective agents securely at scale—no infrastructure management needed. The platform accelerates agents to production with composable services that work with any framework and any model, providing a gateway for secure tool and data access, enterprise-grade runtime with dynamic scaling, and comprehensive monitoring capabilities.

AgentCore provides both a developer toolkit and console that give teams control throughout the agent lifecycle. The platform converts APIs and Lambda functions into agent-compatible tools through its gateway, deploys agents with complete session isolation and support for long-running workloads, and integrates with existing identity providers for automated authentication and permission delegation. Developers can monitor agent quality through continuous evaluations that sample and score live interactions for correctness, helpfulness, safety, and goal success rate—with full observability powered by Amazon CloudWatch.

## Region availability

This service is available in the following AWS GovCloud (US) Regions:

- AWS GovCloud (US-West)

## How Amazon Bedrock AgentCore differs

The following differences apply to Amazon Bedrock AgentCore:

- AgentCore Gateway does not include semantic search functionality.
- AWS Agent Registry (Preview) is not available.
- Bedrock Guardrails Policy is not availalbe
- Temporal Policy is not available
- The following CloudFormation resources are not available:

  - `AWS::BedrockAgentCore::OnlineEvaluationConfig`
  - `AWS::BedrockAgentCore::OAuth2CredentialProvider`
  - `AWS::BedrockAgentCore::Evaluator`
  - `AWS::BedrockAgentCore::ApiKeyCredentialProvider`
  - `AWS::BedrockAgentCore::Policy`
  - `AWS::BedrockAgentCore::PolicyEngine`

## Documentation

- [Amazon Bedrock AgentCore documentation](../../../bedrock-agentcore.md "../../../bedrock-agentcore.md")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

The following customer-defined metadata may leave the AWS GovCloud (US) Regions only when the customer asks AWS to investigate a reported issue:

- AgentCore Runtime metadata (agent runtime names, descriptions, environment variable keys)
- AgentCore Runtime endpoint metadata
- AgentCore Gateway metadata (gateway names, target definitions)
- AgentCore Identity metadata (workload identity names)
- AgentCore Evaluations metadata (evaluation configuration names, custom evaluator definitions)
- AgentCore Code Interpreter metadata (resource and session configuration)
- AgentCore Browser metadata (browser tool configuration)

The following customer-initiated configurations result in data plane traffic being sent to customer-specified endpoints, which may be located outside the AWS GovCloud (US) Regions:

- When customers configure AgentCore Gateway targets that connect to external services (such as MCP servers, OpenAPI endpoints, or built-in integration provider templates), data plane requests including tool invocation payloads are sent to the customer-specified server URLs.
- When customers configure AgentCore Identity with external identity providers, authentication token validation and OAuth credential exchange requests are sent to the customer-specified identity provider discovery and token endpoints.
- When agents use the AgentCore Browser tool, the browser session makes HTTP requests to whatever web application URLs the agent navigates to, which may be located outside the AWS GovCloud (US) Regions.
- When customers enable internet access for AgentCore Code Interpreter sessions, code executing within the sandbox environment can make outbound network requests to endpoints outside the AWS GovCloud (US) Regions.

Amazon Bedrock AgentCore metadata is not permitted to contain export-controlled data. This includes all configuration data that you enter when creating or managing AgentCore resources across any service—such as resource names, descriptions, Amazon Resource Names (ARNs), network and authentication configuration, environment variables, and resource tags.
