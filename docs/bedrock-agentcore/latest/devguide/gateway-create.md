# Create an Amazon Bedrock AgentCore gateway

This guide walks you through the process of creating and configuring an Amazon Bedrock AgentCore
Gateway. The Gateway serves as a unified entry point for agents to access tools
and resources through the Model Context Protocol (MCP) and creating it is the first step in
building your tool integration platform. When you create a gateway, you create a managed service that handles authentication and invokes callable endpoints as tools.

To create a gateway, you set up inbound authorization and configure invocable targets. Targets establish the connection between your gateway and various tool types, including Lambda functions and REST API services. Each target contains configuration details that specify the tool location, authentication requirements, and any necessary request transformation rules.

You can create a gateway in the following ways:

- **AWS Management Console** – With the console, you can configure authorization, create the gateway, and add targets all on one page.
- **Amazon Bedrock AgentCore API** – You can directly invoke the [CreateGateway](../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md") API or through the help of a supported tool. If you use the API, you will add targets to your gateway in a separate step.
  When creating a gateway, you provide the following required fields:

- A name for the gateway.
- The Amazon Resource Name (ARN) of an [AgentCore service role](gateway-prerequisites-permissions.md#gateway-service-role-permissions "gateway-prerequisites-permissions.md#gateway-service-role-permissions") with permissions to create and make requests to the gateway on your behalf.
- The type of authorizer to use for [inbound authorization](gateway-inbound-auth.md "gateway-inbound-auth.md") to the gateway.
- (If you use JWT authentication) An authorizer configuration that specifies how incoming requests to the gateway should be authenticated.
- The protocol type for the gateway.
  You can optionally provide the following fields:

- A description of the gateway.
- A client token value to ensure that a request completes no more than once. If you don't include this token, one is randomly generated for you. If you don't include a value, one is randomly generated for you. For more information, see [Ensuring idempotency](../../../ec2/latest/devguide/ec2-api-idempotency.md "../../../ec2/latest/devguide/ec2-api-idempotency.md").

###### Note

When you create a gateway, a [workload identity](identity-manage-agent-ids.md "identity-manage-agent-ids.md") is automatically created for the gateway.

###### Gateway features that can be set during creation

You can activate the following features of the gateway during creation:

- **Protocol configuration** – Configure how the gateway implements the protocol.
- **Custom encryption of the gateway** – Specify the Amazon Resource Name (ARN) of a customer-managed AWS KMS key for greater control over the encryption process of your resource. If you don't include one, AWS encrypts the resource with an AWS-managed key. For more information, see [Encrypt your AgentCore gateway with a customer-managed
  KMS key](gateway-encryption.md "gateway-encryption.md").
- **Debug mode** – Allow the return of specific error messages during gateway invocation to help you with debugging. For more information, see [Turn on debugging messages](gateway-debug-messages.md "gateway-debug-messages.md").
- **Semantic search** – Add the `x_amz_bedrock_agentcore_search` to the gateway so that the target can deliver tools that are relevant to the search query. For more information, see [Search for tools in your AgentCore gateway with a natural language query](gateway-using-mcp-semantic-search.md "gateway-using-mcp-semantic-search.md").

###### Note

Note the following for semantic search:

    + You can only enable semantic search when creating a gateway. After you've created a gateway, you can't change its configuration to enable semantic search.
    + For an identity to create a gateway with semantic search, ensure that it has permissions to use the `bedrock-agentcore:SynchronizeGatewayTargets` IAM action.

Select a topic to learn how to create a gateway using that method:

###### Topics

- [Create an AgentCore gateway using the AWS Management Console](gateway-create-console.md "gateway-create-console.md")
- [Create an AgentCore gateway using the API](gateway-create-api.md "gateway-create-api.md")
