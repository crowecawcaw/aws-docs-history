

# Connect to runtime sessions through a session endpoint
<a name="runtime-session-endpoints"></a>

With session endpoints, you can connect to application servers running inside an Amazon Bedrock AgentCore Runtime session. A session endpoint is an authenticated HTTPS URL that addresses one runtime session. Use it to:
+ View a web preview.
+ Call custom HTTP routes.
+ Stream responses.
+ Call a gRPC service.
+ Open a WebSocket connection.

Configure `allowedPorts` to choose which container ports you can reach. Connect through the session endpoint URL that Runtime returns.

For each request, Runtime checks your credentials and access to the requested port. It forwards allowed requests to your server and relays the response.

To customize `InvokeAgentRuntime` without session endpoints, see [Configure your agent’s serving port and invocation path](runtime-configure-invocation.md).

**Note**  
Session endpoints and custom invocation settings support microVM runtimes. They don’t support Instances with capacity providers. Session endpoints use public HTTPS ingress. AWS PrivateLink ingress isn’t supported.

## Session endpoints and runtime endpoints
<a name="runtime-session-endpoints-vs-runtime-endpoints"></a>

A session endpoint is different from a [runtime endpoint](runtime-how-it-works.md#runtime-endpoints), which AgentCore Runtime already provides. They solve different problems:
+  **Use a runtime endpoint to reach your agent.** A runtime endpoint, such as `DEFAULT`, controls which version of your agent callers reach. `InvokeAgentRuntime` calls resolve through it, so you can keep development and production on different versions and promote or roll back without changing callers.
+  **Use a session endpoint to reach what your agent runs.** An agent often starts other applications in its session, such as a web preview of the app it’s building, a development server, or a service it’s testing. A session endpoint is an authenticated URL that opens those applications, on only the ports that you allow.


|  | Runtime endpoint | Session endpoint | 
| --- | --- | --- | 
| What it is | Named pointer to an agent version, such as `DEFAULT` or `prod`, with its own ARN | HTTPS URL for one runtime session. It isn’t a separate resource. | 
| Typical use | Separate development and production, promote and roll back | Web previews, custom APIs, streaming, gRPC, and WebSocket connections | 
| Created by |  `CreateAgentRuntime` (`DEFAULT`) and `CreateAgentRuntimeEndpoint`  | Runtime, when a session starts on a runtime with `allowedPorts`  | 
| How you use it |  `InvokeAgentRuntime` with `qualifier`  | Send authenticated HTTPS requests to the returned URL | 
| What it reaches | The agent’s serving port and invocation path | Any port in `allowedPorts`, with any method and path | 
| Version | Chooses the version | Uses the session it belongs to, which was created through a runtime endpoint | 
| Scope | All sessions that use the endpoint | One session | 
| Lifetime | Until you delete it | Tied to the session’s lifecycle | 

Continue to send requests to your agent with `InvokeAgentRuntime`. When you invoke the agent through a runtime endpoint, Runtime returns a session endpoint URL for the session that the invocation uses. Use that URL to reach the other servers in the session.

## How session endpoints work
<a name="runtime-session-endpoints-how-it-works"></a>

1. Create a runtime with `allowedPorts` and an application that listens on those ports.

1. Start or reuse a session with a Runtime operation, such as `InvokeAgentRuntime`. Read the session endpoint URL from the response header.

1. Send an authenticated request to the session endpoint URL. Choose the hostname for your port and the path for your application.

1. Runtime checks access to the runtime and the requested port. It prepares compute if needed and forwards the request to your application.

The proxy preserves the application’s HTTP method, path, query string, and request body. For example, `GET /preview/index.html` reaches that route on your server, and `POST /api/tasks` reaches `/api/tasks`. `protocolConfiguration.path` does not rewrite or prepend a path to session endpoint requests.

The proxy doesn’t forward the session endpoint hostname. Your application receives an internal Runtime hostname in the `Host` header, and the request doesn’t include an `X-Forwarded-Host` header. The internal hostname can change, so don’t depend on its value.
+ If your server validates the `Host` header, configure it to accept the requests that Runtime forwards. For example, set `server.allowedHosts` to `true` for the Vite dev server, or set `devServer.allowedHosts` to `'all'` for webpack-dev-server. Other frameworks have similar settings, such as `ALLOWED_HOSTS` in Django.
+ Use relative URLs for links, assets, and redirects. Absolute URLs that your application builds from the `Host` header point to the internal hostname, which clients can’t reach.

Start your application servers and bind them to `0.0.0.0` on their configured ports. Adding a port to `allowedPorts` doesn’t start or configure a server.

The agent server must also satisfy the [Runtime service contract](runtime-service-contract.md).

## Configure allowed ports
<a name="runtime-session-endpoints-allowed-ports"></a>

Set `allowedPorts` in the [CreateAgentRuntime](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateAgentRuntime.html) request. The list follows these rules:
+ Include 1–5 entries. Each entry specifies exactly one `port` or one `portRange`.
+ Port numbers and range endpoints must be between `8000` and `12000`, inclusive.
+ A range includes both its `from` and `to` ports. `from` must be less than or equal to `to`.
+ Entries must be unique and must not overlap, including a single port that falls inside another entry’s range.
+ Exclude all [reserved platform ports](runtime-service-contract.md#runtime-reserved-ports), including `8443`. Runtime rejects a range that contains even one reserved port.

Omit `allowedPorts` when creating a runtime if you don’t need session endpoints.

The example allows the default HTTP serving port `8080`, web application ports `8081`–`8086`, and gRPC port `10000`. The range counts as one entry.

Replace the Region, image URI, and execution role ARN with your values. Use an AWS SDK version that supports `allowedPorts` and the serving port and invocation path settings.

```
import boto3

region = "us-west-2"
control = boto3.client("bedrock-agentcore-control", region_name=region)

runtime = control.create_agent_runtime(
    agentRuntimeName="session_endpoint_agent",
    agentRuntimeArtifact={
        "containerConfiguration": {
            "containerUri": (
                "123456789012.dkr.ecr.us-west-2.amazonaws.com/my-agent:latest"
            )
        }
    },
    roleArn="arn:aws:iam::123456789012:role/AgentCoreRuntimeExecutionRole",
    networkConfiguration={"networkMode": "PUBLIC"},
    protocolConfiguration={"serverProtocol": "HTTP"},
    allowedPorts=[
        {"port": 8080},
        {"portRange": {"from": 8081, "to": 8086}},
        {"port": 10000},
    ],
)

agent_runtime_arn = runtime["agentRuntimeArn"]
```

You can also combine `allowedPorts` with a custom `protocolConfiguration.port` or `.path`. If you want to access the custom serving port through the session endpoint URL, include that port in `allowedPorts`.

## Get the session endpoint URL
<a name="runtime-session-endpoints-get-url"></a>

After the runtime reaches `READY` status, invoke it to establish a session. For a runtime with session endpoints enabled, the response can include this header:

```
X-Amzn-Bedrock-AgentCore-Runtime-Session-Endpoint-Url
```

The following operations can return the header:
+  `InvokeAgentRuntime` 
+  `InvokeAgentRuntimeWithWebSocketStream` 
+  `InvokeAgentRuntimeCommand` 
+  `InvokeAgentRuntimeCommandShell` 
+  `GetAgentCard` 

For the two WebSocket operations, read the header from the HTTP `101 Switching Protocols` handshake response. SDKs that model the header expose it as `sessionEndpointUrl`.

The header is optional. Runtime omits it when session endpoints aren’t enabled or a session endpoint URL isn’t available. `CreateAgentRuntime` stores the configuration but does not return a session endpoint URL.

The following IAM-authenticated example invokes the runtime and reads the URL. It uses `sessionEndpointUrl` when your SDK exposes it, and otherwise reads the raw header. You can read the URL before consuming the response body.

```
import json
import uuid

client = boto3.client("bedrock-agentcore", region_name=region)
session_id = str(uuid.uuid4())
response = client.invoke_agent_runtime(
    agentRuntimeArn=agent_runtime_arn,
    runtimeSessionId=session_id,
    contentType="application/json",
    payload=json.dumps({"prompt": "Hello"}).encode("utf-8"),
)

try:
    headers = response["ResponseMetadata"]["HTTPHeaders"]
    session_endpoint_url = response.get("sessionEndpointUrl") or headers.get(
        "x-amzn-bedrock-agentcore-runtime-session-endpoint-url"
    )
    if not session_endpoint_url:
        raise RuntimeError(
            "No session endpoint URL returned. Check the allowedPorts configuration."
        )
    print(response["response"].read().decode("utf-8"))
finally:
    response["response"].close()
```

For an OAuth-configured runtime, send an authenticated HTTPS invocation and read the same response header. For instructions, see [Authenticate and authorize with Inbound Auth and Outbound Auth](runtime-oauth.md).

Store the returned URL with the corresponding session ID. The opaque identifier in the URL is different from `runtimeSessionId`; use the URL returned by Runtime.

## Select the destination port and path
<a name="runtime-session-endpoints-select-port"></a>

An unprefixed session endpoint URL uses the agent’s configured serving port. If `protocolConfiguration.port` is omitted, it uses the protocol default: `8080` for HTTP and AG-UI, `8000` for MCP, or `9000` for A2A.

To select another port, prefix the first hostname label with the port number and two hyphens (`--`). Keep the session endpoint identifier and the service domain from the returned URL.

```
https://<session-endpoint-id>.<service-domain>/application/path
https://8081--<session-endpoint-id>.<service-domain>/application/path
https://10000--<session-endpoint-id>.<service-domain>/package.Service/Method
```

The first URL uses the serving port. The second selects port `8081`, and the third selects port `10000`. The client connects over TLS on port `443`; the hostname prefix selects the destination port inside the session.

Every selected port must be in `allowedPorts`. This includes the serving port used by an unprefixed URL.

You can allow only additional application ports and omit the serving port from the list. In that case, use a port-prefixed URL. Runtime denies requests to the unprefixed URL with HTTP `403`.

For the example runtime, construct a preview URL for port `8081` as follows:

```
from urllib.parse import urlsplit, urlunsplit

parts = urlsplit(session_endpoint_url)
preview_url = urlunsplit(
    ("https", f"8081--{parts.hostname}", "/", "", "")
)
```

Append the path and query string that your application expects. Authenticate requests for web preview assets as well as requests for the initial page.

## Authenticate requests
<a name="runtime-session-endpoints-authentication"></a>

Use the inbound authentication mode configured for your runtime. Each HTTP request, HTTP/2 stream, and WebSocket handshake requires authentication. Possession of a session endpoint URL does not grant access.

### IAM and Signature Version 4
<a name="runtime-session-endpoints-sigv4"></a>

IAM callers need `bedrock-agentcore:InvokeAgentRuntimeProxy` permission for the runtime and runtime endpoint. If you use `InvokeAgentRuntime` to obtain the URL, you also need `bedrock-agentcore:InvokeAgentRuntime` permission.

The following policy grants those two actions for one runtime and its `DEFAULT` endpoint. Replace the resource ARNs with your runtime and endpoint ARNs. Attach the policy to the calling identity.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock-agentcore:InvokeAgentRuntime",
                "bedrock-agentcore:InvokeAgentRuntimeProxy"
            ],
            "Resource": [
                "arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/session_endpoint_agent-a1b2c3d4e5",
                "arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/session_endpoint_agent-a1b2c3d4e5/runtime-endpoint/DEFAULT"
            ]
        }
    ]
}
```

Sign requests with Signature Version 4 (SigV4), using the signing service name `bedrock-agentcore` and the runtime’s AWS Region. Sign the destination hostname, HTTP method, path, query string, and applicable headers of the request you send.

For session endpoint requests, `X-Amz-Content-Sha256` is optional. Use the following payload hash in the canonical SigV4 request:
+ If you omit the header, use the SHA-256 hash of an empty payload, even when the application request has a body.
+ If you supply the header, use its value as the payload hash. Set the header before signing so that the signature matches the value you send.

When you omit the header, sign without the application body and attach the body after signing.

The following example uses Boto3 credentials and `requests` to make a signed GET request to the preview URL without `X-Amz-Content-Sha256`. Install `boto3` and `requests` in your client environment and configure AWS credentials before running it.

For requests without a body, such as this GET request, send `Content-Length: 0` so that the application server receives an explicitly empty body. The example sets the header before signing.

```
import boto3
import requests
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest

