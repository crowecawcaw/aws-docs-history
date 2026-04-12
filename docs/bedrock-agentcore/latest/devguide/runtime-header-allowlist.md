# Pass custom headers to Amazon Bedrock AgentCore Runtime

Custom headers let you pass contextual information from your application directly to your agent code without cluttering the main request payload. This includes authentication tokens like JWT (JSON Web Tokens, which contain user identity and authorization claims) through the `Authorization` header, allowing your agent to make decisions based on who is calling it. You can also pass custom metadata like user preferences, session identifiers, or trace context using headers prefixed with `X-Amzn-Bedrock-AgentCore-Runtime-Custom-` , giving your agent access to up to 20 pieces of runtime context that travel alongside each request. This information can be also used in downstream systems like AgentCore Memory that you can namespace based on those characteristics like `user_id` or `aud` in claims like line of business.

Amazon Bedrock AgentCore Runtime lets you pass headers in a request to your agent code provided the headers match the following criteria:

- Header name is one of the following:
  - Starts with `X-Amzn-Bedrock-AgentCore-Runtime-Custom-`
  - Equal to `Authorization` . This is reserved for agents with OAuth inbound access to pass in the incoming JWT token to the agent code.

- Header value is not greater than 4KB in size.
- Up to 20 headers can be configured per runtime.

###### Topics

- [Step 1: Create your agent](#create-agent-headers "#create-agent-headers")
- [Step 2: Configure and deploy your agent with custom headers](#deploy-agentcore-runtime "#deploy-agentcore-runtime")
- [Step 3: Invoke your agent with custom headers](#invoke-custom-headers "#invoke-custom-headers")
- [Step 4: (Optional) Configure inbound JWT authentication](#pass-jwt-token "#pass-jwt-token")

## Step 1: Create your agent

Create an AgentCore project using the AgentCore CLI:

```
agentcore create --name MyHeaderAgent
cd MyHeaderAgent
```

Update your agent’s entrypoint file to access the custom headers from the request context:

```
import json
from bedrock_agentcore import BedrockAgentCoreApp, RequestContext
from strands import Agent

app = BedrockAgentCoreApp()
agent = Agent()

@app.entrypoint
def agent_invocation(payload, context: RequestContext):
    """Handler for agent invocation"""
    user_message = payload.get(
        "prompt", "No prompt found in input, please guide customer to create a json payload with prompt key"
    )
    app.logger.info("invoking agent with user message: %s", payload)
    response = agent(user_message)

    # access request headers here
    request_headers = context.request_headers
    app.logger.info("Headers: %s", json.dumps(request_headers))
    return response

app.run()
```

## Step 2: Configure and deploy your agent with custom headers

Configure the request header allowlist on your agent runtime so that custom headers are forwarded to your agent code at invocation time.

###### Example

AgentCore CLI

1. Add the `requestHeaderAllowlist` field to your agent configuration in `agentcore/agentcore.json` :

```
{
  "agents": [
    {
      "name": "MyHeaderAgent",
      "requestHeaderAllowlist": [
        "X-Amzn-Bedrock-AgentCore-Runtime-Custom-H1",
        "X-Amzn-Bedrock-AgentCore-Runtime-Custom-UserId"
      ]
    }
  ]
}
```

Deploy your agent:

```
agentcore deploy
```

Note the agent runtime ARN from the output. You need it if you plan to invoke using the AWS SDK.

AWS SDK

1. After deploying your agent, update the runtime configuration using the AWS SDK:

```
import boto3

client = boto3.client('bedrock-agentcore')

client.update_agent_runtime(
    agentRuntimeId='your-runtime-id',
    requestHeaderConfiguration={
        'requestHeaderAllowlist': [
            'X-Amzn-Bedrock-AgentCore-Runtime-Custom-H1'
        ]
    }
)
```

You can find your runtime ID by running `agentcore status`.

## Step 3: Invoke your agent with custom headers

Pass custom headers when invoking your agent so that your agent code can access them through the request context.

###### Example

AgentCore CLI

1. Use the `-H` flag to pass custom headers with `agentcore invoke` :

```
agentcore invoke "Tell me a joke" \
  -H "X-Amzn-Bedrock-AgentCore-Runtime-Custom-H1: test header1"
```

You can pass multiple headers by repeating the `-H` flag:

```
agentcore invoke "Tell me a joke" \
  -H "X-Amzn-Bedrock-AgentCore-Runtime-Custom-H1: test header1" \
  -H "X-Amzn-Bedrock-AgentCore-Runtime-Custom-UserId: user-123"
```

AWS SDK

1. Use boto3 with event handlers to add custom headers to your agent invocation. For more details on botocore events, see [botocore events documentation](https://botocore.amazonaws.com/v1/documentation/api/latest/topics/events.html "https://botocore.amazonaws.com/v1/documentation/api/latest/topics/events.html").

```
import json
import boto3

agent_arn = YOUR_AGENT_ARN_HERE
prompt = "Tell me a joke"

agent_core_client = boto3.client('bedrock-agentcore')
event_system = agent_core_client.meta.events

EVENT_NAME = 'before-sign.bedrock-agentcore.InvokeAgentRuntime'
CUSTOM_HEADER_NAME = 'X-Amzn-Bedrock-AgentCore-Runtime-Custom-H1'
CUSTOM_HEADER_VALUE = 'test header1'

def add_custom_runtime_header(request, **kwargs):
    request.headers.add_header(CUSTOM_HEADER_NAME, CUSTOM_HEADER_VALUE)

handler = event_system.register_first(EVENT_NAME, add_custom_runtime_header)

payload = json.dumps({"prompt": prompt}).encode()
response = agent_core_client.invoke_agent_runtime(
    agentRuntimeArn=agent_arn,
    payload=payload
)

event_system.unregister(EVENT_NAME, handler)

content = []
for chunk in response.get("response", []):
    content.append(chunk.decode('utf-8'))
print(json.loads(''.join(content)))
```

## Step 4: (Optional) Configure inbound JWT authentication

To pass the JWT token used for OAuth-based inbound access to your agent, configure `authorizerType` and `authorizerConfiguration` in your agent configuration.

###### Example

AgentCore CLI

1. Add the authorizer configuration to your agent in `agentcore/agentcore.json` :

```
{
  "agents": [
    {
      "name": "MyHeaderAgent",
      "authorizerType": "CUSTOM_JWT",
      "authorizerConfiguration": {
        "customJwtAuthorizer": {
          "discoveryUrl": "https://cognito-idp.us-east-1.amazonaws.com/user-pool-id/.well-known/openid-configuration",
          "allowedAudience": ["your-client-id"],
          "allowedClients": ["your-client-id"]
        }
      },
      "requestHeaderAllowlist": [
        "Authorization"
      ]
    }
  ]
}
```

Deploy to apply the configuration:

```
agentcore deploy
```

With this configuration, the `Authorization` header from incoming requests is validated against your OIDC provider and forwarded to your agent code.

AWS SDK

1. For information about setting up an agent with OAuth inbound access using the AWS SDK, see [Authenticate and authorize with Inbound Auth and Outbound Auth](runtime-oauth.md "runtime-oauth.md").
