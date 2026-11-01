

# Configure your agent’s serving port and invocation path
<a name="runtime-configure-invocation"></a>

Use `protocolConfiguration.port` and `protocolConfiguration.path` to customize your agent server’s serving port and invocation path. You continue to call `InvokeAgentRuntime` with the runtime ARN, session ID, and payload. AgentCore Runtime sends the POST request to the configured destination in your container.

For example, an existing application might accept `POST /agent/invoke` on port `9090`. You can configure Runtime to use that endpoint without changing the application’s invocation route.

You can use these settings without session endpoints. Omit `allowedPorts` if you only need to customize `InvokeAgentRuntime`.

To reach other routes or servers in the session, enable session endpoints. See [How session endpoints work](runtime-session-endpoints.md#runtime-session-endpoints-how-it-works).

**Note**  
Custom serving port and invocation path settings are supported for microVM runtimes. They aren’t supported for the Instances compute type with capacity providers.

## Serving port and invocation path settings
<a name="runtime-configure-invocation-settings"></a>

Specify the settings in `protocolConfiguration` when you call [CreateAgentRuntime](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateAgentRuntime.html).

 `serverProtocol`   
The application’s protocol: `HTTP`, `MCP`, `A2A`, or `AGUI`. Include this field when you supply `protocolConfiguration`.

 `port`   
The serving port for your agent server. The supported range is `8000`–`12000`, inclusive. Choose a port other than the [reserved platform ports](runtime-service-contract.md#runtime-reserved-ports).  
Configure your server to listen on `0.0.0.0` at that port. Setting this field does not start or reconfigure the server.

 `path`   
The container path to which `InvokeAgentRuntime` sends its POST request. It must start with `/` and contain 1–2048 characters.  
Supported characters are letters, digits, `/`, `-`, `.`, `_`, `~`, and valid percent-encoded sequences, such as `%20`. Supply a path without a query string or fragment.

The serving port and invocation path overrides are independent. If you specify only a serving port, Runtime keeps the protocol’s default invocation path. If you specify only an invocation path, Runtime keeps the protocol’s default serving port.


| Protocol | Default serving port | Default invocation path | 
| --- | --- | --- | 
| HTTP |  `8080`  |  `/invocations`  | 
| MCP |  `8000`  |  `/mcp`  | 
| A2A |  `9000`  |  `/`  | 
| AG-UI (`AGUI`) |  `8080`  |  `/invocations`  | 

The invocation method remains POST. Only `InvokeAgentRuntime` uses the path override. `InvokeAgentRuntimeWithWebSocketStream` always connects to `/ws` on the configured serving port.

## Configure your application server
<a name="runtime-configure-invocation-server"></a>

Your server must listen on `0.0.0.0` at the configured serving port.

The following FastAPI application accepts invocations at `/agent/invoke`. Replace the invocation handler with your agent logic.

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class InvocationRequest(BaseModel):
    prompt: str


@app.get("/ping")
def ping():
    return {"status": "Healthy"}


@app.post("/agent/invoke")
def invoke(request: InvocationRequest):
    return {"response": request.prompt}
```

If you save the application as `app.py`, start it in your container with the following command:

```
uvicorn app:app --host 0.0.0.0 --port 9090
```

For packaging instructions, see [Get started without the AgentCore CLI](getting-started-custom.md). For permissions, see [Execution role for running an agent in AgentCore Runtime](runtime-permissions.md#runtime-permissions-execution).

## Create and invoke the runtime
<a name="runtime-configure-invocation-create"></a>

The following example creates a runtime for the application. Replace the Region, container image URI, and execution role ARN with your values.

The image must include your application and its dependencies. It must start the server on port `9090`.

```
import boto3

region = "us-west-2"
control = boto3.client("bedrock-agentcore-control", region_name=region)

runtime = control.create_agent_runtime(
    agentRuntimeName="custom_endpoint_agent",
    agentRuntimeArtifact={
        "containerConfiguration": {
            "containerUri": (
                "123456789012.dkr.ecr.us-west-2.amazonaws.com/my-agent:latest"
            )
        }
    },
    roleArn="arn:aws:iam::123456789012:role/AgentCoreRuntimeExecutionRole",
    networkConfiguration={"networkMode": "PUBLIC"},
    protocolConfiguration={
        "serverProtocol": "HTTP",
        "port": 9090,
        "path": "/agent/invoke",
    },
)

agent_runtime_arn = runtime["agentRuntimeArn"]
```

This request omits `allowedPorts`. It configures invocation routing without enabling session endpoints.

After the runtime reaches `READY` status, invoke it as usual. You can check the status with [GetAgentRuntime](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetAgentRuntime.html).

```
import json
import uuid

client = boto3.client("bedrock-agentcore", region_name=region)
response = client.invoke_agent_runtime(
    agentRuntimeArn=agent_runtime_arn,
    runtimeSessionId=str(uuid.uuid4()),
    contentType="application/json",
    payload=json.dumps({"prompt": "Hello"}).encode("utf-8"),
)

try:
    print(response["response"].read().decode("utf-8"))
finally:
    response["response"].close()
```

Runtime sends this request to `POST /agent/invoke` on port `9090` in the session’s container. You still call the standard `InvokeAgentRuntime` API endpoint.

## Related topics
<a name="runtime-configure-invocation-related-topics"></a>
+  [Configure allowed ports](runtime-session-endpoints.md#runtime-session-endpoints-allowed-ports) 
+  [Reserved platform ports](runtime-service-contract.md#runtime-reserved-ports) 