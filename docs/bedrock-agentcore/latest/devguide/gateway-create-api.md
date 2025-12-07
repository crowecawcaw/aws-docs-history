# Create an AgentCore gateway using the API

To create a AgentCore gateway using the API, make a [CreateGateway](../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateGateway.md") request with one of the [AgentCore control plane endpoints](../../../general/latest/gr/bedrock_agentcore.md#bedrock_agentcore_cp "../../../general/latest/gr/bedrock_agentcore.md#bedrock_agentcore_cp").

Minimally, you must specify the following fields:

- `name` – The name of the gateway.
- `roleArn` – The ARN of the gateway service role. For more information, see [AgentCore Gateway service role permissions](gateway-prerequisites-permissions.md#gateway-service-role-permissions "gateway-prerequisites-permissions.md#gateway-service-role-permissions").
- `authorizerType` – The type of authorizer to use for the gateway. Depends on the inbound authorization that you set up. For more information, see [Set up inbound authorization for your gateway](gateway-inbound-auth.md "gateway-inbound-auth.md").
- `protocolType` – The protocol type for the gateway.
  The following optional fields add metadata to your gateway:

- `description` – A description of the gateway.
- `tags` – A dictionary of key-value pairs specifying tags that you can use to label your gateway for monitoring purposes.
  The remaining fields depend on your gateway configuration and whether you want to toggle custom features for your gateway:

- `clientToken` – A client token value to ensure that a request completes no more than once. If you don't include this token, one is randomly generated for you. If you don't include a value, one is randomly generated for you. For more information, see [Ensuring idempotency](../../../ec2/latest/devguide/ec2-api-idempotency.md "../../../ec2/latest/devguide/ec2-api-idempotency.md").
- `authorizerConfiguration` – If your authorizer type is `CUSTOM_JWT`, you must include this field to specify the gateway authorization and authentication parameters. For more information, see [The authorizer configuration](#gateway-create-api-authorizer-config "#gateway-create-api-authorizer-config").
- `kmsKeyArn` – To encrypt your gateway with a KMS key include the ARN of the key in this field. For more information, see [Encrypt your AgentCore gateway with a customer-managed
  KMS key](gateway-encryption.md "gateway-encryption.md").
- `exceptionLevel` – To turn on debugging messages when invoking the gateway, set this value to `DEBUG`. For more information, see [Turn on debugging messages](gateway-debug-messages.md "gateway-debug-messages.md"). For examples of creating a gateway with this setting, see [Create a gateway with debugging messages](#gateway-create-ex-debug "#gateway-create-ex-debug").
- `interceptorConfigurations` – To turn on custom code that is run when invoking your gateway, include this field. For more information, see [Using interceptors with Gateway](gateway-interceptors.md "gateway-interceptors.md"). For examples of creating a gateway with interceptors, see [Create a gateway with interceptor configurations](#gateway-create-ex-basic-interceptors "#gateway-create-ex-basic-interceptors").
- `protocolConfiguration` – To include customizations for the gateway protocol, configure the settings in this field. For options in this configuration, see [GatewayProtocolConfiguration](../../../bedrock-agentcore-control/latest/APIReference/API_GatewayProtocolConfiguration.md "../../../bedrock-agentcore-control/latest/APIReference/API_GatewayProtocolConfiguration.md").
  - One example option is the addition of a tool search tool in your gateway. For more information, see [Search for tools in your AgentCore gateway with a natural language query](gateway-using-mcp-semantic-search.md "gateway-using-mcp-semantic-search.md"). For examples of creating a gateway with this search tool, see [Create a gateway with semantic search](#gateway-create-ex-semantic "#gateway-create-ex-semantic").

## The authorizer configuration

If your authorizer type is `CUSTOM_JWT`, you must also include an authorizer configuration in the `authorizerConfiguration` field. The basic structure of the authorizer configuration is as follows:

```
{
  "customJWTAuthorizer": {
    "discoveryUrl": "`string`",
    "allowedAudience": ["`string`"],
    "allowedClients": ["`string`"],
    "allowedScopes": ["`string`"],
    "customClaims:" see below
  }
}
```

You must provide the discovery URL for the authentication token. The remaining fields define restrictions for the authentication claims:

- `allowedAudience` – The audiences or services that can handle the JWT.
- `allowedClients` – The clients that are allowed to create a JWT.
- `allowedScopes` – The scopes of that limit the set of claims.
- `customClaims` – An array of objects that allows you to define custom fields and values that limit the claims to be authenticated. Each object is a `CustomClaimValidationsType` object contains the following fields:
  - `inboundTokenClaimName` – The name of the custom claim field to check.
  - `inboundTokenClaimValueType` – The data type of the claim value to check for.
  - `authorizingClaimMatchValue` – Defines the value to match the claim value to. Contains the following fields:
    - `claimMatchOperator` – Defines the relationship to look for between the match value and claim value.
    - `claimMatchValue` – An object that contains only one of the following fields:
      - matchValueString – Used in the following situations:
        - If the `inboundTokenClaimValueType` is `STRING` and the `claimMatchOperator` is `EQUALS`, specify a string that you want the claim value to match with for authentication.
        - If the `inboundTokenClaimValueType` is `STRING_ARRAY` and the `claimMatchOperator` is `CONTAINS`, specify a string that you want the claim value array to contain for authentication.

      - `matchValueArray` – If the `inboundTokenClaimValueType` is `STRING_ARRAY` and the `claimMatchOperator` is `CONTAINS_ANY`, specify an array of values that you want to check for authentication. If any of the values in the claim value array matches any of the values in the `matchValueArray`, the claim can be authenticated.

The following examples show the structure of the CustomClaimValidationsType objects that you can specify:

String matches string

```
{
  "inboundTokenClaimName": "`string`",
  "inboundTokenClaimValueType": "STRING",
  "authorizingClaimMatchValue": {
    "claimMatchValue": {
      "matchValueString": "`string`"
    },
    "claimMatchOperator": "EQUALS"
  }
}
```

Array contains string

```
{
  "inboundTokenClaimName": "`string`",
  "inboundTokenClaimValueType": "STRING_ARRAY",
  "authorizingClaimMatchValue": {
    "claimMatchValue": {
      "matchValueString": "`string`"
    },
    "claimMatchOperator": "CONTAINS"
  }
}
```

Array contains any value in array

```
{
  "inboundTokenClaimName": "`string`",
  "inboundTokenClaimValueType": "STRING_ARRAY",
  "authorizingClaimMatchValue": {
    "claimMatchValue": {
      "matchValueStringList": ["`string`"]
    },
    "claimMatchOperator": "CONTAINS_ANY"
  }
}
```

To see examples of how to create a gateway, expand the section that corresponds to your use case:

###### Topics

- [Create a gateway: basic example (Custom JWT
  authorization)](#gateway-create-ex-basic-jwt "#gateway-create-ex-basic-jwt")
- [Create a gateway: basic example (IAM
  authorization)](#gateway-create-ex-basic-iam "#gateway-create-ex-basic-iam")
- [Create a gateway: basic example (NONE authorizer)](#gateway-create-ex-basic-none-auth "#gateway-create-ex-basic-none-auth")
- [Create a gateway with semantic search](#gateway-create-ex-semantic "#gateway-create-ex-semantic")
- [Create a gateway with debugging messages](#gateway-create-ex-debug "#gateway-create-ex-debug")
- [Create a gateway with interceptor configurations](#gateway-create-ex-basic-interceptors "#gateway-create-ex-basic-interceptors")
- [Create a gateway with a policy engine configuration](#gateway-create-ex-policy-engine "#gateway-create-ex-policy-engine")

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

## Create a gateway: basic example (NONE authorizer)

This section provides basic examples of creating a gateway with a NONE authorizer type. This represents a gateway that will not perform authentication or authorization for any incoming requests.

###### Note

- The NONE authorizer type represents a gateway that will not perform authentication or authorization for any incoming requests. See [inbound authorization](gateway-inbound-auth.md "gateway-inbound-auth.md") for security concerns and details around using this configuration.
- If you choose an option that involves specifying an overt gateway service role ARN,
  ensure that you specify an existing one that you've set up. For more information, see
  [AgentCore Gateway service role permissions](gateway-prerequisites-permissions.md#gateway-service-role-permissions "gateway-prerequisites-permissions.md#gateway-service-role-permissions").

Select one of the following methods:

AgentCore starter toolkit (CLI)
The AgentCore starter toolkit CLI provides a simple way to create a gateway with NONE authorizer type in a command line interface.

The following command shows how to create a gateway with NONE authorizer type:

```
agentcore create_mcp_gateway \
  --region us-west-2 \
  --name my-gateway \
  --role-arn arn:aws:iam::123456789012:role/my-gateway-service-role \
  --authorizer-type NONE \
  --enable_semantic_search
```

The `gatewayUrl` in the response is the endpoint to use when you invoke the
gateway.

AgentCore starter toolkit (Python)
The AgentCore starter toolkit helps you easily create a gateway with NONE authorizer type. First, you initialize a client and then you use the
`create_mcp_gateway` method of the client.

The following example code shows how to create a gateway with NONE authorizer type:

```
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient

# Initialize the Gateway client
client = GatewayClient(region_name="us-west-2")

# Create the gateway with NONE authorizer type
gateway = client.create_mcp_gateway(
  name="my-gateway",
  role_arn="arn:aws:iam::123456789012:role/my-gateway-service-role",
  authorizer_type="NONE",
  enable_semantic_search=False
)

print(f"MCP Endpoint: {gateway['gatewayUrl']}")
```

AWS CLI
Run the following code in a terminal to create a gateway with NONE authorizer type using the AWS CLI:

```
aws bedrock-agentcore-control create-gateway \
  --name my-gateway \
  --role-arn arn:aws:iam::123456789012:role/my-gateway-service-role \
  --protocol-type MCP \
  --authorizer-type NONE
```

The `gatewayUrl` in the response is the endpoint to use when you invoke the
gateway.

AWS Python SDK (Boto3)
The following Python code shows how to create a gateway with NONE authorizer type using the
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
  authorizerType="NONE"
)

print(f"MCP Endpoint: {gateway['gatewayUrl']}")
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

## Create a gateway with interceptor configurations

This section provides examples of creating a gateway that has interceptors configured. Interceptors will be invoked at runtime of the gateway for each request.

###### Note

- Interceptors will be invoked at runtime of the gateway for each request.
- If you choose an option that involves specifying an overt gateway service role ARN,
  ensure that you specify an existing one that you've set up. For more information, see
  [AgentCore Gateway service role permissions](gateway-prerequisites-permissions.md#gateway-service-role-permissions "gateway-prerequisites-permissions.md#gateway-service-role-permissions").

Select one of the following methods:

AgentCore starter toolkit (CLI)
The AgentCore starter toolkit CLI provides a simple way to create a gateway with interceptor configurations in a command line interface.

The following command shows how to create a gateway with interceptor configurations:

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
  --interceptor-configurations '[{
      "interceptor": {
          "lambda": {
            "arn":"arn:aws:lambda:us-west-2:123456789012:function:my-interceptor-lambda"
          }
      },
      "interceptionPoints": ["REQUEST"]
  }]' \
  --enable_semantic_search
```

The `gatewayUrl` in the response is the endpoint to use when you invoke the
gateway.

AgentCore starter toolkit (Python)
The AgentCore starter toolkit helps you easily create a gateway with interceptor configurations. First, you initialize a client and then you use the
`create_mcp_gateway` method of the client.

The following example code shows how to create a gateway with interceptor configurations:

```
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient

# Initialize the Gateway client
client = GatewayClient(region_name="us-west-2")

# Create the gateway with interceptor configurations
gateway = client.create_mcp_gateway(
  name="my-gateway",
  role_arn="arn:aws:iam::123456789012:role/my-gateway-service-role",
  authorizer_config={
    "customJWTAuthorizer": {
      "discoveryUrl": "https://cognito-idp.us-west-2.amazonaws.com/some-user-pool/.well-known/openid-configuration",
      "allowedClients": ["clientId"]
    }
  },
  interceptor_configurations=[{
      "interceptor": {
          "lambda": {
            "arn":"arn:aws:lambda:us-west-2:123456789012:function:my-interceptor-lambda"
          }
      },
      "interceptionPoints": ["REQUEST"]
  }],
  enable_semantic_search=False
)

print(f"MCP Endpoint: {gateway['gatewayUrl']}")
```

AWS CLI
Run the following code in a terminal to create a gateway with interceptor configurations using the AWS CLI:

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
  --interceptor-configurations '[{
      "interceptor": {
          "lambda": {
            "arn":"arn:aws:lambda:us-west-2:123456789012:function:my-interceptor-lambda"
          }
      },
      "interceptionPoints": ["REQUEST"]
  }]'
```

The `gatewayUrl` in the response is the endpoint to use when you invoke the
gateway.

AWS Python SDK (Boto3)
The following Python code shows how to create a gateway with interceptor configurations using the
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
  interceptorConfigurations=[{
      "interceptor": {
          "lambda": {
            "arn":"arn:aws:lambda:us-west-2:123456789012:function:my-interceptor-lambda"
          }
      },
      "interceptionPoints": ["REQUEST"]
  }]
)

print(f"MCP Endpoint: {gateway['gatewayUrl']}")
```

## Create a gateway with a policy engine configuration

You can create a gateway with a policy engine configuration. A policy engine is a collection of policies that evaluates and authorizes agent tool calls. When associated with a gateway, the policy engine intercepts all agent requests and determines whether to allow or deny each action based on the defined policies. The enforcement `mode` specifies whether to test policies (`LOG_ONLY`) or enforce them (`ENFORCE`).

AWS CLI
Run the following code in a terminal to create a gateway with a policy engine configuration using the AWS CLI:

```
aws bedrock-agentcore-control create-gateway \
  --name my-gateway \
  --role-arn arn:aws:iam::123456789012:role/my-gateway-service-role \
  --protocol-type MCP \
  --authorizer-type CUSTOM_JWT \
  --authorizer-configuration '{
    "customJWTAuthorizer": {
      "discoveryUrl": "https://cognito-idp.us-west-2.amazonaws.com/pool-id/.well-known/openid-configuration",
      "allowedClients": ["clientId"]
    }
  }' \
  --policy-engine-configuration '{
    "arn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:policy-engine/policy-id",
    "mode": "LOG_ONLY"
  }' \
  --exception-level DEBUG
```

The `gatewayUrl` in the response is the endpoint to use when you invoke the
gateway.
