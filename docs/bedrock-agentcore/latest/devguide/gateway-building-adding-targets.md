# Add targets to an existing AgentCore gateway

After creating a gateway, you can add targets, which define the tools that your gateway will host. AgentCore Gateway supports multiple target type that are detailed in the following topics. Each target can have its own credential provider attached, enabling you to securely control access targets. By adding targets, your gateway becomes a single MCP URL that enables access to all of the relevant tools for an agent.

When you add a target, you provide the following required fields:

- The ID of the gateway to which to add the target.
- A name for the gateway target. To understand how the target name affects tool names, see [Understand how AgentCore Gateway tools are named](gateway-tool-naming.md "gateway-tool-naming.md").
- A target configuration. The configuration differs depending on your gateway target type.
- A credential provider configuration. The configuration depends on the [outbound authorization](gateway-outbound-auth.md "gateway-outbound-auth.md").
  You can optionally provide the following fields:

- A description of the gateway target.
- A client token value to ensure that a request completes no more than once. If you don't include this token, one is randomly generated for you. If you don't include a value, one is randomly generated for you. For more information, see [Ensuring idempotency](../../../ec2/latest/devguide/ec2-api-idempotency.md "../../../ec2/latest/devguide/ec2-api-idempotency.md").
  Select a topic to learn how to add a target to an existing gateway using that method:

###### Topics

