# Define the gateway target configuration

The target configuration depends on the target type that you’re adding to the gateway. For more information about supported gateway target types, see [Supported targets for Amazon Bedrock AgentCore gateways](gateway-supported-targets.md "gateway-supported-targets.md").

Select a topic to see examples of adding a target type:

###### Topics

- [Add a Lambda target](#gateway-add-target-api-lambda "#gateway-add-target-api-lambda")
- [Add an API Gateway stage target](#gateway-add-target-api-gateway "#gateway-add-target-api-gateway")
- [Add an OpenAPI target](#gateway-add-target-api-openapi "#gateway-add-target-api-openapi")
- [Add a Smithy target](#gateway-add-target-api-smithy "#gateway-add-target-api-smithy")
- [Add an HTTP runtime target](#gateway-add-target-api-http-runtime "#gateway-add-target-api-http-runtime")
- [Add an MCP server target](#gateway-add-target-api-MCPserver "#gateway-add-target-api-MCPserver")
- [Add a Connector target with Amazon Bedrock Managed Knowledge Bases](#gateway-add-target-api-connector-managed-kb "#gateway-add-target-api-connector-managed-kb")
- [Add a Connector target with Web Search Tool](#gateway-add-target-api-connector-web-search "#gateway-add-target-api-connector-web-search")

## Add a Lambda target

You can add a Lambda target to your gateway using the AgentCore CLI by specifying the `--type` as `lambda-function-arn` and providing the Lambda ARN and a tool schema file.

**Target configuration**

The target configuration (or payload) for a Lambda function contains the following fields:

- **lambdaArn** – The ARN of the Lambda function to use as your target.
- **toolSchema** – The tool schema for the gateway target.

For more information about Lambda targets, see [AWS Lambda function targets](gateway-add-target-lambda.md "gateway-add-target-lambda.md").

Select one of the following methods:

###### Example

AgentCore CLI

1. To add a Lambda function as a target, run `agentcore add gateway-target` with the `--type lambda-function-arn` option. Provide the Lambda ARN and a JSON file containing the tool schema:

```
agentcore add gateway-target \
  --name MyLambdaTarget \
  --type lambda-function-arn \
  --lambda-arn arn:aws:lambda:us-east-1:123456789012:function:MyFunction \
  --tool-schema-file tools.json \
  --gateway MyGateway
agentcore deploy
```

AgentCore Python SDK

1. With the AgentCore CLI, you can easily create a Lambda target with default configurations.

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

The following is an example argument you can provide for the `target_payload` . If you omit the `target_payload` argument, this payload is used:

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

1. The following Python code shows how to add a Lambda target using the AWS Python SDK (Boto3):

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

Interactive

1. In the AgentCore CLI interactive terminal UI, run `agentcore` , select **add** , choose **Gateway Target** , and then select **Lambda function** :

![TUI target type selection with Lambda function highlighted](images/tui/gateway-target-type-lambda.png)

The wizard then prompts you for the target name, Lambda function ARN, tool schema file, and outbound authorization configuration.

## Add an API Gateway stage target

To add a stage of an API Gateway REST API as a target, specify the ARN of the API and stage and define settings to filter tools in the API gateway or to override names and descriptions of tools in the gateway:

The following examples show how to add an API Gateway target. The following configurations are also applied:

- The tools filtered for are the GET and POST methods for the `/products` path.
- GET /products is renamed as `get_items`.

Select one of the following methods:

###### Example

AgentCore CLI

1. To add an API Gateway REST API stage as a target, run `agentcore add gateway-target` with the `--type api-gateway` option:

```
agentcore add gateway-target \
  --name MyAPIGatewayTarget \
  --type api-gateway \
  --rest-api-id your-rest-api-id \
  --stage your-stage \
  --gateway MyGateway
agentcore deploy
```

AWS CLI

1. The following command uses the AWS CLI:

```
aws bedrock-agentcore-control create-gateway-target \
    --gateway-identifier "your-gateway-id" \
    --name "SearchAPITarget" \
    --target-configuration '{
        "mcp": {
            "apiGateway": {
                "restApiId": rest-api-id,
                "stage": stage,
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

1. The following code shows uses the AWS Python SDK (Boto3):

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
                "restApiId": rest-api-id,
                "stage": stage,
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

Interactive

1. In the AgentCore CLI interactive terminal UI, run `agentcore` , select **add** , choose **Gateway Target** , and then select **API Gateway REST API** :

![TUI target type selection showing API Gateway REST API option](images/tui/gateway-target-type-apigw.png)

The wizard then prompts you for the target name, REST API ID, stage, and outbound authorization configuration.

## Add an OpenAPI target

Select one of the following methods:

###### Example

AgentCore CLI

1. To add an OpenAPI schema target, run `agentcore add gateway-target` with the `--type open-api-schema` option and provide the path to your OpenAPI specification file:

```
agentcore add gateway-target \
  --name MyOpenAPITarget \
  --type open-api-schema \
  --schema path/to/openapi-spec.json \
  --outbound-auth none|api-key|oauth \
  --gateway MyGateway
agentcore deploy
```

Boto3

1. The following Python code shows how to add an OpenAPI target using the AWS Python SDK (Boto3). The schema has been uploaded to an S3 location whose URI is referenced in the `target_payload` . Outbound authorization for the target is through an API key.

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

Interactive

1. In the AgentCore CLI interactive terminal UI, run `agentcore` , select **add** , choose **Gateway Target** , and then select **OpenAPI Schema** :

![TUI target type selection showing OpenAPI Schema option](images/tui/gateway-target-type-openapi.png)

The wizard then prompts you for the target name, path to the OpenAPI specification file, and outbound authorization configuration.

## Add a Smithy target

Select one of the following methods:

###### Example

AgentCore CLI

1. To add a Smithy model target, run `agentcore add gateway-target` with the `--type smithy-model` option and provide the path to your Smithy model file:

```
agentcore add gateway-target \
  --name MySmithyTarget \
  --type smithy-model \
  --schema path/to/smithy-model.json \
  --gateway MyGateway
agentcore deploy
```

Boto3

1. The following Python code shows how to add a Smithy model target using the AWS Python SDK (Boto3):

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

Interactive

1. In the AgentCore CLI interactive terminal UI, run `agentcore` , select **add** , choose **Gateway Target** , and then select **Smithy Model** :

![TUI target type selection showing Smithy Model option](images/tui/gateway-target-type-smithy.png)

The wizard then prompts you for the target name, path to the Smithy model file, and outbound authorization configuration.

## Add an HTTP runtime target

You can add an Amazon Bedrock AgentCore Runtime agent as an HTTP target to your gateway. The gateway sends traffic directly to the runtime agent without aggregation or protocol translation.

For more information about HTTP targets, see [Amazon Bedrock AgentCore Runtime targets](gateway-target-http-runtime.md "gateway-target-http-runtime.md").

Select one of the following methods:

###### Example

AWS CLI

1. The following command creates an HTTP runtime target with IAM authorization:

```
aws bedrock-agentcore-control create-gateway-target \
    --gateway-identifier "your-gateway-id" \
    --name "MyRuntimeTarget" \
    --description "Runtime gateway target" \
    --target-configuration '{
        "http": {
            "agentcoreRuntime": {
                "arn": "arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/RUNTIME_ID"
            }
        }
    }' \
    --credential-provider-configurations '[{
        "credentialProviderType": "GATEWAY_IAM_ROLE"
    }]'
```

Boto3

1. The following Python code shows how to add an HTTP runtime target using the AWS Python SDK (Boto3):

```
import boto3

agentcore_client = boto3.client('bedrock-agentcore-control')

target = agentcore_client.create_gateway_target(
    gatewayIdentifier="your-gateway-id",
    name="MyRuntimeTarget",
    description="Runtime gateway target",
    targetConfiguration={
        "http": {
            "agentcoreRuntime": {
                "arn": "arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/RUNTIME_ID"
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

You can add an MCP server target using the AgentCore CLI or AWS Python SDK (Boto3). The following examples show how to create an MCP server target with different outbound authorization types.

**MCP server with IAM (SigV4) authorization**

The following example creates an MCP server target with IAM authorization. The gateway signs requests to the MCP server using SigV4 with the gateway service role’s credentials. You must specify the `service` name for signing. The `region` is optional and defaults to the gateway’s Region.

The value of `service` depends on where your MCP server is hosted. The following are common values:

- `bedrock-agentcore` – For MCP servers hosted on Amazon Bedrock AgentCore, such as the runtime (see [Deploy MCP servers in AgentCore Runtime](runtime-mcp.md "runtime-mcp.md") ) or another gateway.
- `execute-api` – For MCP servers behind Amazon API Gateway.
- `lambda` – For MCP servers behind Lambda Function URLs.

Select one of the following methods:

###### Example

AWS CLI

1. ```

   ```

aws bedrock-agentcore-control create-gateway-target \
--gateway-identifier "your-gateway-id" \
--name "MyMCPTarget" \
--target-configuration '{
"mcp": {
"mcpServer": {
"endpoint": "https://my-server.bedrock-agentcore.us-west-2.api.aws"
}
}
}' \
--credential-provider-configurations '[{
"credentialProviderType": "GATEWAY_IAM_ROLE",
"credentialProvider": {
"iamCredentialProvider": {
"service": "bedrock-agentcore",
"region": "us-west-2"
}
}
}]'

````


Interactive

1. In the AgentCore CLI interactive terminal UI, run `agentcore` , select **add** , choose **Gateway Target** , and then select **MCP Server endpoint** :



![TUI target type selection with MCP Server endpoint highlighted](images/tui/gateway-target-type-mcp.png)

The wizard then prompts you for the target name, MCP server endpoint URL, and outbound authorization configuration.


Boto3

1. ```
import boto3

agentcore_client = boto3.client('bedrock-agentcore-control')

target = agentcore_client.create_gateway_target(
    gatewayIdentifier="your-gateway-id",
    name="MyMCPTarget",
    targetConfiguration={
        "mcp": {
            "mcpServer": {
                "endpoint": "https://my-server.bedrock-agentcore.us-west-2.api.aws"
            }
        }
    },
    credentialProviderConfigurations=[
        {
            "credentialProviderType": "GATEWAY_IAM_ROLE",
            "credentialProvider": {
                "iamCredentialProvider": {
                    "service": "bedrock-agentcore",
                    "region": "us-west-2"
                }
            }
        }
    ]
)
````

**MCP server with OAuth authorization**

The following example creates an MCP server target with OAuth (client credentials) authorization.

Select one of the following methods:

###### Example

AWS CLI

1. ```

   ```

aws bedrock-agentcore-control create-gateway-target \
--gateway-identifier "your-gateway-id" \
--name "MyMCPTarget" \
--target-configuration '{
"mcp": {
"mcpServer": {
"endpoint": "https://my-mcp-server.example.com"
}
}
}' \
--credential-provider-configurations '[{
"credentialProviderType": "OAUTH",
"credentialProvider": {
"oauthCredentialProvider": {
"providerArn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:token-vault/default/oauth2credentialprovider/my-oauth-provider",
"scopes": []
}
}
}]'

```


AgentCore CLI

1. To add an MCP server target with OAuth authorization, run `agentcore add gateway-target` with the `--type mcp-server` option and specify the OAuth credentials:



```

agentcore add gateway-target \
--type mcp-server \
--name MyMCPTarget \
--endpoint https://my-mcp-server.example.com \
--gateway MyGateway \
--outbound-auth oauth \
--oauth-client-id my-client \
--oauth-client-secret my-secret \
--oauth-discovery-url https://auth.example.com/.well-known/openid-configuration
agentcore deploy

````


Boto3

1. ```
import boto3

agentcore_client = boto3.client('bedrock-agentcore-control')

target = agentcore_client.create_gateway_target(
    gatewayIdentifier="your-gateway-id",
    name="MyMCPTarget",
    targetConfiguration={
        "mcp": {
            "mcpServer": {
                "endpoint": "https://my-mcp-server.example.com"
            }
        }
    },
    credentialProviderConfigurations=[
        {
            "credentialProviderType": "OAUTH",
            "credentialProvider": {
                "oauthCredentialProvider": {
                    "providerArn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:token-vault/default/oauth2credentialprovider/my-oauth-provider",
                    "scopes": []
                }
            }
        }
    ]
)
````

**MCP server with API key authorization**

The following example creates an MCP server target with API key authorization.

Select one of the following methods:

###### Example

AWS CLI

1. ```

   ```

aws bedrock-agentcore-control create-gateway-target \
--gateway-identifier "your-gateway-id" \
--name "MyMCPTarget" \
--target-configuration '{
"mcp": {
"mcpServer": {
"endpoint": "https://my-mcp-server.example.com"
}
}
}' \
--credential-provider-configurations '[{
"credentialProviderType": "API_KEY",
"credentialProvider": {
"apiKeyCredentialProvider": {
"providerArn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:token-vault/default/apikeycredentialprovider/my-api-key",
"credentialLocation": "HEADER",
"credentialParameterName": "x-api-key",
"credentialPrefix": ""
}
}
}]'

````


Boto3

1. ```
import boto3

agentcore_client = boto3.client('bedrock-agentcore-control')

target = agentcore_client.create_gateway_target(
    gatewayIdentifier="your-gateway-id",
    name="MyMCPTarget",
    targetConfiguration={
        "mcp": {
            "mcpServer": {
                "endpoint": "https://my-mcp-server.example.com"
            }
        }
    },
    credentialProviderConfigurations=[
        {
            "credentialProviderType": "API_KEY",
            "credentialProvider": {
                "apiKeyCredentialProvider": {
                    "providerArn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:token-vault/default/apikeycredentialprovider/my-api-key",
                    "credentialLocation": "HEADER",
                    "credentialParameterName": "x-api-key",
                    "credentialPrefix": ""
                }
            }
        }
    ]
)
````

## Add a Connector target with Amazon Bedrock Managed Knowledge Bases

You can add the Amazon Bedrock Managed Knowledge Bases connector as a target to your gateway.

For more information about the Amazon Bedrock Managed Knowledge Bases connector, see [Amazon Bedrock Managed Knowledge Bases](gateway-target-connector-managed-kb.md "gateway-target-connector-managed-kb.md").

### Set up a managed knowledge base

The connector exposes two tools, each named after its backend operation: `AgenticRetrieveStream` (multi-step, streaming agentic retrieval) and `Retrieve` (a single hybrid search). You add a configuration entry per tool.

For `AgenticRetrieveStream`, set `retrievers` (the managed knowledge bases to query) and `agenticRetrieveConfiguration` in `parameterValues`. Both are required — omitting `agenticRetrieveConfiguration` causes a runtime error. It can be an empty object (`{}`) to accept service-managed defaults, but specifying `foundationModelType` and `rerankingModelType` makes the configuration explicit. The agent does not supply knowledge base IDs at call time. For `Retrieve`, set the `knowledgeBaseId` in `parameterValues`; it is required.

The connector supports only managed knowledge bases. Connector targets support only the `GATEWAY_IAM_ROLE` credential provider type.

###### Example

Boto3

1. The following Python code shows how to create a Gateway Target with the Amazon Bedrock Managed Knowledge Bases connector configuration using the AWS Python SDK (Boto3):

```
import boto3

gateway_client = boto3.client("bedrock-agentcore-control", region_name="<REGION>")

gateway_client.create_gateway_target(
    name="managed-kb",
    gatewayIdentifier="<GATEWAY_ID>",
    targetConfiguration={
        "mcp": {
            "connector": {
                "source": {"connectorId": "bedrock-knowledge-bases"},
                "configurations": [
                    {
                        "name": "AgenticRetrieveStream",
                        "parameterValues": {
                            "retrievers": [
                                {
                                    "description": "Product documentation",
                                    "configuration": {"knowledgeBase": {"knowledgeBaseId": "<KB_ID_1>"}},
                                },
                                {
                                    "description": "Engineering runbooks",
                                    "configuration": {"knowledgeBase": {"knowledgeBaseId": "<KB_ID_2>"}},
                                },
                            ],
                            "agenticRetrieveConfiguration": {
                                "foundationModelType": "MANAGED",
                                "rerankingModelType": "MANAGED",
                            },
                        },
                    },
                    {
                        "name": "Retrieve",
                        "parameterValues": {"knowledgeBaseId": "<KB_ID>"},
                    },
                ],
            }
        }
    },
    credentialProviderConfigurations=[
        {"credentialProviderType": "GATEWAY_IAM_ROLE"}
    ],
)
```

AWS CLI

1. The following command creates a Gateway Target with the Amazon Bedrock Managed Knowledge Bases connector configuration using the AWS CLI:

```
aws bedrock-agentcore-control create-gateway-target \
  --gateway-identifier "<GATEWAY_ID>" \
  --name "managed-kb" \
  --target-configuration '{
    "mcp": {
      "connector": {
        "source": {
          "connectorId": "bedrock-knowledge-bases"
        },
        "configurations": [
          {
            "name": "AgenticRetrieveStream",
            "parameterValues": {
              "retrievers": [
                {
                  "description": "Product documentation",
                  "configuration": {"knowledgeBase": {"knowledgeBaseId": "<KB_ID_1>"}}
                },
                {
                  "description": "Engineering runbooks",
                  "configuration": {"knowledgeBase": {"knowledgeBaseId": "<KB_ID_2>"}}
                }
              ],
              "agenticRetrieveConfiguration": {
                "foundationModelType": "MANAGED",
                "rerankingModelType": "MANAGED"
              }
            }
          },
          {
            "name": "Retrieve",
            "parameterValues": {
              "knowledgeBaseId": "<KB_ID>"
            }
          }
        ]
      }
    }
  }' \
  --credential-provider-configurations '[{"credentialProviderType": "GATEWAY_IAM_ROLE"}]' \
  --region "<REGION>"
```

AgentCore CLI

1. To add a managed knowledge base connector target, run `agentcore add gateway-target` with `--type connector --connector bedrock-knowledge-bases`:

```
agentcore add gateway-target \
  --name MyKnowledgeBaseTarget \
  --type connector \
  --connector bedrock-knowledge-bases \
  --knowledge-base-id <KB_ID> \
  --gateway MyGateway
agentcore deploy
```

Interactive

1. In the AgentCore CLI interactive terminal UI, run `agentcore add gateway-target`, then select **Amazon Bedrock Knowledge Bases** from the target type picker:

![Add Gateway Target menu with Amazon Bedrock Knowledge Bases highlighted in interactive terminal.](images/tui/knowledge-base-add.png)

The wizard prompts you for a name, description, and allow you to select one or more source types & sources.

After you call `CreateGatewayTarget`, the Gateway validates the configuration asynchronously (typically within about 30 seconds), which includes a `GetKnowledgeBase` check on each bound knowledge base. Poll `GetGatewayTarget` until `status` is `READY`; a `FAILED` status includes a reason describing the problem.

To customize agentic retrieval — for example, to cap planning iterations or attach a guardrail — add the optional fields to `agenticRetrieveConfiguration`. If you omit them, service-managed defaults apply. For all accepted values, see [Configuration reference](gateway-target-connector-managed-kb.md#gateway-target-connector-managed-kb-config-reference "gateway-target-connector-managed-kb.md#gateway-target-connector-managed-kb-config-reference").

```
{
  "name": "AgenticRetrieveStream",
  "parameterValues": {
    "retrievers": [
      { "configuration": { "knowledgeBase": { "knowledgeBaseId": "<KB_ID>" } } }
    ],
    "agenticRetrieveConfiguration": {
      "maxAgentIteration": 5,
      "policyConfiguration": {
        "guardrailConfiguration": {
          "guardrailId": "<GUARDRAIL_ID>",
          "guardrailVersion": "1"
        }
      }
    }
  }
}
```

### Control which parameters the agent can set

Each tool configuration entry accepts two parameter controls that determine what the calling agent sees and what the Gateway sends to the knowledge base:

- `parameterValues` — administrator-set values sent to the knowledge base on every call, such as the bound `knowledgeBaseId` or a default `numberOfResults`. These are used unless the agent overrides a field you have exposed.
- `parameterOverrides` — a list that controls which request fields the agent can see and set at call time. Each entry has:

  - `path` — the field in the `Retrieve` request, for example `$.retrievalQuery.text` or `$.retrievalConfiguration.managedSearchConfiguration.numberOfResults`.
  - `description` — optional text shown to the agent describing the field.
  - `visible` — set to `true` to expose the field to the agent, or `false` to hide it while still sending any administrator-configured default.

Bind `knowledgeBaseId` in `parameterValues` and do not expose it.

The following configuration entry binds the knowledge base, sets a default of 10 results, and exposes the query text and result count to the agent:

```
{
  "name": "Retrieve",
  "description": "Search the knowledge base for relevant documents.",
  "parameterValues": {
    "knowledgeBaseId": "<KB_ID>",
    "retrievalConfiguration": {
      "managedSearchConfiguration": {
        "numberOfResults": 10
      }
    }
  },
  "parameterOverrides": [
    {
      "path": "$.retrievalQuery.text",
      "description": "The search query. Use specific keywords for best results.",
      "visible": true
    },
    {
      "path": "$.retrievalConfiguration.managedSearchConfiguration.numberOfResults",
      "description": "Number of results to retrieve (1-100).",
      "visible": true
    }
  ]
}
```

### Configure the Gateway Service Role

This connector uses the **gateway execution role** — the IAM role ARN you pass to `CreateGateway`, which the AgentCore service assumes to call the backend on your behalf. This is a role you create, not a service-linked role. For the Amazon Bedrock Managed Knowledge Bases connector, it needs the following permissions:

- `bedrock:GetKnowledgeBase` — to validate the bound knowledge base when the target is created. Scoped to the managed knowledge base resource.
- `bedrock:Retrieve` — for the `Retrieve` tool. Scoped to the managed knowledge base resource.
- `bedrock:AgenticRetrieveStream` — for the `AgenticRetrieveStream` tool. This action is not scoped to a managed knowledge base resource, so grant it on `*`.

The Gateway signs the backend calls as the `bedrock` service. Include `bedrock:GetKnowledgeBase` regardless of which tools you add; if you add only one tool, include only that tool’s retrieval action.

###### Note

`bedrock-agentcore:InvokeGateway` is not part of the execution role. That permission belongs to the **caller** — the agent or application invoking the Gateway — not to the role the Gateway assumes.

Add a policy with the following content to the execution role attached to the Gateway:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ValidateKnowledgeBase",
      "Effect": "Allow",
      "Action": "bedrock:GetKnowledgeBase",
      "Resource": "arn:aws:bedrock:<REGION>:<ACCOUNT_ID>:knowledge-base/<KB_ID>"
    },
    {
      "Sid": "RetrieveFromKnowledgeBase",
      "Effect": "Allow",
      "Action": "bedrock:Retrieve",
      "Resource": "arn:aws:bedrock:<REGION>:<ACCOUNT_ID>:knowledge-base/<KB_ID>"
    },
    {
      "Sid": "AgenticRetrieveStream",
      "Effect": "Allow",
      "Action": "bedrock:AgenticRetrieveStream",
      "Resource": "*"
    }
  ]
}
```

The service role must also trust the AgentCore service so that it can assume the role. Attach the following trust policy, scoping it to your account and Gateway with the `aws:SourceAccount` and `aws:SourceArn` conditions:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAgentCoreToAssumeRole",
      "Effect": "Allow",
      "Principal": {
        "Service": "bedrock-agentcore.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<ACCOUNT_ID>"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:bedrock-agentcore:<REGION>:<ACCOUNT_ID>:gateway/*"
        }
      }
    }
  ]
}
```

## Add a Connector target with Web Search Tool

You can add a built-in connector as a target to your gateway. The Web Search Tool connector provides managed web search capabilities without requiring custom infrastructure or API keys.

For more information about the Web Search Tool connector, see [Web Search Tool](gateway-target-connector-web-search-tool.md "gateway-target-connector-web-search-tool.md").

### Set up Web Search Tool

###### Example

Boto3

1. The following Python code shows how to create a Gateway Target with the Web Search Tool connector configuration using the AWS Python SDK (Boto3):

```
import boto3

gateway_client = boto3.client("bedrock-agentcore-control", region_name="<REGION>")

gateway_client.create_gateway_target(
    name="web-search-tool",
    gatewayIdentifier="<GATEWAY_ID>",
    targetConfiguration={
        "mcp": {
            "connector": {
                "source": {"connectorId": "web-search"},
                "configurations": [{"name": "WebSearch", "parameterValues": {}}],
            }
        }
    },
    credentialProviderConfigurations=[
        {"credentialProviderType": "GATEWAY_IAM_ROLE"}
    ],
)
```

AWS CLI

1. The following command creates a Gateway Target with the Web Search Tool connector configuration using the AWS CLI:

```
aws bedrock-agentcore-control create-gateway-target \
  --gateway-identifier "<GATEWAY_ID>" \
  --name "web-search-tool" \
  --target-configuration '{
    "mcp": {
      "connector": {
        "source": {
          "connectorId": "web-search"
        },
        "configurations": [
          {
            "name": "WebSearch",
            "parameterValues": {}
          }
        ]
      }
    }
  }' \
  --credential-provider-configurations '[{"credentialProviderType": "GATEWAY_IAM_ROLE"}]' \
  --region "<REGION>"
```

AgentCore CLI

1. To add a Web Search Tool target, run `agentcore add gateway-target` with `--type connector --connector web-search`:

```
agentcore add gateway-target \
  --name MyWebSearchTarget \
  --type connector \
  --connector web-search \
  --gateway MyGateway
agentcore deploy
```

Interactive

1. In the AgentCore CLI interactive terminal UI, run `agentcore add gateway-target`, then select **Amazon Web Search** from the target type picker:

![Add Gateway Target menu with Amazon Web Search highlighted in interactive terminal.](images/tui/web-search-add.png)

The wizard prompts you for a target name, the gateway to attach to, and an optional list of domains to exclude from search results.

### Configure domain filtering

You can restrict which domains the Web Search Tool is allowed to query by configuring a domain denylist. This is useful for administrators who want to prevent agents from returning results from specific websites.

Domain filtering is configured at the tool level using the `parameterValues.domainFilter.exclude` field when creating or updating a Gateway Target. The denylist is enforced server-side and is hidden from the LLM — the agent is unaware of the restriction and simply receives no results from excluded domains.

The following examples create a Web Search Tool target with domain filtering that excludes results from `blocked-website-1.com` and `blocked-website-2.com`:

###### Example

Boto3

1. The following Python code shows how to create a Web Search Tool target with domain filtering using the AWS Python SDK (Boto3):

```
import boto3

gateway_client = boto3.client("bedrock-agentcore-control", region_name="<REGION>")

gateway_client.create_gateway_target(
    name="web-search-tool",
    gatewayIdentifier="<GATEWAY_ID>",
    targetConfiguration={
        "mcp": {
            "connector": {
                "source": {"connectorId": "web-search"},
                "configurations": [
                    {
                        "name": "WebSearch",
                        "parameterValues": {
                            "domainFilter": {
                                "exclude": ["blocked-website-1.com", "blocked-website-2.com"]
                            }
                        },
                    }
                ],
            }
        }
    },
    credentialProviderConfigurations=[
        {"credentialProviderType": "GATEWAY_IAM_ROLE"}
    ],
)
```

AWS CLI

1. The following command creates a Web Search Tool target with domain filtering using the AWS CLI:

```
aws bedrock-agentcore-control create-gateway-target \
  --gateway-identifier "<GATEWAY_ID>" \
  --name "web-search-tool" \
  --target-configuration '{
    "mcp": {
      "connector": {
        "source": {
          "connectorId": "web-search"
        },
        "configurations": [
          {
            "name": "WebSearch",
            "parameterValues": {
              "domainFilter": {
                "exclude": ["blocked-website-1.com", "blocked-website-2.com"]
              }
            }
          }
        ]
      }
    }
  }' \
  --credential-provider-configurations '[{"credentialProviderType": "GATEWAY_IAM_ROLE"}]' \
  --region "<REGION>"
```

AgentCore CLI

1. Pass a comma-separated list of domains via `--exclude-domains`:

```
agentcore add gateway-target \
  --name MyWebSearchTarget \
  --type connector \
  --connector web-search \
  --exclude-domains blocked-website-1.com,blocked-website-2.com \
  --gateway MyGateway
agentcore deploy
```

Interactive

1. In the AgentCore CLI interactive terminal UI, the Add Gateway Target wizard prompts for an optional comma-separated list of domains to exclude from search results after you select **Amazon Web Search** and choose a gateway. Leaving the prompt empty creates the target with no domain filtering.

![Domain filtering prompt for Web Search Tool in interactive terminal.](images/tui/web-search-domain-filter.png)

You can also update an existing target to add or modify domain filtering using `UpdateGatewayTarget`.

### Configure the Gateway Service Role

The Gateway needs a service role that allows the AgentCore service to perform actions on your behalf. For the Web Search Tool, the role needs the following permissions:

- `bedrock-agentcore:InvokeGateway` — to invoke the Gateway
- `bedrock-agentcore:InvokeWebSearch` — to authorize web search invocations, checked per-request against the service-owned ARN `arn:aws:bedrock-agentcore:<region>:aws:tool/web-search.v1`

Add a policy with the following content to the service role attached to the Gateway:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "InvokeGateway",
      "Effect": "Allow",
      "Action": "bedrock-agentcore:InvokeGateway",
      "Resource": "arn:aws:bedrock-agentcore:<REGION>:<ACCOUNT_ID>:gateway/*"
    },
    {
      "Sid": "InvokeWebSearch",
      "Effect": "Allow",
      "Action": "bedrock-agentcore:InvokeWebSearch",
      "Resource": "arn:aws:bedrock-agentcore:<REGION>:aws:tool/web-search.v1"
    }
  ]
}
```
