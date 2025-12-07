# Define the gateway target configuration

The target configuration depends on the target type that you're adding to the gateway. For more information about supported gateway target types, see [Supported targets for Amazon Bedrock AgentCore gateways](gateway-supported-targets.md "gateway-supported-targets.md").

Select a topic to see examples of adding a target type:

###### Topics

- [Add a Lambda target](#gateway-add-target-api-lambda "#gateway-add-target-api-lambda")
- [Add an API Gateway stage target](#gateway-add-target-api-gateway "#gateway-add-target-api-gateway")
- [Add an OpenAPI target](#gateway-add-target-api-openapi "#gateway-add-target-api-openapi")
- [Add a Smithy target](#gateway-add-target-api-smithy "#gateway-add-target-api-smithy")
- [Add an MCP server target](#gateway-add-target-api-MCPserver "#gateway-add-target-api-MCPserver")

## Add a Lambda target

If you use the AgentCore starter toolkit (either the CLI or the Python SDK), you can
add a Lambda target to your gateway by specifying the `--target_type` as
`lambda` and omitting all optional arguments. The default Lambda function
and accompanying tool schema can be found in the [AgentCore starter toolkit github](https://github.com/aws/bedrock-agentcore-starter-toolkit/blob/main/src/bedrock_agentcore_starter_toolkit/operations/gateway/constants.py "https://github.com/aws/bedrock-agentcore-starter-toolkit/blob/main/src/bedrock_agentcore_starter_toolkit/operations/gateway/constants.py").

###### Target configuration

The target configuration (or payload) for a Lambda function contains the following
fields:

- **lambdaArn** – The ARN of the Lambda
  function to use as your target.
- **toolSchema** – The tool schema for the
  gateway target.

For more information about Lambda targets, see [AWS Lambda function targets](gateway-add-target-lambda.md "gateway-add-target-lambda.md").

Select one of the following methods:

AgentCore starter toolkit (CLI)

###### Add a default Lambda function as a target

To add the default Lambda function as a target to your gateway in the
AgentCore starter toolkit CLI, run the
`create_mcp_gateway_target` command and specify the
`--target_type` argument as `lambda`. The
following example shows the minimum arguments you can provide:

```
agentcore create_mcp_gateway_target \
  --gateway-arn arn:aws:bedrock-agentcore:us-east-1:123456789012:gateway/my-gateway \
  --gateway-url https://gateway-id.gateway.bedrock-agentcore.us-west-2.amazonaws.com/mcp \
  --role-arn arn:aws:iam::123456789012:role/AgentCoreGatewayExecutionRole \
  --target-type lambda
```

AgentCore starter toolkit (Python)
With the AgentCore starter toolkit, you can easily create a Lambda target
with default configurations.s

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

The following is an example argument you can provide for the
`target_payload`. If you omit the `target_payload`
argument, this payload is used:

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
The following Python code shows how to add a Lambda target using the
AWS Python SDK (Boto3):

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

## Add an API Gateway stage target

To add a stage of an API Gateway REST API as a target, specify the ARN of the API and stage and define settings to filter tools in the API gateway or to override names and descriptions of tools in the gateway:

The following examples show how to add an API Gateway target. The following configurations are also applied:

- The tools filtered for are the GET and POST methods for the `/products` path.
- GET /products is renamed as `get_items`.

Select one of the following methods:

AWS CLI
The following command uses the AWS CLI:

```
aws bedrock-agentcore-control create-gateway-target \
    --gateway-identifier "your-gateway-id" \
    --name "SearchAPITarget" \
    --target-configuration '{
        "mcp": {
            "apiGateway": {
                "restApiId": `rest-api-id`,
                "stage": `stage`,
                "apiGatewayToolConfiguration": {
                    "toolFilters": [
                        {
                            "filterPath": "/products",
                            "methods": [
                                "GET",
                                "POST"
                            ]
                        }
                    ],
                    "toolOverrides": [
                        {
                            "path": "/products",
                            "method": "GET",
                            "name": "get_items",
                            "description": "Gets information for items in the list of products."
                        }
                    ]
                }
            }
        }
    }'
    --credential-provider-configurations '[
        {
            "credentialProviderType": "GATEWAY_IAM_ROLE"
        }
    ]'
```

Boto3
The following code shows uses the AWS Python SDK (Boto3):

```
import boto3

# Create the client
agentcore_client = boto3.client('bedrock-agentcore-control')

# Create an API gateway REST API target with gateway service role authentication
target = agentcore_client.create_gateway_target(
    gatewayIdentifier="your-gateway-id",
    name="SearchAPITarget",
    targetConfiguration={
        "mcp": {
            "apiGateway": {
                "restApiId": `rest-api-id`,
                "stage": `stage`,
                "apiGatewayToolConfiguration": {
                    "toolFilters": [
                        {
                            "filterPath": "/products",
                            "methods": [
                                "GET",
                                "POST"
                            ]
                        }
                    ],
                    "toolOverrides": [
                        {
                            "path": "/products",
                            "method": "GET",
                            "name": "get_item",
                            "description": "Gets information for a specific item in the product list."
                        }
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

## Add an OpenAPI target

Select one of the following methods:

AgentCore starter toolkit

###### Example with S3 definition and API key outbound authorization

The following example demonstrates adding an OpenAPI schema target to
a gateway. The schema has been uploaded to an S3 location whose URI is
referenced in the `target_payload`. Outbound authorization
for the target is through an API key.

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

The following example demonstrates adding an OpenAPI schema target to
a gateway. The schema has been uploaded to an S3 location whose URI is
referenced in the `target_payload`. Outbound authorization
for the target is through an OAuth.

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
The following Python code shows how to add an OpenAPI target using the
AWS Python SDK (Boto3). The schema has been uploaded to an S3 location whose URI
is referenced in the `target_payload`. Outbound authorization for
the target is through an API key.

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

## Add a Smithy target

Select one of the following methods:

AgentCore starter toolkit
The AgentCore starter toolkit lets you create a Smithy target with a
default model definition in DynamoDB if you omit the
`targetConfiguration` field. The following example shows the
creation of the default Smithy model definition and also a custom one
uploaded to S3.

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
The following Python code shows how to add a Smithy model target using the
AWS Python SDK (Boto3):

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

## Add an MCP server target

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
