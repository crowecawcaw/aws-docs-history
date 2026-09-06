

# WorkSpaces Applications MCP server
<a name="agent-access-mcp-server"></a>

The WorkSpaces Applications MCP server is a fully managed service that provides AI agents with Model Context Protocol (MCP) tools to interact with desktop applications during streaming sessions. Agents can click buttons, enter text, scroll, and take screenshots of the desktop.

## Overview
<a name="agent-access-mcp-server-overview"></a>

When you enable agent access on a stack, agents can connect to the managed MCP server to interact with desktop applications. The MCP server handles the communication between your agent and the streaming session. Your agent sends MCP tool requests, and the server executes them on the desktop.

The MCP server is hosted in the AWS cloud. You don't need to install or maintain any server components. The server uses Streamable HTTP as its transport protocol.

Agent access supports both non-domain-joined and domain-joined fleets. The connection method differs by fleet type. Non-domain-joined fleets authenticate the session with a streaming URL, while domain-joined fleets authenticate through SAML federation. For the path that matches your fleet, see [Connecting to the MCP server](#agent-access-mcp-server-endpoint).

## Connecting to the MCP server
<a name="agent-access-mcp-server-endpoint"></a>

Agents connect to the MCP server at the following endpoint:

```
https://agentaccess-mcp.{{region}}.api.aws/mcp
```

The MCP server is hosted in the AWS cloud and uses Streamable HTTP as its transport protocol. You don't need to install or maintain any server components.

Every request must be SigV4-signed using IAM credentials with the service name `agentaccess-mcp`. The following Python example shows the general connection pattern using `mcp-proxy-for-aws`:

```
from mcp_proxy_for_aws import aws_iam_streamablehttp_client

async with aws_iam_streamablehttp_client(
    endpoint="https://agentaccess-mcp.{{region}}.api.aws/mcp",
    aws_service="agentaccess-mcp",
    aws_region="{{region}}",
    headers={
        # Fleet-type-specific headers (see the following subsections)
    },
    metadata={
        # Fleet-type-specific metadata (see the following subsections)
    },
) as (read, write, _):
    # Use read/write streams with your MCP client
    ...
```

For other languages, write your own SigV4 signing logic for outgoing MCP requests or use a library that supports SigV4 signing. For more information about `mcp-proxy-for-aws`, see [mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws) on GitHub.

How you authenticate the streaming session depends on your fleet type:
+ **Non-domain-joined fleets** — Pass a streaming URL as a header. See [Connecting with non-domain-joined fleets](#agent-access-mcp-server-connect-ndj).
+ **Domain-joined fleets** — Pass a signed SAML assertion as metadata. See [Connecting with domain-joined fleets](#agent-access-mcp-server-connect-dj).

**Note**  
At any given time, only one agent can connect to a unique session. Named users, specified through the `UserId` parameter, can have only one active session per fleet at a time. To run multiple agents concurrently, each agent must connect to its own unique session.

### Connecting with non-domain-joined fleets
<a name="agent-access-mcp-server-connect-ndj"></a>

For non-domain-joined fleets, generate a streaming URL using the `CreateStreamingURL` API and pass it as the `X-Amzn-AgentAccess-Streaming-Session-Url` header on every request. No agent-specific parameters are required. The agent behavior is determined by the stack's agent access configuration.

```
import boto3
from mcp_proxy_for_aws import aws_iam_streamablehttp_client

# Generate streaming URL
appstream = boto3.client("appstream", region_name="{{region}}")
response = appstream.create_streaming_url(
    StackName="{{stack-name}}",
    FleetName="{{fleet-name}}",
    UserId="{{user-id}}",
)
streaming_url = response["StreamingURL"]

# Connect to MCP server
async with aws_iam_streamablehttp_client(
    endpoint="https://agentaccess-mcp.{{region}}.api.aws/mcp",
    aws_service="agentaccess-mcp",
    aws_region="{{region}}",
    headers={
        "X-Amzn-AgentAccess-Streaming-Session-Url": streaming_url,
    },
) as (read, write, _):
    ...
```

For more information about the `CreateStreamingURL` API, see [CreateStreamingURL](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStreamingURL.html) in the *Amazon WorkSpaces Applications 2.0 API Reference*.

### Connecting with domain-joined fleets
<a name="agent-access-mcp-server-connect-dj"></a>

When agents access domain-joined streaming instances, the connection must be federated through a SAML provider. This requirement applies to both traditional and agent sessions. For agent sessions, [Certificate-Based Authentication](certificate-based-authentication.md) is required.

Because domain-joined streaming instances require access through SAML, your MCP client must provide a signed SAML assertion instead of a streaming URL. Encoded SAML assertions exceed HTTP header size limits. To avoid this, use the `metadata` field in `mcp-proxy-for-aws`:

```
from mcp_proxy_for_aws import aws_iam_streamablehttp_client

# saml_response: your signed, base64-encoded SAML assertion
# stack_arn: the ARN of the AppStream stack for the AD user

async with aws_iam_streamablehttp_client(
    endpoint="https://agentaccess-mcp.{{region}}.api.aws/mcp",
    aws_service="agentaccess-mcp",
    aws_region="{{region}}",
    metadata={
        "saml_response": saml_response,
        "stack_arn": stack_arn,
    },
) as (read, write, _):
    ...
```

**Note**  
The `metadata` parameter was added in `mcp-proxy-for-aws` version 1.6.1. Earlier versions cannot inject the `_meta` field without additional development. To upgrade, run `pip install -U mcp-proxy-for-aws`.

For more information about setting up SAML federation with WorkSpaces Applications, see [Setting up SAML](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-overview.html) in the *Amazon WorkSpaces Applications Administration Guide*. For more information and a complete working example, see the [sample-code-for-workspaces-agent-access](https://github.com/aws-samples/sample-code-for-workspaces-agent-access/tree/main) repository in AWS Samples on GitHub.

## Connection modes
<a name="agent-access-mcp-server-connect-mode"></a>

You can control how your agent waits for the desktop session to become available by setting the `X-Amzn-AgentAccess-Connect-Mode` header on your MCP requests.

**Note**  
Connection modes apply to both non-domain-joined and domain-joined fleets. Set the `X-Amzn-AgentAccess-Connect-Mode` header alongside whichever authentication mechanism your fleet type uses (the streaming-URL header for non-domain-joined fleets, or the SAML assertion metadata for domain-joined fleets).

The following modes are available:
+ **BLOCKING** (default) — The MCP server waits until the desktop connection is fully established before responding. When `tools/list` returns, all tools are immediately available.
+ **POLLING** — The MCP server responds immediately without waiting for the desktop connection. Initially, only the `connection_status` tool is available. Your agent polls this tool until the connection is established, at which point the full tool set becomes available.

Use POLLING mode when you want your agent to perform other work while waiting for the desktop connection, or when you need more control over connection timeout behavior.

The following example shows how to use POLLING mode:

```
# Pass the header when creating the MCP connection
headers = {
    "X-Amzn-AgentAccess-Streaming-Session-Url": streaming_url,  # non-domain-joined fleets
    "X-Amzn-AgentAccess-Connect-Mode": "POLLING",
}

# After initialize, tools/list returns immediately with connection_status
tools = await session.list_tools()
# tools = [connection_status]

# Poll connection_status until the desktop is ready
while True:
    result = await session.call_tool("connection_status", {})
    status = json.loads(result.content[0].text)
    if status["state"] == "CONNECTED":
        break
    time.sleep(2)

# Now tools/list returns the full set (screenshot, left_click, type_text, etc.)
tools = await session.list_tools()
```

## Session cleanup
<a name="agent-access-mcp-server-session-cleanup"></a>

You can control whether the streaming session is expired when your agent ends its connection by setting the `X-Amzn-AgentAccess-Expire-Streaming-Session-On-Delete` header on your MCP requests. The following values are available:
+ **true** — When your agent sends an explicit HTTP `DELETE` request, the MCP server expires the WorkSpaces Applications streaming session as part of cleanup. Expiring the session terminates the underlying streaming instance and triggers the fleet's configured autoscaling policy. For more information, see [Fleet Auto Scaling for Amazon WorkSpaces Applications](autoscaling.md).
+ **false** (default) — The streaming session continues running until the disconnect timeout is reached. For more information about the disconnect timeout, see [Create a Fleet in Amazon WorkSpaces Applications](set-up-stacks-fleets-create.md).

**Note**  
By default, an `mcp-proxy-for-aws` MCP client automatically handles the `DELETE` request when you properly end the client lifecycle.

## Available tools
<a name="agent-access-mcp-server-tools"></a>

The MCP server provides the following tools for agents to interact with the desktop during a streaming session. All tool names use the `agentaccess___` prefix.

### Mouse tools
<a name="agent-access-mcp-tools-mouse"></a>

`left_click`  
Perform a left click at the given coordinates.  
Parameters: `x` (required), `y` (required), `modifiers` (optional, for example `ctrl` or `ctrl+shift`).

`double_click`  
Perform a double click at the given coordinates.  
Parameters: `x` (required), `y` (required), `modifiers` (optional).

`triple_click`  
Perform a triple click at the given coordinates.  
Parameters: `x` (required), `y` (required), `modifiers` (optional).

`right_click`  
Perform a right click at the given coordinates.  
Parameters: `x` (required), `y` (required), `modifiers` (optional).

`middle_click`  
Perform a middle click at the given coordinates.  
Parameters: `x` (required), `y` (required), `modifiers` (optional).

`left_click_drag`  
Perform a left click drag from start coordinates to end coordinates.  
Parameters: `start_x` (required), `start_y` (required), `end_x` (required), `end_y` (required).

`left_mouse_down`  
Press and hold the left mouse button at the given coordinates.  
Parameters: `x` (required), `y` (required), `modifiers` (optional).

`left_mouse_up`  
Release the left mouse button at the given coordinates.  
Parameters: `x` (required), `y` (required), `modifiers` (optional).

`move_pointer`  
Move the pointer to the given coordinates.  
Parameters: `x` (required), `y` (required).

`scroll`  
Scroll the mouse wheel at the given coordinates.  
Parameters: `x` (required), `y` (required), `scroll_direction` (required — `Up`, `Down`, `Left`, or `Right`), `scroll_amount` (required — in ticks, where 120 ticks equals one wheel notch), `modifiers` (optional).

### Keyboard tools
<a name="agent-access-mcp-tools-keyboard"></a>

`type_text`  
Type text by simulating keyboard events for each character.  
Parameters: `text` (required — up to 10,000 characters).

`key`  
Press a key or key combination.  
Parameters: `keys` (required — a single key or combination joined by `+`, for example `a`, `ctrl+c`, or `ctrl+shift+s`).

`hold_key`  
Hold a key or key combination for a specified duration.  
Parameters: `keys` (required), `duration` (required — 1 to 30 seconds).

### Screen tools
<a name="agent-access-mcp-tools-screen"></a>

`screenshot`  
Capture a screenshot of the desktop. The returned image dimensions define the coordinate space for all mouse tools.  
Parameters: `include_cursor` (optional — defaults to `false`).

## MCP tool forwarding
<a name="agent-access-mcp-tool-forwarding-details"></a>

MCP tool forwarding allows agents to interact with applications and the desktop operating system through direct MCP calls rather than using computer use tools. When you enable tool forwarding, the MCP server forwards tools configured on the WorkSpaces application session to your agent.

### Setting up tool forwarding
<a name="agent-access-tool-forwarding-setup"></a>

To set up MCP tool forwarding:

1. **Enable tool forwarding** — Turn on the `FORWARD_MCP_TOOLS` agent action through the API or console settings.

1. **Verify that the MCP server configuration file is present** — The service looks for a configuration file at the following path:

   ```
   C:\ProgramData\NICE\dcv\mcp_server_redirection_config.json
   ```

1. **Configure the MCP server on the WorkSpace image** — The configuration file is JSON with a single top-level `mcpServers` object. Each key is a unique name that you choose for a server. Each value specifies how to launch that server.

   ```
   {
       "mcpServers": {
           "filesystem": {
               "command": "C:/path/to/python.exe",
               "args": ["C:/mcpServerPath/filesystem.py", "C:/UserName/Documents"]
           },
           "weather": {
               "command": "C:/Program Files/my-mcp/weather.exe"
           }
       }
   }
   ```    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/appstream2/latest/developerguide/agent-access-mcp-server.html)

1. **Verify tool availability** — If the configuration file is present, the service connects to the MCP servers configured in the file and forwards the tools. The forwarded tools appear when the agent lists its available tools.

**Note**  
Both IAM access and the service setting must be enabled for tool forwarding to work. IAM permissions do not override the service setting.

### MCP tool forwarding considerations
<a name="agent-access-tool-forwarding-considerations"></a>

Note the following considerations when you configure MCP tool forwarding:
+ **Transport is standard I/O (stdio) only.** Each entry must launch a process that speaks MCP over its standard input and output. Remote HTTP or SSE MCP endpoints are not supported. To use a remote endpoint, wrap it in a local stdio server.
+ **Only `command` and `args` are supported.** There is no field for environment variables or working directory. Each server inherits the environment of the streaming session and runs as the session user. Use absolute paths for `command` and for any path arguments.
+ **Use forward slashes in paths** (for example, `C:/Program Files/my-mcp/server.exe`). JSON treats the backslash as an escape character, so a Windows-style path written with single backslashes is invalid. Windows accepts forward slashes for absolute paths, which avoids the need to escape every separator as `\\`.
+ **Tool-call timeout.** Each forwarded tool call must complete within 5 seconds. The MCP server cancels calls that take longer and returns an error to the agent. Design forwarded tools to return quickly.

### How forwarded tools appear to the agent
<a name="agent-access-tool-forwarding-naming"></a>

To prevent collisions between servers, the MCP server renames each forwarded tool in the agent's tool list using the following pattern:

```
forwarded___{{server-name}}___{{original-tool-name}}
```

The {{server-name}} is the key from your configuration file. For example, a `get_forecast` tool from the `weather` server is listed as `forwarded___weather___get_forecast`. When the agent calls the forwarded name, the MCP server routes the request to the original tool on the owning server. Agent code that matches on tool names must expect this prefix.

### IAM permissions for tool forwarding
<a name="agent-access-tool-forwarding-iam"></a>

The IAM action for calling forwarded tools is `CallForwardedTool`. You can scope access to specific stacks using the `StackArn` condition key:

```
{
  "Action": "agentaccess-mcp:*",
  "Resource": "*",
  "Condition": {
    "ArnLike": {
      "agentaccess-mcp:StackArn": "arn:aws:appstream:{{region}}:{{account-id}}:stack/{{stack-name}}"
    }
  }
}
```

## Compatible frameworks
<a name="agent-access-mcp-server-frameworks"></a>

You can connect to the WorkSpaces Applications MCP server from any MCP-compatible agent framework that supports Streamable HTTP and SigV4 signing. The following frameworks have been tested:
+ [Strands Agents SDK](https://strandsagents.com/docs/user-guide/concepts/tools/mcp-tools/) — Provides native MCP client support.
+ [mcp-proxy-for-aws](https://github.com/aws/mcp-proxy-for-aws) — A lightweight transport that handles SigV4 signing for MCP requests in Python.

## Monitoring
<a name="agent-access-mcp-server-monitoring"></a>

You can monitor agent activity through the following services:
+ **AWS CloudTrail** — Agent session events are logged in CloudTrail. You can view when agents connect, which tools they use, and when sessions end. Tool calls are data events and require that you set up a trail to log data events. For more information, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the *CloudTrail User Guide*.
+ **CloudWatch** — Operational metrics for agent sessions are available in CloudWatch.
+ **Amazon S3** — If you configure screenshot storage, screenshots captured during agent sessions are available in the Amazon S3 bucket that you specify. Screenshots are stored with the following key format:

  ```
  agentaccess/screenshots/year={{YYYY}}/month={{MM}}/day={{DD}}/{{session-id}}/{{timestamp}}.png
  ```

  The UUID in the path is the WorkSpaces Applications streaming session ID.

## Get started
<a name="agent-access-mcp-server-get-started"></a>

To get started with the WorkSpaces Applications MCP server, see [Get started providing agents with access to WorkSpaces Applications](getting-started-agent-access.md).