credentials = boto3.Session(region_name=region).get_credentials()
if credentials is None:
    raise RuntimeError("Configure AWS credentials before making this request.")

request = AWSRequest(
    method="GET",
    url=preview_url,
    headers={"Content-Length": "0"},
)
SigV4Auth(
    credentials.get_frozen_credentials(), "bedrock-agentcore", region
).add_auth(request)

result = requests.get(
    request.url,
    headers=dict(request.headers),
    timeout=60,
    allow_redirects=False,
)
result.raise_for_status()
print(result.text)
```

If you follow an application redirect, sign a new request for the redirect destination.

### OAuth bearer tokens
<a name="runtime-session-endpoints-oauth"></a>

For a runtime configured with an inbound OAuth authorizer, send a valid bearer token in the `Authorization` header. The token must satisfy the runtime’s authorizer configuration. For setup details, see [Authenticate and authorize with Inbound Auth and Outbound Auth](runtime-oauth.md).

Set `PREVIEW_URL` to the URL for your application’s allowed port and `ACCESS_TOKEN` to your OAuth access token.

```
curl --request GET \
  --header "Authorization: Bearer ${ACCESS_TOKEN}" \
  "${PREVIEW_URL}"
```

Runtime handles inbound authentication and filters service authentication headers and reserved transport headers before forwarding the request to your application.

## HTTP, gRPC, and WebSocket connections
<a name="runtime-session-endpoints-protocols"></a>

Use a client that supports the protocol exposed by your application server:

HTTP/1.1  
Use HTTPS with the application’s HTTP method, path, query string, and payload. Responses can be streamed, including server-sent events (SSE).

HTTP/2 and gRPC  
Connect to the session endpoint URL using TLS and HTTP/2. To select HTTP/2 over cleartext (`h2c`) for the application connection, set `X-Amzn-Bedrock-AgentCore-Runtime-Session-Target-Transport: h2c`. The application connection does not use TLS.  
For gRPC, use the port-prefixed hostname for your gRPC server. Supply authentication with each RPC.

WebSocket  
Use `wss` with the session hostname, optional port prefix, and your application’s WebSocket path. Use a client that can supply authentication headers in its HTTP/1.1 upgrade request.

The target-transport header controls only the connection from Runtime to the application server. Your client connection to the session endpoint URL still uses TLS.

Omit this header for an HTTP/1.1 application server or a WebSocket upgrade. When provided, the supported value is `h2c`.

These connections use your application’s routes. For example, a WebSocket server on port `8081` with a `/live` route is addressed as follows:

```
wss://8081--<session-endpoint-id>.<service-domain>/live
```

## Handle proxy errors
<a name="runtime-session-endpoints-errors"></a>

Runtime relays application responses using the application’s status, body, and protocol. Platform proxy errors have an HTTP status, an empty body, and the following attribution header:

```
X-Amzn-Bedrock-AgentCore-Runtime-Error
```

Use the header to distinguish a platform error from an application response with the same HTTP status. Platform errors aren’t wrapped in MCP, A2A, or AG-UI response envelopes.


| HTTP status | Proxy error | What to check | 
| --- | --- | --- | 
|  `400`  |  `MalformedRequest` or `ProtocolError`  | Check the URL, request format, and transport settings. | 
|  `401`  |  `AuthenticationRequired`  | Supply valid credentials for the runtime’s configured authentication mode. | 
|  `403`  |  `AccessDenied`  | Check SigV4 signing or other authorization requirements and verify that the selected port is in `allowedPorts`. Authentication failures can also return `403`. | 
|  `404`  |  `SessionNotFound`  | Verify that you’re using a returned session endpoint URL and that the session still exists. | 
|  `409`  |  `SessionConflict`  | A session operation is in progress. Retry with bounded backoff when the application request is safe to retry. | 
|  `424`  |  `RuntimeClientError`  | The application didn’t become ready or respond within the timeout. Check application startup, readiness, and response times. | 
|  `429`  |  `Throttled`  | Reduce the request rate and use bounded backoff. | 
|  `500`  |  `InternalError`  | An unexpected platform error occurred. | 
|  `502`  |  `PortNotReachable`  | Check that the application is listening on the selected port and bound to `0.0.0.0`. | 
|  `503`  |  `ServiceUnavailable`  | The service cannot currently accept or prepare the request. Use bounded backoff for requests that are safe to retry. | 

An error after response headers have been sent, or after a WebSocket upgrade, can terminate the stream or connection. A second HTTP error response cannot replace a response that has already started.

## Log session endpoint requests in CloudTrail
<a name="runtime-session-endpoints-cloudtrail"></a>

 AWS CloudTrail records session endpoint requests as data events with the event name `InvokeAgentRuntimeProxy` and the event source `bedrock-agentcore.amazonaws.com`. Like `InvokeAgentRuntime` events, these events use the `AWS::BedrockAgentCore::Runtime` resource type.

Data events aren’t logged by default, and they don’t appear in CloudTrail **Event history**. To record session endpoint requests, create a trail or event data store and add an advanced event selector for the `AWS::BedrockAgentCore::Runtime` resource type. To log only session endpoint requests, also filter on the `InvokeAgentRuntimeProxy` event name.

**Important**  
Additional charges apply for data events. A web preview can send many requests, one for each page, asset, and API call. For more information, see [AWS CloudTrail pricing](https://aws.amazon.com/cloudtrail/pricing/) on the AWS website.

## Session lifecycle and reconnection
<a name="runtime-session-endpoints-lifecycle"></a>

Session endpoints address runtime sessions and follow the [session lifecycle settings](runtime-lifecycle-settings.md). A request can wait while Runtime prepares compute. Configure client timeouts for your application’s startup and streaming behavior.

Compute replacement can interrupt active HTTP streams, gRPC calls, and WebSocket connections. Reconnect with authentication to the session endpoint URL while the session remains available.

Reconnection creates a new connection. It doesn’t guarantee that application memory or an interrupted response is preserved. For persistence options, see [File system configurations for AgentCore Runtime](runtime-filesystem-configurations.md).

Retry only requests that your application can safely repeat. A failed connection doesn’t prove that the server didn’t execute a request.

Use bounded retries and backoff. Before replaying a request, apply your application’s idempotency rules.

## Related topics
<a name="runtime-session-endpoints-related-topics"></a>
+  [Serving port and invocation path settings](runtime-configure-invocation.md#runtime-configure-invocation-settings) 
+  [Reserved platform ports](runtime-service-contract.md#runtime-reserved-ports) 