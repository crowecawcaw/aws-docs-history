# Pass custom headers to Amazon Bedrock AgentCore Runtime

Custom headers let you pass contextual information from your application directly to your
agent code without cluttering the main request payload. This includes authentication tokens
like JWT (JSON Web Tokens, which contain user identity and authorization claims) through the
`Authorization` header, allowing your agent to make decisions based on who is calling it. You
can also pass custom metadata like user preferences, session identifiers, or trace context
using headers prefixed with `X-Amzn-Bedrock-AgentCore-Runtime-Custom-`, giving
your agent access to up to 20 pieces of runtime context that travel alongside each request.
This information can be also used in downstream systems like AgentCore Memory that you can
namespace based on those characteristics like `user_id` or `aud` in
claims like line of business.

Amazon Bedrock AgentCore Runtime lets you pass headers in a request to your agent code provided the
headers match the following criteria:

- Header name is one of the following:
  - Starts with `X-Amzn-Bedrock-AgentCore-Runtime-Custom-`
  - Equal to `Authorization`. This is reserved for agents with
    OAuth inbound access to pass in the incoming JWT token to the agent
    code.

- Header value is not greater than 4KB in size.
- Up to 20 headers can be configured per runtime.

###### Topics

- [Step 1: Create your agent](#create-agent-headers "#create-agent-headers")
- [Step 2: Deploy your agent](#deploy-agentcore-runtime "#deploy-agentcore-runtime")
- [Step 3: Invoke your agent with custom headers](#invoke-custom-headers "#invoke-custom-headers")
- [Step 4: (Optional) Pass the JWT token used for OAuth based inbound access to your agent](#pass-jwt-token "#pass-jwt-token")

## Step 1: Create your agent

Start by creating a basic agent with the following project structure:

```

your_project_directory/
├── agent_example.py # Your main agent code
└── requirements.txt # Dependencies for your agent

```

Create the following files:

###### agent_example.py

Create your main agent code file and add the following code:

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

###### requirements.txt

Create your dependencies file and add the following dependencies:

```

strands-agents
bedrock-agentcore

```

## Step 2: Deploy your agent

Configure your agent with the starter toolkit:

```
agentcore configure --entrypoint agent_example.py \
--name hello_agent \
--execution-role `your-execution-role-arn` \
--disable-otel \
--requirements-file requirements.txt \
--request-header-allowlist "X-Amzn-Bedrock-AgentCore-Runtime-Custom-H1"
```

Deploy your agent with the starter toolkit:

```

agentcore launch

```

Note the agent runtime ARN from the output. you need it in the next step.

## Step 3: Invoke your agent with custom headers

Starter toolkit Use the Amazon Bedrock AgentCore starter toolkit command line interface to invoke
your agent with custom headers.

```

agentcore invoke '{"prompt": "Hello what is 1+1?"}' --headers "X-Amzn-Bedrock-AgentCore-Runtime-Custom-H1:test header"

```

Python
Use boto3 with event handlers to add custom headers to your agent
invocation.

For more details on botocore events, see [botocore events documentation](https://botocore.amazonaws.com/v1/documentation/api/latest/topics/events.html "https://botocore.amazonaws.com/v1/documentation/api/latest/topics/events.html").

```
import json
import boto3

agent_arn = `YOUR_AGENT_ARN_HERE`
prompt = "Tell me a joke"


agent_core_client = boto3.client('bedrock-agentcore')
event_system = agent_core_client.meta.events

# Constants for event handler configuration
EVENT_NAME = 'before-sign.bedrock-agentcore.InvokeAgentRuntime'
CUSTOM_HEADER_NAME = 'X-Amzn-Bedrock-AgentCore-Runtime-Custom-H1'
CUSTOM_HEADER_VALUE = 'test header1'

def add_custom_runtime_header(request, **kwargs):
    """Add custom header for agent runtime authentication/identification."""
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

## Step 4: (Optional) Pass the JWT token used for OAuth based inbound access to your agent

For information about setting up an agent with OAuth inbound access and enabling an
Authorization header to be passed into AgentCore Runtime, see [Authenticate and authorize with Inbound Auth and Outbound Auth](runtime-oauth.md "runtime-oauth.md").
