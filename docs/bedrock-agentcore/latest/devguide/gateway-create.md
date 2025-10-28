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
- The Amazon Resource Name (ARN) of an [AgentCore service role](gateway-prerequisites-permissions.md#gateway-execution-permissions "gateway-prerequisites-permissions.md#gateway-execution-permissions") with permissions to make requests to the gateway on your behalf.
- The type of authorizer to use for inbound requests to the gateway. AgentCore Gateway supports the following types of authentication:
  - JSON Web Token (JWT) authentication
  - AWS IAM credentials

- (If you use JWT authentication) An authorizer configuration that specifies how incoming requests to the gateway should be authenticated.
- The protocol type for the gateway.
  You can optionally provide the following fields:

- A description of the gateway.
- A client token value to ensure that a request completes no more than once. If you don't include this token, one is randomly generated for you. If you don't include a value, one is randomly generated for you. For more information, see [Ensuring idempotency](../../../ec2/latest/devguide/ec2-api-idempotency.md "../../../ec2/latest/devguide/ec2-api-idempotency.md").

###### Gateway features that can be set during creation

You can activate the following features of the gateway during creation:

- **Protocol configuration** – Configure how the gateway implements the protocol.
- **Custom encryption of the gateway** – Specify the Amazon Resource Name (ARN) of a customer-managed AWS KMS key for greater control over the encryption process of your resource. If you don't include one, AWS encrypts the resource with an AWS-managed key. For more information, see [Encrypt your AgentCore gateway with a customer-managed
  KMS key](gateway-encryption.md "gateway-encryption.md").
- **Debug mode** – Allow the return of specific error messages during gateway invocation to help you with debugging. For more information, see [Turn on debugging messages](gateway-debug-messages.md "gateway-debug-messages.md").
- **Semantic search** – Add the `x_amz_bedrock_agentcore_search` to the gateway so that the target can deliver tools that are relevant to the search query. For more information, see [Search for tools in your AgentCore gateway with a natural language query](gateway-using-mcp-semantic-search.md "gateway-using-mcp-semantic-search.md").
  Select a topic to learn how to create a gateway using that method:

###### Topics

