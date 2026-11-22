

# Configure lifecycle hooks for AgentCore Runtime

Lifecycle hooks are an optional, advanced way to run your own code at specific points in your agent runtime’s lifecycle. A lifecycle hook is an endpoint in your container that AgentCore Runtime calls at one of those points, for example to prepare your agent before sessions start so that sessions start faster. You configure hooks with the `hooksConfiguration` field of [CreateAgentRuntime](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateAgentRuntime.html) and [UpdateAgentRuntime](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateAgentRuntime.html), grouped by the lifecycle phase that they belong to.

Lifecycle hooks are available for agent runtimes that use platform version V2 on microVMs. For more information, see [Platform versions](runtime-how-it-works.md#runtime-platform-versions).

**Topics**
+ [Requirements](#runtime-lifecycle-hooks-requirements)
+ [How a hook call works](#runtime-lifecycle-hooks-how-it-works)
+ [Configure lifecycle hooks](#runtime-lifecycle-hooks-configure)
+ [Supported hooks](#runtime-lifecycle-hooks-supported)
+ [View hook logs](#runtime-lifecycle-hooks-logs)

## Requirements
<a name="runtime-lifecycle-hooks-requirements"></a>
+ The agent runtime must use platform version V2. On V1, the request fails with a `ValidationException`.
+ The agent runtime must use the microVMs compute type. Lifecycle hooks aren’t supported on Instances: if you combine `hooksConfiguration` with `capacityProviderConfiguration`, the request fails with a `ValidationException`.

## How a hook call works
<a name="runtime-lifecycle-hooks-how-it-works"></a>

When your agent runtime reaches a hook’s point in its lifecycle, AgentCore Runtime runs the hook’s action once. It makes a single request to your container and waits for your implementation to report success within the hook’s time limit. AgentCore Runtime doesn’t retry a hook call.

If the call fails, or doesn’t succeed within the time limit, the operation that triggered the hook fails. For example, when a build hook fails, the runtime moves to `CREATE_FAILED` or `UPDATE_FAILED` with a `failureReason` that describes the failure. For more information, see [Troubleshoot lifecycle hooks](runtime-troubleshooting.md#troubleshoot-runtime-lifecycle-hooks).

How your implementation reports success depends on the hook’s action.

### Hook actions
<a name="runtime-lifecycle-hooks-actions"></a>

Each hook has one action, which defines how AgentCore Runtime calls your container.

#### HTTP actions
<a name="runtime-lifecycle-hooks-http-actions"></a>

An HTTP action sends an HTTP request to the `path` and `port` that you choose, on a server in your container. Your implementation reports success by returning any `2xx` status code after its work is done. Any other status code, or a failed connection, fails the call. Each request may include headers that identify the call. Each hook lists the headers and values that it sends.

Hooks support the `httpPost` action, which sends a `POST` request. You configure it in the hook’s `action.httpPost` field, which has the following fields.


| Field | Type | Required | Description | 
| --- | --- | --- | --- | 
|  `path`  | String | Yes | The path that AgentCore Runtime sends the request to. The path must meet these rules:+  It contains 1–32 characters and matches the pattern `^/[A-Za-z0-9._~/-]*$`. <br />+  It’s in canonical form. It doesn’t end in `/` (except for the path `/` itself), and it doesn’t contain `//`, or `.` or `..` segments. <br />+  It doesn’t conflict with a route that AgentCore Runtime already uses on the same port. For more information, see [Platform routes](#runtime-lifecycle-hooks-routes).  | 
|  `port`  | Integer | No | The port that AgentCore Runtime sends the request to. The supported range is `8000`–`12000`, inclusive. Choose a port other than the [reserved platform ports](runtime-service-contract.md#runtime-reserved-ports). If you don’t specify a port, the default is your agent’s serving port: `protocolConfiguration.port` if you set it, otherwise the protocol’s default port (`8080` for HTTP and AG-UI, `8000` for MCP, and `9000` for A2A). Leave `port` unset unless a separate server in your container listens on another port. If no server listens on the port, the hook fails, and so does the create or update. | 

A hook’s route is its HTTP method, path, and port. It can’t match a route that AgentCore Runtime already uses on your agent’s serving port. The following table lists these platform routes.


**Platform routes that a hook can’t use**  

| Protocol | Routes that a hook can’t use | 
| --- | --- | 
| All protocols |  +   `POST` to the invocation path: `protocolConfiguration.path` if you set it, otherwise the protocol’s default (`/invocations` for HTTP and AG-UI, `/mcp` for MCP, and `/` for A2A) <br />+   `GET /ws`  <br />+   `GET /ping`    | 
| MCP |  `POST /mcp`, even if you change the invocation path | 
| A2A |  `GET /.well-known/agent-card.json`  | 

Conflicts compare the method as well as the path. For example, `POST /ping` is a valid hook route, because AgentCore Runtime uses `GET /ping`. For your serving port and invocation path, see [Configure your agent’s serving port and invocation path](runtime-configure-invocation.md).

**Note**  
If your agent runtime uses [session endpoints](runtime-session-endpoints.md), AgentCore Runtime protects your hooks from session endpoint requests:  
A request that targets a hook’s route is rejected with HTTP `403` and `AccessDenied` before it reaches your container. Path matching ignores case, and treats common equivalent spellings of a path as the same path. These include repeated or trailing slashes, `.` and `..` segments, percent-encoded characters, and `;` parameters.
Hook headers are reserved. AgentCore Runtime drops them from session endpoint requests, so your application receives hook headers only on hook calls.

## Configure lifecycle hooks
<a name="runtime-lifecycle-hooks-configure"></a>

Specify `hooksConfiguration` when you create or update an agent runtime. The following example creates a V2 runtime with a build warmup hook that calls `POST /warmup` on port `8080`. For what the hook does, see [Warmup hook](#runtime-lifecycle-hooks-warmup). Replace the Region, container image URI, and execution role ARN with your values.

**Example**  

```python
import boto3

client = boto3.client('bedrock-agentcore-control', region_name='us-west-2')

try:
    response = client.create_agent_runtime(
        agentRuntimeName='my_agent_runtime',
        agentRuntimeArtifact={
            'containerConfiguration': {
                'containerUri': '123456789012.dkr.ecr.us-west-2.amazonaws.com/my-agent:latest'
            }
        },
        networkConfiguration={'networkMode': 'PUBLIC'},
        roleArn='arn:aws:iam::123456789012:role/AgentRuntimeRole',
        platformVersion='V2',
        hooksConfiguration={
            'build': {
                'warmup': {
                    'action': {
                        'httpPost': {
                            'path': '/warmup',
                            'port': 8080
                        }
                    }
                }
            }
        }
    )

    print(f"Agent runtime created: {response['agentRuntimeArn']}")
except client.exceptions.ValidationException as e:
    print(f"Validation error: {e}")
```

```bash
aws bedrock-agentcore-control create-agent-runtime \
  --agent-runtime-name "my_agent_runtime" \
  --role-arn "arn:aws:iam::123456789012:role/AgentRuntimeRole" \
  --agent-runtime-artifact '{
    "containerConfiguration": {
      "containerUri": "123456789012.dkr.ecr.us-west-2.amazonaws.com/my-agent:latest"
    }
  }' \
  --network-configuration '{"networkMode": "PUBLIC"}' \
  --platform-version V2 \
  --hooks-configuration '{
    "build": {
      "warmup": {
        "action": {
          "httpPost": {"path": "/warmup", "port": 8080}
        }
      }
    }
  }'
```

 `UpdateAgentRuntime` replaces the whole hook configuration. Include `hooksConfiguration` in every update request for which you want to keep your hooks. To remove your hooks, call `UpdateAgentRuntime` without `hooksConfiguration`.

## Supported hooks
<a name="runtime-lifecycle-hooks-supported"></a>


| Phase | Hook | When AgentCore Runtime calls it | Use it to | 
| --- | --- | --- | --- | 
|  `build`  |  `warmup`  | While it prepares your agent, during `CreateAgentRuntime` and `UpdateAgentRuntime`  | Prepare memory and disk so that sessions start faster. For more information, see [Warmup hook](#runtime-lifecycle-hooks-warmup). | 

### Warmup hook
<a name="runtime-lifecycle-hooks-warmup"></a>

AgentCore Runtime calls the build warmup hook while it prepares your agent, during `CreateAgentRuntime` and `UpdateAgentRuntime`, after your agent passes its health check and before the runtime reaches `READY`.

AgentCore Runtime calls the hook twice, first with the warmup type `memory` and then with `disk`. With an HTTP action, it sends the warmup type in the `X-Amzn-Bedrock-AgentCore-Runtime-Warmup-Type` header.


| Warmup type | Order | What to do | 
| --- | --- | --- | 
|  `memory`  | First, after your agent passes its health check | Load into memory what every session needs, such as imports, models, and caches. Each new session starts with what you load here. | 
|  `disk`  | Second, after the snapshot | Read the files that your agent reads when a session starts. AgentCore Runtime uses these reads to make those files fast for new sessions. | 

The two calls share a time limit of 120 seconds, which you can’t change. A warmup hook can add up to 120 seconds to the time that `CreateAgentRuntime` and `UpdateAgentRuntime` take to reach `READY`. Each warmup log line can appear more than once for one create or update.

For how to use the warmup hook to make the first requests of new sessions fast, see [Prepare your agent before sessions start](runtime-v2-optimize.md#runtime-v2-optimize-warmup).

#### Write the warmup handler
<a name="runtime-lifecycle-hooks-warmup-handler"></a>

Your warmup handler runs in your agent’s server, alongside `/ping` and your invocation handler:
+  **Keep `/ping` responsive.** Your server must keep answering `/ping` while the warmup runs. Don’t block your server’s only thread inside the warmup handler. Run the work in a separate thread or process, or use a server that handles requests concurrently.
+  **Return `2xx` only after the work is done.** What you’ve loaded when you respond is what sessions start with.
+  **Serve the warmup hook from a single server process.** AgentCore Runtime sends each warmup call to one process. Sessions start with what that process and the processes that it starts hold when the call returns. If your server runs several worker processes, for example `uvicorn --workers 2`, the other workers don’t receive the call.

The following FastAPI application serves `/ping`, `/invocations`, and a warmup hook at `POST /warmup` on port `8080`. It runs the warmup work in a worker thread, so the server keeps answering `/ping`. Replace `load_shared_state` and `STARTUP_FILES` with your agent’s own work and files.

```python
import asyncio

from fastapi import FastAPI, Request, Response

app = FastAPI()

# Files that each session reads when it starts.
STARTUP_FILES = ["/app/models/tokenizer.json", "/app/config/agent.json"]


def load_shared_state():
    # Load what every session needs into memory, such as heavy imports,
    # model weights, and caches.
    ...


def read_startup_files():
    # Read the files that a session reads when it starts, so that new
    # sessions can use them faster.
    for path in STARTUP_FILES:
        with open(path, "rb") as f:
            while f.read(1024 * 1024):
                pass


@app.get("/ping")
def ping():
    return {"status": "Healthy"}


@app.post("/warmup")
async def warmup(request: Request):
    # Header lookup in Starlette and FastAPI is case-insensitive.
    warmup_type = request.headers.get(
        "X-Amzn-Bedrock-AgentCore-Runtime-Warmup-Type", ""
    ).lower()

    # Run the work in a worker thread so that /ping keeps answering.
    if warmup_type == "memory":
        await asyncio.to_thread(load_shared_state)
    elif warmup_type == "disk":
        await asyncio.to_thread(read_startup_files)

    # Respond only after the work is done.
    return Response(status_code=200)


@app.post("/invocations")
async def invoke(request: Request):
    payload = await request.json()
    # Per-request work runs here on every session.
    return {"response": payload.get("prompt", "")}
```

If you save the application as `app.py`, start it in your container with the following command:

```bash
uvicorn app:app --host 0.0.0.0 --port 8080
```

## View hook logs
<a name="runtime-lifecycle-hooks-logs"></a>

AgentCore Runtime writes the progress and result of each build hook call to your runtime’s log group, `/aws/bedrock-agentcore/runtimes/<agentRuntimeId>-DEFAULT`, in log streams whose names start with `build-logs-`. Each line starts with `[LIFECYCLE-HOOK <epoch-milliseconds>]`, followed by `[LIFECYCLE]` for progress or `[ERROR]` for failures. For the lines and how to act on them, see [Troubleshoot lifecycle hooks](runtime-troubleshooting.md#troubleshoot-runtime-lifecycle-hooks).