- [Add a target using the AWS Management Console](#gateway-add-target-console "#gateway-add-target-console")
- [Add a target using the API](#gateway-add-target-api "#gateway-add-target-api")

## Add a target using the AWS Management Console

In the AWS Management Console, you can add gateway targets when you create the gateway. After you've created a gateway, you can add targets by doing the following:

###### To add a target to an existing gateway

1. Open the AgentCore console at [https://console.aws.amazon.com/bedrock-agentcore/home#](https://console.aws.amazon.com/bedrock-agentcore/home# "https://console.aws.amazon.com/bedrock-agentcore/home#").
2. Choose **Gateways**.
3. Select the gateway to which you want to add a target.
4. In the **Targets** section, choose **Add**.
5. (Optional) Change the auto-generated **Target name**.
6. (Optional) Provide an **Target description**.
7. Select the **Target type** and fill in the fields that appear.
8. (If applicable) Choose whether to define the target inline or by selecting an S3 location.
9. Select a supported outbound authorization configuration and choose the outbound authorization resource, if applicable.
10. (Optional, if applicable) Expand **Additional configurations** and configure them.
11. Choose **Add target**.

## Add a target using the API

To add a target using the API, make a [CreateGatewayTarget](../../../bedrock-agentcore-control/latest/APIReference/API_CreateGatewayTarget.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateGatewayTarget.md") request with one of the [AgentCore control plane endpoints](../../../general/latest/gr/bedrock_agentcore.md#bedrock_agentcore_cp "../../../general/latest/gr/bedrock_agentcore.md#bedrock_agentcore_cp").

###### Note

To add an integration provider template as a gateway target, you must use the AWS Management Console. For more information, see [Built-in templates from integration providers as targets](gateway-target-integrations.md "gateway-target-integrations.md").

To see examples of adding different target types, expand the following sections:

Select one of the following methods:

AgentCore CLI

```
# Create a gateway with Lambda target
agentcore create_mcp_gateway_target \
  --region us-east-1 \
  --gateway-arn arn:aws:bedrock-agentcore:us-east-1:123456789012:gateway/gateway-id \
  --gateway-url https://gateway-id.gateway.bedrock-agentcore.us-west-2.amazonaws.com/mcp \
  --role-arn arn:aws:iam::123456789012:role/BedrockAgentCoreGatewayRole \
  --target-type lambda
```

AgentCore starter toolkit
With the AgentCore starter toolkit, you can easily create a Lambda target with default configurations.s

```
# Import dependencies
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient

# Initialize the client
client = GatewayClient(region_name="us-east-1")

# Create a lambda target.
lambda_target = client.create_mcp_gateway_target(
    gateway=gateway,
    name=None, # If you don't set one, one will be generated.
    target_type="lambda",
    target_payload=None, # Define your own lambda if you pre-created one. Otherwise leave this as None and one will be created for you.
    credentials=None, # If you leave this as None, one will be created for you
)

```

The following is an example argument you can provide for the `target_payload`. If you omit the `target_payload` argument, this payload is used:

```
{
    "lambdaArn": "<insert your lambda arn>",
    "toolSchema": {
        "inlinePayload": [
            {
                "name": "get_weather",
                "description": "Get weather for a location",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "the location e.g. seattle, wa"
                        }
                    },
                    "required": [
                        "location"
                    ]
                }
            },
            {
                "name": "get_time",
                "description": "Get time for a timezone",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "timezone": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "timezone"
                    ]
                }
            }
        ]
    }
}
```

Boto3
The following Python code shows how to add a Lambda target using the Boto3 Python SDK:

```
import boto3

# Create the agentcore client
agentcore_client = boto3.client('bedrock-agentcore-control')

# Create a Lambda target
target = agentcore_client.create_gateway_target(
    gatewayIdentifier="your-gateway-id",
    name="LambdaTarget",
    targetConfiguration={
        "mcp": {
            "lambda": {
                "lambdaArn": "arn:aws:lambda:us-west-2:123456789012:function:YourLambdaFunction",
                "toolSchema": {
                    "inlinePayload": [
                        {
                            "name": "get_weather",
                            "description": "Get weather for a location",
                            "inputSchema": {
                                "type": "object",
                                "properties": {"location": {"type": "string"}},
                                "required": ["location"],
                            },
                        },
                        {
                            "name": "get_time",
                            "description": "Get time for a timezone",
                            "inputSchema": {
                                "type": "object",
                                "properties": {"timezone": {"type": "string"}},
                                "required": ["timezone"],
                            },
                        },
                    ]
                }
            }
        }
    },
    credentialProviderConfigurations=[
        {
            "credentialProviderType": "GATEWAY_IAM_ROLE"
        }
    ]
)
```

Select one of the following methods:

AgentCore starter toolkit

###### Example with S3 definition and API key outbound authorization

The following example demonstrates adding an OpenAPI schema target to a gateway. The schema has been uploaded to an S3 location whose URI is referenced in the `target_payload`. Outbound authorization for the target is through an API key.

```
# Import dependencies
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient

# Initialize the client
gateway_client = GatewayClient(region_name="us-west-2")

# Create an OpenAPI target with API Key authentication
open_api_target = gateway_client.create_mcp_gateway_target(
    gateway="your-gateway-id",
    target_type="openApiSchema",
    target_payload={
        "s3": {
            "uri": "s3://your-bucket/path/to/open-api-spec.json"
        }
    },
    credentials={
        "api_key": "your-api-key",
        "credential_location": "HEADER",
        "credential_parameter_name": "X-API-Key"
    }
)
```

###### Example with S3 definition and OAuth outbound authorization

The following example demonstrates adding an OpenAPI schema target to a gateway. The schema has been uploaded to an S3 location whose URI is referenced in the `target_payload`. Outbound authorization for the target is through an OAuth.

```
# Import dependencies
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient

# Initialize the client
gateway_client = GatewayClient(region_name="us-west-2")

# Create an OpenAPI target with OAuth authentication
open_api_with_oauth_target = gateway_client.create_mcp_gateway_target(
    gateway="your-gateway-id",
    target_type="openApiSchema",
    target_payload={
        "s3": {
            "uri": "s3://your-bucket/path/to/open-api-spec.json"
        }
    },
    credentials={
      "oauth2_provider_config": {
        "customOauth2ProviderConfig": {
        "oauthDiscovery": {
          "authorizationServerMetadata": {
            "issuer": "https://example.auth0.com",
            "authorizationEndpoint": "https://example.auth0.com/authorize",
            "tokenEndpoint": "https://example.auth0.com/oauth/token"
          }
        },
        "clientId": "your-client-id",
        "clientSecret": "your-client-secret"
      }
    }
  }
)
```

Boto3
The following Python code shows how to add an OpenAPI target using the Boto3 Python SDK. The schema has been uploaded to an S3 location whose URI is referenced in the `target_payload`. Outbound authorization for the target is through an API key.

```
import boto3

# Create the client
agentcore_client = boto3.client('bedrock-agentcore-control')

# Create an OpenAPI target with API Key authentication
target = agentcore_client.create_gateway_target(
    gatewayIdentifier="your-gateway-id",
    name="SearchAPITarget",
    targetConfiguration={
        "mcp": {
            "openApiSchema": {
                "s3": {
                    "uri": "s3://your-bucket/path/to/open-api-spec.json",
                    "bucketOwnerAccountId": "123456789012"
                }
            }
        }
    },
    credentialProviderConfigurations=[
        {
            "credentialProviderType": "API_KEY",
            "credentialProvider": {
                "apiKeyCredentialProvider": {
                    "providerArn": "arn:aws:agent-credential-provider:us-east-1:123456789012:token-vault/default/apikeycredentialprovider/abcdefghijk",
                    "credentialLocation": "HEADER",
                    "credentialParameterName": "X-API-Key"
                }
            }
        }
    ]
)
```

Select one of the following methods:

AgentCore starter toolkit
The AgentCore starter toolkit lets you create a Smithy target with a default model definition in DynamoDB if you omit the `targetConfiguration` field. The following example shows the creation of the default Smithy model definition and also a custom one uploaded to S3.

```
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient

# Initialize the Gateway client
gateway_client = GatewayClient(region_name="us-west-2")

# Create a Smithy model target for a built-in AWS service (this default configuration uses a DynamoDB Smithy model)
smithy_target = gateway_client.create_mcp_gateway_target(
    gateway=gateway,
    target_type="smithyModel"
)

# Or create a Smithy model target with a custom model
custom_smithy_target = gateway_client.create_mcp_gateway_target(
    gateway=gateway,
    target_type="smithyModel",
    target_payload={
        "s3": {
            "uri": "s3://your-bucket/path/to/smithy-model.json"
        }
    }
)
```

Boto3
The following Python code shows how to add a Smithy model target using the Boto3 Python SDK:

```
import boto3

# Create the agentcore client
agentcore_client = boto3.client('bedrock-agentcore-control')

# Create a Smithy model target
target = agentcore_client.create_gateway_target(
    gatewayIdentifier="your-gateway-id",
    name="DynamoDBTarget",
    targetConfiguration={
        "mcp": {
            "smithyModel": {
                "s3": {
                    "uri": "s3://your-bucket/path/to/smithy-model.json",
                    "bucketOwnerAccountId": "123456789012"
                }
            }
        }
    },
    credentialProviderConfigurations=[
        {
            "credentialProviderType": "GATEWAY_IAM_ROLE"
        }
    ]
)
```

You can add an MCP server target and synchronize targets using the CLI.

CLI
The AgentCore CLI provides a simple way to add MCP server targets:

```
# Create MCP server as target
{gatewayUrl}/gateways/{gatewayIdentifier}/targets
{
    "name": "myMCPTarget",
    "description": "description of my MCP target",
    "credentialProviderConfigurations": [{
        "credentialProviderType": "OAUTH",
        "credentialProvider": {
            "oauthCredentialProvider": {
                "providerArn": "arn:aws:bedrock-agentcore:{region}:{account}:token-vault/default/oauth2credentialprovider/resource-provider-oauth-test",
                "scopes": []
            }
        }
    }],
    "targetConfiguration": {
        "mcp": {
            "mcpServer": {
                "endpoint": "myMCPServerURL"
            }
        }
    }
}

# SynchronizeGatewayTargets
{gatewayUrl}/gateways/{gatewayIdentifier}/synchronizeTargets
{
    "targetIdList": [
        "<targetId>"
    ]
}


```
