# Create an AgentCore gateway using the API

To create a AgentCore gateway using the API, make a [CreateGateway](../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md") request with one of the [AgentCore control plane endpoints](../../../general/latest/gr/bedrock_agentcore.md#bedrock_agentcore_cp "../../../general/latest/gr/bedrock_agentcore.md#bedrock_agentcore_cp").

To see examples of how to create a gateway, expand the section that corresponds to your use case:

###### Topics

- [Create a gateway: basic example (Custom JWT
  authorization)](#gateway-create-ex-basic-jwt "#gateway-create-ex-basic-jwt")
- [Create a gateway: basic example (IAM
  authorization)](#gateway-create-ex-basic-iam "#gateway-create-ex-basic-iam")
- [Create a gateway with semantic search](#gateway-create-ex-semantic "#gateway-create-ex-semantic")
- [Create a gateway with debugging messages](#gateway-create-ex-debug "#gateway-create-ex-debug")

## Create a gateway: basic example (Custom JWT

authorization)

This section provides basic examples of creating a gateway.

###### Note

Note the following:

- The values for the authorization configuration are from when you set up [inbound authorization](gateway-inbound-auth.md "gateway-inbound-auth.md").
- If you choose an option that involves specifying an overt gateway service role ARN,
  ensure that you specify an existing one that you've set up. For more information, see
  [AgentCore Gateway service role permissions](gateway-prerequisites-permissions.md#gateway-service-role-permissions "gateway-prerequisites-permissions.md#gateway-service-role-permissions").

Select one of the following methods:

AgentCore starter toolkit (CLI)
The AgentCore starter toolkit CLI provides a simple way to create a gateway in a
command line interface.

To create the gateway, you use the `create_mcp_gateway` method. The
following list enumerates the default value used for each argument if you omit it:

- **--region** – us-west-2
- **--name** – TestGateway + random alphanumeric
  sequence
- **--role-arn** –
  arn:aws:iam:::`your-account-id`:role/AgentCoreGatewayExecutionRole
  (if the role doesn't exist yet, it's automatically created for you)
- **--authorizer-config** – Creates an Amazon Cognito
  OAuth configuration for you.
- **--enable-semantic-search** – True

###### Using default arguments

Run the following command in a terminal to create a gateway with default
specifications:

```
agentcore create_mcp_gateway
```

###### Specifying arguments

The following command shows how to create a gateway with overt arguments:

```
agentcore create_mcp_gateway \
  --region us-west-2 \
  --name my-gateway \
  --role-arn arn:aws:iam::123456789012:role/my-gateway-service-role \
  --authorizer-config '{
      "customJWTAuthorizer": {
        "discoveryUrl": "https://cognito-idp.us-west-2.amazonaws.com/some-user-pool/.well-known/openid-configuration",
        "allowedClients": ["clientId"]
      }
    }' \
  --enable_semantic_search
```

The `gatewayUrl` in the response is the endpoint to use when you invoke the
gateway.

AgentCore starter toolkit (Python)
The AgentCore starter toolkit helps you easily create a gateway with minimal
specification. First, you initialize a client and then you use the
`create_mcp_gateway` method of the client. The following list enumerates the
default value used for each argument if you omit it:

- `GatewayClient` arguments:
  - **region_name** – us-west-2

- `GatewayClient create_mcp_gateway` method arguments:
  - **name** – TestGateway + random
    alphanumeric sequence
  - **role_arn** –
    arn:aws:iam:::`your-account-id`:role/AgentCoreGatewayExecutionRole
    (if the role doesn't exist yet, it's automatically created for you)
  - **authorizer_config** – Creates an Amazon Cognito
    OAuth configuration for you.
  - **enable_semantic_search** – True

###### Using default arguments

The following example code shows how to create a gateway with default
specifications:

```
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient

# Initialize the Gateway client
client = GatewayClient()

# Create a gateway with default configurations
gateway = client.create_mcp_gateway()

print(f"MCP Endpoint: {gateway['gatewayUrl']}")
```

###### Specifying arguments

The following example code shows how to use the AgentCore starter toolkit to set
up a client, outbound authorization, and a gateway with your own arguments:

```
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient

# Initialize the Gateway client
client = GatewayClient(region_name="us-west-2")

# Create the gateway
gateway = client.create_mcp_gateway(
  name="my-gateway",
  role_arn="arn:aws:iam::123456789012:role/my-gateway-service-role",
  authorizer_config={
    "customJWTAuthorizer": {
      "discoveryUrl": "https://cognito-idp.us-west-2.amazonaws.com/some-user-pool/.well-known/openid-configuration",
      "allowedClients": ["clientId"]
    }
  },
  enable_semantic_search=False
)

print(f"MCP Endpoint: {gateway['gatewayUrl']}")
```

AWS CLI
Run the following code in a terminal to create a basic gateway with the AWS CLI:

```
aws bedrock-agentcore-control create-gateway \
  --name my-gateway \
  --role-arn arn:aws:iam::123456789012:role/my-gateway-service-role \
  --protocol-type MCP \
  --authorizer-type CUSTOM_JWT \
  --authorizer-configuration '{
    "customJWTAuthorizer": {
      "discoveryUrl": "https://cognito-idp.us-west-2.amazonaws.com/some-user-pool/.well-known/openid-configuration",
      "allowedClients": ["clientId"]
    }
  }'
```

The `gatewayUrl` in the response is the endpoint to use when you invoke the
gateway.

AWS Python SDK (Boto3)
The following Python code shows how to create a basic gateway with the
AWS Python SDK (Boto3):

```
import boto3

# Initialize the AgentCore client
client = boto3.client('bedrock-agentcore-control')

# Create a gateway
gateway = client.create_gateway(
  name="my-gateway",
  roleArn="arn:aws:iam::123456789012:role/my-gateway-service-role",
  protocolType="MCP",
  authorizerType="CUSTOM_JWT",
  authorizerConfiguration={
      "customJWTAuthorizer": {
          "discoveryUrl": "https://cognito-idp.us-west-2.amazonaws.com/some-user-pool/.well-known/openid-configuration",
          "allowedClients": ["clientId"]
      }
  }
)

print(f"MCP Endpoint: {gateway['gatewayUrl']}")
```

## Create a gateway: basic example (IAM

authorization)

This section provides basic examples of creating a gateway using IAM authorization. With IAM authorization, you don't need an authorizer configuration.

Select one of the following methods:

AWS CLI
Run the following in a terminal:

```
aws bedrock-agentcore-control create-gateway \
--name my-gateway \
--role-arn arn:aws:iam::123456789012:role/MyAgentCoreServiceRole \
--protocol-type MCP \
--authorizer-type AWS_IAM
```

Boto3

```
import boto3

# Create the AgentCore client
agentcore_client = boto3.client('bedrock-agentcore-control')

# Create a gateway
gateway = agentcore_client.create_gateway(
  name="my-gateway",
  roleArn="arn:aws:iam::123456789012:role/MyAgentCoreServiceRole",
  protocolType="MCP",
  authorizerType="AWS_IAM"
)
```

## Create a gateway with semantic search

This section provides basic examples of creating a gateway with a tool to allow you to semantically search for relevant tools. To learn how to use this tool, see [Search for tools in your AgentCore gateway with a natural language query](gateway-using-mcp-semantic-search.md "gateway-using-mcp-semantic-search.md").

Select one of the following methods:

AgentCore starter toolkit (CLI)
By default, semantic search is enabled if you don't overtly specify the `--enable_semantic_search` flag when you send a `create_mcp_gateway` request using the AgentCore starter toolkit CLI, as in the following example:

```
agentcore create_mcp_gateway
```

AgentCore starter toolkit (Python)
By default, semantic search is enabled if you don't overtly specify the `enable_semantic_search` field as `False` when you send a `create_mcp_gateway` request using the AgentCore starter toolkit Python SDK. The following example specifies the value as `True` overtly:

```
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient

# Initialize the Gateway client
client = GatewayClient()

# Create a gateway with default configurations
gateway = client.create_mcp_gateway(enable_semantic_search=True)

print(f"MCP Endpoint: {gateway['gatewayUrl']}")
```

AWS CLI
Turn on semantic search when creating a gateway in the AWS CLI by specifying `searchType` as `SEMANTIC` in the `--protocol-configuration` object, as in the following example:

```
aws bedrock-agentcore-control create-gateway \
  --name my-gateway \
  --role-arn arn:aws:iam::123456789012:role/my-gateway-service-role \
  --protocol-type MCP \
  --authorizer-type CUSTOM_JWT \
  --authorizer-configuration '{
    "customJWTAuthorizer": {
      "discoveryUrl": "https://cognito-idp.us-west-2.amazonaws.com/some-user-pool/.well-known/openid-configuration",
      "allowedClients": ["clientId"]
    }
  }' \
  --protocol-configuration '{
    "mcp": {
        "searchType": "SEMANTIC"
    }
  }'
```

The `gatewayUrl` in the response is the endpoint to use when you invoke the
gateway.

AWS Python SDK (Boto3)
Turn on semantic search when creating a gateway using the AWS Python SDK (Boto3) by specifying `searchType` as `SEMANTIC` in the `protocolConfiguration` object, as in the following example:

```
import boto3

# Initialize the AgentCore client
client = boto3.client('bedrock-agentcore-control')

# Create a gateway
gateway = client.create_gateway(
  name="my-gateway",
  roleArn="arn:aws:iam::123456789012:role/my-gateway-service-role",
  protocolType="MCP",
  authorizerType="CUSTOM_JWT",
  authorizerConfiguration={
      "customJWTAuthorizer": {
          "discoveryUrl": "https://cognito-idp.us-west-2.amazonaws.com/some-user-pool/.well-known/openid-configuration",
          "allowedClients": ["clientId"]
      }
  },
  protocolConfiguration={
    "mcp": {
        "searchType": "SEMANTIC"
    }
  }
)

print(f"MCP Endpoint: {gateway['gatewayUrl']}")
```

## Create a gateway with debugging messages

You can create a gateway with debugging messages by specifying the `exceptionLevel` value as `DEBUG`. This section provides examples of creating a gateway with debugging messages. To learn more, see [Turn on debugging messages](gateway-debug-messages.md "gateway-debug-messages.md").

###### Note

If you use the AgentCore starter toolkit (either the CLI or the Python SDK) to create a gateway, the `exceptionLevel` is automatically set to `DEBUG`. You can turn off debugging messages by sending an [UpdateGateway](../../../bedrock-agentcore-control/latest/APIReference/API_UpdateGateway.md "../../../bedrock-agentcore-control/latest/APIReference/API_UpdateGateway.md") request and omitting the `exceptionLevel` argument.

Select one of the following methods:

AWS CLI
Run the following code in a terminal to create a gateway with debugging messages turned on in the AWS CLI:

```
aws bedrock-agentcore-control create-gateway \
  --name my-gateway \
  --role-arn arn:aws:iam::123456789012:role/my-gateway-service-role \
  --protocol-type MCP \
  --authorizer-type CUSTOM_JWT \
  --authorizer-configuration '{
    "customJWTAuthorizer": {
      "discoveryUrl": "https://cognito-idp.us-west-2.amazonaws.com/some-user-pool/.well-known/openid-configuration",
      "allowedClients": ["clientId"]
    }
  }' \
  --exception-level DEBUG

```

The `gatewayUrl` in the response is the endpoint to use when you invoke the
gateway.

AWS Python SDK (Boto3)
The following Python code shows how to create a basic gateway with the
AWS Python SDK (Boto3):

```
import boto3

# Initialize the AgentCore client
client = boto3.client('bedrock-agentcore-control')

# Create a gateway
gateway = client.create_gateway(
  name="my-gateway",
  roleArn="arn:aws:iam::123456789012:role/my-gateway-service-role",
  protocolType="MCP",
  authorizerType="CUSTOM_JWT",
  authorizerConfiguration={
      "customJWTAuthorizer": {
          "discoveryUrl": "https://cognito-idp.us-west-2.amazonaws.com/some-user-pool/.well-known/openid-configuration",
          "allowedClients": ["clientId"]
      }
  },
  exceptionLevel="DEBUG"
)

print(f"MCP Endpoint: {gateway['gatewayUrl']}")
```