- [Create an AgentCore gateway using the AWS Management Console](#gateway-create-console "#gateway-create-console")
- [Create an AgentCore gateway using the API](#gateway-create-api "#gateway-create-api")

## Create an AgentCore gateway using the AWS Management Console

###### To create a gateway using the console

1. Open the AgentCore console at [https://console.aws.amazon.com/bedrock-agentcore/home#](https://console.aws.amazon.com/bedrock-agentcore/home# "https://console.aws.amazon.com/bedrock-agentcore/home#").
2. From the left navigation pane, select **Gateways**.
3. In the **Gateways** section, choose **Create gateway**.
4. (Optional) In the **Gateway details** section, do the following:
   1. Change the generated **Gateway name**
   2. Expand the **Additional configurations** section and do the following:
      1. In the **Gateway description** field, provide a description for your gateway.
      2. In the **Instruction** field, enter any special instructions or context that should be passed to tools when they are invoked.
      3. To enable a built-in tool for searching tools in the gateway, select **Enable semantic search**. If you enable this tool, you can't disable it later. For more information, see [Search for tools in your AgentCore gateway with a natural language query](gateway-using-mcp-semantic-search.md "gateway-using-mcp-semantic-search.md").
      4. To enable detailed debugging messages to be returned in the gateway response, select **Exception level debug**. You can disable debugging messages later. For more information, see [Turn on debugging messages](gateway-debug-messages.md "gateway-debug-messages.md").

5. In the **Inbound Auth configurations** section, select one of the following options:
   - To allow Amazon Cognito to create authorization resources for you, select **Quick create configurations with Cognito**.
   - To use an authorization configuration that you have set up already, select **Use existing identity provider configurations** and then configure the following fields:
     - **Discovery URL** – Enter the discovery URL from your identity provider.
     - **Allowed audiences** – Enter the audience value that your gateway will accept. To add more audiences, choose **Add audience**.
     - **Allowed clients** – Enter the public identifier of the client that your gateway will accept. To add more clients, choose **Add client**.

6. In the **Permissions** section, do the following:
   1. To use an IAM service role to invoke the gateway on the user's behalf, select **Use an IAM service role**.
   2. (If you use an IAM service role) Choose one of the following options under **IAM role**:
      - To create a service role with the necessary permissions to access your gateway, choose **Create and use a new service role** and optionally change the generated **Service role name**.
      - To use an existing service role, choose **Use an existing service role** and then select a role from the **Service role name** dropdown menu. Make sure that the service role that you choose has the necessary permissions. For more information, see [AgentCore Gateway service role permissions](gateway-prerequisites-permissions.md#gateway-execution-permissions "gateway-prerequisites-permissions.md#gateway-execution-permissions").

7. (Optional) By default, your gateway is encrypted with an AWS managed key. To encrypt your gateway with a custom KMS key, expand the **KMS key** section, select **Customize encryption settings (advanced)**, and choose a customer managed key. For more information, see [Encrypt your AgentCore gateway with a customer-managed
   KMS key](gateway-encryption.md "gateway-encryption.md").
8. In the **Target: `${target-name}`** section, do the following:
   1. (Optional) Change the generated **Target name**.
   2. (Optional) Provide a **Target description**.
   3. For the **Target type**, choose an option. For more information about different target types, see [Add targets to an existing AgentCore gateway](gateway-building-adding-targets.md "gateway-building-adding-targets.md").
   4. Select or enter how the target type is defined.
   5. For the **Outbound Auth configurations**, select an outbound authorization method. Then, select or provide the necessary details and any optional additional configurations. For more information, see [Set up outbound authorization for your gateway](gateway-outbound-auth.md "gateway-outbound-auth.md").

9. To add more targets, choose **Add another target** and repeat
   the target configuration steps.
10. Choose **Create gateway**.

After creating your gateway, you can view its details, including the endpoint URL and associated targets.

## Create an AgentCore gateway using the API

To create a AgentCore gateway using the API, make a [CreateGateway](../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md") request with one of the [AgentCore control plane endpoints](../../../general/latest/gr/bedrock_agentcore.md#bedrock_agentcore_cp "../../../general/latest/gr/bedrock_agentcore.md#bedrock_agentcore_cp").

To see examples of how to create a gateway, expand the section that corresponds to your use case:

This section provides basic examples of creating a gateway.

Select one of the following methods:

AgentCore starter toolkit
The AgentCore starter toolkit helps you easily create a gateway with minimal specifications.

```
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient

# Initialize the Gateway client
client = GatewayClient(region_name="us-west-2")

# Automatically set up Cognito OAuth. Replace with a name of your choice
cognito_result = client.create_oauth_authorizer_with_cognito(gateway_name="my-gateway")

# Get the authorizer configuration
authorization=cognito_result["authorizer_config"]

# Create the gateway.
gateway = client.create_mcp_gateway(
  name=None, # You can omit this field
  role_arn=None, # the role arn that the Gateway will use - if you don't set one, one will be created.
  authorizer_config=authorization, # Variable from inbound authorization setup steps. Contains the OAuth authorizer details for authorizing callers to your Gateway (MCP only supports OAuth).
  enable_semantic_search=True, # enable semantic search.
  exception_level="DEBUG" # enable debugging
)

print(f"MCP Endpoint: {gateway.get_mcp_url()}")
print(f"OAuth Credentials:")
print(f"  Client ID: {cognito_result['client_info']['client_id']}")
print(f"  Scope: {cognito_result['client_info']['scope']}")

```

CLI
The AgentCore CLI provides a simple way to create and manage gateways:

```

# Create a Gateway with Lambda target
agentcore create_mcp_gateway \
--name my-gateway \
--target arn:aws:lambda:us-west-2:123456789012:function:MyFunction \
--execution-role BedrockAgentCoreGatewayRole

```

The CLI automatically:

- Detects target type from ARN patterns or file extensions
- Sets up Cognito OAuth (EZ Auth)
- Detects your AWS region and account
- Builds full role ARN from role name

Console

###### To create your Gateway endpoint

1. Open the AgentCore console at [https://console.aws.amazon.com/bedrock-agentcore/home#](https://console.aws.amazon.com/bedrock-agentcore/home# "https://console.aws.amazon.com/bedrock-agentcore/home#").
2. Choose **Gateways**.
3. Choose **Create gateway**.
4. In the **Gateway details** section:
   1. Enter a **Gateway name**
   2. Expand the **Additional configurations** section
      and:
      1. Enter an optional **Description** for your
         gateway.
      2. (Optional) For **Instructions**, enter any special
         instructions or context that should be passed to tools when they are
         invoked.
      3. (Optional) Optionally enable **Semantic search** to
         enable the built-in tool that can be used to search the tools on the
         gateway.

5. In the **Inbound Identity** section, configure authentication
   for users accessing your gateway:
   1. For **Discovery URL**, enter the OpenID Connect discovery
      URL for your identity provider (for example,
      `https://auth.example.com/.well-known/openid-configuration`).
   2. For **Allowed audiences**, enter the audience values that
      your gateway will accept. Add multiple audiences by choosing **Add
      audience**.

6. In the **Permissions** section:
   1. For **Service role**, choose an existing IAM role or
      create a new one that allows Amazon Bedrock AgentCore to access your tools on your
      behalf.
   2. (Optional) For **KMS key**, choose a customer managed key
      for encrypting your gateway data, or leave blank to use the default
      Amazon Bedrock AgentCore managed key.

7. In the **Target configuration** section:
   1. Enter a **Target name**.
   2. (Optional) Provide an optional **Target
      description**.
   3. For **Target type**, choose either:
      - **Lambda ARN** - To connect to an Lambda function that
        implements your tools
      - **REST API** - To connect to a REST API
        service

   4. Configure the target based on your selection:
      - **For Lambda function targets:**
        - For **Lambda ARN**, enter the ARN of your Lambda
          function.
        - For **Tool schema**, choose to either provide the
          schema inline or reference an Amazon S3 location containing your tool
          schema.

      - **For REST API targets:**
        - For **OpenAPI schema**, choose to either provide
          the schema inline or reference an Amazon S3 location containing your
          OpenAPI specification.

   5. (Optional) In the **Outbound authentication** section,
      configure authentication for accessing external services:
      - For **Authentication type**, choose **OAuth
        client** or **API key**.
      - Select the appropriate authentication resource from your
        account.

8. To add more targets, choose **Add another target** and repeat
   the target configuration steps.
9. Choose **Create gateway**.

After creating your gateway, you can view its details, including the endpoint URL
and associated targets, in the AgentCore console. The gateway endpoint URL follows
the format:
`https://{gatewayId}.gateway.{region}.amazonaws.com/mcp`.

Boto3
The following Python code shows how to create a gateway with boto3 (AWS SDK for
Python)

```

import boto3

# Create the agentcore client
agentcore_client = boto3.client('bedrock-agentcore-control')

# Create a gateway
gateway = agentcore_client.create_gateway(
  name="<target-name e.g. ProductSearch>",
  roleArn="<existing role ARN e.g. arn:aws:iam::123456789012:role/MyRole>",
  protocolType="MCP",
  authorizerType="CUSTOM_JWT",
  authorizerConfiguration= {
      "customJWTAuthorizer": {
          "discoveryUrl": "<existing discovery URL e.g. https://cognito-idp.us-west-2.amazonaws.com/some-user-pool/.well-known/openid-configuration>",
          "allowedClients": ["<clientId>"]
      }
  }
)
```

API
Use `CreateGateway` to create a gateway. The operation requires a
gateway name and protocol type, while accepting optional parameters like role ARN for
IAM permissions, authorizer configuration for JWT-based authentication, and custom
transform configuration for request/response processing.

###### Example request

The following example creates a Gateway with MCP protocol and JWT
authorization:

```

POST /gateways/ HTTP/1.1
Content-Type: application/json

{
  "name": "my-ai-gateway",
  "description": "Gateway for AI model interactions",
  "clientToken": "12345678-1234-1234-1234-123456789012",
  "roleArn": "arn:aws:iam::123456789012:role/AgentCoreGatewayRole",
  "protocolType": "MCP",
  "protocolConfiguration": {
      "mcp": {
          "version": "1.0",
          "searchType": "SEMANTIC"
      }
  },
  "authorizerConfiguration": {
      "customJWTAuthorizer": {
          "discoveryUrl": "https://auth.example.com/.well-known/openid-configuration",
          "allowedAudience": ["api.example.com"],
          "allowedClients": ["client-app-123"]
      }
  },
  "encryptionKeyArn": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
}

```

This section provides basic examples of creating a gateway using IAM authorization. With IAM authorization, you don't need an authorizer configuration.

Select one of the following methods:

AWS CLI
Run the following in a terminal:

```
aws bedrock-agentcore create-gateway --name my-gateway --role-arn arn:aws:iam::123456789012:role/MyAgentCoreServiceRole --protocol-type MCP --authorizer-type AWS_IAM
```

Boto3

```
import boto3

# Create the AgentCore client
agentcore_client = boto3.client('bedrock-agentcore-control')

# Create a gateway
gateway = agentcore_client.create_gateway(
  name="MyGateway",
  roleArn="arn:aws:iam::123456789012:role/MyAgentCoreServiceRole",
  protocolType="MCP",
  authorizerType="AWS_IAM"
)
```

Semantic search enables intelligent tool discovery so that we are not limited by typical
list tools limits (typically 100 or so). Our semantic search capability delivers contextually
relevant tool subsets, significantly improving tool selection accuracy through focused, relevant
results, inference performance with reduced token processing and overall orchestration efficiency
and response times.

To enable it, add `"searchType": "SEMANTIC"` to the
`CreateGateway` request in the MCP object within the
`protocolConfiguration` field:

```
"protocolConfiguration": {
  "mcp": {
      "searchType": "SEMANTIC"
  }
}
```

###### Note

You can only enable it during create, you cannot update a gateway later to be able to
support search.

For an identity to create a gateway with semantic search, ensure that it has permissions to use the `bedrock-agentcore:SynchronizeGatewayTargets"` IAM action.
