# Configuration

Interceptors can be configured with an input parameter called `passRequestHeaders`

## Interceptor input configuration

When configuring interceptors, you can specify whether request headers should be passed to the interceptor function using the `passRequestHeaders` field:

**`passRequestHeaders`**

A boolean value that determines whether request headers are included in the interceptor input payload. When set to `true`, all request headers will be passed to your interceptor Lambda function. When set to `false` (default), headers are not included.

###### Warning

Use caution when setting this to `true` as request headers may contain sensitive information such as authentication tokens and credentials.

## Configuring interceptors during gateway creation

The following examples show how to create a gateway with interceptors that have `passRequestHeaders` set to `true`:

AgentCore starter toolkit (CLI)
Use the following command to create a gateway with interceptors configured to pass request headers:

```
agentcore create_mcp_gateway \
  --region us-west-2 \
  --name my-gateway-with-headers \
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
      "interceptionPoints": ["REQUEST", "RESPONSE"],
      "inputConfiguration": {
        "passRequestHeaders": true
      }
  }]'
```

AgentCore starter toolkit (Python)
Use the following Python code to create a gateway with interceptors configured to pass request headers:

```
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient

# Initialize the Gateway client
client = GatewayClient(region_name="us-west-2")

# Create the gateway with interceptor configurations
gateway = client.create_mcp_gateway(
  name="my-gateway-with-headers",
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
      "interceptionPoints": ["REQUEST", "RESPONSE"],
      "inputConfiguration": {
        "passRequestHeaders": True
      }
  }],
  enable_semantic_search=False
)

print(f"MCP Endpoint: {gateway['gatewayUrl']}")
```

AWS CLI
Use the following AWS CLI command to create a gateway with interceptors configured to pass request headers:

```
aws bedrock-agentcore-control create-gateway \
  --name my-gateway-with-headers \
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
      "interceptionPoints": ["REQUEST", "RESPONSE"],
      "inputConfiguration": {
        "passRequestHeaders": true
      }
  }]'
```

AWS Python SDK (Boto3)
Use the following Python code with the AWS Python SDK (Boto3) to create a gateway with interceptors configured to pass request headers:

```
import boto3

# Initialize the AgentCore client
client = boto3.client('bedrock-agentcore-control')

# Create a gateway
gateway = client.create_gateway(
  name="my-gateway-with-headers",
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
      "interceptionPoints": ["REQUEST", "RESPONSE"],
      "inputConfiguration": {
        "passRequestHeaders": True
      }
  }]
)

print(f"MCP Endpoint: {gateway['gatewayUrl']}")
```

## Updating interceptor configurations

You can update existing gateway interceptor configurations to modify the `passRequestHeaders` setting or other parameters using the update gateway API operations.
